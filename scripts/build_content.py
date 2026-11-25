#!/usr/bin/env python3
"""Build phrases.js + Mexican Spanish audio clips (edge-tts es-MX-JorgeNeural)."""
from __future__ import annotations

import asyncio
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIO = ROOT / "audio"
OUT_JS = ROOT / "phrases.js"

VOICE = "es-MX-JorgeNeural"

# (cat, es, en, tip)
RAW = [
  # Safety
  ("Safety", "¡Cuidado!", "Watch out!", "Yell it. Don't whisper it."),
  ("Safety", "¡Alto!", "Stop! Right now.", "Immediate command"),
  ("Safety", "¡Peligro!", "Danger!", "Hazard nearby"),
  ("Safety", "¡Aguas!", "Heads up!", "Mexican crews say this constantly"),
  ("Safety", "¡Abajo!", "Below! / Heads down!", "Something's falling — move"),
  ("Safety", "Ponte el casco.", "Put on your hard hat.", "No hat, no work"),
  ("Safety", "Usa las gafas.", "Wear your safety glasses.", "Short form crews use"),
  ("Safety", "Necesitas el arnés.", "You need the harness.", "Fall protection"),
  ("Safety", "El arnés está jodido.", "The harness is wrecked.", "Report it — don't use it"),
  ("Safety", "Se requiere EPP siempre.", "PPE required at all times.", "Equipo de protección personal"),
  ("Safety", "Aléjate de la máquina.", "Get away from the machine.", "Equipment swing radius"),
  ("Safety", "No toques eso.", "Don't touch that.", "Hot, sharp, or live"),
  ("Safety", "¿Estás bien?", "You okay?", "After a near miss"),
  ("Safety", "Llama al nueve-uno-uno.", "Call 911.", "Emergency"),
  ("Safety", "Hay un hueco abierto.", "There's an open hole.", "Cover / barricade it"),
  ("Safety", "No camines por ahí.", "Don't walk over there.", "Keep people out of the zone"),
  ("Safety", "Suelta eso, está caliente.", "Drop it — it's hot.", "Burns happen fast"),
  ("Safety", "Área restringida.", "Restricted area.", "Barricade tape means stop"),
  ("Safety", "Reporta el incidente.", "Report the incident.", "Near misses count too"),
  # Tools
  ("Tools", "el martillo", "hammer", "Basic"),
  ("Tools", "el taladro", "drill", "Power tool"),
  ("Tools", "la amoladora", "angle grinder", "Sparks flying = this"),
  ("Tools", "la sierra circular", "circular saw", "Cutting"),
  ("Tools", "la cinta métrica", "tape measure", "Measure twice"),
  ("Tools", "el nivel", "level", "Is it plumb?"),
  ("Tools", "la escalera", "ladder", "3-point contact"),
  ("Tools", "el andamio", "scaffold", "Elevated work"),
  ("Tools", "la llave inglesa", "adjustable wrench", "Also just 'la llave'"),
  ("Tools", "los alicates", "pliers", "Hand tool"),
  ("Tools", "el destornillador", "screwdriver", "Also 'desarmador'"),
  ("Tools", "la pala", "shovel", "Dig"),
  ("Tools", "la carretilla", "wheelbarrow", "Haul materials"),
  ("Tools", "Pásame el martillo.", "Pass me the hammer.", "Most-used sentence on site"),
  ("Tools", "¿Dónde está el taladro?", "Where's the drill?", "Finding tools"),
  ("Tools", "Trae las herramientas.", "Bring the tools.", "Direct"),
  ("Tools", "Eso está chueco.", "That's crooked / off.", "Quality check, unfiltered"),
  ("Tools", "¿Tienes una extensión?", "Got an extension cord?", "Power everywhere"),
  ("Tools", "Está bien pinche pesado.", "This thing is damn heavy.", "Unfiltered — get a second hand"),
  # Materials
  ("Materials", "el cemento", "cement", "Bags"),
  ("Materials", "el concreto", "concrete", "Also 'hormigón'"),
  ("Materials", "el ladrillo", "brick", "Masonry"),
  ("Materials", "la varilla", "rebar", "Also 'acero de refuerzo'"),
  ("Materials", "la madera", "wood / lumber", "Framing"),
  ("Materials", "el acero", "steel", "Structural"),
  ("Materials", "la arena", "sand", "Mix"),
  ("Materials", "la grava", "gravel", "Aggregate"),
  ("Materials", "el triplay", "plywood", "Sheets — common word on site"),
  ("Materials", "la tablaroca", "drywall", "Also just 'drywall'"),
  ("Materials", "Necesitamos más cemento.", "We need more cement.", "Ordering"),
  ("Materials", "¿Dónde está la varilla?", "Where's the rebar?", "Locate"),
  ("Materials", "Deja la madera aquí.", "Leave the wood here.", "Staging"),
  ("Materials", "Eso está muy pesado.", "That's too heavy.", "Ask for help before you blow your back"),
  # Welding
  ("Welding", "la soldadora MIG", "MIG welder", "GMAW"),
  ("Welding", "la soldadora TIG", "TIG welder", "GTAW"),
  ("Welding", "soldadura de electrodo", "stick welding", "SMAW — also 'stick'"),
  ("Welding", "el casco de soldar", "welding helmet", "No helmet, no arc"),
  ("Welding", "los guantes de soldadura", "welding gloves", "Heat"),
  ("Welding", "el electrodo", "electrode / rod", "Consumable"),
  ("Welding", "el alambre", "welding wire", "MIG/TIG filler"),
  ("Welding", "la antorcha", "torch / gun", "Welding torch"),
  ("Welding", "el gas de protección", "shielding gas", "Argon, CO2…"),
  ("Welding", "soldadura de filete", "fillet weld", "Common joint"),
  ("Welding", "soldar a tope", "butt weld", "Joint type"),
  ("Welding", "Baja el amperaje.", "Lower the amperage.", "Settings"),
  ("Welding", "Sube el amperaje.", "Crank up the amps.", "Settings"),
  ("Welding", "Limpia la escoria.", "Chip the slag.", "Post-weld"),
  ("Welding", "El arco está inestable.", "The arc is unstable.", "Troubleshoot"),
  ("Welding", "Usa el casco.", "Use the helmet.", "Flash burn is not a flex"),
  ("Welding", "Ventila el área.", "Ventilate the area.", "Fumes"),
  ("Welding", "Esta soldadura está fea.", "This weld looks ugly.", "Honest QC"),
  ("Welding", "¿Necesitas más electrodos?", "Need more rods?", "Supply"),
  ("Welding", "No mires el arco.", "Don't stare at the arc.", "Flash burn lecture incoming"),
  # Electrical
  ("Electrical", "el cable", "wire / cable", "Say the gauge if it matters"),
  ("Electrical", "el breaker", "circuit breaker", "Everyone just says 'breaker'"),
  ("Electrical", "Apaga el breaker.", "Kill the breaker.", "Before you touch anything"),
  ("Electrical", "Está energizado.", "It's live / hot.", "Back off"),
  ("Electrical", "Verifica el voltaje.", "Check the voltage.", "Test before touch"),
  ("Electrical", "el multímetro", "multimeter", "Testing"),
  ("Electrical", "la cinta aislante", "electrical tape", "Insulation"),
  ("Electrical", "No toques el cable.", "Don't touch the wire.", "Safety"),
  ("Electrical", "Bloqueo y etiquetado.", "Lockout / tagout.", "LOTO — non-negotiable"),
  ("Electrical", "Se fue la luz.", "Power's out.", "Whole circuit or site"),
  # Concrete
  ("Concrete", "el colado", "the pour", "Big day language"),
  ("Concrete", "la losa", "the slab", "Floor / deck"),
  ("Concrete", "la cimbra", "formwork", "Also 'encofrado'"),
  ("Concrete", "Mezcla el concreto.", "Mix the concrete.", "Prep"),
  ("Concrete", "La losa está lista.", "The slab's ready.", "Status"),
  ("Concrete", "Necesitamos más varilla.", "We need more rebar.", "Materials"),
  ("Concrete", "Nivela el concreto.", "Level the concrete.", "Finish"),
  ("Concrete", "No camines en el fresco.", "Don't walk on the fresh pour.", "You'll hear about it if you do"),
  # Commands
  ("Commands", "Más rápido.", "Faster.", "Pace"),
  ("Commands", "Más despacio.", "Slow it down.", "Pace"),
  ("Commands", "Ayúdame a levantar esto.", "Help me lift this.", "Team lift"),
  ("Commands", "Mide aquí.", "Measure here.", "Layout"),
  ("Commands", "Corta esto.", "Cut this.", "Direct"),
  ("Commands", "Nivélalo.", "Level it.", "Quality"),
  ("Commands", "Empieza por aquí.", "Start here.", "Direction"),
  ("Commands", "¿Entiendes?", "You get it?", "Check comprehension"),
  ("Commands", "Repite, por favor.", "Say that again.", "Clarity over ego"),
  ("Commands", "Buen trabajo.", "Good work.", "Say it when it's true"),
  ("Commands", "Así no.", "Not like that.", "Correction without a speech"),
  ("Commands", "Haz esto.", "Do this.", "Point while you say it"),
  ("Commands", "Ven conmigo.", "Come with me.", "Follow"),
  ("Commands", "Déjalo ahí.", "Leave it there.", "Stop moving stuff around"),
  ("Commands", "Muévelo para allá.", "Move it over there.", "Point"),
  ("Commands", "Espérame.", "Wait up / hold on.", "Buy yourself 10 seconds"),
  ("Commands", "Órale.", "Alright / let's go / okay.", "Swiss-army word on many crews"),
  ("Commands", "No te hagas pendejo.", "Don't screw around / quit messing about.", "Harsh — know your crew before you use it"),
  ("Commands", "Apúrate, por favor.", "Hurry up, please.", "Softer than barking"),
  # Daily
  ("Daily", "Buenos días.", "Morning.", "Start right"),
  ("Daily", "¿Qué hacemos hoy?", "What are we doing today?", "Day one question"),
  ("Daily", "Estoy listo.", "I'm ready.", "Ready to work"),
  ("Daily", "Es hora del descanso.", "Break time.", "Don't skip water"),
  ("Daily", "¿Dónde está el baño?", "Where's the bathroom?", "Practical"),
  ("Daily", "Necesito ayuda.", "I need help.", "Ask early"),
  ("Daily", "¿Quién es el capataz?", "Who's the foreman?", "Roles"),
  ("Daily", "Hasta mañana.", "See you tomorrow.", "End of day"),
  ("Daily", "Soy nuevo en esta obra.", "I'm new on this job.", "Intro"),
  ("Daily", "¿A qué hora terminamos?", "What time do we wrap?", "Schedule"),
  ("Daily", "Buen trabajo hoy.", "Good work today.", "Close strong"),
  ("Daily", "Tengo hambre.", "I'm hungry.", "Lunch diplomacy"),
  ("Daily", "Hace un calor de los mil demonios.", "It's brutally hot out.", "Unfiltered weather talk"),
  ("Daily", "Vamos a echarle ganas.", "Let's put our backs into it.", "Hype without being corny"),
  ("Daily", "¿Trajiste lonche?", "Did you bring lunch?", "Lonche = lunch on many sites"),
  ("Daily", "Ya casi cerramos.", "We're almost wrapped.", "End of day"),
  # HVAC — new
  ("HVAC", "el ducto", "duct", "Air path"),
  ("HVAC", "el condensador", "condenser unit", "Outside box"),
  ("HVAC", "el evaporador", "evaporator coil", "Inside coil"),
  ("HVAC", "el termostato", "thermostat", "Set point"),
  ("HVAC", "el refrigerante", "refrigerant", "Don't vent it"),
  ("HVAC", "la unidad de aire", "AC unit", "Package / split"),
  ("HVAC", "Apaga la unidad.", "Shut the unit off.", "Before opening panels"),
  ("HVAC", "Hay una fuga de gas.", "There's a gas leak.", "Evacuate / report"),
  ("HVAC", "Cambia el filtro.", "Change the filter.", "Maintenance"),
  ("HVAC", "El ducto está tapado.", "The duct is blocked.", "Airflow issue"),
  ("HVAC", "Revisa la presión.", "Check the pressure.", "Gauges"),
  ("HVAC", "¿Cuántos BTUs?", "How many BTUs?", "Sizing talk"),
  # Plumbing — new
  ("Plumbing", "la tubería", "pipe / piping", "Supply or drain"),
  ("Plumbing", "el PVC", "PVC", "Plastic pipe"),
  ("Plumbing", "el cobre", "copper", "Sweat joints"),
  ("Plumbing", "la llave de paso", "shutoff valve", "Kill the water"),
  ("Plumbing", "Cierra el agua.", "Shut the water off.", "Before you cut"),
  ("Plumbing", "Hay un chorro.", "There's a leak / spray.", "Stop it fast"),
  ("Plumbing", "el drenaje", "drain", "Waste line"),
  ("Plumbing", "está tapado", "it's clogged", "Snake it"),
  ("Plumbing", "el calentador", "water heater", "Tank or tankless"),
  ("Plumbing", "Suelda el cobre.", "Sweat the copper.", "Torch work"),
  ("Plumbing", "Pega el PVC.", "Glue the PVC.", "Primer then cement"),
  ("Plumbing", "¿Dónde está la llave principal?", "Where's the main shutoff?", "Find it day one"),
  # Scaffolding — new
  ("Scaffolding", "arma el andamio", "build / erect the scaffold", "Base plates first"),
  ("Scaffolding", "la plataforma", "platform / plank", "Fully decked"),
  ("Scaffolding", "el barandal", "guardrail", "Fall protection"),
  ("Scaffolding", "la rueda", "caster / wheel", "Lock before climbing"),
  ("Scaffolding", "Traba las ruedas.", "Lock the casters.", "Non-negotiable"),
  ("Scaffolding", "No sobrecargues el andamio.", "Don't overload the scaffold.", "Weight limits"),
  ("Scaffolding", "Inspecciona antes de subir.", "Inspect before you climb.", "Daily check"),
  ("Scaffolding", "usa el arnés en altura", "use the harness at height", "Tie off"),
  ("Scaffolding", "Baja despacio.", "Come down slow.", "Three points of contact"),
  ("Scaffolding", "el nivel del andamio", "scaffold level / bay", "Plumb and level"),
  ("Scaffolding", "Está flojo.", "It's loose / wobbly.", "Fix before loading"),
  ("Scaffolding", "Desarma por secciones.", "Tear it down section by section.", "Don't freestyle"),
  # Heavy Equipment — new
  ("Heavy", "la excavadora", "excavator", "Digging machine"),
  ("Heavy", "el buldócer", "bulldozer", "Push dirt"),
  ("Heavy", "la cargadora", "loader / front-end loader", "Scoop and haul"),
  ("Heavy", "la grúa", "crane", "Swing radius = danger"),
  ("Heavy", "el montacargas", "forklift", "Spotter required"),
  ("Heavy", "el camión de volteo", "dump truck", "Haul spoil"),
  ("Heavy", "Retrocede despacio.", "Back up slow.", "Spotter eyes"),
  ("Heavy", "Mantente fuera del radio.", "Stay out of the swing radius.", "Crane / excavator"),
  ("Heavy", "Levanta la carga.", "Raise the load.", "Signal clearly"),
  ("Heavy", "Baja la carga.", "Lower the load.", "Soft landing"),
  ("Heavy", "¿Quién es el operador?", "Who's the operator?", "Know who's in the seat"),
  ("Heavy", "Señalízalo.", "Flag / signal it.", "Hand signals matter"),
]

