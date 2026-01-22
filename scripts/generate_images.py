#!/usr/bin/env python3
"""
Generate images from storyboard prompts using ComfyUI API.
Usage: python generate_images.py <project_folder>
"""

import sys
import os
import json
import time
import re
import urllib.request
import urllib.parse
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from vault root
vault_root = Path(__file__).parent.parent
load_dotenv(vault_root / ".env")

COMFYUI_URL = os.getenv("COMFYUI_URL", "http://localhost:8000")

# Basic txt2img workflow - adjust based on your ComfyUI setup
# This is a minimal workflow - you'll want to customize with your preferred models
BASIC_WORKFLOW = {
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "cfg": 7,
            "denoise": 1,
            "latent_image": ["5", 0],
            "model": ["4", 0],
            "negative": ["7", 0],
            "positive": ["6", 0],
            "sampler_name": "euler",
            "scheduler": "normal",
            "seed": 42,
            "steps": 20
        }
    },
    "4": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "sd_xl_base_1.0.safetensors"
        }
    },
    "5": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "batch_size": 1,
            "height": 1920,
            "width": 1080
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": ["4", 1],
            "text": "PROMPT_PLACEHOLDER"
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": ["4", 1],
            "text": "ugly, blurry, low quality, distorted, deformed"
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": ["3", 0],
            "vae": ["4", 2]
        }
    },
    "9": {
        "class_type": "SaveImage",
        "inputs": {
            "filename_prefix": "scene",
            "images": ["8", 0]
        }
    }
}

def read_storyboard(project_path: Path) -> str:
    """Read storyboard file."""
    storyboard_file = project_path / "storyboard.md"
    if not storyboard_file.exists():
        raise FileNotFoundError(f"No storyboard.md found. Generate storyboard first.")
    return storyboard_file.read_text()

def extract_prompts(storyboard: str) -> list[dict]:
    """Extract scene prompts from storyboard markdown."""
    scenes = []

    # Pattern to match scene blocks
    scene_pattern = r'## Scene (\d+)[^\n]*\n(.*?)(?=## Scene \d+|---\n## |$)'
    matches = re.findall(scene_pattern, storyboard, re.DOTALL)

    for scene_num, content in matches:
        # Extract prompt
        prompt_match = re.search(r'\*\*Prompt:\*\*\s*["\']?([^"\']*?)["\']?\s*(?:\n|$)', content)
        if prompt_match:
            prompt = prompt_match.group(1).strip()
            scenes.append({
                "scene": int(scene_num),
                "prompt": prompt
            })

    # Also try to extract style block
    style_match = re.search(r'STYLE:\s*(.+?)(?:\n|CHARACTER:|$)', storyboard, re.DOTALL)
    style_suffix = ""
    if style_match:
        style_suffix = ", " + style_match.group(1).strip()

    # Append style to all prompts
    for scene in scenes:
        if style_suffix and style_suffix not in scene["prompt"]:
            scene["prompt"] += style_suffix

    return scenes

