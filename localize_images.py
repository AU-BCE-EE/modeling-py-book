"""
Replace GitHub user-attachment <img> tags in a .qmd file with local,
Quarto-native ![]() markdown images.

Finds every <img ... src="https://github.com/user-attachments/assets/<uuid>" ...>
tag, downloads the image if a matching file isn't already sitting in the
images dir (matched by uuid, regardless of any extra prefix GitHub/the
browser stuck on the filename), saves it as <uuid>.<ext>, and replaces the
whole tag with a markdown image using a path relative to the qmd file's
directory and the tag's alt/width attributes.

Usage:
    python localize_images.py appx_vs_code.qmd images-vs-code
"""

import argparse
import mimetypes
import re
import urllib.request
from pathlib import Path

IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
URL_RE = re.compile(
    r"https://github\.com/user-attachments/assets/([0-9a-fA-F-]{36})"
)


def find_existing(images_dir: Path, uuid: str) -> Path | None:
    matches = list(images_dir.glob(f"*{uuid}*"))
    return matches[0] if matches else None


def download(url: str, uuid: str, images_dir: Path) -> Path:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
        final_url = resp.geturl()
        content_type = resp.headers.get("Content-Type", "")

    ext = Path(final_url.split("?", 1)[0]).suffix
    if not ext:
        ext = mimetypes.guess_extension(content_type.split(";")[0].strip()) or ".png"

    dest = images_dir / f"{uuid}{ext}"
    dest.write_bytes(data)
    return dest


def localize(uuid: str, images_dir: Path) -> tuple[Path, str]:
    url = f"https://github.com/user-attachments/assets/{uuid}"
    existing = find_existing(images_dir, uuid)
    if existing:
        clean = images_dir / f"{uuid}{existing.suffix}"
        if existing != clean:
            existing.rename(clean)
        return clean, "reused local copy of"
    return download(url, uuid, images_dir), "downloaded"


def to_markdown(tag: str, rel_path: Path) -> str:
    attrs = dict(ATTR_RE.findall(tag))
    alt = attrs.get("alt", "")
    width = attrs.get("width")
    md = f"![{alt}]({rel_path})"
    if width:
        md += f'{{width="{width}px"}}'
    return md


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("qmd_file", type=Path)
    parser.add_argument("images_dir", type=Path)
    args = parser.parse_args()

    text = args.qmd_file.read_text()
    args.images_dir.mkdir(exist_ok=True)

    count = 0
    for tag in IMG_TAG_RE.findall(text):
        url_match = URL_RE.search(tag)
        if not url_match:
            continue  # not a GitHub-hosted screenshot; leave it alone
        uuid = url_match.group(1)

        dest, action = localize(uuid, args.images_dir)
        rel = dest.relative_to(args.qmd_file.parent)
        print(f"{action} {uuid} -> {rel}")

        text = text.replace(tag, to_markdown(tag, rel))
        count += 1

    args.qmd_file.write_text(text)
    print(f"\nUpdated {args.qmd_file} ({count} image(s) converted to markdown).")


if __name__ == "__main__":
    main()
