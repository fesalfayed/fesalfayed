#!/usr/bin/env python3
"""
system.svg — the pipeline as a diagram, in the attention.svg design language.

Not a generic box-and-arrow kit drawing: it states the actual thesis of the
work — siloed sources are pulled through an agentic harness into structured
signal, and the human steers, the agents scaffold. Same palette, same
monospace, same dark plate and terminal brand line as attention.svg, so the
two read as one authored system, not two clip-art widgets.

Palette taken verbatim from attention.svg / fesalfayed.com.
"""

BG     = "#0a0a0a"
PLATE  = "#1a1a1a"
FG     = "#e8e8e8"
DIM    = "#6a6a6a"
DIM2   = "#3a3a3a"
GRID   = "#141414"
GREEN  = "#00ff88"   # the steered signal / human
BLUE   = "#4ea1ff"   # the harness
MAUVE  = "#c792ea"   # long-range / memory

W, H = 860, 300
s = []
s.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'width="{W}" height="{H}" '
    f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" '
    f'role="img" aria-label="siloed sources pulled through an agentic harness into structured signal, steered by a human">'
)
s.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="{BG}" stroke="{PLATE}"/>')

# brand line
s.append(
    f'<text x="40" y="34" font-size="13">'
    f'<tspan fill="{GREEN}">fesal</tspan><tspan fill="{DIM}">@</tspan>'
    f'<tspan fill="{BLUE}">fayed</tspan><tspan fill="{DIM}">:~$ </tspan>'
    f'<tspan fill="{FG}">./run --steer</tspan></text>'
)

MIDY = 168

# ---- column 1: siloed sources (scattered, dim, disconnected) ----
src_x = 70
sources = ["files", "apis", "chats", "docs", "feeds"]
sy0 = 92
s.append(f'<text x="{src_x}" y="74" font-size="11.5" fill="{DIM}">siloed sources</text>')
src_cy = []
for k, label in enumerate(sources):
    yy = sy0 + k * 34
    src_cy.append(yy)
    s.append(f'<rect x="{src_x}" y="{yy-13}" width="84" height="24" rx="4" fill="{GRID}" stroke="{DIM2}"/>')
    s.append(f'<text x="{src_x+42}" y="{yy+3}" font-size="11" fill="{DIM}" text-anchor="middle">{label}</text>')

# ---- column 2: the agentic harness (the engine, blue, central) ----
hx, hw = 330, 150
hy, hh = 96, 150
s.append(f'<text x="{hx+hw/2:.0f}" y="74" font-size="11.5" fill="{BLUE}" text-anchor="middle">agentic harness</text>')
s.append(f'<rect x="{hx}" y="{hy}" width="{hw}" height="{hh}" rx="8" fill="rgba(78,161,255,0.06)" stroke="{BLUE}" stroke-opacity="0.5"/>')
for k, line in enumerate(["fine-tune", "tool-use", "context", "adapters"]):
    yy = hy + 30 + k * 28
    s.append(f'<circle cx="{hx+22}" cy="{yy-4}" r="2.6" fill="{BLUE}"/>')
    s.append(f'<text x="{hx+34}" y="{yy}" font-size="11.5" fill="{FG}">{line}</text>')

# converging wires: sources -> harness
for yy in src_cy:
    s.append(
        f'<path d="M {src_x+84} {yy} C {src_x+150} {yy}, {hx-60} {MIDY}, {hx} {MIDY}" '
        f'fill="none" stroke="{DIM2}" stroke-width="1.1"/>'
    )
# one travelling pulse along the middle wire — the system pulling
s.append(
    f'<circle r="2.6" fill="{BLUE}"><animateMotion dur="3.2s" repeatCount="indefinite" '
    f'path="M {src_x+84} {src_cy[2]} C {src_x+150} {src_cy[2]}, {hx-60} {MIDY}, {hx} {MIDY}"/>'
    f'<animate attributeName="opacity" values="0;1;1;0" dur="3.2s" repeatCount="indefinite"/></circle>'
)

# ---- column 3: structured signal (single, bright, green, ordered) ----
ox = 600
s.append(f'<text x="{ox+70}" y="74" font-size="11.5" fill="{GREEN}" text-anchor="middle">structured signal</text>')
s.append(f'<rect x="{ox}" y="{MIDY-44}" width="180" height="88" rx="8" fill="rgba(0,255,136,0.06)" stroke="{GREEN}" stroke-opacity="0.55"/>')
# tidy ordered rows = the structured output
for k in range(4):
    yy = MIDY - 28 + k * 16
    wbar = [150, 120, 138, 96][k]
    s.append(f'<rect x="{ox+18}" y="{yy-7}" width="{wbar}" height="6" rx="3" fill="{GREEN}" opacity="{0.85 - k*0.15:.2f}"/>')

# harness -> signal wire + pulse
s.append(f'<path d="M {hx+hw} {MIDY} L {ox} {MIDY}" stroke="{GREEN}" stroke-width="1.3" stroke-opacity="0.5" fill="none"/>')
s.append(
    f'<circle r="2.8" fill="{GREEN}"><animateMotion dur="3.2s" begin="1.4s" repeatCount="indefinite" '
    f'path="M {hx+hw} {MIDY} L {ox} {MIDY}"/>'
    f'<animate attributeName="opacity" values="0;1;1;0" dur="3.2s" begin="1.4s" repeatCount="indefinite"/></circle>'
)

# ---- the human hand on the wheel: steering line from above into the harness ----
steer_x = hx + hw / 2
s.append(f'<text x="{steer_x:.0f}" y="278" font-size="11" fill="{MAUVE}" text-anchor="middle">human steers &#183; agents scaffold</text>')
s.append(f'<path d="M {steer_x:.0f} 262 L {steer_x:.0f} {hy+hh}" stroke="{MAUVE}" stroke-width="1.1" stroke-dasharray="3 3" stroke-opacity="0.7"/>')
s.append(f'<circle cx="{steer_x:.0f}" cy="262" r="3" fill="{MAUVE}"/>')

s.append('</svg>')
out = "\n".join(s)
import os
os.makedirs("/tmp/gh-audit/fesalfayed", exist_ok=True)
with open("/tmp/gh-audit/fesalfayed/system.svg", "w") as f:
    f.write(out)
print(f"wrote system.svg ({W}x{H}, {len(out)} bytes)")
