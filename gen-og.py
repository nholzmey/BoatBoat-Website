#!/usr/bin/env python3
"""Generate a brand-faithful 1200x630 OG image for BoatBoat (Discord music bot)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (13, 17, 23)        # #0d1117
PANEL = (22, 27, 34)     # #161b22
ACCENT = (88, 166, 255)  # #58a6ff
GREEN = (35, 134, 54)    # #238636
TEXT = (201, 209, 217)   # #c9d1d9
MUTED = (139, 148, 158)  # #8b949e
BORDER = (48, 54, 61)    # #30363d

FONT_BOLD = "/mnt/HC_Volume_106549717/adventure-products/.fonts/JetBrainsMono-Bold.ttf"
FONT_REG = "/mnt/HC_Volume_106549717/adventure-products/.fonts/JetBrainsMono-Regular.ttf"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle top accent bar
d.rectangle([0, 0, W, 6], fill=ACCENT)

# left panel (brand block)
d.rounded_rectangle([60, 70, 560, 560], radius=18, fill=PANEL, outline=BORDER, width=2)

# music note glyph (simple)
note = "\U0001F3B5"
f_note = ImageFont.truetype(FONT_BOLD, 120)
d.text((120, 120), note, font=f_note, fill=ACCENT)

f_title = ImageFont.truetype(FONT_BOLD, 64)
f_sub = ImageFont.truetype(FONT_REG, 30)
f_body = ImageFont.truetype(FONT_REG, 26)
f_small = ImageFont.truetype(FONT_REG, 22)

d.text((120, 300), "BoatBoat", font=f_title, fill=TEXT)
d.text((120, 380), "Your Personal Discord", font=f_sub, fill=ACCENT)
d.text((120, 420), "Music Companion", font=f_sub, fill=ACCENT)

# right panel (feature bullets)
d.rounded_rectangle([620, 70, 1140, 560], radius=18, fill=PANEL, outline=BORDER, width=2)
features = [
    "Personal Autoqueue",
    "Global Autoqueue",
    "Live progress bars",
    "Priority PlayNext",
    "Queue management",
    "Top played songs",
    "Adjustable volume",
    "Fun gamble feature",
]
y = 110
for f in features:
    d.ellipse([650, y + 8, 666, y + 24], fill=GREEN)
    d.text((682, y), f, font=f_body, fill=TEXT)
    y += 56

# footer
d.text((60, 580), "www.boatboatbot.com", font=f_small, fill=MUTED)

img.save("/mnt/HC_Volume_106549717/adventure-products/BoatBoat-Website/social-preview.png")
print("saved social-preview.png", img.size)
