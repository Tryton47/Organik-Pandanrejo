import os
import io
import shutil
import tempfile
from PIL import Image

folder = r'd:\organikpandarejo\images\Berita'
max_width = 1920
quality = 90
tmpdir = tempfile.mkdtemp()

files = sorted(os.listdir(folder))
ok_count = 0
err_count = 0

for fname in files:
    fpath = os.path.join(folder, fname)
    if not os.path.isfile(fpath):
        continue
    ext = fname.lower().rsplit('.', 1)[-1]
    if ext not in ('jpg', 'jpeg', 'png'):
        continue

    size_kb = os.path.getsize(fpath) // 1024
    if size_kb < 300:
        print(f'SKIP {fname} ({size_kb}KB)')
        continue

    # Copy to temp dir first to avoid lock issues
    tmp_src = os.path.join(tmpdir, fname)
    base = os.path.splitext(fname)[0]
    out_name = base + '.jpg'
    out_path = os.path.join(folder, out_name)
    tmp_out = os.path.join(tmpdir, out_name)

    try:
        shutil.copy2(fpath, tmp_src)

        img = Image.open(tmp_src)
        img.load()
        if img.mode not in ('RGB',):
            img = img.convert('RGB')

        w, h = img.size
        if w > max_width:
            ratio = max_width / w
            img = img.resize((max_width, int(h * ratio)), Image.LANCZOS)

        img.save(tmp_out, 'JPEG', quality=quality, optimize=True)
        img.close()

        new_kb = os.path.getsize(tmp_out) // 1024

        # Remove original and copy compressed version in
        if os.path.exists(out_path):
            os.remove(out_path)
        shutil.copy2(tmp_out, out_path)

        # Remove original if it was PNG
        if fpath != out_path and os.path.exists(fpath):
            try:
                os.remove(fpath)
            except:
                pass

        ok_count += 1
        print(f'OK  {fname}: {size_kb}KB -> {new_kb}KB  (saved {size_kb - new_kb}KB)')

    except Exception as e:
        err_count += 1
        print(f'ERR {fname}: {e}')
    finally:
        for p in (tmp_src, tmp_out):
            if os.path.exists(p):
                try:
                    os.remove(p)
                except:
                    pass

shutil.rmtree(tmpdir, ignore_errors=True)
print(f'\nDONE: {ok_count} compressed, {err_count} errors')
