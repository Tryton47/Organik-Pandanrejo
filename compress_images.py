"""
Compress all images in-place for web optimization.
- Enforces lowercase '.jpg' extension.
- Resize to max 1920px, JPEG quality 85%.
- Handles read-only files on Windows.
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
    if os.path.exists(path):
        current = os.stat(path).st_mode
        os.chmod(path, current | stat.S_IWRITE)

def compress_and_rename(path):
    sb = os.path.getsize(path)
    ext = os.path.splitext(path)[1]
    
    # Read into memory via BytesIO to avoid file locking
    with open(path, 'rb') as f:
        data = io.BytesIO(f.read())

    img = Image.open(data)
    
    # Handle transparency if converting to JPEG
    target_ext = ext.lower()
    if target_ext in (".jpg", ".jpeg", ".JPG", ".JPEG"):
        target_ext = ".jpg"
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
    fmt = "JPEG" if target_ext == ".jpg" else "PNG"
    buf = io.BytesIO()
    img.save(buf, fmt, quality=QUALITY, optimize=True)
    img.close()
    compressed = buf.getvalue()

    # Determine final path
    final_path = os.path.splitext(path)[0] + target_ext
    
    # If we are changing name (e.g. .JPG -> .jpg), we must be careful on Windows
    if final_path.lower() == path.lower() and final_path != path:
        # Standardize to lowercase
        make_writable(path)
        # On Windows, renaming to the same name with different case requires a temp step
        temp_path = path + ".tmp"
        with open(temp_path, 'wb') as f:
            f.write(compressed)
        os.remove(path)
        os.rename(temp_path, final_path)
    else:
        # Same path or completely different extension
        make_writable(path)
        with open(final_path, 'wb') as f:
            f.write(compressed)
        if final_path != path:
            os.remove(path)

    sa = os.path.getsize(final_path)
    return sb, sa, resized, final_path

def main():
    # Support common formats
    exts = {".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"}
    files = []
    for root, _, fnames in os.walk(SRC):
        for f in fnames:
            if os.path.splitext(f)[1] in exts:
                files.append(os.path.join(root, f))

    print(f"Found {len(files)} images\n")
    tb, ta = 0, 0
    ok = 0

    for i, p in enumerate(files, 1):
        rel = os.path.relpath(p, SRC)
        try:
            sb, sa, resized, final_path = compress_and_rename(p)
            tb += sb
            ta += sa
            ok += 1
            pct = (1 - sa / sb) * 100 if sb > 0 else 0
            tag = " [RESIZED]" if resized else ""
            final_rel = os.path.relpath(final_path, SRC)
            print(f"[{i}/{len(files)}] {rel} -> {final_rel}: {sb/1024:.0f}KB -> {sa/1024:.0f}KB (-{pct:.0f}%){tag}")
        except Exception as e:
            sz = os.path.getsize(p)
            tb += sz
            ta += sz
            print(f"[{i}/{len(files)}] {rel}: ERROR - {e}")

    print(f"\n{'='*50}")
    print(f"Processed: {ok}/{len(files)} files")
    print(f"BEFORE: {tb/1024/1024:.1f} MB")
    print(f"AFTER:  {ta/1024/1024:.1f} MB")
    saved = tb - ta
    pct = (saved / tb) * 100 if tb > 0 else 0
    print(f"SAVED:  {saved/1024/1024:.1f} MB ({pct:.0f}%)")

if __name__ == "__main__":
    main()
