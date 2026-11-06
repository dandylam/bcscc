"""Build a copy of the game with the hero's photo embedded.

The photo is never committed to this repository. Usage:
    python3 tools/build_with_avatar.py path/to/avatar.jpg dist/index.html
The photo should be a square crop of the face (about 240 x 240 px).
"""
import base64, mimetypes, pathlib, sys

src = pathlib.Path(__file__).resolve().parent.parent / "index.html"
img, out = map(pathlib.Path, sys.argv[1:3])
mime = mimetypes.guess_type(img.name)[0] or "image/jpeg"
uri = f"data:{mime};base64," + base64.b64encode(img.read_bytes()).decode()
html = src.read_text(encoding="utf-8")
assert "/*AVATAR*/null" in html, "avatar marker not found in index.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html.replace("/*AVATAR*/null", repr(uri)), encoding="utf-8")
print(f"wrote {out}")
