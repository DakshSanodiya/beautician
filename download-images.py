"""
One-time helper: downloads the service photos used on the site and saves
them into the images/ folder as .webp files, matching the filenames
already referenced in index.html.

Run this once, on a computer with internet access, before you deploy:

    pip install requests pillow
    python download-images.py

All photos are free-to-use stock photos from Pexels (no attribution
required): https://www.pexels.com/license/
"""

import io
import os

import requests
from PIL import Image

IMAGES = [
    ("19788008", "bridal.webp"),
    ("13022170", "party.webp"),
    ("3813896",  "hd-makeup.webp"),
    ("8467969",  "hair-styling.webp"),
    ("3993449",  "hairspa.webp"),
    ("4672653",  "facial.webp"),
    ("5240450",  "cleanup.webp"),
    ("9486704",  "waxing.webp"),
    ("4572091",  "threading.webp"),
    ("8809259",  "nail-art.webp"),
]

OUT_DIR = os.path.join(os.path.dirname(__file__), "images")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for photo_id, filename in IMAGES:
        url = (
            f"https://images.pexels.com/photos/{photo_id}/"
            f"pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=800"
        )
        print(f"Downloading {filename} ...")
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        img = Image.open(io.BytesIO(response.content)).convert("RGB")
        out_path = os.path.join(OUT_DIR, filename)
        img.save(out_path, "WEBP", quality=82)
        print(f"  saved to {out_path}")

    print("\nAll images downloaded. You're ready to deploy the site.")


if __name__ == "__main__":
    main()
