#!/usr/bin/env python3
"""Hand-built jobsite illustrations. One SVG per object, yellow/black, no people, no logos.

Run from the repo root: python3 scripts/build_images.py
Writes images/*.svg and scripts/image_catalog.json for build_content.py.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images"
CATALOG = Path(__file__).resolve().parent / "image_catalog.json"

INK = "#0A0A0A"
PAPER = "#FFFFFF"
DEEP = "#E6B800"
COPPER = "#C46B2F"


def svg(body: str) -> str:
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">'
        f'<rect width="128" height="128" rx="18" fill="#FFD100"/>'
        f'<ellipse cx="64" cy="112" rx="36" ry="5" fill="{INK}" opacity="0.14"/>'
        f"{body}</svg>\n"
    )


def wh(attrs: str) -> str:
    """White shape with the shared bold outline."""
    return (
        f'<path {attrs} fill="{PAPER}" stroke="{INK}" stroke-width="5" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    )


def ln(attrs: str, width: str = "5") -> str:
    return (
        f'<path {attrs} fill="none" stroke="{INK}" stroke-width="{width}" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    )


# Each drawing is original geometry for this set: flat, thick outline, no people, no brands.
ICONS: dict[str, str] = {}

ICONS["hard-hat"] = svg(
    wh('d="M26 74h76c0 10-8 16-18 16H44c-10 0-18-6-18-16z"')
    + f'<path d="M36 74c2-30 14-46 28-46s26 16 28 46" fill="{PAPER}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    + f'<rect x="58" y="36" width="12" height="12" rx="2" fill="{INK}"/>'
    + ln('d="M46 74h36"', "4")
)

ICONS["safety-glasses"] = svg(
    wh('d="M16 52h40c2 0 4 4 4 10s-2 12-6 12H22c-6 0-10-6-10-12s2-10 4-10z"')
    + wh('d="M68 52h40c2 0 6 4 6 10s-4 12-10 12H74c-4 0-6-6-6-12s2-10 4-10z"')
    + ln('d="M56 60h16"', "5")
    + ln('d="M18 56 L10 50 M110 56 L118 50"', "5")
    + f'<path d="M24 58h24M76 58h24" stroke="{DEEP}" stroke-width="3" fill="none" stroke-linecap="round"/>'
)

ICONS["harness"] = svg(
    # Laid-flat harness: shoulder straps, chest buckle, waist belt, leg loops. No body.
    ln('d="M40 24c0 22-6 30-6 40h20c0-10-6-18-6-40"', "6")
    + ln('d="M88 24c0 22 6 30 6 40H74c0-10 6-18 6-40"', "6")
    + wh('d="M46 62h36v16H46z"')
    + f'<rect x="58" y="66" width="12" height="8" rx="2" fill="{INK}"/>'
    + wh('d="M30 84h68v12H30z"')
    + f'<rect x="58" y="87" width="12" height="6" rx="1" fill="{INK}"/>'
    + ln('d="M40 96c-6 8-8 16-4 22M88 96c6 8 8 16 4 22"', "5")
    + ln('d="M52 96c-2 10 0 18 6 22M76 96c2 10 0 18-6 22"', "5")
)

ICONS["ppe"] = svg(
    # Kit laid out: hat, glasses, glove, vest. No person.
    f'<path d="M14 40h28c0 6-4 10-8 10h-12c-4 0-8-4-8-10z" fill="{INK}"/>'
    + f'<path d="M18 40c1-12 6-18 10-18s9 6 10 18" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + wh('d="M62 30h18v12H78c-2 0-4 3-4 6s2 6 6 6h8v-4"')
    + ln('d="M80 36h10"', "3")
    + wh('d="M96 28c10 2 16 12 14 24l-8 4c-2-10-6-16-12-16l-2-8z"')
    + ln('d="M100 40c4 4 6 8 6 12"', "3")
    + wh('d="M22 78h40l8 22H18z"')
    + ln('d="M34 78v22M50 78l6 22"', "3")
    + wh('d="M78 74h28v26H78z"')
    + f'<path d="M84 80h16M84 88h16M84 94h10" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
)

ICONS["machine"] = svg(
    wh('d="M22 46h58v40H22z"')
    + ln('d="M30 56h18M30 64h18M30 72h18"', "3")
    + f'<circle cx="92" cy="66" r="16" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="92" cy="66" r="5" fill="{INK}"/>'
    + ln('d="M80 66h-0.1"', "5")
    + f'<rect x="74" y="60" width="10" height="12" fill="{INK}"/>'
    + wh('d="M30 34h28v12H30z"')
)

ICONS["hammer"] = svg(
    f'<g transform="rotate(-38 64 70)">'
    f'<rect x="56" y="36" width="14" height="70" rx="6" fill="{INK}"/>'
    f'<path d="M34 30h58v16c-8 8-16 10-24 10H52c-6 0-14-2-18-10V30z" fill="{PAPER}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M34 32c8-14 16-16 22-8" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    f"</g>"
)

ICONS["drill"] = svg(
    # Pistol drill: chuck and bit point left, grip down, yellow body.
    wh('d="M40 40h52c8 0 14 6 14 14v6H52v-8c0-8-4-12-12-12z"')
    + wh('d="M58 64h22v30H66c-8 0-8-8-8-14V64z"')
    + f'<rect x="22" y="46" width="22" height="16" rx="3" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + ln('d="M10 54h14"', "5")
    + f'<rect x="78" y="34" width="12" height="16" rx="3" fill="{INK}"/>'
)

ICONS["grinder"] = svg(
    wh('d="M58 36h28c8 0 14 8 14 16v6H64v-8c0-8-2-14-6-14z"')
    + f'<circle cx="40" cy="70" r="24" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="40" cy="70" r="8" fill="{INK}"/>'
    + wh('d="M22 46h28v16H28c-6 0-6-6-6-10v-6z"')
    + f'<rect x="78" y="58" width="16" height="28" rx="6" fill="{INK}"/>'
    + ln('d="M18 50c8-16 20-16 28-6"', "5")
)

ICONS["circular-saw"] = svg(
    wh('d="M18 70h92v14H18z"')
    + f'<circle cx="62" cy="62" r="26" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="62" cy="62" r="7" fill="{INK}"/>'
    + ln('d="M62 40v10M62 74v10M40 62h10M74 62h10M46 46l7 7M72 72l7 7M78 46l-7 7"', "3")
    + wh('d="M70 28h26v22H78c-8 0-8-8-8-14v-8z"')
    + f'<rect x="86" y="18" width="10" height="22" rx="4" fill="{INK}"/>'
)

ICONS["tape-measure"] = svg(
    wh('d="M24 36h46v56H36c-10 0-12-10-12-20V36z"')
    + f'<circle cx="46" cy="64" r="12" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + wh('d="M70 58h40v14H70z"')
    + ln('d="M78 65v8M88 65v8M98 65v8"', "3")
    + f'<rect x="104" y="54" width="8" height="8" fill="{INK}"/>'
)

ICONS["level"] = svg(
    wh('d="M12 52h104v24H12z"')
    + f'<rect x="48" y="46" width="32" height="36" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="64" cy="64" r="6" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M64 46v-6M64 82v6"', "3")
    + f'<rect x="22" y="58" width="16" height="12" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>'
    + f'<rect x="90" y="58" width="16" height="12" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>'
    + f'<circle cx="30" cy="64" r="3" fill="{INK}"/>'
    + f'<circle cx="98" cy="64" r="3" fill="{INK}"/>'
)

ICONS["ladder"] = svg(
    ln('d="M40 18 L32 108"', "6")
    + ln('d="M88 18 L96 108"', "6")
    + ln('d="M38 36h52M36 54h56M35 72h58M34 90h60"', "5")
)

ICONS["scaffold"] = svg(
    ln('d="M28 100V28M52 100V28M76 100V28M100 100V28"', "5")
    + ln('d="M28 28h72M28 100h72"', "5")
    + wh('d="M24 58h80v8H24z"')
    + ln('d="M28 44h72M28 78h72"', "4")
    + ln('d="M28 58 L52 28M52 58 L76 28M76 58 L100 28"', "3")
    + wh('d="M22 24h12v8H22z"')
    + wh('d="M94 24h12v8H94z"')
)

ICONS["wrench"] = svg(
    # Adjustable wrench: open jaw, worm screw, long handle.
    f'<g transform="rotate(-42 64 66)">'
    + wh('d="M54 46h16l6 58h-16z"')
    + wh('d="M36 18h28v22H50v12H40V30H36z"')
    + wh('d="M64 24h26v14H64z"')
    + f'<circle cx="62" cy="46" r="8" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + ln('d="M56 46h12"', "3")
    + f"</g>"
)

ICONS["pliers"] = svg(
    # Linesman pliers: flat jaws on top, pivot, two handles.
    wh('d="M46 16h12l6 28H52z"')
    + wh('d="M70 16h12l-2 28H64z"')
    + ln('d="M58 16v20M76 16v20"', "3")
    + f'<circle cx="64" cy="52" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="64" cy="52" r="3" fill="{INK}"/>'
    + ln('d="M56 60 L34 100"', "7")
    + ln('d="M72 60 L94 100"', "7")
    + f'<rect x="24" y="96" width="18" height="12" rx="5" fill="{INK}"/>'
    + f'<rect x="86" y="96" width="18" height="12" rx="5" fill="{INK}"/>'
)

ICONS["screwdriver"] = svg(
    f'<g transform="rotate(-40 64 64)">'
    f'<rect x="54" y="18" width="20" height="46" rx="8" fill="{INK}"/>'
    f'<rect x="58" y="28" width="12" height="6" rx="2" fill="{DEEP}"/>'
    f'<rect x="60" y="60" width="8" height="36" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    f'<path d="M58 96h12l-6 12z" fill="{INK}"/>'
    f"</g>"
)

ICONS["shovel"] = svg(
    f'<rect x="58" y="16" width="12" height="58" rx="5" fill="{INK}"/>'
    + wh('d="M36 70h56l-8 36c-2 6-10 8-20 8s-18-2-20-8z"')
    + ln('d="M64 78v28"', "3")
    + f'<rect x="52" y="14" width="24" height="10" rx="4" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
)

ICONS["wheelbarrow"] = svg(
    wh('d="M28 48h62l10 28H36z"')
    + f'<circle cx="36" cy="90" r="16" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="36" cy="90" r="5" fill="{INK}"/>'
    + ln('d="M52 76 L28 104M70 76 L108 98"', "5")
    + ln('d="M96 70 L114 58"', "5")
    + f'<rect x="108" y="50" width="10" height="8" rx="2" fill="{INK}"/>'
    + ln('d="M44 48 L52 36h28"', "4")
)

ICONS["toolbox"] = svg(
    wh('d="M18 52h92v42H18z"')
    + wh('d="M40 40h48v12H40z"')
    + ln('d="M52 40v-6c0-8 24-8 24 0v6"', "5")
    + f'<rect x="56" y="66" width="16" height="12" rx="2" fill="{INK}"/>'
    + ln('d="M18 74h92"', "4")
)

ICONS["extension-cord"] = svg(
    f'<circle cx="58" cy="64" r="28" fill="none" stroke="{INK}" stroke-width="8"/>'
    + f'<circle cx="58" cy="64" r="12" fill="none" stroke="{INK}" stroke-width="6"/>'
    + ln('d="M84 58h22"', "6")
    + wh('d="M104 50h14v20h-14z"')
    + f'<rect x="118" y="54" width="6" height="4" fill="{INK}"/>'
    + f'<rect x="118" y="64" width="6" height="4" fill="{INK}"/>'
)

ICONS["cement"] = svg(
    wh('d="M30 40h54l14 14v42H30z"')
    + ln('d="M84 40v14h14"', "5")
    + f'<path d="M40 70h36v8H40z" fill="{INK}"/>'
    + f'<path d="M46 88c8 10 20 10 28 0" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + f'<circle cx="48" cy="100" r="3" fill="{INK}"/>'
    + f'<circle cx="60" cy="104" r="3" fill="{INK}"/>'
    + f'<circle cx="74" cy="100" r="2.5" fill="{INK}"/>'
)

ICONS["concrete"] = svg(
    # Wet slab with trowel ripples. No boat-like shape.
    wh('d="M14 50h100v40H14z"')
    + ln('d="M24 64c8 7 14 7 22 0s14-7 22 0 14 7 22 0 14-7 20 0"', "4")
    + ln('d="M24 78c8 7 14 7 22 0s14-7 22 0 14 7 22 0 14-7 20 0"', "4")
    + ln('d="M64 50v40"', "4")
)

ICONS["brick"] = svg(
    wh('d="M24 40h80v36H24z"')
    + f'<ellipse cx="44" cy="58" rx="7" ry="5" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + f'<ellipse cx="84" cy="58" rx="7" ry="5" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M24 76h80"', "4")
    + wh('d="M34 76h60v14H34z"')
)

ICONS["rebar"] = svg(
    ln('d="M28 28v72M50 28v72M72 28v72M94 28v72"', "6")
    + ln('d="M20 42h88M20 64h88M20 86h88"', "6")
    + f'<circle cx="28" cy="42" r="3" fill="{DEEP}"/>'
    + f'<circle cx="50" cy="64" r="3" fill="{DEEP}"/>'
    + f'<circle cx="72" cy="86" r="3" fill="{DEEP}"/>'
    + f'<circle cx="94" cy="42" r="3" fill="{DEEP}"/>'
)

ICONS["lumber"] = svg(
    wh('d="M22 70h84v14H22z"')
    + wh('d="M28 54h72v14H28z"')
    + wh('d="M34 38h60v14H34z"')
    + f'<path d="M22 70h10v14H22zM96 70h10v14H96z" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M40 46c6 4 8 4 14 0M62 46c6 4 8 4 14 0"', "2")
)

ICONS["steel"] = svg(
    wh('d="M22 28h84v18H22z"')
    + wh('d="M50 46h28v36H50z"')
    + wh('d="M22 82h84v18H22z"')
    + ln('d="M30 37h68M30 91h68"', "3")
)

ICONS["sand"] = svg(
    wh('d="M20 88c10-28 22-40 44-40s34 12 44 40z"')
    + f'<circle cx="46" cy="78" r="3" fill="{INK}"/>'
    + f'<circle cx="64" cy="70" r="3" fill="{INK}"/>'
    + f'<circle cx="80" cy="80" r="2.5" fill="{INK}"/>'
    + f'<circle cx="58" cy="86" r="2" fill="{INK}"/>'
    + ln('d="M18 96h92"', "5")
)

ICONS["gravel"] = svg(
    f'<ellipse cx="40" cy="78" rx="16" ry="12" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + f'<ellipse cx="64" cy="66" rx="18" ry="13" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + f'<ellipse cx="88" cy="80" rx="15" ry="11" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + f'<ellipse cx="52" cy="92" rx="14" ry="10" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + f'<ellipse cx="78" cy="94" rx="12" ry="9" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + f'<ellipse cx="30" cy="94" rx="10" ry="8" fill="{INK}"/>'
)

ICONS["plywood"] = svg(
    wh('d="M26 24h76v80H26z"')
    + ln('d="M36 36c10 6 14 6 24 0s14-6 24 0M36 52c10 6 14 6 24 0s14-6 24 0M36 68c10 6 14 6 24 0s14-6 24 0M36 84c10 6 14 6 24 0s14-6 24 0"', "3")
)

ICONS["drywall"] = svg(
    wh('d="M22 28h84v72H22z"')
    + ln('d="M22 40c8 4 8 4 0 8M106 40c-8 4-8 4 0 8"', "3")
    + f'<circle cx="48" cy="58" r="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + f'<circle cx="80" cy="78" r="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M34 96h60"', "3")
)

ICONS["mig-welder"] = svg(
    wh('d="M18 40h52v48H18z"')
    + f'<rect x="26" y="48" width="18" height="10" rx="2" fill="{INK}"/>'
    + f'<circle cx="56" cy="72" r="5" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M70 58c12 2 16 8 16 16"', "5")
    + wh('d="M84 68h22v16H88c-4 0-4-6-4-8v-8z"')
    + f'<rect x="100" y="84" width="6" height="14" fill="{INK}"/>'
    + ln('d="M30 28h28"', "5")
)

ICONS["tig-welder"] = svg(
    wh('d="M16 44h48v44H16z"')
    + ln('d="M26 56h28M26 66h20"', "3")
    + ln('d="M64 60h18"', "4")
    + wh('d="M80 50h10v28H80z"')
    + f'<path d="M85 78l-4 18h18l-4-18z" fill="{PAPER}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
    + ln('d="M90 96v10"', "3")
    + f'<circle cx="32" cy="76" r="4" fill="{INK}"/>'
)

ICONS["stick-welder"] = svg(
    wh('d="M18 36h46v40H18z"')
    + ln('d="M28 48h26M28 58h18"', "3")
    + f'<rect x="48" y="66" width="22" height="14" rx="3" fill="{INK}"/>'
    + ln('d="M70 72h16"', "5")
    + f'<rect x="84" y="64" width="14" height="16" rx="3" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + ln('d="M96 58l14-22"', "5")
    + f'<path d="M108 30l10 6-8 4z" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
)

ICONS["welding-helmet"] = svg(
    wh('d="M30 28h68c4 18 4 40-6 62H36C26 68 26 46 30 28z"')
    + f'<rect x="40" y="48" width="48" height="28" rx="4" fill="{INK}"/>'
    + f'<rect x="48" y="54" width="32" height="8" fill="{DEEP}"/>'
    + wh('d="M24 34h14v18H24z"')
    + ln('d="M46 28c6-10 30-10 36 0"', "4")
)

ICONS["welding-gloves"] = svg(
    # Pair of gauntlet gloves, laid flat. No hands inside them.
    wh('d="M16 58h26l6 8 6-14h8v18l8 4v28H22c-6 0-6-8-6-16V58z"')
    + ln('d="M22 78h36"', "3")
    + wh('d="M70 50h26l6 8 6-14h8v18l6 6v26H76c-6 0-6-8-6-16V50z"')
    + ln('d="M76 72h40"', "3")
    + f'<path d="M20 90h40M74 86h42" stroke="{DEEP}" stroke-width="4" stroke-linecap="round"/>'
)

ICONS["electrode"] = svg(
    f'<g transform="rotate(-35 64 64)">'
    f'<rect x="24" y="56" width="70" height="14" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    f'<rect x="24" y="56" width="16" height="14" rx="6" fill="{INK}"/>'
    f'<rect x="86" y="56" width="18" height="14" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    f'<path d="M40 63h8M52 63h8M64 63h8" stroke="{INK}" stroke-width="2"/>'
    f"</g>"
)

ICONS["welding-wire"] = svg(
    f'<circle cx="64" cy="64" r="30" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="64" cy="64" r="10" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + ln('d="M64 34c10 8 10 18 0 26s-10 18 0 30"', "3")
    + ln('d="M44 44c8 6 14 8 22 4M86 78c-8 6-16 6-24 0"', "3")
    + ln('d="M94 40c8 4 12 4 16-2"', "4")
)

ICONS["torch"] = svg(
    f'<g transform="rotate(-40 64 64)">'
    + wh('d="M22 52h46v20H34c-8 0-12-6-12-10v-10z"')
    + wh('d="M66 56h22v12H66z"')
    + f'<path d="M88 58l16 6-16 6z" fill="{INK}"/>'
    + f'<rect x="30" y="70" width="10" height="18" rx="3" fill="{INK}"/>'
    + ln('d="M18 62h8"', "5")
    + f"</g>"
)

ICONS["gas-cylinder"] = svg(
    wh('d="M48 36h32v62H48z"')
    + f'<rect x="46" y="28" width="36" height="12" rx="3" fill="{INK}"/>'
    + wh('d="M58 16h12v14H58z"')
    + f'<circle cx="64" cy="16" r="5" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M80 20h12"', "4")
    + ln('d="M56 50h16M56 66h16"', "3")
)

ICONS["slag"] = svg(
    # Steel plate, a raised weld bead, and a few slag chips.
    wh('d="M14 74h100v18H14z"')
    + f'<path d="M22 74l8-14 8 14 8-14 8 14 8-14 8 14 8-14 8 14 8-14 8 14" fill="{DEEP}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
    + wh('d="M24 46l10 14H22z"')
    + wh('d="M96 42l12 16H92z"')
    + f'<circle cx="48" cy="40" r="5" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>'
)

ICONS["cable"] = svg(
    ln('d="M24 78c12-28 20-28 32 0s20 28 32 0 16-20 20-16"', "8")
    + wh('d="M18 70h16v16H18z"')
    + ln('d="M22 86v8M30 86v8"', "3")
)

ICONS["breaker"] = svg(
    wh('d="M36 20h56v88H36z"')
    + wh('d="M48 36h32v40H48z"')
    + f'<rect x="58" y="44" width="12" height="22" rx="3" fill="{INK}"/>'
    + ln('d="M64 32v-4M52 84h24"', "3")
    + f'<circle cx="56" cy="96" r="3" fill="{INK}"/>'
    + f'<circle cx="72" cy="96" r="3" fill="{INK}"/>'
)

ICONS["multimeter"] = svg(
    wh('d="M28 22h72v70H28z"')
    + f'<rect x="38" y="32" width="52" height="22" rx="3" fill="{INK}"/>'
    + f'<path d="M44 42h28" stroke="{DEEP}" stroke-width="4" stroke-linecap="round"/>'
    + f'<circle cx="48" cy="70" r="6" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>'
    + f'<circle cx="68" cy="70" r="6" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>'
    + f'<circle cx="88" cy="70" r="6" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M40 92c-8 10-8 16 0 22"', "4")
    + ln('d="M88 92c8 10 8 16 0 22"', "4")
    + f'<circle cx="36" cy="116" r="4" fill="{INK}"/>'
    + f'<circle cx="92" cy="116" r="4" fill="{INK}"/>'
)

ICONS["electrical-tape"] = svg(
    f'<circle cx="64" cy="64" r="30" fill="{INK}"/>'
    + f'<circle cx="64" cy="64" r="12" fill="{DEEP}" stroke="{PAPER}" stroke-width="4"/>'
    + ln('d="M88 48c16 8 18 20 8 28"', "6")
    + wh('d="M96 72h18v12H96z"')
)

ICONS["lockout"] = svg(
    wh('d="M40 58h48v40H40z"')
    + ln('d="M50 58V42c0-12 28-12 28 0v16"', "6")
    + f'<circle cx="64" cy="74" r="6" fill="{INK}"/>'
    + ln('d="M64 80v10"', "4")
    + wh('d="M78 36h28v22H78z"')
    + f'<circle cx="86" cy="42" r="3" fill="{INK}"/>'
    + ln('d="M92 40h8"', "3")
)

ICONS["slab"] = svg(
    wh('d="M14 46h100v42H14z"')
    + ln('d="M14 67h100M47 46v42M80 46v42"', "4")
    + f'<circle cx="30" cy="56" r="3" fill="{INK}" opacity="0.45"/>'
    + f'<circle cx="96" cy="78" r="2.5" fill="{INK}" opacity="0.45"/>'
)

ICONS["formwork"] = svg(
    wh('d="M20 40h22v52H20z"')
    + wh('d="M86 40h22v52H86z"')
    + f'<rect x="42" y="48" width="44" height="36" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + ln('d="M20 52h22M20 68h22M20 80h22M86 52h22M86 68h22M86 80h22"', "3")
    + ln('d="M28 28v12M100 28v12"', "4")
)

ICONS["duct"] = svg(
    wh('d="M16 36h46v28H16z"')
    + wh('d="M62 36h28v56H62z"')
    + ln('d="M24 50h28M70 48v36"', "3")
    + wh('d="M54 48h16v12H54z"')
)

ICONS["condenser"] = svg(
    wh('d="M24 28h80v72H24z"')
    + f'<circle cx="64" cy="60" r="22" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + ln('d="M64 40v40M44 60h40M50 46l28 28M78 46L50 74"', "3")
    + f'<circle cx="64" cy="60" r="5" fill="{INK}"/>'
    + ln('d="M32 92h64"', "4")
)

ICONS["evaporator"] = svg(
    wh('d="M36 24h56v80H36z"')
    + ln('d="M48 24v80M64 24v80M80 24v80"', "4")
    + ln('d="M36 40h56M36 56h56M36 72h56M36 88h56"', "3")
    + wh('d="M28 20h72v10H28z"')
)

ICONS["thermostat"] = svg(
    wh('d="M40 18h48v92H40z"')
    + f'<circle cx="64" cy="58" r="20" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="64" cy="58" r="4" fill="{INK}"/>'
    + ln('d="M64 58 L76 46"', "4")
    + ln('d="M52 90h24"', "4")
    + f'<rect x="56" y="28" width="16" height="6" rx="2" fill="{INK}"/>'
)

ICONS["refrigerant"] = svg(
    wh('d="M50 40h28v58H50z"')
    + f'<rect x="46" y="32" width="36" height="12" rx="3" fill="{INK}"/>'
    + wh('d="M58 18h12v16H58z"')
    + ln('d="M78 22h16c6 0 8 6 4 10"', "4")
    + f'<circle cx="64" cy="70" r="8" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M58 66h12"', "3")
)

ICONS["ac-unit"] = svg(
    wh('d="M16 36h96v48H16z"')
    + ln('d="M28 50h72M28 60h72M28 70h72"', "4")
    + wh('d="M24 84h20v12H24z"')
    + f'<circle cx="100" cy="46" r="5" fill="{INK}"/>'
)

ICONS["air-filter"] = svg(
    wh('d="M28 22h72v84H28z"')
    + ln('d="M40 22c8 10 8 10 0 20s-8 10 0 20 8 10 0 20 8 10 0 24"', "4")
    + ln('d="M56 22c8 10 8 10 0 20s-8 10 0 20 8 10 0 20 8 10 0 24"', "4")
    + ln('d="M72 22c8 10 8 10 0 20s-8 10 0 20 8 10 0 20 8 10 0 24"', "4")
    + ln('d="M88 22c8 10 8 10 0 20s-8 10 0 20 8 10 0 20 8 10 0 24"', "4")
)

ICONS["pipe"] = svg(
    wh('d="M14 50h40v28H14z"')
    + wh('d="M74 50h40v28H74z"')
    + f'<rect x="48" y="44" width="32" height="40" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="5"/>'
    + ln('d="M22 64h20M86 64h20"', "3")
)

ICONS["pvc"] = svg(
    wh('d="M18 58h48v20H18z"')
    + wh('d="M54 30h22v48H54z"')
    + f'<rect x="48" y="52" width="28" height="26" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + ln('d="M62 38v10M30 68h16"', "3")
)

ICONS["copper"] = svg(
    f'<path d="M18 58h48v20H18z" fill="{COPPER}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    + f'<path d="M54 30h22v48H54z" fill="{COPPER}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    + f'<rect x="48" y="52" width="28" height="26" fill="{COPPER}" stroke="{INK}" stroke-width="5"/>'
    + ln('d="M62 38v10M30 68h16"', "3")
)

ICONS["shutoff"] = svg(
    wh('d="M16 58h96v16H16z"')
    + f'<circle cx="64" cy="50" r="22" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + ln('d="M64 32v36M46 50h36M52 38l24 24M76 38L52 62"', "4")
    + f'<circle cx="64" cy="50" r="4" fill="{INK}"/>'
    + f'<rect x="58" y="66" width="12" height="16" fill="{INK}"/>'
)

ICONS["water"] = svg(
    wh('d="M64 22c16 18 28 32 28 48a28 28 0 0 1-56 0c0-16 12-30 28-48z"')
    + ln('d="M48 70c6 6 10 6 16 0s10-6 16 0"', "4")
    + f'<path d="M52 58c4-8 8-8 12 0" fill="none" stroke="{DEEP}" stroke-width="4" stroke-linecap="round"/>'
)

ICONS["drain"] = svg(
    f'<circle cx="64" cy="64" r="34" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="64" cy="64" r="16" fill="{DEEP}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="64" cy="64" r="6" fill="{INK}"/>'
    + ln('d="M64 30v12M64 86v12M30 64h12M86 64h12M40 40l8 8M80 80l8 8M88 40l-8 8M48 80l-8 8"', "4")
)

ICONS["water-heater"] = svg(
    wh('d="M40 28h48v74H40z"')
    + f'<rect x="40" y="22" width="48" height="12" rx="4" fill="{INK}"/>'
    + ln('d="M52 18V10M76 18V10"', "4")
    + wh('d="M52 48h24v16H52z"')
    + f'<circle cx="64" cy="84" r="6" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + ln('d="M88 40h12v10"', "4")
)

ICONS["plank"] = svg(
    wh('d="M12 48h104v32H12z"')
    + ln('d="M28 48v32M52 48v32M76 48v32M100 48v32"', "4")
    + ln('d="M20 64c8 4 10 4 16 0M60 64c8 4 10 4 16 0"', "2")
)

ICONS["guardrail"] = svg(
    ln('d="M24 96V40M48 96V32M80 96V32M104 96V40"', "6")
    + ln('d="M18 40h92M18 62h92"', "6")
    + f'<circle cx="48" cy="40" r="4" fill="{INK}"/>'
    + f'<circle cx="80" cy="40" r="4" fill="{INK}"/>'
)

ICONS["caster"] = svg(
    wh('d="M36 28h56v16H36z"')
    + f'<rect x="56" y="44" width="16" height="18" fill="{INK}"/>'
    + f'<circle cx="64" cy="82" r="22" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="64" cy="82" r="6" fill="{INK}"/>'
    + wh('d="M84 70h22v10H86z"')
    + f'<rect x="100" y="64" width="8" height="8" rx="2" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
)

ICONS["excavator"] = svg(
    f'<rect x="18" y="78" width="74" height="16" rx="8" fill="{INK}"/>'
    + f'<rect x="26" y="74" width="14" height="22" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + f'<rect x="46" y="74" width="14" height="22" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + f'<rect x="66" y="74" width="14" height="22" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + wh('d="M28 70h52l8 10H24z"')
    + wh('d="M58 42h26v22H58z"')
    + f'<rect x="63" y="47" width="14" height="10" fill="{INK}"/>'
    + ln('d="M58 52 H40 L24 34"', "6")
    + wh('d="M12 30h20l4 16H16z"')
    + ln('d="M16 46h16"', "3")
)

ICONS["bulldozer"] = svg(
    f'<rect x="22" y="70" width="78" height="18" rx="8" fill="{INK}"/>'
    + f'<rect x="30" y="66" width="16" height="24" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + f'<rect x="54" y="66" width="16" height="24" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + f'<rect x="76" y="66" width="16" height="24" rx="4" fill="{DEEP}" stroke="{INK}" stroke-width="3"/>'
    + wh('d="M36 48h50v24H40z"')
    + wh('d="M70 34h24v20H70z"')
    + f'<rect x="75" y="39" width="14" height="10" fill="{INK}"/>'
    + wh('d="M14 40h16v40H14z"')
    + ln('d="M30 48 H36M30 78H36"', "4")
)

ICONS["loader"] = svg(
    f'<rect x="28" y="74" width="70" height="16" rx="8" fill="{INK}"/>'
    + f'<circle cx="46" cy="82" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + f'<circle cx="84" cy="82" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    + wh('d="M48 52h40v24H52z"')
    + wh('d="M70 36h22v18H70z"')
    + f'<rect x="74" y="40" width="12" height="8" fill="{INK}"/>'
    + ln('d="M48 64 L24 56"', "6")
    + wh('d="M10 46h22v22H14z"')
)

ICONS["crane"] = svg(
    ln('d="M40 100V28"', "8")
    + wh('d="M28 100h24v10H28z"')
    + ln('d="M40 32 H108"', "6")
    + ln('d="M40 32 L78 48"', "4")
    + ln('d="M96 32v28"', "4")
    + wh('d="M88 60h16v10H88z"')
    + ln('d="M92 70v8M100 70v8"', "3")
    + wh('d="M30 48h18v16H30z"')
    + f'<rect x="34" y="52" width="8" height="7" fill="{INK}"/>'
)

ICONS["forklift"] = svg(
    wh('d="M30 46h40v28H34z"')
    + wh('d="M58 30h20v20H58z"')
    + f'<rect x="62" y="35" width="12" height="9" fill="{INK}"/>'
    + f'<circle cx="42" cy="86" r="14" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="78" cy="88" r="10" fill="{INK}"/>'
    + ln('d="M92 70V40"', "6")
    + ln('d="M92 48h24M92 58h20"', "5")
    + f'<rect x="18" y="74" width="16" height="8" fill="{INK}"/>'
)

ICONS["dump-truck"] = svg(
    wh('d="M14 48h58l10 20v16H14z"')
    + wh('d="M82 60h28v24H82z"')
    + f'<rect x="88" y="66" width="14" height="10" fill="{INK}"/>'
    + f'<circle cx="36" cy="92" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="96" cy="92" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="36" cy="92" r="4" fill="{INK}"/>'
    + f'<circle cx="96" cy="92" r="4" fill="{INK}"/>'
    + ln('d="M22 48 L34 32"', "4")
)

ICONS["load"] = svg(
    # Wooden crate on a pallet, with a strap. Not a sheet of paper.
    wh('d="M30 36h68v52H30z"')
    + ln('d="M30 52h68M30 68h68"', "4")
    + ln('d="M46 36v52M82 36v52"', "4")
    + f'<rect x="58" y="36" width="12" height="52" fill="{DEEP}" stroke="{INK}" stroke-width="4"/>'
    + wh('d="M18 88h92v8H18z"')
    + f'<rect x="26" y="96" width="12" height="10" fill="{INK}"/>'
    + f'<rect x="58" y="96" width="12" height="10" fill="{INK}"/>'
    + f'<rect x="90" y="96" width="12" height="10" fill="{INK}"/>'
)


ALTS: dict[str, tuple[str, str]] = {
    "hard-hat": ("Hard hat", "Casco"),
    "safety-glasses": ("Safety glasses", "Gafas de seguridad"),
    "harness": ("Safety harness laid flat", "Arnés de seguridad"),
    "ppe": ("PPE kit: hat, glasses, gloves, and vest", "Equipo de protección personal"),
    "machine": ("Generic jobsite machine", "Máquina de obra"),
    "hammer": ("Claw hammer", "Martillo de uña"),
    "drill": ("Power drill", "Taladro"),
    "grinder": ("Angle grinder", "Amoladora"),
    "circular-saw": ("Circular saw", "Sierra circular"),
    "tape-measure": ("Tape measure", "Cinta métrica"),
    "level": ("Spirit level", "Nivel"),
    "ladder": ("Ladder", "Escalera"),
    "scaffold": ("Scaffold frame", "Andamio"),
    "wrench": ("Adjustable wrench", "Llave inglesa"),
    "pliers": ("Pliers", "Alicates"),
    "screwdriver": ("Screwdriver", "Destornillador"),
    "shovel": ("Shovel", "Pala"),
    "wheelbarrow": ("Wheelbarrow", "Carretilla"),
    "toolbox": ("Toolbox", "Caja de herramientas"),
    "extension-cord": ("Extension cord and plug", "Extensión eléctrica"),
    "cement": ("Bag of cement", "Costal de cemento"),
    "concrete": ("Wet concrete", "Concreto fresco"),
    "brick": ("Brick", "Ladrillo"),
    "rebar": ("Rebar grid", "Varilla"),
    "lumber": ("Stack of lumber", "Madera"),
    "steel": ("Steel I-beam", "Viga de acero"),
    "sand": ("Pile of sand", "Montón de arena"),
    "gravel": ("Pile of gravel", "Grava"),
    "plywood": ("Sheet of plywood", "Triplay"),
    "drywall": ("Sheet of drywall", "Tablaroca"),
    "mig-welder": ("MIG welder and gun", "Soldadora MIG"),
    "tig-welder": ("TIG welder and torch", "Soldadora TIG"),
    "stick-welder": ("Stick welder and electrode holder", "Soldadora de electrodo"),
    "welding-helmet": ("Welding helmet", "Casco de soldar"),
    "welding-gloves": ("Welding gloves", "Guantes de soldadura"),
    "electrode": ("Welding electrode", "Electrodo"),
    "welding-wire": ("Spool of welding wire", "Rollo de alambre"),
    "torch": ("Welding torch", "Antorcha de soldar"),
    "gas-cylinder": ("Shielding-gas cylinder", "Cilindro de gas"),
    "slag": ("Weld slag chips", "Escoria de soldadura"),
    "cable": ("Electrical cable", "Cable"),
    "breaker": ("Circuit breaker", "Breaker"),
    "multimeter": ("Multimeter with probes", "Multímetro"),
    "electrical-tape": ("Roll of electrical tape", "Cinta aislante"),
    "lockout": ("Lockout padlock and tag", "Candado de bloqueo"),
    "slab": ("Concrete slab", "Losa"),
    "formwork": ("Concrete formwork", "Cimbra"),
    "duct": ("Air duct", "Ducto"),
    "condenser": ("Outdoor condenser unit", "Condensador"),
    "evaporator": ("Evaporator coil", "Evaporador"),
    "thermostat": ("Thermostat", "Termostato"),
    "refrigerant": ("Refrigerant cylinder", "Refrigerante"),
    "ac-unit": ("Air-conditioning unit", "Unidad de aire"),
    "air-filter": ("Pleated air filter", "Filtro de aire"),
    "pipe": ("Pipe with a coupling", "Tubería"),
    "pvc": ("White PVC pipe elbow", "Tubo de PVC"),
    "copper": ("Copper pipe elbow", "Tubo de cobre"),
    "shutoff": ("Shutoff valve", "Llave de paso"),
    "water": ("Water", "Agua"),
    "drain": ("Floor drain", "Drenaje"),
    "water-heater": ("Water heater", "Calentador de agua"),
    "plank": ("Scaffold plank", "Plataforma"),
    "guardrail": ("Guardrail", "Barandal"),
    "caster": ("Scaffold caster wheel", "Rueda de andamio"),
    "excavator": ("Excavator", "Excavadora"),
    "bulldozer": ("Bulldozer", "Buldócer"),
    "loader": ("Front-end loader", "Cargadora"),
    "crane": ("Crane and hook", "Grúa"),
    "forklift": ("Forklift", "Montacargas"),
    "dump-truck": ("Dump truck", "Camión de volteo"),
    "load": ("Strapped load on a pallet", "Carga"),
}

# Exact Spanish lines from the phrase book. Commands, Jerga, Daily, and shouts are absent on purpose.
BY_PHRASE: dict[str, str] = {
    "Ponte el casco.": "hard-hat",
    "Usa las gafas.": "safety-glasses",
    "Necesitas el arnés.": "harness",
    "El arnés está jodido.": "harness",
    "Se requiere EPP siempre.": "ppe",
    "Aléjate de la máquina.": "machine",
    "el martillo": "hammer",
    "el taladro": "drill",
    "la amoladora": "grinder",
    "la sierra circular": "circular-saw",
    "la cinta métrica": "tape-measure",
    "el nivel": "level",
    "la escalera": "ladder",
    "el andamio": "scaffold",
    "la llave inglesa": "wrench",
    "los alicates": "pliers",
    "el destornillador": "screwdriver",
    "la pala": "shovel",
    "la carretilla": "wheelbarrow",
    "Pásame el martillo.": "hammer",
    "¿Dónde está el taladro?": "drill",
    "Trae las herramientas.": "toolbox",
    "¿Tienes una extensión?": "extension-cord",
    "¿Dónde está esa pinche llave?": "wrench",
    "el cemento": "cement",
    "el concreto": "concrete",
    "el ladrillo": "brick",
    "la varilla": "rebar",
    "la madera": "lumber",
    "el acero": "steel",
    "la arena": "sand",
    "la grava": "gravel",
    "el triplay": "plywood",
    "la tablaroca": "drywall",
    "Necesitamos más cemento.": "cement",
    "¿Dónde está la varilla?": "rebar",
    "Deja la madera aquí.": "lumber",
    "la soldadora MIG": "mig-welder",
    "la soldadora TIG": "tig-welder",
    "soldadura de electrodo": "stick-welder",
    "el casco de soldar": "welding-helmet",
    "los guantes de soldadura": "welding-gloves",
    "el electrodo": "electrode",
    "el alambre": "welding-wire",
    "la antorcha": "torch",
    "el gas de protección": "gas-cylinder",
    "Limpia la escoria.": "slag",
    "Usa el casco.": "welding-helmet",
    "¿Necesitas más electrodos?": "electrode",
    "el cable": "cable",
    "el breaker": "breaker",
    "Apaga el breaker.": "breaker",
    "el multímetro": "multimeter",
    "la cinta aislante": "electrical-tape",
    "No toques el cable.": "cable",
    "Bloqueo y etiquetado.": "lockout",
    "el colado": "concrete",
    "la losa": "slab",
    "la cimbra": "formwork",
    "Mezcla el concreto.": "concrete",
    "La losa está lista.": "slab",
    "Necesitamos más varilla.": "rebar",
    "Nivela el concreto.": "concrete",
    "No camines en el fresco.": "concrete",
    "el ducto": "duct",
    "el condensador": "condenser",
    "el evaporador": "evaporator",
    "el termostato": "thermostat",
    "el refrigerante": "refrigerant",
    "la unidad de aire": "ac-unit",
    "Apaga la unidad.": "ac-unit",
    "Cambia el filtro.": "air-filter",
    "El ducto está tapado.": "duct",
    "la tubería": "pipe",
    "el PVC": "pvc",
    "el cobre": "copper",
    "la llave de paso": "shutoff",
    "Cierra el agua.": "water",
    "el drenaje": "drain",
    "el calentador": "water-heater",
    "Suelda el cobre.": "copper",
    "Pega el PVC.": "pvc",
    "¿Dónde está la llave principal?": "shutoff",
    "arma el andamio": "scaffold",
    "la plataforma": "plank",
    "el barandal": "guardrail",
    "la rueda": "caster",
    "Traba las ruedas.": "caster",
    "No sobrecargues el andamio.": "scaffold",
    "usa el arnés en altura": "harness",
    "el nivel del andamio": "scaffold",
    "la excavadora": "excavator",
    "el buldócer": "bulldozer",
    "la cargadora": "loader",
    "la grúa": "crane",
    "el montacargas": "forklift",
    "el camión de volteo": "dump-truck",
    "Levanta la carga.": "load",
    "Baja la carga.": "load",
}


def main() -> None:
    missing_icons = [k for k in ALTS if k not in ICONS]
    extra_icons = [k for k in ICONS if k not in ALTS]
    if missing_icons or extra_icons:
        raise SystemExit(f"icon/alt mismatch missing={missing_icons} extra={extra_icons}")
    unknown = sorted({v for v in BY_PHRASE.values() if v not in ICONS})
    if unknown:
        raise SystemExit(f"phrase map uses unknown keys: {unknown}")

    # Confirm every mapped line exists in the phrase book and is not a shout/command category.
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "build_content", Path(__file__).resolve().parent / "build_content.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    raw = {(cat, es) for cat, es, _en, _tip in mod.RAW}
    es_seen = {}
    for cat, es, _en, _tip in mod.RAW:
        es_seen.setdefault(es, []).append(cat)
    problems = []
    for es, key in BY_PHRASE.items():
        if es not in {e for _c, e in raw}:
            problems.append(f"not in phrase book: {es}")
            continue
        cats = es_seen[es]
        if any(c in {"Commands", "Jerga", "Daily"} for c in cats):
            problems.append(f"excluded category: {es} {cats}")
    if problems:
        raise SystemExit("\n".join(problems))

    OUT.mkdir(parents=True, exist_ok=True)
    # Remove stale illustrations so the folder only holds this set.
    for old in OUT.glob("*.svg"):
        if old.stem not in ICONS:
            old.unlink()
    sizes = []
    for key, body in ICONS.items():
        path = OUT / f"{key}.svg"
        path.write_text(body, encoding="utf-8")
        sizes.append((key, path.stat().st_size))
        if path.stat().st_size > 20 * 1024:
            raise SystemExit(f"{key} is over 20 KB")

    images = {
        key: {
            "src": f"images/{key}.svg",
            "altEn": en,
            "altEs": es,
        }
        for key, (en, es) in ALTS.items()
    }
    payload = {"images": images, "byPhrase": BY_PHRASE}
    CATALOG.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(ICONS)} svgs, {len(BY_PHRASE)} phrase links")
    print(f"largest: {max(sizes, key=lambda x: x[1])}")


if __name__ == "__main__":
    main()