CATEGORIES = [
  {"id": "Safety", "mark": "SF", "name": "Safety", "desc": "Yell these loud"},
  {"id": "Tools", "mark": "TL", "name": "Tools", "desc": "Pass me that"},
  {"id": "Materials", "mark": "MT", "name": "Materials", "desc": "Bags, bars, boards"},
  {"id": "Welding", "mark": "WD", "name": "Welding", "desc": "MIG, TIG, stick"},
  {"id": "Electrical", "mark": "EL", "name": "Electrical", "desc": "Kill the power first"},
  {"id": "Concrete", "mark": "CN", "name": "Concrete", "desc": "Pour day talk"},
  {"id": "HVAC", "mark": "HV", "name": "HVAC", "desc": "Ducts, units, gas"},
  {"id": "Plumbing", "mark": "PL", "name": "Plumbing", "desc": "Shut the water first"},
  {"id": "Scaffolding", "mark": "SC", "name": "Scaffolding", "desc": "Lock casters, tie off"},
  {"id": "Heavy", "mark": "HE", "name": "Heavy Equip", "desc": "Stay out of the radius"},
  {"id": "Commands", "mark": "CM", "name": "Commands", "desc": "Boss energy"},
  {"id": "Daily", "mark": "DY", "name": "Daily", "desc": "Crew small talk"},
  {"id": "Custom", "mark": "MY", "name": "My Phrases", "desc": "Your additions"},
]