def queue_prompt(prompt: dict) -> str:
    """Queue a prompt to ComfyUI and return the prompt_id."""
    data = json.dumps({"prompt": prompt}).encode('utf-8')
    req = urllib.request.Request(
        f"{COMFYUI_URL}/prompt",
        data=data,
        headers={'Content-Type': 'application/json'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            return result.get('prompt_id')
    except urllib.error.URLError as e:
        raise ConnectionError(f"Cannot connect to ComfyUI at {COMFYUI_URL}: {e}")

def get_history(prompt_id: str) -> dict:
    """Get the history/status of a prompt."""
    try:
        with urllib.request.urlopen(f"{COMFYUI_URL}/history/{prompt_id}") as response:
            return json.loads(response.read())
    except:
        return {}

def wait_for_completion(prompt_id: str, timeout: int = 300) -> dict:
    """Wait for a prompt to complete."""
    start = time.time()
    while time.time() - start < timeout:
        history = get_history(prompt_id)
        if prompt_id in history:
            return history[prompt_id]
        time.sleep(2)
    raise TimeoutError(f"Generation timed out after {timeout}s")

def get_image(filename: str, subfolder: str = "", folder_type: str = "output") -> bytes:
    """Download generated image from ComfyUI."""
    params = urllib.parse.urlencode({
        "filename": filename,
        "subfolder": subfolder,
        "type": folder_type
    })

    with urllib.request.urlopen(f"{COMFYUI_URL}/view?{params}") as response:
        return response.read()

def generate_scene(scene: dict, output_dir: Path, seed: int) -> Path:
    """Generate image for a single scene."""
    workflow = json.loads(json.dumps(BASIC_WORKFLOW))  # Deep copy

    # Update prompt
    workflow["6"]["inputs"]["text"] = scene["prompt"]

    # Update seed
    workflow["3"]["inputs"]["seed"] = seed + scene["scene"]

    # Update filename
    workflow["9"]["inputs"]["filename_prefix"] = f"scene-{scene['scene']:02d}"

    print(f"  Generating scene {scene['scene']}...")
    print(f"  Prompt: {scene['prompt'][:80]}...")

    prompt_id = queue_prompt(workflow)
    result = wait_for_completion(prompt_id)

    # Get output images
    outputs = result.get('outputs', {})
    for node_id, node_output in outputs.items():
        if 'images' in node_output:
            for img_info in node_output['images']:
                img_data = get_image(
                    img_info['filename'],
                    img_info.get('subfolder', ''),
                    img_info.get('type', 'output')
                )

                output_path = output_dir / f"scene-{scene['scene']:02d}.png"
                output_path.write_bytes(img_data)
                print(f"  ✓ Saved: {output_path.name}")
                return output_path

    raise RuntimeError(f"No image output for scene {scene['scene']}")

def create_gallery_note(project_path: Path, scenes: list[dict]):
    """Create a markdown gallery for reviewing generated images."""
    gallery_file = project_path / "image-gallery.md"

    lines = [
        "# Generated Images",
        "",
        "Review and select the best images for each scene.",
        "Mark your selection with [x] in the checkbox.",
        "",
        "---",
        ""
    ]

    for scene in scenes:
        lines.extend([
            f"## Scene {scene['scene']}",
            f"**Prompt:** {scene['prompt'][:100]}...",
            "",
            f"![[images/scene-{scene['scene']:02d}.png]]",
            "",
            f"- [ ] Approved",
            f"- [ ] Needs regeneration",
            "",
            "**Notes:**",
            "",
            "---",
            ""
        ])

    gallery_file.write_text("\n".join(lines))
    print(f"✓ Gallery created: {gallery_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_images.py <project_folder> [--seed SEED]")
        print("Example: python generate_images.py '01-Projects/jan-shorts/2026-01-21-cat-astronaut'")
        sys.exit(1)

    project_rel_path = sys.argv[1]
    project_path = vault_root / project_rel_path

    # Parse optional seed
    seed = 42
    if "--seed" in sys.argv:
        seed_idx = sys.argv.index("--seed")
        if seed_idx + 1 < len(sys.argv):
            seed = int(sys.argv[seed_idx + 1])

    if not project_path.exists():
        print(f"Error: Project folder not found: {project_path}")
        sys.exit(1)

    # Create images directory
    images_dir = project_path / "images"
    images_dir.mkdir(exist_ok=True)

    print(f"Project: {project_path}")
    print(f"Output: {images_dir}")
    print(f"Seed: {seed}")
    print(f"ComfyUI: {COMFYUI_URL}")
    print()

    try:
        storyboard = read_storyboard(project_path)
        scenes = extract_prompts(storyboard)

        if not scenes:
            print("Error: No scene prompts found in storyboard.")
            print("Make sure storyboard.md has scenes with **Prompt:** fields.")
            sys.exit(1)

        print(f"Found {len(scenes)} scenes to generate")
        print("="*50)

        for scene in scenes:
            try:
                generate_scene(scene, images_dir, seed)
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                continue

        print()
        print("="*50)
        print("Generation complete!")

        create_gallery_note(project_path, scenes)
        print("\nOpen image-gallery.md in Obsidian to review.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ConnectionError as e:
        print(f"ComfyUI Error: {e}")
        print("\nMake sure ComfyUI is running at", COMFYUI_URL)
        sys.exit(1)

if __name__ == "__main__":
    main()
