from PIL import Image, ImageDraw, ImageFont
import os

width, height = 1600, 480
scale = 2

img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Background with rounded corners
bg_color = (11, 15, 23, 255)
border_color = (38, 48, 64, 255)
divider_color = (30, 41, 59, 255)
radius = 16 * scale

# Outer container
draw.rounded_rectangle([(scale, scale), (width - scale, height - scale)], radius=radius, fill=bg_color, outline=border_color, width=3)

# Top Gradient Accent Line (Cyan -> Purple -> Coral)
for x in range(16 * scale, width - 16 * scale):
    ratio = (x - 32) / (width - 64)
    if ratio < 0.5:
        r = int(56 + (129 - 56) * (ratio * 2))
        g = int(189 + (140 - 189) * (ratio * 2))
        b = int(248 + (248 - 248) * (ratio * 2))
    else:
        r = int(129 + (255 - 129) * ((ratio - 0.5) * 2))
        g = int(140 + (67 - 140) * ((ratio - 0.5) * 2))
        b = int(248 + (101 - 248) * ((ratio - 0.5) * 2))
    draw.line([(x, 3), (x, 7)], fill=(r, g, b, 255), width=1)

# Divider lines between 3 columns
draw.line([(533, 90), (533, 400)], fill=divider_color, width=2)
draw.line([(1067, 90), (1067, 400)], fill=divider_color, width=2)

# Load fonts
try:
    font_title = ImageFont.truetype("arialbd.ttf", 16 * scale)
    font_badge = ImageFont.truetype("arialbd.ttf", 10 * scale)
    font_number = ImageFont.truetype("arialbd.ttf", 36 * scale)
    font_label = ImageFont.truetype("arialbd.ttf", 13 * scale)
    font_subtext = ImageFont.truetype("arial.ttf", 11 * scale)
    font_micro = ImageFont.truetype("arialbd.ttf", 10 * scale)
    font_streak_num = ImageFont.truetype("arialbd.ttf", 24 * scale)
    font_streak_label = ImageFont.truetype("arialbd.ttf", 13 * scale)
except Exception:
    font_title = ImageFont.load_default()
    font_badge = font_title
    font_number = font_title
    font_label = font_title
    font_subtext = font_title
    font_micro = font_title
    font_streak_num = font_title
    font_streak_label = font_title

# Top Header Row: Title on Left, Live Telemetry Pill on Right
draw.text((48, 42), "GITHUB CONTRIBUTIONS SUMMARY", font=font_title, fill=(241, 245, 249, 255))

# Live Pulse Indicator Badge
pill_x, pill_y = 1320, 36
draw.rounded_rectangle([(pill_x, pill_y), (pill_x + 230, pill_y + 40)], radius=12, fill=(15, 23, 42, 255), outline=(56, 189, 248, 180), width=2)
draw.ellipse([(pill_x + 16, pill_y + 13), (pill_x + 30, pill_y + 27)], fill=(34, 197, 94, 255))
draw.text((pill_x + 40, pill_y + 10), "LIVE TELEMETRY STREAM", font=font_badge, fill=(56, 189, 248, 255))