def slugify(cat: str, es: str, idx: int) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", f"{cat}-{es}".lower())
    base = re.sub(r"-+", "-", base).strip("-")[:48] or "phrase"
    return f"{base}-{idx:03d}"


def build_phrases():
    phrases = []
    for i, (cat, es, en, tip) in enumerate(RAW):
        pid = slugify(cat, es, i)
        phrases.append({"id": pid, "cat": cat, "es": es, "en": en, "tip": tip, "audio": f"audio/{pid}.mp3"})
    return phrases


async def gen_one(sem, phrase, force: bool):
    path = ROOT / phrase["audio"]
    if path.exists() and path.stat().st_size > 500 and not force:
        return phrase["id"], "skip"
    async with sem:
        try:
            import edge_tts
            communicate = edge_tts.Communicate(phrase["es"], VOICE, rate="-5%")
            await communicate.save(str(path))
            return phrase["id"], "ok"
        except Exception as e:
            return phrase["id"], f"err:{e}"


async def generate_audio(phrases, force=False, concurrency=8):
    AUDIO.mkdir(parents=True, exist_ok=True)
    # remove test file
    test = AUDIO / "_test.mp3"
    if test.exists():
        test.unlink()
    sem = asyncio.Semaphore(concurrency)
    results = await asyncio.gather(*[gen_one(sem, p, force) for p in phrases])
    ok = sum(1 for _, s in results if s in ("ok", "skip"))
    err = [(i, s) for i, s in results if s.startswith("err")]
    print(f"audio: {ok}/{len(phrases)} ready; {len(err)} errors", flush=True)
    for i, s in err[:10]:
        print(" ", i, s, flush=True)
    return len(err) == 0


def write_js(phrases):
    payload = {
        "voice": VOICE,
        "categories": CATEGORIES,
        "phrases": phrases,
    }
    # Compact but readable enough
    body = json.dumps(payload, ensure_ascii=False, indent=2)
    OUT_JS.write_text(
        f"/* Generated by scripts/build_content.py — do not edit by hand */\n"
        f"window.JOBSITE_DATA = {body};\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT_JS} ({len(phrases)} phrases)", flush=True)


def main():
    force = "--force" in sys.argv
    skip_audio = "--js-only" in sys.argv
    phrases = build_phrases()
    write_js(phrases)
    if skip_audio:
        return
    ok = asyncio.run(generate_audio(phrases, force=force))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
