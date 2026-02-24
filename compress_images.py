"""
Compress all images in-place for web optimization.
Resize to max 1920px, JPEG quality 85%.
Handles read-only files on Windows.
"""
import os
import io
import stat
from PIL import Image, ImageOps

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
MAX_DIM = 1920
QUALITY = 85

def make_writable(path):
    """Remove read-only attribute on Windows."""
    current = os.stat(path).st_mode
    os.chmod(path, current | stat.S_IWRITE)

def compress(path):
    sb = os.path.getsize(path)

    # Read into memory via BytesIO to avoid file locking
    with open(path, 'rb') as f:
        data = io.BytesIO(f.read())

    img = Image.open(data)
    if img.mode in ("RGBA", "P", "LA"):
        img = img.convert("RGB")
    img = ImageOps.exif_transpose(img)

    w, h = img.size
    resized = False
    if max(w, h) > MAX_DIM:
        ratio = MAX_DIM / max(w, h)
        img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)
        resized = True

    # Compress to bytes
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=QUALITY, optimize=True)
    img.close()
    compressed = buf.getvalue()

    # Make file writable, then overwrite
    make_writable(path)
    with open(path, 'wb') as f:
        f.write(compressed)

    sa = os.path.getsize(path)
    return sb, sa, resized

def main():
    exts = {".jpg", ".jpeg", ".png"}
    files = []
    for root, _, fnames in os.walk(SRC):
        for f in fnames:
            if os.path.splitext(f)[1].lower() in exts:
                files.append(os.path.join(root, f))

    print(f"Found {len(files)} images\n")
    tb, ta = 0, 0
    ok = 0

    for i, p in enumerate(files, 1):
        rel = os.path.relpath(p, SRC)
        try:
            sb, sa, resized = compress(p)
            tb += sb
            ta += sa
            ok += 1
            pct = (1 - sa / sb) * 100 if sb > 0 else 0
            tag = " [RESIZED]" if resized else ""
            print(f"[{i}/{len(files)}] {rel}: {sb/1024:.0f}KB -> {sa/1024:.0f}KB (-{pct:.0f}%){tag}")
        except Exception as e:
            sz = os.path.getsize(p)
            tb += sz
            ta += sz
            print(f"[{i}/{len(files)}] {rel}: ERROR - {e}")

    print(f"\n{'='*50}")
    print(f"Compressed: {ok}/{len(files)} files")
    print(f"BEFORE: {tb/1024/1024:.1f} MB")
    print(f"AFTER:  {ta/1024/1024:.1f} MB")
    saved = tb - ta
    pct = (saved / tb) * 100 if tb > 0 else 0
    print(f"SAVED:  {saved/1024/1024:.1f} MB ({pct:.0f}%)")

if __name__ == "__main__":
    main()
