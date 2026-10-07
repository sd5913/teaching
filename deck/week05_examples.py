"""Self-contained Python examples shown in the Week 5 slides."""

TINY_PIXEL_EXAMPLE = '''from PIL import Image

pixels = [
    [(255, 0, 0), (0, 255, 0)],
    [(0, 0, 255), (255, 255, 0)],
]
image = Image.new("RGB", (2, 2))
image.putdata([pixel for row in pixels for pixel in row])
image.resize((120, 120), Image.Resampling.NEAREST).save("tiny-image.png")
print("saved tiny-image.png")
'''

NOISE_EXAMPLE = '''import random
from PIL import Image

rng = random.Random(7)
pixels = [(rng.randrange(256), rng.randrange(256), rng.randrange(256))
          for _ in range(256 * 256)]
image = Image.new("RGB", (256, 256))
image.putdata(pixels)
image.save("noise.png")
print(image.size, image.mode)
'''

FRAME_EXAMPLE = '''from PIL import Image, ImageDraw

frames = []
for x in (8, 26, 44):
    frame = Image.new(
        "RGB", (64, 48), "white")
    draw = ImageDraw.Draw(frame)
    draw.ellipse(
        (x, 18, x + 12, 30),
        fill=(232, 120, 53))
    frames.append(frame)

frames[0].save(
    "moving-dot.gif", save_all=True,
    append_images=frames[1:],
    duration=200, loop=0,
)
print("saved", len(frames), "frames")
'''

API_EXAMPLE = '''import base64, json, os
from urllib.request import Request
from urllib.request import urlopen

url = ("https://easel.ait4x.org"
       "/v1/images/generations")
payload = {
    "model": "qwen-image-2.1",
    "prompt": ("An orange circle "
               "on cream paper"),
    "size": "1024x1024",
    "n": 1,
    "response_format": "b64_json",
}
key = os.environ["EASEL_KEY"]
headers = {
    "Authorization": "Bearer " + key,
    "Content-Type": "application/json",
}
body = json.dumps(payload).encode()
request = Request(
    url, data=body, headers=headers)
with urlopen(
    request, timeout=600
) as response:
    result = json.load(response)
encoded = result["data"][0]["b64_json"]
image = base64.b64decode(encoded)
with open("api-image.png", "wb") as f:
    f.write(image)
print("saved api-image.png")
'''

# Readable excerpts; the linked student script adds MPS, a revision pin and metadata.
DIFFUSION_LOAD_EXAMPLE = '''import torch
from diffusers import StableDiffusionPipeline
model = "stable-diffusion-v1-5/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32
pipe = StableDiffusionPipeline.from_pretrained(
    model, dtype=dtype, use_safetensors=True,
    variant="fp16" if device == "cuda" else None,
).to(device)
'''

DIFFUSION_GENERATE_EXAMPLE = '''prompt = ("An orange ceramic sphere on cream paper, "
          "studio photograph, soft shadow, centered composition")
generator = torch.Generator("cpu").manual_seed(7)
image = pipe(
    prompt, num_inference_steps=20, guidance_scale=7.5,
    width=512, height=512, generator=generator,
).images[0]
image.save("stable-diffusion-7.png")
'''

RUNNABLE_EXAMPLES = {
    'tiny image': TINY_PIXEL_EXAMPLE,
    'random noise': NOISE_EXAMPLE,
    'frame animation': FRAME_EXAMPLE,
    'image API': API_EXAMPLE,
}