# --- LEFT PANEL: Total Contributions ---
num_left = "2,187+"
bbox_num_left = draw.textbbox((0, 0), num_left, font=font_number)
w_num_left = bbox_num_left[2] - bbox_num_left[0]
draw.text((266 - w_num_left // 2, 140), num_left, font=font_number, fill=(255, 255, 255, 255))

lbl_left = "TOTAL CONTRIBUTIONS"
bbox_lbl_left = draw.textbbox((0, 0), lbl_left, font=font_label)
w_lbl_left = bbox_lbl_left[2] - bbox_lbl_left[0]
draw.text((266 - w_lbl_left // 2, 226), lbl_left, font=font_label, fill=(226, 232, 240, 255))

sub_left = "Oct 1, 2024 - Present"
bbox_sub_left = draw.textbbox((0, 0), sub_left, font=font_subtext)
w_sub_left = bbox_sub_left[2] - bbox_sub_left[0]
draw.text((266 - w_sub_left // 2, 270), sub_left, font=font_subtext, fill=(148, 163, 184, 255))

# Mini pill badge on left
draw.rounded_rectangle([(146, 316), (386, 356)], radius=10, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255), width=1)
draw.text((160, 326), "VELOCITY: ~8.4 COMMITS/DAY", font=font_micro, fill=(56, 189, 248, 255))


# --- CENTER PANEL: Flame Icon + Circular Progress Ring ---
cx, cy = 800, 182
ring_radius = 64

# Glowing multi-layer circular ring
draw.ellipse([(cx - ring_radius - 4, cy - ring_radius - 4), (cx + ring_radius + 4, cy + ring_radius + 4)], outline=(255, 67, 101, 80), width=4)
draw.ellipse([(cx - ring_radius, cy - ring_radius), (cx + ring_radius, cy + ring_radius)], outline=(255, 67, 101, 255), width=7)

# Center Streak Number
num_center = "181"
bbox_num_center = draw.textbbox((0, 0), num_center, font=font_streak_num)
w_num_center = bbox_num_center[2] - bbox_num_center[0]
h_num_center = bbox_num_center[3] - bbox_num_center[1]
draw.text((cx - w_num_center // 2, cy - h_num_center // 2 - 2), num_center, font=font_streak_num, fill=(255, 255, 255, 255))

# Flame Icon on top of the ring
flame_pts = [
    (cx, cy - ring_radius - 32),
    (cx + 12, cy - ring_radius - 14),
    (cx + 14, cy - ring_radius - 2),
    (cx + 9, cy - ring_radius + 6),
    (cx, cy - ring_radius + 6),
    (cx - 9, cy - ring_radius + 6),
    (cx - 14, cy - ring_radius - 2),
    (cx - 12, cy - ring_radius - 14),
]
draw.polygon(flame_pts, fill=(255, 67, 101, 255))
inner_flame = [
    (cx, cy - ring_radius - 22),
    (cx + 6, cy - ring_radius - 8),
    (cx + 4, cy - ring_radius + 3),
    (cx - 4, cy - ring_radius + 3),
    (cx - 6, cy - ring_radius - 8),
]
draw.polygon(inner_flame, fill=(251, 191, 36, 255))

lbl_center = "CURRENT STREAK"
bbox_lbl_center = draw.textbbox((0, 0), lbl_center, font=font_streak_label)
w_lbl_center = bbox_lbl_center[2] - bbox_lbl_center[0]
draw.text((cx - w_lbl_center // 2, 274), lbl_center, font=font_streak_label, fill=(255, 67, 101, 255))

sub_center = "Active Engineering Sync"
bbox_sub_center = draw.textbbox((0, 0), sub_center, font=font_subtext)
w_sub_center = bbox_sub_center[2] - bbox_sub_center[0]
draw.text((cx - w_sub_center // 2, 314), sub_center, font=font_subtext, fill=(148, 163, 184, 255))

# Mini pill badge on center
draw.rounded_rectangle([(cx - 110, 356), (cx + 110, 396)], radius=10, fill=(15, 23, 42, 255), outline=(255, 67, 101, 150), width=1)
draw.text((cx - 92, 366), "STATUS: CONTINUOUS SYNC", font=font_micro, fill=(255, 67, 101, 255))


# --- RIGHT PANEL: Longest Streak ---
num_right = "1,617"
bbox_num_right = draw.textbbox((0, 0), num_right, font=font_number)
w_num_right = bbox_num_right[2] - bbox_num_right[0]
draw.text((1333 - w_num_right // 2, 140), num_right, font=font_number, fill=(255, 255, 255, 255))

lbl_right = "LONGEST STREAK"
bbox_lbl_right = draw.textbbox((0, 0), lbl_right, font=font_label)
w_lbl_right = bbox_lbl_right[2] - bbox_lbl_right[0]
draw.text((1333 - w_lbl_right // 2, 226), lbl_right, font=font_label, fill=(226, 232, 240, 255))

sub_right = "2025 Full-Year Matrix"
bbox_sub_right = draw.textbbox((0, 0), sub_right, font=font_subtext)
w_sub_right = bbox_sub_right[2] - bbox_sub_right[0]
draw.text((1333 - w_sub_right // 2, 270), sub_right, font=font_subtext, fill=(148, 163, 184, 255))

# Mini pill badge on right
draw.rounded_rectangle([(1200, 316), (1466, 356)], radius=10, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255), width=1)
draw.text((1218, 326), "COVERAGE: 16 REPOSITORIES", font=font_micro, fill=(129, 140, 248, 255))


# Bottom Sub-Footer Info Strip
draw.line([(32, 422), (width - 32, 422)], fill=divider_color, width=1)
footer_text = "ENGINEERING TELEMETRY MATRIX  •  PYTORCH / FASTAPI / TYPESCRIPT / REACT  •  CONTINUOUS VERIFIED BUILDS"
bbox_ft = draw.textbbox((0, 0), footer_text, font=font_micro)
w_ft = bbox_ft[2] - bbox_ft[0]
draw.text((width // 2 - w_ft // 2, 442), footer_text, font=font_micro, fill=(100, 116, 139, 255))

# Save image
out_path = r"C:\Users\tarun\.gemini\antigravity\scratch\tarun1790\github_streak_summary.png"
img.save(out_path, "PNG")
print(f"Rendered advanced streak summary PNG to {out_path}")
