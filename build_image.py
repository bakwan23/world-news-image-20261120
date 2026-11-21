#!/usr/bin/env python3
"""Build the 1024x1024 front-page image for make.fun bounty
'Sum up 20 November's world news in one image' (news-image-20261120).
Deterministic: same input -> same bytes. No network."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 243, 234)   # paper
INK = (18, 18, 18)
RED = (178, 34, 34)
GREY = (90, 90, 90)
RULE = (18, 18, 18)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines

def draw_block(draw, x, y, w, kicker, headline, body, hf, bf, kf, gap=6):
    """Draw one story block; returns y after the block."""
    if kicker:
        draw.text((x, y), kicker, font=kf, fill=RED)
        y += kf.size + 4
    lines = wrap(draw, headline, hf, w)
    for ln in lines:
        draw.text((x, y), ln, font=hf, fill=INK)
        y += hf.size + 4
    y += 2
    for ln in wrap(draw, body, bf, w):
        draw.text((x, y), ln, font=bf, fill=INK)
        y += bf.size + 3
    return y + gap

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

M = 44  # margin
# --- Masthead ---
f_mast = font(SERIF_B, 62)
f_date = font(SANS, 22)
f_tag = font(SERIF, 24)
title = "THE WORLD IN ONE DAY"
tw = d.textlength(title, font=f_mast)
d.text(((W - tw) / 2, 30), title, font=f_mast, fill=INK)
d.line([(M, 108), (W - M, 108)], fill=RULE, width=3)
date = "FRIDAY, 20 NOVEMBER 2026"
dw = d.textlength(date, font=f_date)
d.text(((W - dw) / 2, 120), date, font=f_date, fill=RED)
tag = "The world's news in one image"
tw2 = d.textlength(tag, font=f_tag)
d.text(((W - tw2) / 2, 152), tag, font=f_tag, fill=GREY)
d.line([(M, 190), (W - M, 190)], fill=RULE, width=2)

y = 208
f_lead = font(SERIF_B, 46)
f_body = font(SERIF, 23)
f_kick = font(SANS_B, 20)
f_head2 = font(SERIF_B, 30)
f_body2 = font(SERIF, 21)

# --- Lead story ---
y = draw_block(d, M, y, W - 2 * M,
               "TOP STORY  ·  THE HAGUE",
               "Court finds Myanmar committed genocide",
               "The International Court of Justice rules Myanmar committed genocide "
               "against the Rohingya \u2014 the first such finding against a state.",
               f_lead, f_body, f_kick)
d.line([(M, y), (W - M, y)], fill=RULE, width=2)
y += 16

# --- Row 2: two columns ---
col_w = (W - 2 * M - 28) // 2
y2_start = y
y_left = draw_block(d, M, y, col_w,
                    "SHENZHEN",
                    "Trump, Xi and Putin hold first three-way summit",
                    "The three leaders issue a joint peace declaration after their "
                    "first meeting together.",
                    f_head2, f_body2, f_kick)
y_right = draw_block(d, M + col_w + 28, y, col_w,
                     "MARKETS",
                     "Stocks tumble as AI sell-off spreads",
                     "Japan's Nikkei falls 4.8%; the S&P 500 enters correction after "
                     "Anthropic's Nasdaq debut.",
                     f_head2, f_body2, f_kick)
y = max(y_left, y_right)
d.line([(M, y), (W - M, y)], fill=RULE, width=1)
y += 16

# --- Row 3: three columns ---
col3 = (W - 2 * M - 2 * 24) // 3
y3 = y
ys = []
ys.append(draw_block(d, M, y, col3,
                     "RIYADH",
                     "Houthi missiles damage skyscraper",
                     "Missiles strike a tower in the Saudi capital.",
                     font(SERIF_B, 24), font(SERIF, 19), f_kick))
ys.append(draw_block(d, M + col3 + 24, y, col3,
                     "KENYA",
                     "Last Ebola patient goes home",
                     "Kenya discharges its final case, 37 days after the first.",
                     font(SERIF_B, 24), font(SERIF, 19), f_kick))
ys.append(draw_block(d, M + 2 * (col3 + 24), y, col3,
                     "CRIMEA",
                     "Ukraine hits bridge; Russia vows reply",
                     "Strikes down a span of the crossing; fuel limits follow.",
                     font(SERIF_B, 24), font(SERIF, 19), f_kick))
y = max(ys)
d.line([(M, y), (W - M, y)], fill=RULE, width=1)
y += 14

# --- Bottom strip: also today ---
f_also_k = font(SANS_B, 19)
f_also = font(SERIF, 20)
d.text((M, y), "ALSO TODAY", font=f_also_k, fill=RED)
y += 28
also = ("Trump threatens penalties for US tech firms building data centres abroad  \u00b7  "
        "Grand Theft Auto VI launches  \u00b7  "
        "French police sentenced over racist beating of a music producer")
for ln in wrap(d, also, f_also, W - 2 * M):
    d.text((M, y), ln, font=f_also, fill=INK)
    y += f_also.size + 4

# --- Markets strip ---
y += 10
d.rectangle([(M, y), (W - M, y + 108)], outline=RULE, width=2)
f_num_k = font(SANS_B, 19)
f_num = font(SERIF, 21)
d.text((M + 16, y + 12), "MARKETS AT THE CLOSE", font=f_num_k, fill=RED)
nums = ("S&P 500  7,175.83  (\u22122.02%)      Nasdaq  23,879.20  (\u22122.25%)\n"
        "Dow  49,097.06  (\u22122.19%)      Gold  $3,530.75  (\u22122.58%)      Nikkei  \u22124.8%")
yy = y + 40
for ln in nums.split("\n"):
    d.text((M + 16, yy), ln, font=f_num, fill=INK)
    yy += f_num.size + 6

# --- Footer ---
d.line([(M, H - 56), (W - M, H - 56)], fill=RULE, width=1)
f_foot = font(SANS, 18)
foot = "20 November 2026 \u2014 one day, one page."
fw = d.textlength(foot, font=f_foot)
d.text(((W - fw) / 2, H - 44), foot, font=f_foot, fill=GREY)

img.save("/home/hatch/workspace/your_files/make-fun-news-image-20261120/entry.png",
         optimize=True)
print("saved")
