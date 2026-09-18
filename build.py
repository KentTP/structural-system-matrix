"""Build the Structural System Matrix from src/template.html.

Embeds the Sense logo PNG bytes (base64) into the page script — the page paints
them onto canvases, because the Artifact viewer blocks both data: images and
relative image files — and writes two outputs:
  index.html         full HTML document (open locally / deploy)
  dist/artifact.html the same page as a fragment for publishing as a Claude Artifact
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
BRAND_SRC = ROOT / "brand"   # Sense logo artwork (320x95 PNGs: light = black text, dark = white text)

def b64(name: str) -> str:
    return base64.b64encode((BRAND_SRC / name).read_bytes()).decode()

page = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
assert page.count("{{LOGO_LIGHT_B64}}") == 1 and page.count("{{LOGO_DARK_B64}}") == 1
page = page.replace("{{LOGO_LIGHT_B64}}", b64("logo_light.png")).replace("{{LOGO_DARK_B64}}", b64("logo_dark.png"))

# Sense brand type: Helvetica Neue subset to Latin as WOFF2 (brand/fonts), inlined as data: URIs
FONTS = {"{{FONT_MD_B64}}": "fonts/sense-md.woff2",    # 65 Medium — UI and body
         "{{FONT_BD_B64}}": "fonts/sense-bd.woff2",    # 75 Bold — emphasis
         "{{FONT_UL_B64}}": "fonts/sense-ul.woff2",    # 25 UltraLight — display numerals, lede
         "{{FONT_ULI_B64}}": "fonts/sense-uli.woff2"}  # 25 UltraLight Italic — taglines (wordmark echo)
for key, rel in FONTS.items():
    assert page.count(key) == 1, key
    page = page.replace(key, b64(rel))

(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "artifact.html").write_text(page, encoding="utf-8")

head_end = page.index("</style>") + len("</style>")
full = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
        + page[:head_end] + "\n</head>\n<body>\n" + page[head_end:].lstrip("\n") + "\n</body>\n</html>\n")
(ROOT / "index.html").write_text(full, encoding="utf-8")
print(f"index.html {len(full)/1024:.0f} KB · dist/artifact.html {len(page)/1024:.0f} KB")
