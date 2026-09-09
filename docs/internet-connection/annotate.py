#!/usr/bin/env python3
"""Draw the paper's annotated screenshots from raw captures + callouts.json.

    python3 annotate.py

Reads screenshots/raw/*.png, writes ../../assets/images/efficiency-and-range/*.png.
Both the raw captures and this script are committed, so a UI change means
swapping one PNG and re-running rather than redoing artwork by hand — the same
bargain render.mjs makes for the maths.

Three things the drawing has to get right:

  * **Both palettes.** _layouts/paper.html has its own light/dark scheme and the
    forum is dark-by-default, so nothing may depend on the page background. Each
    image is a self-contained dark card with its own padding — no transparent
    edges, and no white canvas that would glare in dark mode.
  * **Density.** The Range tile packs five distinct features into 190x189 raw
    pixels. Badges sitting on top of them would cover the very things they point
    at, so callouts are leader lines out to a label column instead.
  * **Small rendering.** Discourse scales images down on a phone. Type is sized
    against the FINAL width, and the whole canvas is drawn at SUPERSAMPLE and
    reduced, because ImageDraw has no line antialiasing of its own.

Coordinates in callouts.json are in RAW capture pixels, which is what makes them
reviewable: open the capture, read off the point, no mental crop-and-scale math.
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SUPERSAMPLE = 2

# Canvas width the base type sizes are tuned for (see the note where k is
# computed). A wider canvas gets proportionally larger type so that every
# figure lands at the same size once the page scales it into the column.
REFERENCE_WIDTH = 1320

# Mirrors CarPlayChipStyle, the same way chipBackgroundUIColor does in the app:
# green is statusTint(.ok) = (0.29, 0.87, 0.50).
GREEN = (74, 222, 128)
CANVAS = (16, 21, 28)
CARD = (26, 33, 43)
TEXT = (232, 237, 242)
MUTED = (154, 167, 180)


def load_font(size, bold=False):
    """SF first — it is what the screenshots themselves are set in. Arial is the
    fallback so the script still runs on a machine without SF."""
    for path in ("/System/Library/Fonts/SFNS.ttf",):
        try:
            font = ImageFont.truetype(path, size)
            if bold:
                try:
                    font.set_variation_by_name("Bold")
                except Exception:
                    pass  # non-variable build of Pillow; regular weight is fine
            return font
        except OSError:
            pass
    name = "Arial Bold.ttf" if bold else "Arial.ttf"
    try:
        return ImageFont.truetype(f"/System/Library/Fonts/Supplemental/{name}", size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, font, max_width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def render(spec, raw_dir, out_dir):
    src = Image.open(os.path.join(raw_dir, spec["source"])).convert("RGB")

    crop = spec.get("crop") or [0, 0, src.width, src.height]
    shot = src.crop(tuple(crop))

    # Everything below is in supersampled canvas pixels; the final reduce at the
    # end divides them all back down.
    S = SUPERSAMPLE
    scale = spec.get("scale", 1.0) * S
    shot = shot.resize(
        (int(shot.width * scale), int(shot.height * scale)), Image.LANCZOS
    )

    pad = int(spec.get("pad", 28) * S)
    gap = int(40 * S)
    has_labels = bool(spec.get("callouts"))
    # A 16:6 CarPlay frame beside a label column makes an image so wide that a
    # phone scales the type down to a few pixels. Wide sources put their legend
    # underneath instead, where it keeps its own size whatever the image does.
    below = spec.get("layout") == "below"

    # The label column is sized off the screenshot rather than fixed, so the
    # canvas keeps a sane aspect whatever the source shape is.
    label_w = int(shot.width * spec.get("label_ratio", 0.85))

    if below or not has_labels:
        width = pad * 2 + shot.width
    else:
        width = pad + shot.width + gap + label_w + pad

    # TYPE IS SIZED AGAINST THE FINAL CANVAS WIDTH, not in absolute pixels.
    # These figures are drawn wider than the 41rem reading column and are scaled
    # down to fit it, so absolute sizes would render at whatever the source
    # aspect happened to dictate — 11.6px on one figure and 7.4px on the next.
    # Scaling by width/REFERENCE lands every figure at the same size on the page.
    k = width / (REFERENCE_WIDTH * S)
    cap_font = load_font(max(9, int(21 * k * S)))
    lab_font = load_font(max(10, int(26 * k * S)), bold=True)
    det_font = load_font(max(9, int(22 * k * S)))
    num_font = load_font(max(8, int(20 * k * S)), bold=True)
    spec["_k"] = k
    caption = spec.get("caption", "")

    tmp = Image.new("RGB", (10, 10))
    tdraw = ImageDraw.Draw(tmp)
    cap_lines = wrap(tdraw, caption, cap_font, width - 2 * pad) if caption else []
    cap_h = int(sum(cap_font.size * 1.45 for _ in cap_lines) + 14 * S) if cap_lines else 0

    legend_cols = 2 if width > 900 * S else 1
    legend_h = (legend_height(spec, tdraw, lab_font, det_font,
                              (width - 2 * pad) // legend_cols, legend_cols, S)
                if below else 0)
    body_h = (shot.height if below else
              max(shot.height, min_label_height(spec, tdraw, lab_font, det_font, label_w, S)))
    height = pad + body_h + legend_h + cap_h + pad

    canvas = Image.new("RGB", (width, height), CANVAS)
    draw = ImageDraw.Draw(canvas)

    shot_x, shot_y = pad, pad
    # A hairline card edge stops a dark screenshot from bleeding into the dark
    # canvas — the tile art and the page background are nearly the same value.
    draw.rounded_rectangle(
        [shot_x - 2 * S, shot_y - 2 * S,
         shot_x + shot.width + 2 * S, shot_y + shot.height + 2 * S],
        radius=int(10 * S), fill=CARD, outline=(58, 70, 86), width=max(1, S),
    )
    if spec.get("highlight"):
        shot = apply_highlight(shot, spec, crop, scale, S)
    if below and has_labels:
        shot = draw_badges(shot, spec, crop, scale, num_font, S)
    canvas.paste(shot, (shot_x, shot_y))

    if has_labels and not below:
        draw_callouts(draw, spec, crop, scale, shot_x, shot_y, shot,
                      pad, gap, label_w, lab_font, det_font, num_font, S)
    elif has_labels:
        draw_legend(draw, spec, pad, pad + shot.height + int(18 * S),
                    (width - 2 * pad) // legend_cols, legend_cols,
                    lab_font, det_font, num_font, S)

    if cap_lines:
        y = pad + body_h + legend_h + int(14 * S)
        for line in cap_lines:
            draw.text((pad, y), line, font=cap_font, fill=MUTED)
            y += int(cap_font.size * 1.45)

    out = canvas.resize((width // S, height // S), Image.LANCZOS)
    path = os.path.join(out_dir, f"{spec['name']}.png")
    out.save(path, optimize=True)
    return path, out.size


def legend_entries(spec, draw, lab_font, det_font, col_w, S):
    """(label, wrapped detail lines) per callout, at the width they will be
    drawn at — so the height calculation and the drawing agree."""
    r = int(11 * spec.get('_k', 1) * S)
    out = []
    for call in spec["callouts"]:
        lines = wrap(draw, call.get("detail", ""), det_font,
                     col_w - r * 3) if call.get("detail") else []
        out.append((call["label"], lines))
    return out


def legend_height(spec, draw, lab_font, det_font, col_w, cols, S):
    entries = legend_entries(spec, draw, lab_font, det_font, col_w, S)
    heights = [lab_font.size * 1.5 + len(lines) * det_font.size * 1.35 + 16 * S
               for _, lines in entries]
    per_col = [sum(heights[i::cols]) for i in range(cols)]
    return int(max(per_col)) + int(10 * S)


def draw_legend(draw, spec, x0, y0, col_w, cols, lab_font, det_font, num_font, S):
    entries = legend_entries(spec, draw, lab_font, det_font, col_w, S)
    r = int(11 * spec.get('_k', 1) * S)
    ys = [y0] * cols
    for i, (label, lines) in enumerate(entries):
        col = i % cols
        x, y = x0 + col * col_w, ys[col]
        cx, cy = x + r, y + r
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN)
        w = draw.textlength(str(i + 1), font=num_font)
        draw.text((cx - w / 2, cy - num_font.size * 0.62), str(i + 1),
                  font=num_font, fill=CANVAS)
        tx = x + r * 3
        draw.text((tx, y), label, font=lab_font, fill=TEXT)
        dy = y + lab_font.size * 1.5
        for line in lines:
            draw.text((tx, dy), line, font=det_font, fill=MUTED)
            dy += det_font.size * 1.35
        ys[col] = dy + 16 * S


def draw_badges(shot, spec, crop, scale, num_font, S):
    """Numbered badges pinned on the image itself, for the below layout. Points
    in callouts.json sit BESIDE their feature, never on it — a badge covering
    the glyph it points at defeats the annotation."""
    draw = ImageDraw.Draw(shot)
    r = int(13 * spec.get('_k', 1) * S)
    for i, call in enumerate(spec["callouts"]):
        x = (call["at"][0] - crop[0]) * scale
        y = (call["at"][1] - crop[1]) * scale
        draw.ellipse([x - r - S, y - r - S, x + r + S, y + r + S],
                     fill=CANVAS)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=GREEN)
        w = draw.textlength(str(i + 1), font=num_font)
        draw.text((x - w / 2, y - num_font.size * 0.62), str(i + 1),
                  font=num_font, fill=CANVAS)
    return shot


def apply_highlight(shot, spec, crop, scale, S):
    """Dim everything except one region and ring it — the "where does this live"
    shot. Dimming rather than cropping keeps the surrounding tiles legible, which
    is the whole point: the reader is locating the tile, not reading it."""
    x0, y0, x1, y1 = spec["highlight"]
    box = [(x0 - crop[0]) * scale, (y0 - crop[1]) * scale,
           (x1 - crop[0]) * scale, (y1 - crop[1]) * scale]

    veil = Image.new("RGB", shot.size, CANVAS)
    shot = Image.blend(shot, veil, spec.get("dim", 0.55))

    # Paste the region back at full strength, then ring it.
    original = Image.open(os.path.join(HERE, spec["_raw_path"])).convert("RGB")
    region = original.crop(tuple(crop)).resize(shot.size, Image.LANCZOS)
    shot.paste(region.crop(tuple(int(v) for v in box)),
               (int(box[0]), int(box[1])))

    draw = ImageDraw.Draw(shot)
    inset = 3 * S
    draw.rounded_rectangle(
        [box[0] - inset, box[1] - inset, box[2] + inset, box[3] + inset],
        radius=int(16 * S), outline=GREEN, width=max(2, int(2.5 * S)),
    )
    return shot


def min_label_height(spec, draw, lab_font, det_font, label_w, S):
    """Labels are laid out down their own column; a tall stack must not be
    clipped by a short screenshot. MEASURED, not estimated — the type scales with
    canvas width (see k), so a fixed per-entry guess silently overruns the
    caption on any figure whose type came out larger than the guess assumed."""
    if not spec.get("callouts"):
        return 0
    total = 0
    for _, lines in legend_entries(spec, draw, lab_font, det_font, label_w, S):
        total += lab_font.size * 1.5 + len(lines) * det_font.size * 1.35 + 18 * S
    return int(total)


def draw_callouts(draw, spec, crop, scale, shot_x, shot_y, shot,
                  pad, gap, label_w, lab_font, det_font, num_font, S):
    label_x = shot_x + shot.width + gap
    calls = spec["callouts"]

    def to_canvas(pt):
        return (shot_x + (pt[0] - crop[0]) * scale,
                shot_y + (pt[1] - crop[1]) * scale)

    # Label rows follow target order top-to-bottom, which is what keeps the
    # leader lines from crossing each other. No routing logic needed.
    ordered = sorted(range(len(calls)), key=lambda i: to_canvas(calls[i]["at"])[1])
    rows = {}
    span = max(shot.height, min_label_height(spec, draw, lab_font, det_font, label_w, S))
    step = span / max(len(calls), 1)
    for slot, idx in enumerate(ordered):
        rows[idx] = shot_y + step * (slot + 0.5)

    r = int(11 * spec.get('_k', 1) * S)
    for i, call in enumerate(calls):
        n = i + 1
        tx, ty = to_canvas(call["at"])
        ly = rows[i]

        # Leader: out of the target, a dogleg, then a straight run to the label.
        elbow_x = shot_x + shot.width + gap * 0.45
        draw.line([(tx, ty), (elbow_x, ly)], fill=GREEN, width=max(1, int(1.5 * S)))
        draw.line([(elbow_x, ly), (label_x - r * 2.2, ly)],
                  fill=GREEN, width=max(1, int(1.5 * S)))
        draw.ellipse([tx - 4 * S, ty - 4 * S, tx + 4 * S, ty + 4 * S],
                     fill=GREEN, outline=CANVAS, width=max(1, S))

        cx, cy = label_x - r * 1.1, ly
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN)
        w = draw.textlength(str(n), font=num_font)
        draw.text((cx - w / 2, cy - num_font.size * 0.62), str(n),
                  font=num_font, fill=CANVAS)

        tx0 = label_x + r
        draw.text((tx0, ly - lab_font.size * 0.92), call["label"],
                  font=lab_font, fill=TEXT)
        detail = call.get("detail", "")
        if detail:
            dy = ly + lab_font.size * 0.42
            for line in wrap(draw, detail, det_font, label_w - r * 2):
                draw.text((tx0, dy), line, font=det_font, fill=MUTED)
                dy += det_font.size * 1.35


def main():
    with open(os.path.join(HERE, "callouts.json")) as fh:
        config = json.load(fh)

    raw_dir = os.path.join(HERE, config.get("raw_dir", "screenshots/raw"))
    out_dir = os.path.join(HERE, config["output_dir"])
    os.makedirs(out_dir, exist_ok=True)

    missing = [s["source"] for s in config["images"]
               if not os.path.exists(os.path.join(raw_dir, s["source"]))]
    if missing:
        sys.exit(f"missing raw captures: {', '.join(sorted(set(missing)))}")

    for spec in config["images"]:
        spec["_raw_path"] = os.path.relpath(
            os.path.join(raw_dir, spec["source"]), HERE)
        path, size = render(spec, raw_dir, out_dir)
        print(f"  {os.path.basename(path):32s} {size[0]}x{size[1]}  "
              f"{len(spec.get('callouts', []))} callouts")
    print(f"images:         {len(config['images'])}")


if __name__ == "__main__":
    main()
