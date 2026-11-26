#!/usr/bin/env python3
"""Card-image catalog helper.

Card pictures are now generated WebP illustrations in images/*.webp
(yellow/black catalog style). Do not run this script to regenerate
SVGs — it would overwrite those files. Update scripts/image_catalog.json
and run: python3 scripts/build_content.py --js-only
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


import importlib.util

_draw = Path(__file__).resolve().parent / "icon_drawings.py"
_spec = importlib.util.spec_from_file_location("icon_drawings", _draw)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
ICONS: dict[str, str] = _mod.ICONS

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
    raise SystemExit(
        "Card images are now generated WebP files in images/*.webp. "
        "This script no longer writes SVGs. Update scripts/image_catalog.json "
        "and run: python3 scripts/build_content.py --js-only"
    )
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
