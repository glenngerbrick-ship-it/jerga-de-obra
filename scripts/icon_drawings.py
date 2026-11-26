"""Side-view silhouettes of real jobsite objects.

Yellow field, black outline, no people, no logos, no shine marks.
Shape and proportion come first. Each drawing is the view a worker
would recognize at arm's length: the drill is a cordless pistol drill,
the grinder is an angle grinder, and so on.
"""
from __future__ import annotations

INK = "#0A0A0A"
PAPER = "#FFFFFF"
DEEP = "#E6B800"
COPPER = "#C46B2F"


def svg(body: str) -> str:
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">'
        '<rect width="128" height="128" rx="16" fill="#FFD100"/>'
        f"{body}</svg>\n"
    )


def p(d: str, fill: str = PAPER, sw: str = "3.6") -> str:
    return (
        f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" '
        'stroke-linejoin="round" stroke-linecap="round"/>'
    )


def r(x, y, w, h, fill: str = PAPER, rx: float = 2, sw: str = "3.6") -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>'
    )


def c(cx, cy, rad, fill: str = PAPER, sw: str = "3.6") -> str:
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="{fill}" '
        f'stroke="{INK}" stroke-width="{sw}"/>'
    )


def l(d: str, sw: str = "3.6") -> str:
    return (
        f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{sw}" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    )


def icon(**named: str) -> dict[str, str]:
    return {key: svg(body) for key, body in named.items()}


# --- PPE -----------------------------------------------------------------

_hard_hat = (
    # Side profile: brim longer in front, dome, crown rib. No sparkle.
    p("M16 84 h96 c2 10-6 16-16 16 H34 C20 100 14 92 16 84z")
    + p("M38 84 C38 46 48 26 68 26 c24 0 38 20 40 58")
    + l("M50 38 c8-8 22-8 32 2", "3")
)

_safety_glasses = (
    r(10, 50, 46, 28, rx=7)
    + r(72, 50, 46, 28, rx=7)
    + l("M56 62 h16", "4.5")
    + l("M14 56 L4 46 M114 56 L124 46", "3.6")
    + r(16, 56, 34, 16, fill="none", rx=4, sw="2.4")
    + r(78, 56, 34, 16, fill="none", rx=4, sw="2.4")
)

_harness = (
    # Webbing only: D-ring, shoulder straps, chest buckle, belt, two closed leg loops.
    c(64, 14, 6)
    + l("M64 20 v6", "4")
    + r(46, 26, 9, 36, fill=INK, rx=2)
    + r(73, 26, 9, 36, fill=INK, rx=2)
    + r(46, 38, 36, 12, rx=2)
    + r(58, 41, 12, 6, fill=INK, rx=1)
    + r(16, 62, 96, 12, fill=INK, rx=3)
    + r(50, 64, 28, 8, rx=2)
    + p("M30 74 h18 v8 c0 18-18 28-18 10 z", fill="none", sw="6")
    + p("M80 74 h18 v8 c0 18-18 28-18 10 z", fill="none", sw="6")
)

_ppe = (
    # Hard hat, glasses, gauntlet, and a hi-vis vest with a stripe. No person.
    p("M8 36 h28 c0 8-4 12-10 12 H16 c-6 0-8-4-8-12z", fill=INK)
    + p("M14 36 c1-12 6-18 10-18 s9 6 10 18")
    + r(46, 26, 20, 12, rx=3)
    + r(70, 26, 20, 12, rx=3)
    + l("M66 31 h8", "3")
    + l("M48 28 L42 22 M88 28 L96 22", "2.4")
    + r(8, 64, 22, 28, rx=2)
    + r(12, 50, 6, 16, rx=2)
    + r(20, 48, 6, 18, rx=2)
    + p("M30 66 l12 4 v8 l-12 2z")
    # Vest: neck hole, open sides, reflective band.
    + p("M58 56 h22 l10 10 v36 H48 V66 z")
    + p("M64 56 v10 h10 V56", fill=DEEP)
    + r(50, 80, 38, 7, fill=DEEP, rx=1)
)

_machine = (
    # Portable generator: frame, engine, fuel tank, outlet panel.
    r(18, 70, 92, 28, rx=3)
    + r(28, 40, 48, 32, rx=3)
    + r(34, 24, 36, 18, rx=4)
    + c(40, 33, 3, fill=INK, sw="2")
    + r(80, 48, 22, 22, rx=2)
    + c(91, 56, 3, fill=INK, sw="2")
    + c(91, 64, 3, fill=INK, sw="2")
    + l("M28 98 v8 M100 98 v8", "4")
    + r(22, 104, 14, 6, rx=1)
    + r(92, 104, 14, 6, rx=1)
)

# --- Hand tools ----------------------------------------------------------

_hammer = (
    r(58, 46, 14, 66, fill=INK, rx=5)
    + p("M22 28 h46 v10 c10 0 18 6 20 14 2 8-4 14-14 16 h-10 V52 H34 c-8 0-12-6-12-14 V28z")
    + p("M68 28 c16-18 34-8 28 8 -2 6-8 8-12 12 l-8 4 V36 H68z")
    + l("M82 18 c8 8 10 16 4 20", "3.2")
)

_drill = (
    # Cordless pistol drill. Bit points right: long twist bit, cylindrical chuck,
    # pistol grip, trigger, battery pack wider than the handle.
    p("M14 34 h66 c8 0 12 6 12 12 v6 c0 8-6 14-14 14 H14 z")
    + r(86, 40, 8, 20, rx=2)  # collar
    + r(94, 42, 14, 16, rx=2)  # chuck, a cylinder not a nail-gun nose
    + l("M98 42 v16 M102 42 v16 M106 42 v16", "1.6")
    + r(108, 46, 16, 8, fill=INK, rx=1)  # twist bit
    + '<path d="M112 46 l4 8 M118 46 l4 8" fill="none" stroke="#FFD100" stroke-width="1.8" stroke-linecap="round"/>'
    + r(26, 62, 22, 32, rx=4)  # grip
    + p("M26 72 h-9 l2 14 h7 z", fill=INK)  # trigger
    + r(18, 92, 40, 22, fill=INK, rx=3)  # battery
    + r(26, 97, 24, 4, fill=DEEP, rx=1, sw="1.6")
    + l("M22 42 h18 M22 50 h14", "2.2")
)

_grinder = (
    # Angle grinder: cylindrical body, side handle, disc at 90 degrees, guard over the disc.
    r(8, 46, 68, 26, rx=13)
    + r(56, 12, 14, 38, rx=6)  # side handle
    + r(70, 50, 16, 20, rx=2)  # gear head
    + c(100, 78, 26)  # disc
    + p(
        "M74 74 A28 28 0 0 1 100 50 A28 28 0 0 1 126 78 "
        "L114 78 A14 14 0 0 0 100 64 A14 14 0 0 0 86 78 Z"
    )  # guard
    + c(100, 78, 5, fill=INK)
)

_circular_saw = (
    c(46, 84, 30)
    + p("M18 80 C18 46 28 40 48 40 C72 40 84 54 84 74 L76 80 C68 60 28 60 20 80 Z")
    + r(10, 76, 108, 8, rx=1)  # shoe
    + p("M32 108 l5 8 h-10 z", fill=INK, sw="2")
    + p("M46 112 l5 8 h-10 z", fill=INK, sw="2")
    + p("M60 108 l5 8 h-10 z", fill=INK, sw="2")
    + p("M52 34 h40 v12 H66 v-6 H52 z")  # rear handle
    + r(86, 46, 28, 26, rx=6)  # motor
    + c(30, 52, 7)  # front knob
)

_tape_measure = (
    r(18, 30, 56, 58, rx=8)
    + r(28, 18, 32, 16, rx=3)  # belt clip
    + r(36, 50, 18, 12, fill=INK, rx=2)  # lock
    + p("M74 64 h38 c0 12-6 16-14 16 H74 Z")  # blade
    + r(108, 58, 8, 12, fill=INK, rx=1)  # hook
    + l("M82 68 v8 M92 68 v10 M102 68 v8", "2.2")
)

_level = (
    r(6, 50, 116, 28, rx=3)
    + r(44, 40, 40, 48, rx=10)  # center vial housing
    + r(50, 56, 28, 16, fill=DEEP, rx=8)
    + c(64, 64, 4)
    + r(14, 58, 20, 12, fill=DEEP, rx=6)
    + c(24, 64, 3, sw="2.4")
    + r(94, 58, 20, 12, fill=DEEP, rx=6)
    + c(104, 64, 3, sw="2.4")
)

_ladder = (
    # Stepladder, front view: top cap, splayed rails, four steps.
    r(30, 14, 68, 12, rx=2)
    + l("M38 26 L22 114", "6")
    + l("M90 26 L106 114", "6")
    + l("M34 42 h60 M31 62 h66 M28 82 h72 M25 102 h78", "5")
)

_scaffold = (
    l("M26 108 V30 M46 108 V30 M82 108 V30 M102 108 V30", "5")
    + l("M26 30 h76 M26 46 h76", "4.5")
    + r(20, 60, 88, 10, rx=1)  # plank
    + l("M26 70 L102 104 M102 70 L26 104", "3.2")  # cross brace
    + r(18, 106, 16, 6, rx=1)
    + r(94, 106, 16, 6, rx=1)
)

_wrench = (
    '<g transform="rotate(-38 64 66)">'
    + p("M52 48 h16 l6 60 h-22 z")
    + p("M34 16 h26 v18 h-10 v12 H42 V32 h-8 z")
    + r(60, 20, 28, 14, rx=2)
    + c(58, 46, 8)
    + l("M52 46 h12", "2.6")
    + "</g>"
)

_pliers = (
    l("M54 14 L60 50", "8")
    + l("M74 14 L68 50", "8")
    + c(64, 56, 9)
    + c(64, 56, 3, fill=INK, sw="2")
    + l("M58 64 L34 104", "7")
    + l("M70 64 L94 104", "7")
    + l("M30 96 L26 112", "11")
    + l("M98 96 L102 112", "11")
    + l("M56 22 h6 M68 22 h6", "2")  # jaw serrations as a short mark, not shine
)

_screwdriver = (
    '<g transform="rotate(-32 64 64)">'
    + r(50, 14, 28, 50, fill=INK, rx=10)
    + r(56, 28, 16, 8, fill=DEEP, rx=2)
    + r(60, 62, 8, 40, rx=1)
    + p("M56 102 h16 l-8 14 z", fill=INK)
    + "</g>"
)

_shovel = (
    r(60, 18, 8, 58, fill=INK, rx=2)
    + p("M48 10 h32 v8 h-8 v8 h-16 v-8 h-8 z")
    + p("M34 74 h60 l-8 34 c-2 8-12 10-22 10 s-20-2-22-10 z")
    + l("M64 82 v28", "2.6")
)

_wheelbarrow = (
    p("M30 46 h64 l14 28 H42 z")
    + c(32, 92, 18)
    + c(32, 92, 5, fill=INK)
    + l("M54 74 L40 110", "4.5")
    + l("M78 74 L104 104", "4.5")
    + l("M92 68 L120 56", "5")
    + r(112, 50, 10, 8, fill=INK, rx=2)
)

_toolbox = (
    r(14, 52, 100, 48, rx=3)
    + r(34, 36, 60, 16, rx=2)
    + l("M46 36 v-10 c0-10 36-10 36 0 v10", "4")
    + r(56, 68, 16, 12, fill=INK, rx=2)
    + l("M14 76 h100", "3")
)

_extension_cord = (
    c(50, 66, 30, fill="none", sw="8")
    + c(50, 66, 14, fill="none", sw="6")
    + l("M78 58 h22", "6")
    + r(98, 46, 16, 24, rx=2)
    + r(114, 50, 8, 4, fill=INK, rx=0.5, sw="2")
    + r(114, 58, 8, 4, fill=INK, rx=0.5, sw="2")
    + c(118, 64, 2.2, fill=INK, sw="1.6")
)

# --- Materials -----------------------------------------------------------

_cement = (
    p("M30 40 h52 l16 14 v48 H30 z")
    + l("M82 40 v14 h16", "3.6")
    + p("M30 40 l10-14 h42 l10 14")
    + p("M36 100 c10 12 36 12 48 0 c-8 8-36 8-48 0z", fill=DEEP)
)

_concrete = (
    # Long finishing trowel lying on wet concrete.
    r(8, 78, 112, 28, rx=2)
    + l("M18 90 c14 5 20 5 32 0 s18-5 32 0 18 5 30 0", "2.2")
    + r(14, 58, 100, 8, rx=1)  # thin blade
    + l("M40 58 v-12 M84 58 v-12", "3")
    + r(36, 40, 52, 8, fill=INK, rx=4)
)

_brick = (
    p("M18 50 h68 v34 H18 z")
    + p("M86 50 l18-12 v34 L86 84 z")
    + p("M18 50 l18-12 h68 L86 50")
    + c(95, 48, 3.5, fill=DEEP, sw="2.2")
    + c(95, 60, 3.5, fill=DEEP, sw="2.2")
    + c(95, 72, 3.5, fill=DEEP, sw="2.2")
)

_rebar = (
    # Three deformed bars with ribs, tied with wire. Not a window grid.
    '<g transform="rotate(-8 64 36)">' + r(14, 30, 100, 12, rx=4) + l("M28 30 v12 M42 30 v12 M56 30 v12 M70 30 v12 M84 30 v12 M98 30 v12", "2.2") + "</g>"
    + '<g transform="rotate(7 64 64)">' + r(14, 58, 100, 12, rx=4) + l("M28 58 v12 M42 58 v12 M56 58 v12 M70 58 v12 M84 58 v12 M98 58 v12", "2.2") + "</g>"
    + '<g transform="rotate(-3 64 92)">' + r(14, 86, 100, 12, rx=4) + l("M28 86 v12 M42 86 v12 M56 86 v12 M70 86 v12 M84 86 v12 M98 86 v12", "2.2") + "</g>"
    + l("M52 64 c8 10 16 10 24 0", "3")
    + l("M58 58 c4 8 8 12 6 18", "2.6")
)

_lumber = (
    r(22, 78, 84, 18, rx=1)
    + r(28, 58, 72, 18, rx=1)
    + r(34, 38, 60, 18, rx=1)
    + c(40, 47, 3, fill="none", sw="1.8")
    + c(48, 47, 5, fill="none", sw="1.6")
    + c(38, 67, 3, fill="none", sw="1.8")
    + c(46, 67, 5, fill="none", sw="1.6")
    + c(36, 87, 3, fill="none", sw="1.8")
    + c(44, 87, 5, fill="none", sw="1.6")
)

_steel = (
    r(14, 22, 100, 16, rx=1)
    + r(50, 38, 28, 42, rx=1)
    + r(14, 80, 100, 16, rx=1)
    + l("M14 30 h100 M14 88 h100", "2")
)

_sand = (
    p("M14 98 C26 98 28 50 64 46 C100 50 102 98 114 98 Z")
    + c(46, 78, 2.2, fill=INK, sw="0")
    + c(60, 70, 2.2, fill=INK, sw="0")
    + c(74, 80, 2, fill=INK, sw="0")
    + c(56, 88, 1.8, fill=INK, sw="0")
    + c(84, 90, 1.8, fill=INK, sw="0")
)

_gravel = (
    p("M22 86 l14-16 16 10 8-18 18 12 10-8 16 20 z")
    + p("M18 96 l12-8 10 10 H18 z")
    + p("M48 100 l16-12 14 8 8-6 16 16 H48 z")
    + p("M30 78 l10-8 8 6 z", fill=DEEP)
    + p("M78 70 l12-6 8 10 z", fill=DEEP)
)

_plywood = (
    # Sheet face plus the layered edge, so the plies read as plywood.
    p("M34 24 h72 v80 H34 z")
    + p("M22 34 l12-10 v80 l-12 10 z")
    + l("M22 44 l12-4 M22 54 l12-4 M22 64 l12-4 M22 74 l12-4 M22 84 l12-4 M22 94 l12-4 M22 104 l12-4", "1.7")
)

_drywall = (
    r(26, 18, 80, 92, rx=1)
    + p("M26 18 l10 10 v72 l-10 10 v-92", fill=DEEP)
    + c(52, 48, 4, fill="none", sw="2.4")
    + l("M49 48 h6 M52 45 v6", "1.8")
    + c(78, 80, 4, fill="none", sw="2.4")
    + l("M75 80 h6 M78 77 v6", "1.8")
)

# --- Welding -------------------------------------------------------------

_mig_welder = (
    # Power source with a wire spool, and a MIG gun on a lead.
    r(6, 46, 50, 52, rx=3)
    + l("M16 46 v-10 h30 v10", "4")
    + c(26, 70, 15)
    + c(26, 70, 5, fill=INK, sw="2")
    + l("M26 58 v8 M18 70 h8", "1.8")
    + l("M40 66 C54 66 58 80 70 82", "3")
    + r(68, 72, 16, 26, rx=3)
    + r(64, 80, 6, 10, fill=INK, rx=1)
    + l("M82 78 C96 74 102 62 106 54", "5")
    + r(100, 44, 16, 14, rx=3)
    + r(114, 47, 6, 8, fill=INK, rx=1, sw="2")
)

_tig_welder = (
    r(8, 52, 46, 44, rx=3)
    + l("M18 64 h22 M18 74 h16", "2.4")
    + l("M54 70 h14", "4")
    + r(66, 58, 16, 40, rx=5)  # torch handle
    + r(84, 96, 8, 12, fill=INK, rx=2)  # back cap, shifted... handle is vertical
)
# The TIG torch above is a bit confused. Rebuild it as one clear torch beside the machine.
_tig_welder = (
    r(8, 50, 44, 46, rx=3)
    + l("M16 62 h24 M16 72 h18", "2.4")
    + c(40, 84, 4, sw="2.4")
    + l("M52 78 h10", "4")
    + r(62, 62, 16, 42, rx=6)  # handle
    + r(66, 100, 8, 12, fill=INK, rx=3)  # back cap
    + r(64, 40, 12, 24, rx=2)  # torch neck
    + p("M62 40 l4-16 h8 l4 16 z")  # ceramic cup
    + r(69, 16, 3, 12, fill=INK, rx=0.5, sw="1.8")  # tungsten
)

_stick_welder = (
    r(8, 40, 52, 40, rx=3)
    + l("M20 40 v-12 h28 v12", "4")
    + l("M16 52 h36 M16 62 h24", "2.2")
    + l("M60 64 h12", "4")
    # stinger
    + r(70, 56, 26, 18, rx=3)
    + p("M92 56 l16-18 -4 22 z", fill=INK)
    + l("M104 42 L120 22", "4.5")  # rod
    + l("M114 28 L120 22", "6")  # bare tip slightly thicker end... use a short black tip
    + c(120, 22, 2.4, fill=DEEP, sw="1.6")
)

_welding_helmet = (
    p("M30 48 C30 24 46 16 66 16 c26 0 40 16 40 40 v24 c0 20-16 32-38 32 -18 0-30-10-34-24z")
    + r(64, 50, 34, 24, fill=INK, rx=2)
    + r(68, 54, 26, 7, fill=DEEP, rx=1, sw="2")
    + c(40, 78, 5)
    + l("M45 78 h18", "4")
)

_welding_gloves = (
    # Two gauntlets: long cuff, separate fingers, thumb.
    r(12, 70, 40, 36, rx=3)
    + r(16, 48, 30, 26, rx=2)
    + r(16, 28, 8, 24, rx=3)
    + r(26, 24, 8, 28, rx=3)
    + r(36, 30, 8, 22, rx=3)
    + p("M46 56 l14 6 v10 l-14 2z")
    + l("M12 90 h40", "4")
    + r(68, 66, 40, 36, rx=3)
    + r(72, 44, 30, 26, rx=2)
    + r(72, 24, 8, 24, rx=3)
    + r(82, 20, 8, 28, rx=3)
    + r(92, 26, 8, 22, rx=3)
    + p("M102 52 l14 6 v10 l-14 2z")
    + l("M68 86 h40", "4")
)

_electrode = (
    '<g transform="rotate(-28 64 64)">'
    + r(16, 58, 74, 14, rx=5)
    + r(86, 60, 24, 10, fill=INK, rx=2)
    + l("M32 58 v14 M48 58 v14 M64 58 v14", "2.2")
    + "</g>"
)

_welding_wire = (
    c(64, 64, 38)
    + c(64, 64, 24)
    + c(64, 64, 8, fill=INK)
    + c(64, 64, 32, fill="none", sw="2")
    + l("M98 40 c14 6 18 4 22-8", "3")
)

_torch = (
    # MIG gun, side view. Cable, pistol grip, trigger, gooseneck, gas cup, tip.
    l("M8 108 C20 108 28 100 36 92", "6")
    + r(22, 40, 34, 58, rx=8)
    + r(54, 62, 10, 18, fill=INK, rx=2)  # trigger
    + l("M40 48 C62 28 84 36 96 52", "9")  # gooseneck
    + r(90, 42, 26, 18, rx=4)  # nozzle cup, fatter than the neck
    + r(114, 46, 8, 10, fill=INK, rx=1)  # contact tip
)

_gas_cylinder = (
    r(46, 40, 36, 66, rx=6)
    + p("M46 48 c0-16 36-16 36 0")
    + r(42, 32, 44, 12, fill=INK, rx=2)
    + r(58, 16, 12, 18, rx=2)
    + c(64, 14, 7)
    + l("M64 8 v12 M58 14 h12", "2.2")
    + l("M78 18 h14", "3.2")
)

_slag = (
    r(10, 80, 108, 16, rx=1)
    + p("M16 80 l8-14 8 14 8-14 8 14 8-14 8 14 8-14 8 14 8-14 8 14 8-14 8 14", fill=DEEP)
    + p("M18 58 l10 10 H16 z")
    + p("M96 62 l12 10 H92 z")
    # chipping hammer: point one end, chisel the other
    + l("M28 64 L78 28", "4")
    + p("M22 66 l10-2 2 10 z", fill=INK)
    + r(74, 22, 16, 7, fill=INK, rx=1)
)

# --- Electrical ----------------------------------------------------------

_cable = (
    l("M14 86 C28 40 44 44 56 74 C70 108 86 100 98 62 C108 36 114 40 118 52", "9")
    + r(108, 44, 12, 16, rx=1)
    + l("M112 44 v-10 M118 44 v-12", "2.4")
)

_breaker = (
    r(42, 14, 44, 100, rx=4)
    + r(52, 36, 24, 40, rx=3)
    + r(56, 42, 16, 22, fill=INK, rx=3)
    + c(64, 98, 5, sw="2.6")
    + l("M64 93 v10 M59 98 h10", "1.8")
)

_multimeter = (
    r(30, 14, 68, 78, rx=6)
    + r(38, 22, 52, 22, fill=INK, rx=2)
    + c(64, 64, 16)
    + l("M64 64 L76 54", "3")
    + c(48, 84, 4, sw="2.4")
    + c(80, 84, 4, sw="2.4")
    + l("M48 88 C40 104 32 110 26 118", "3")
    + l("M80 88 C90 104 98 110 106 118", "3")
    + p("M22 114 l4 10 6-6 z", fill=INK, sw="2")
    + p("M102 114 l8 4 2 8 z", fill=INK, sw="2")
)

_electrical_tape = (
    c(58, 64, 34, fill=INK)
    + c(58, 64, 12, fill=DEEP, sw="3")
    + p("M88 54 h28 v16 H90 z", fill=INK)
)

_lockout = (
    r(34, 54, 42, 38, rx=3)
    + l("M44 54 V36 c0-14 32-14 32 0 v18", "6")
    + c(55, 68, 4, fill=INK, sw="2")
    + l("M55 72 v12", "3")
    + r(80, 24, 34, 28, rx=2)
    + c(90, 32, 3, fill="none", sw="2.2")
    + l("M74 36 H80", "2.4")
    + l("M88 40 h18 M88 46 h14", "2")
)

# --- Concrete, HVAC, plumbing, scaffold parts, iron --------------------

_slab = (
    r(12, 34, 104, 60, rx=2)
    + l("M12 64 h104 M64 34 v60", "3.2")
)

_formwork = (
    r(14, 34, 16, 68, rx=1)
    + r(98, 34, 16, 68, rx=1)
    + l("M18 22 v14 M110 22 v14", "4")
    + l("M14 50 h16 M14 78 h16 M98 50 h16 M98 78 h16", "4")
    + r(34, 48, 60, 42, fill=DEEP, rx=1)
)

_duct = (
    p("M16 46 h70 v40 H16 z")
    + p("M86 46 l22-16 v40 L86 86 z")
    + p("M16 46 l22-16 h70 L86 46")
    + l("M16 60 h70", "2.4")
)

_condenser = (
    r(26, 36, 76, 64, rx=3)
    + p("M26 36 l14-16 h76 L102 36")
    + c(64, 58, 18)
    + l("M64 42 v32 M48 58 h32 M52 46 l24 24 M76 46 L52 70", "2.2")
    + c(64, 58, 4, fill=INK, sw="2")
    + l("M34 84 h60 M34 92 h60", "2.6")
)

_evaporator = (
    r(34, 30, 60, 74, rx=1)
    + l("M46 30 v74 M58 30 v74 M70 30 v74 M82 30 v74", "2.4")
    + l("M46 30 v-10 h36 v10", "4")
)

_thermostat = (
    r(40, 14, 48, 100, rx=6)
    + r(48, 26, 32, 24, fill=INK, rx=2)
    + c(64, 72, 14)
    + l("M64 72 L74 62", "2.6")
    + r(50, 98, 12, 8, fill=INK, rx=2)
    + r(66, 98, 12, 8, fill=INK, rx=2)
)

_refrigerant = (
    r(42, 42, 44, 62, rx=8)
    + l("M52 42 V28 h24 v14", "4")
    + r(58, 16, 12, 14, rx=2)
    + c(64, 14, 5)
    + r(42, 64, 44, 16, fill=DEEP, rx=1)
)

_ac_unit = (
    r(8, 40, 112, 42, rx=8)
    + r(16, 66, 96, 10, rx=3)
    + r(86, 48, 22, 10, fill=INK, rx=1)
    + l("M24 56 h48", "2.4")
)

_air_filter = (
    r(22, 16, 84, 96, rx=2)
    + l("M36 24 l14 14 -14 14 14 14 -14 14 14 14 -14 14", "3.2")
    + l("M58 24 l14 14 -14 14 14 14 -14 14 14 14 -14 14", "3.2")
    + l("M80 24 l14 14 -14 14 14 14 -14 14 14 14 -14 14", "3.2")
)

_pipe = (
    r(8, 54, 40, 22, rx=2)
    + r(80, 54, 40, 22, rx=2)
    + r(42, 46, 44, 38, rx=3)
    + l("M16 54 v22 M24 54 v22 M88 54 v22 M96 54 v22", "1.8")
)

_pvc = (
    r(12, 58, 52, 22, rx=6)
    + r(52, 24, 22, 56, rx=6)
    + r(8, 54, 14, 30, rx=3)
    + r(48, 16, 30, 14, rx=3)
)

_copper = (
    # One copper elbow: a tube bent 90 degrees, with a coupling at each end.
    p("M8 58 H50 V22 H68 V80 H8 Z", fill=COPPER)
    + r(6, 54, 12, 28, fill=COPPER, rx=2)
    + r(46, 16, 26, 12, fill=COPPER, rx=2)
)

_shutoff = (
    r(8, 78, 112, 16, rx=2)
    + r(46, 70, 36, 32, rx=2)
    + r(60, 46, 8, 26, fill=INK, rx=1)
    + c(64, 40, 20)
    + l("M64 22 v36 M46 40 h36 M52 28 l24 24 M76 28 L52 52", "2.4")
)

_water = (
    r(6, 36, 40, 16, rx=2)
    + l("M46 44 C62 52 66 78 58 100", "7")
    + p("M70 108 c8 10 18 8 18-2 c0-12-9-18-9-18 s-9 6-9 20z")
)

_drain = (
    # P-trap
    r(34, 12, 28, 8, rx=1)
    + r(40, 18, 16, 36, rx=2)
    + p("M40 50 h16 v22 c0 20 32 20 32 0 V44 h16 v36 c0 30-48 40-64 16 V50 z")
)

_water_heater = (
    r(40, 30, 48, 80, rx=10)
    + r(50, 12, 8, 20, rx=2)
    + r(70, 12, 8, 20, rx=2)
    + r(52, 58, 24, 22, rx=2)
    + l("M88 44 h16 v10", "3.4")
    + r(34, 98, 12, 6, fill=INK, rx=1)
)

_plank = (
    r(8, 48, 112, 30, rx=2)
    + r(8, 48, 14, 30, fill=INK, rx=1)
    + r(106, 48, 14, 30, fill=INK, rx=1)
    + l("M32 48 v30 M52 48 v30 M72 48 v30 M92 48 v30", "2.2")
)

_guardrail = (
    l("M28 108 V40 M64 108 V28 M100 108 V40", "6")
    + l("M16 40 h96 M16 62 h96", "6")
    + r(20, 90, 88, 12, rx=1)
)

_caster = (
    # Stem, fork, wheel, and a brake lever. Scaffold caster.
    r(58, 10, 12, 22, fill=INK, rx=2)
    + p("M40 30 h48 v16 H84 v14 H44 v-14 H40 z")
    + c(64, 88, 26)
    + c(64, 88, 7, fill=INK)
    + r(78, 36, 8, 28, rx=2)  # brake lever
    + r(74, 30, 16, 8, rx=2)
)

# --- Heavy equipment -----------------------------------------------------

_excavator = (
    r(14, 78, 74, 22, fill=INK, rx=11)
    + c(30, 88, 6, fill=DEEP, sw="2.4")
    + c(48, 88, 6, fill=DEEP, sw="2.4")
    + c(66, 88, 6, fill=DEEP, sw="2.4")
    + p("M26 78 L34 58 h40 l10 20 z")
    + r(56, 38, 28, 24, rx=2)
    + r(60, 42, 18, 14, fill=INK, rx=1)
    + l("M56 50 H34 L18 30", "7")
    + l("M18 30 L12 50", "6")
    + p("M4 44 h18 l4 16 H8 z")
    + l("M8 60 v6 M14 60 v6 M20 60 v6", "3")
)

_bulldozer = (
    r(36, 72, 70, 20, fill=INK, rx=10)
    + c(50, 82, 6, fill=DEEP, sw="2.4")
    + c(68, 82, 6, fill=DEEP, sw="2.4")
    + c(86, 82, 6, fill=DEEP, sw="2.4")
    + p("M48 72 h32 V56 h16 V42 H76 V56 H48 z")
    + r(80, 44, 16, 12, fill=INK, rx=1)
    # Big curved blade out front, on push arms.
    + p("M6 30 h16 c6 10 8 28 4 46 H6 C2 58 2 40 6 30 z")
    + l("M22 42 H48 M22 68 H52", "5")
    + r(66, 30, 6, 14, fill=INK, rx=1)
)

_loader = (
    c(38, 90, 16)
    + c(38, 90, 6, fill=INK)
    + c(92, 90, 16)
    + c(92, 90, 6, fill=INK)
    + p("M48 80 h34 V60 h20 V46 H80 V56 H58 V64 H48 z")
    + r(82, 48, 16, 12, fill=INK, rx=1)
    + l("M58 66 L30 58", "6")
    + p("M8 40 h28 l8 24 H14 z")
)

_crane = (
    r(12, 86, 78, 16, rx=2)
    + c(30, 108, 8)
    + c(30, 108, 3, fill=INK, sw="2")
    + c(72, 108, 8)
    + c(72, 108, 3, fill=INK, sw="2")
    + r(16, 68, 24, 18, rx=2)
    + r(20, 72, 14, 10, fill=INK, rx=1)
    + l("M44 78 L112 22", "6")
    + l("M48 70 L104 28", "2.2")
    + l("M112 22 v18", "3")
    + r(106, 40, 12, 8, rx=1)
    + l("M112 48 v6", "3")
    + l("M112 54 c8 6 8 14 0 16", "3.2")
)

_forklift = (
    p("M22 78 h46 V52 h18 V36 H74 V52 H56 V48 H34 V78 H22 z")
    + r(12, 62, 16, 28, fill=INK, rx=2)
    + l("M34 48 V30 h42 v20", "4")
    + r(58, 54, 16, 12, fill=INK, rx=1)
    + r(88, 28, 8, 62, rx=1)
    + l("M96 62 h26 M96 72 h22", "5")
    + c(36, 98, 12)
    + c(36, 98, 4, fill=INK, sw="2")
    + c(78, 100, 10, fill=INK)
)

_dump_truck = (
    p("M10 50 h60 l10 16 v18 H10 z")
    + p("M80 58 h34 v26 H80 z")
    + r(88, 64, 16, 12, fill=INK, rx=1)
    + c(34, 98, 14)
    + c(34, 98, 5, fill=INK)
    + c(50, 100, 11)
    + c(50, 100, 4, fill=INK, sw="2")
    + c(102, 98, 14)
    + c(102, 98, 5, fill=INK)
)

_load = (
    r(14, 82, 100, 8, rx=1)
    + r(20, 90, 12, 14, fill=INK, rx=1)
    + r(58, 90, 12, 14, fill=INK, rx=1)
    + r(96, 90, 12, 14, fill=INK, rx=1)
    + r(26, 32, 76, 50, rx=2)
    + l("M26 48 h76 M26 64 h76", "3")
    + r(58, 32, 12, 50, fill=DEEP, rx=1)
)


ICONS: dict[str, str] = {
    "hard-hat": svg(_hard_hat),
    "safety-glasses": svg(_safety_glasses),
    "harness": svg(_harness),
    "ppe": svg(_ppe),
    "machine": svg(_machine),
    "hammer": svg(_hammer),
    "drill": svg(_drill),
    "grinder": svg(_grinder),
    "circular-saw": svg(_circular_saw),
    "tape-measure": svg(_tape_measure),
    "level": svg(_level),
    "ladder": svg(_ladder),
    "scaffold": svg(_scaffold),
    "wrench": svg(_wrench),
    "pliers": svg(_pliers),
    "screwdriver": svg(_screwdriver),
    "shovel": svg(_shovel),
    "wheelbarrow": svg(_wheelbarrow),
    "toolbox": svg(_toolbox),
    "extension-cord": svg(_extension_cord),
    "cement": svg(_cement),
    "concrete": svg(_concrete),
    "brick": svg(_brick),
    "rebar": svg(_rebar),
    "lumber": svg(_lumber),
    "steel": svg(_steel),
    "sand": svg(_sand),
    "gravel": svg(_gravel),
    "plywood": svg(_plywood),
    "drywall": svg(_drywall),
    "mig-welder": svg(_mig_welder),
    "tig-welder": svg(_tig_welder),
    "stick-welder": svg(_stick_welder),
    "welding-helmet": svg(_welding_helmet),
    "welding-gloves": svg(_welding_gloves),
    "electrode": svg(_electrode),
    "welding-wire": svg(_welding_wire),
    "torch": svg(_torch),
    "gas-cylinder": svg(_gas_cylinder),
    "slag": svg(_slag),
    "cable": svg(_cable),
    "breaker": svg(_breaker),
    "multimeter": svg(_multimeter),
    "electrical-tape": svg(_electrical_tape),
    "lockout": svg(_lockout),
    "slab": svg(_slab),
    "formwork": svg(_formwork),
    "duct": svg(_duct),
    "condenser": svg(_condenser),
    "evaporator": svg(_evaporator),
    "thermostat": svg(_thermostat),
    "refrigerant": svg(_refrigerant),
    "ac-unit": svg(_ac_unit),
    "air-filter": svg(_air_filter),
    "pipe": svg(_pipe),
    "pvc": svg(_pvc),
    "copper": svg(_copper),
    "shutoff": svg(_shutoff),
    "water": svg(_water),
    "drain": svg(_drain),
    "water-heater": svg(_water_heater),
    "plank": svg(_plank),
    "guardrail": svg(_guardrail),
    "caster": svg(_caster),
    "excavator": svg(_excavator),
    "bulldozer": svg(_bulldozer),
    "loader": svg(_loader),
    "crane": svg(_crane),
    "forklift": svg(_forklift),
    "dump-truck": svg(_dump_truck),
    "load": svg(_load),
}
