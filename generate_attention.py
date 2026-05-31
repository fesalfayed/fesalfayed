#!/usr/bin/env python3
"""
A self-attention matrix as a self-portrait.

The conceit: self-attention is the self attending to the self. The glowing
diagonal IS the portrait. The pattern is a real decoder-attention shape
(causal mask, self diagonal, previous-token head, attention-to-origin sink,
faint induction stripes); the quiet background texture is seeded
deterministically from the identity string, so the piece is unique to one
person and reproducible from their name alone. Born from the work.

Palette taken verbatim from fesalfayed.com.
"""
import hashlib

IDENTITY = "fesalfayed · agents type, humans steer"
N = 28
CELL = 9.0
GAP = 1.6
STEP = CELL + GAP

# layout — a landscape plate: matrix left, legend right, generous negative space
MAR_L = 46
TOP = 60
BOTTOM = 72
MATRIX = N * STEP - GAP                 # ~295
LEGEND_X = MAR_L + MATRIX + 72          # right-hand legend column
W = LEGEND_X + 226
H = TOP + MATRIX + BOTTOM

BG      = "#0a0a0a"
FG      = "#e8e8e8"
DIM     = "#6a6a6a"
DIM2    = "#3a3a3a"
GRIDOFF = "#141414"
GREEN = (0, 255, 136)     # the self / diagonal
BLUE  = (78, 161, 255)    # attention to origin (BOS sink)
MAUVE = (199, 146, 234)   # induction / long-range

def seeded_rand(seed_str):
    h = int(hashlib.sha256(seed_str.encode()).hexdigest(), 16)
    s = [h & 0xFFFFFFFFFFFFFFFF]
    def rnd():
        x = s[0]
        x ^= (x << 13) & 0xFFFFFFFFFFFFFFFF
        x ^= (x >> 7)
        x ^= (x << 17) & 0xFFFFFFFFFFFFFFFF
        s[0] = x & 0xFFFFFFFFFFFFFFFF
        return s[0] / 0xFFFFFFFFFFFFFFFF
    return rnd

rnd = seeded_rand(IDENTITY)

def rgba(rgb, a):
    a = max(0.0, min(1.0, a))
    return f"rgba({rgb[0]},{rgb[1]},{rgb[2]},{a:.3f})"

cells = []
for i in range(N):
    row = []
    for j in range(N):
        if j > i:
            continue  # causal mask: upper triangle is negative space
        if j == i:
            w, kind = 0.92 + 0.08 * rnd(), "self"
        elif j == i - 1:
            w, kind = 0.45 + 0.35 * rnd(), "self"
        elif j == 0:
            w, kind = 0.30 + 0.45 * rnd() * (i / N), "bos"
        elif (i - j) in (4, 9) and rnd() > 0.45:
            w, kind = 0.18 + 0.30 * rnd(), "induction"
        else:
            w, kind = (rnd() ** 4) * 0.34, "off"
        row.append((j, w, kind))
    cells.append((i, row))

COLOR = {"self": GREEN, "bos": BLUE, "induction": MAUVE, "off": None}

s = []
s.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
    f'width="{W:.0f}" height="{H:.0f}" '
    f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" '
    f'role="img" aria-label="a self-attention matrix as a self-portrait — the diagonal is the self">'
)
s.append(f'<rect x="0.5" y="0.5" width="{W-1:.0f}" height="{H-1:.0f}" rx="10" fill="{BG}" stroke="#1a1a1a"/>')

# brand line, aligned to the matrix's left edge
s.append(
    f'<text x="{MAR_L:.0f}" y="36" font-size="13">'
    f'<tspan fill="rgb{GREEN}">fesal</tspan><tspan fill="{DIM}">@</tspan>'
    f'<tspan fill="rgb{BLUE}">fayed</tspan><tspan fill="{DIM}">:~$ </tspan>'
    f'<tspan fill="{FG}">attention(self, self)</tspan></text>'
)

# the matrix
for i, row in cells:
    for (j, w, kind) in row:
        x = MAR_L + j * STEP
        y = TOP + i * STEP
        rgb = COLOR[kind]
        if rgb is None or w < 0.04:
            s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{CELL}" height="{CELL}" rx="1.4" fill="{GRIDOFF}"/>')
        else:
            s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{CELL}" height="{CELL}" rx="1.4" fill="{rgba(rgb, 0.10 + 0.90*w)}"/>')

# earned motion: one slow forward-pass scan down the rows — the system computing attention
s.append(
    f'<rect x="{MAR_L-2:.0f}" y="{TOP-2:.0f}" width="{MATRIX+4:.1f}" height="{CELL+4:.1f}" rx="2" '
    f'fill="rgb{GREEN}" opacity="0">'
    f'<animateTransform attributeName="transform" attributeType="XML" type="translate" '
    f'values="0,0; 0,{MATRIX - CELL:.1f}" dur="7s" repeatCount="indefinite" calcMode="linear"/>'
    f'<animate attributeName="opacity" values="0;0.06;0" dur="7s" repeatCount="indefinite"/>'
    f'</rect>'
)

# legend, right column — teaches the viewer to read the portrait. quiet, vertically centered.
ly = TOP + 64
leg = [
    (GREEN, "self",      "each token attends to itself"),
    (BLUE,  "origin",    "every token watches the first"),
    (MAUVE, "induction", "the pattern remembering itself"),
]
for k, (rgb, label, desc) in enumerate(leg):
    yy = ly + k * 56
    s.append(f'<rect x="{LEGEND_X:.0f}" y="{yy:.0f}" width="9" height="9" rx="1.4" fill="rgb{rgb}"/>')
    s.append(f'<text x="{LEGEND_X+18:.0f}" y="{yy+9:.0f}" font-size="12.5" fill="{FG}">{label}</text>')
    s.append(f'<text x="{LEGEND_X:.0f}" y="{yy+26:.0f}" font-size="10.5" fill="{DIM}">{desc}</text>')

# caption, bottom — the thesis, two quiet lines, left-aligned under the matrix
cap_y = TOP + MATRIX + 30
s.append(
    f'<text x="{MAR_L:.0f}" y="{cap_y:.0f}" font-size="11.5" fill="{DIM}">'
    f'fig.1 &#8212; self-attention, seeded from a name</text>'
)
s.append(
    f'<text x="{MAR_L:.0f}" y="{cap_y+18:.0f}" font-size="11" fill="{DIM2}">'
    f'the only honest self-portrait is the one your weights draw</text>'
)

s.append('</svg>')
out = "\n".join(s)
with open("/tmp/fesalfayed/attention.svg", "w") as f:
    f.write(out)
print(f"wrote attention.svg  ({W:.0f}x{H:.0f}, {len(out)} bytes)")
