#!/usr/bin/env python3
"""Build the Jerga de Obra cover, PWA splash, and iOS startup images.

Uses the official hard-hat illustration (high-res crop if present, else icon-512)
on the app's yellow/black theme, with the product title.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT

INK = (10, 10, 10, 255)
BLAZE = (255, 209, 0, 255)
WHITE = (255, 255, 255, 255)
TAG = (232, 232, 232, 255)
GLOW = (255, 209, 0, 255)

FONT_BEBAS = Path("/usr/share/fonts/truetype/sand-box/google/Bebas Neue/BebasNeue-Regular.ttf")
FONT_MANROPE = Path("/usr/share/fonts/truetype/sand-box/google/Manrope/Manrope-VariableFont_wght.ttf")

HAT_CANDIDATES = [
    Path("/workspace/jerga-samples/logo-work2/optionD_card_crop.png"),
    ROOT / "icon-512.png",
]


def font(path: Path, size: int, weight: int | None = None) -> ImageFont.FreeTypeFont:
    if weight is not None and "Variable" in path.name:
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.truetype(str(path), size=size)


def manrope(size: int) -> ImageFont.FreeTypeFont:
    # Pillow does not always honor variable weight; try a reasonable size.
    return ImageFont.truetype(str(FONT_MANROPE), size=size)


def bebas(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BEBAS), size=size)


def load_hat() -> Image.Image:
    for p in HAT_CANDIDATES:
        if p.exists():
            im = Image.open(p).convert("RGBA")
            return im
    raise SystemExit("No hard-hat source image found")


def rounded_rect_mask(size: tuple[int, int], radius: int) -> Image.Image:
    w, h = size
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=255)
    return m


def _apply_mask(im: Image.Image, mask: Image.Image) -> Image.Image:
    r, g, b, a = im.split()
    a = ImageChops.multiply(a, mask)
    return Image.merge("RGBA", (r, g, b, a))


def hat_tile(hat: Image.Image, size: int, radius: int, border: int) -> Image.Image:
    """Square tile: hat on its studio ground, black border, yellow drop shadow."""
    inner = size
    shadow = max(6, round(size * 0.045))
    canvas = Image.new("RGBA", (inner + shadow, inner + shadow), (0, 0, 0, 0))

    # yellow offset shadow
    sd = ImageDraw.Draw(canvas)
    sd.rounded_rectangle(
        (shadow, shadow, shadow + inner - 1, shadow + inner - 1),
        radius=radius,
        fill=BLAZE,
    )

    tile = Image.new("RGBA", (inner, inner), (0, 0, 0, 0))
    td = ImageDraw.Draw(tile)
    td.rounded_rectangle((0, 0, inner - 1, inner - 1), radius=radius, fill=(245, 245, 245, 255))
    # hat, slightly inset so the brim isn't clipped by the border
    inset = border + max(4, round(inner * 0.02))
    fitted = hat.resize((inner - 2 * inset, inner - 2 * inset), Image.Resampling.LANCZOS)
    tile.alpha_composite(fitted, (inset, inset))
    # black border
    td.rounded_rectangle(
        (border // 2, border // 2, inner - 1 - border // 2, inner - 1 - border // 2),
        radius=max(1, radius - border // 2),
        outline=INK,
        width=border,
    )
    tile = _apply_mask(tile, rounded_rect_mask((inner, inner), radius))
    canvas.alpha_composite(tile, (0, 0))
    return canvas


def radial_glow(size: tuple[int, int], center: tuple[int, int], radius: int, color=GLOW, alpha=90) -> Image.Image:
    w, h = size
    # draw a soft yellow glow
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    # use a smaller grayscale blob and colorize
    blob_size = radius * 2
    blob = Image.new("L", (blob_size, blob_size), 0)
    bd = ImageDraw.Draw(blob)
    bd.ellipse((0, 0, blob_size - 1, blob_size - 1), fill=alpha)
    blob = blob.filter(ImageFilter.GaussianBlur(radius=int(radius * 0.45)))
    colored = Image.new("RGBA", (blob_size, blob_size), color)
    colored.putalpha(blob)
    x = center[0] - radius
    y = center[1] - radius
    overlay.alpha_composite(colored, (x, y))
    return overlay


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, spacing=0):
    bbox = draw.textbbox((0, 0), text, font=fnt, spacing=spacing)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_title_block(base: Image.Image, x: int, y: int, jerga_size: int, obra_size: int, align="left", gap=None):
    """Draw JERGA and a yellow-highlighted DE OBRA. Returns the bottom y of the block."""
    draw = ImageDraw.Draw(base)
    f_jerga = bebas(jerga_size)
    f_obra = bebas(obra_size)
    gap = jerga_size // 8 if gap is None else gap

    w1, h1 = text_size(draw, "JERGA", f_jerga)
    # measure DE OBRA with padding
    pad_x = max(10, obra_size // 8)
    pad_y = max(4, obra_size // 14)
    w2, h2 = text_size(draw, "DE OBRA", f_obra)
    box_w = w2 + pad_x * 2
    box_h = h2 + pad_y * 2

    if align == "center":
        jerga_x = x - w1 // 2
        box_x = x - box_w // 2
    else:
        jerga_x = x
        box_x = x

    # JERGA in blaze yellow
    # Bebas has a large ascent; use anchor ltop via bbox compensation
    jerga_bbox = draw.textbbox((0, 0), "JERGA", font=f_jerga)
    draw.text((jerga_x - jerga_bbox[0], y - jerga_bbox[1]), "JERGA", font=f_jerga, fill=BLAZE)

    box_y = y + h1 + gap
    # yellow highlight plate
    d = ImageDraw.Draw(base)
    radius = max(4, box_h // 8)
    d.rounded_rectangle((box_x, box_y, box_x + box_w, box_y + box_h), radius=radius, fill=BLAZE)
    obra_bbox = draw.textbbox((0, 0), "DE OBRA", font=f_obra)
    tx = box_x + pad_x - obra_bbox[0]
    ty = box_y + pad_y - obra_bbox[1]
    draw.text((tx, ty), "DE OBRA", font=f_obra, fill=INK)
    return box_y + box_h, box_w, w1


def draw_tagline(base: Image.Image, text: str, cx_or_x: int, y: int, size: int, align="left"):
    draw = ImageDraw.Draw(base)
    fnt = manrope(size)
    bbox = draw.textbbox((0, 0), text, font=fnt)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = cx_or_x - w // 2 if align == "center" else cx_or_x
    draw.text((x - bbox[0], y - bbox[1]), text, font=fnt, fill=TAG)
    return y + h


def compose_cover(hat: Image.Image) -> Image.Image:
    W, H = 1200, 630
    base = Image.new("RGBA", (W, H), INK)
    # glow behind the mark
    tile_size = 390
    tile = hat_tile(hat, tile_size, radius=48, border=8)
    mark_x = 86
    mark_y = (H - tile.size[1]) // 2 + 4
    glow = radial_glow((W, H), (mark_x + tile_size // 2, H // 2), 340, alpha=80)
    base.alpha_composite(glow)
    base.alpha_composite(tile, (mark_x, mark_y))

    text_x = mark_x + tile.size[0] + 54
    # vertically center the title stack
    # estimate height: jerga + gap + obra box + tag gap + tag
    jerga_size, obra_size, tag_size = 148, 92, 28
    # dry-run measurements on a scratch
    scratch = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bottom, _, _ = draw_title_block(scratch, 0, 0, jerga_size, obra_size)
    tag_h = text_size(ImageDraw.Draw(scratch), "Crew slang. Not tourist Spanish.", manrope(tag_size))[1]
    stack_h = bottom + 22 + tag_h
    text_y = (H - stack_h) // 2 - 4
    bottom, _, _ = draw_title_block(base, text_x, text_y, jerga_size, obra_size)
    draw_tagline(base, "Crew slang. Not tourist Spanish.", text_x, bottom + 22, tag_size, align="left")
    return base.convert("RGB")


def compose_portrait(hat: Image.Image, W: int, H: int) -> Image.Image:
    base = Image.new("RGBA", (W, H), INK)
    # scale elements by the shorter dimension, leaving safe areas
    safe_top = int(H * 0.12)
    safe_bot = int(H * 0.10)
    usable = H - safe_top - safe_bot
    tile_size = int(min(W * 0.58, usable * 0.38))
    tile = hat_tile(
        hat,
        tile_size,
        radius=max(18, tile_size // 8),
        border=max(6, tile_size // 48),
    )
    cx = W // 2
    # Title sizes
    jerga_size = max(64, int(W * 0.16))
    obra_size = max(40, int(W * 0.10))
    tag_size = max(18, int(W * 0.032))

    scratch = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    t_bottom, box_w, jerga_w = draw_title_block(scratch, 0, 0, jerga_size, obra_size, align="left")
    tag_h = text_size(ImageDraw.Draw(scratch), "Crew slang. Not tourist Spanish.", manrope(tag_size))[1]
    gap_hat_title = int(tile_size * 0.18)
    gap_title_tag = max(16, int(jerga_size * 0.16))
    stack_h = tile.size[1] + gap_hat_title + t_bottom + gap_title_tag + tag_h
    y0 = safe_top + max(0, (usable - stack_h) // 2)

    glow = radial_glow((W, H), (cx, y0 + tile_size // 2), int(tile_size * 1.05), alpha=70)
    base.alpha_composite(glow)
    base.alpha_composite(tile, (cx - tile.size[0] // 2, y0))

    title_y = y0 + tile.size[1] + gap_hat_title
    bottom, _, _ = draw_title_block(base, cx, title_y, jerga_size, obra_size, align="center")
    draw_tagline(base, "Crew slang. Not tourist Spanish.", cx, bottom + gap_title_tag, tag_size, align="center")
    return base.convert("RGB")


def save_rgb(im: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)
    print(f"wrote {path.relative_to(ROOT)} {im.size[0]}x{im.size[1]} {path.stat().st_size // 1024}KB")


# iPhone / iPad portrait startup sizes: (w, h, css_w, css_h, dpr)
# media queries use device-width/height in CSS pixels.
IOS_SPLASHES = [
    (1320, 2868, 440, 956, 3),  # iPhone 16 Pro Max
    (1290, 2796, 430, 932, 3),  # iPhone 15/14 Pro Max
    (1206, 2622, 402, 874, 3),  # iPhone 16 Pro
    (1179, 2556, 393, 852, 3),  # iPhone 15/14/16 Pro
    (1170, 2532, 390, 844, 3),  # iPhone 13/14/15
    (1284, 2778, 428, 926, 3),  # iPhone 14 Plus / 13 Pro Max
    (1242, 2688, 414, 896, 3),  # iPhone 11 Pro Max / XS Max
    (1125, 2436, 375, 812, 3),  # iPhone X / 11 Pro / 12-13 mini
    (828, 1792, 414, 896, 2),   # iPhone 11 / XR
    (750, 1334, 375, 667, 2),   # iPhone 8 / SE
    (1242, 2208, 414, 736, 3),  # iPhone 8 Plus
    (2048, 2732, 1024, 1366, 2),  # iPad Pro 12.9
    (1668, 2388, 834, 1194, 2),   # iPad Pro 11
    (1640, 2360, 820, 1180, 2),   # iPad Air
    (1620, 2160, 810, 1080, 2),   # iPad 10.2
]


def apple_link_tags() -> str:
    lines = []
    for w, h, css_w, css_h, dpr in IOS_SPLASHES:
        media = (
            f"(device-width: {css_w}px) and (device-height: {css_h}px) "
            f"and (-webkit-device-pixel-ratio: {dpr}) and (orientation: portrait)"
        )
        href = f"splash/{w}x{h}.png"
        lines.append(f'<link rel="apple-touch-startup-image" media="{media}" href="{href}">')
    return "\n".join(lines)


def main() -> None:
    hat = load_hat()
    print("hat source", hat.size)

    cover = compose_cover(hat)
    save_rgb(cover, OUT / "cover.png")

    splash = compose_portrait(hat, 1080, 1920)
    save_rgb(splash, OUT / "splash.png")

    splash_dir = OUT / "splash"
    for w, h, *_ in IOS_SPLASHES:
        im = compose_portrait(hat, w, h)
        save_rgb(im, splash_dir / f"{w}x{h}.png")

    print("\n<!-- apple-touch-startup-image tags -->")
    print(apple_link_tags())


if __name__ == "__main__":
    main()
