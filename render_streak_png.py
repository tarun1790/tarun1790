from PIL import Image, ImageDraw, ImageFont
import os

width, height = 1600, 420
scale = 2

img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Background with rounded corners
bg_color = (13, 17, 23, 255)
border_color = (48, 54, 61, 255)
divider_color = (48, 54, 61, 255)
radius = 20 * scale

draw.rounded_rectangle([(scale, scale), (width - scale, height - scale)], radius=radius, fill=bg_color, outline=border_color, width=3)

# Divider lines
draw.line([(533, 100), (533, 370)], fill=divider_color, width=2)
draw.line([(1067, 100), (1067, 370)], fill=divider_color, width=2)

# Load fonts
try:
    font_title = ImageFont.truetype("arialbd.ttf", 18 * scale)
    font_number = ImageFont.truetype("arialbd.ttf", 34 * scale)
    font_label = ImageFont.truetype("arialbd.ttf", 14 * scale)
    font_subtext = ImageFont.truetype("arial.ttf", 12 * scale)
    font_streak_num = ImageFont.truetype("arialbd.ttf", 22 * scale)
    font_streak_label = ImageFont.truetype("arialbd.ttf", 14 * scale)
except Exception:
    font_title = ImageFont.load_default()
    font_number = font_title
    font_label = font_title
    font_subtext = font_title
    font_streak_num = font_title
    font_streak_label = font_title

# Top Title
draw.text((48, 50), "GitHub contributions summary", font=font_title, fill=(255, 255, 255, 255))

# --- LEFT PANEL: Total Contributions ---
num_left = "2,187+"
bbox_num_left = draw.textbbox((0, 0), num_left, font=font_number)
w_num_left = bbox_num_left[2] - bbox_num_left[0]
draw.text((266 - w_num_left // 2, 170), num_left, font=font_number, fill=(255, 255, 255, 255))

lbl_left = "Total Contributions"
bbox_lbl_left = draw.textbbox((0, 0), lbl_left, font=font_label)
w_lbl_left = bbox_lbl_left[2] - bbox_lbl_left[0]
draw.text((266 - w_lbl_left // 2, 250), lbl_left, font=font_label, fill=(255, 255, 255, 255))

sub_left = "Oct 1, 2024 - Present"
bbox_sub_left = draw.textbbox((0, 0), sub_left, font=font_subtext)
w_sub_left = bbox_sub_left[2] - bbox_sub_left[0]
draw.text((266 - w_sub_left // 2, 295), sub_left, font=font_subtext, fill=(139, 148, 158, 255))


# --- CENTER PANEL: Flame Icon + Circular Progress Ring ---
cx, cy = 800, 195
ring_radius = 62

# Circular ring
draw.ellipse([(cx - ring_radius, cy - ring_radius), (cx + ring_radius, cy + ring_radius)], outline=(255, 67, 101, 255), width=7)

# Center Streak Number
num_center = "181"
bbox_num_center = draw.textbbox((0, 0), num_center, font=font_streak_num)
w_num_center = bbox_num_center[2] - bbox_num_center[0]
h_num_center = bbox_num_center[3] - bbox_num_center[1]
draw.text((cx - w_num_center // 2, cy - h_num_center // 2 - 2), num_center, font=font_streak_num, fill=(255, 255, 255, 255))

# Flame Icon on top of the ring
flame_pts = [
    (cx, cy - ring_radius - 28),
    (cx + 10, cy - ring_radius - 12),
    (cx + 12, cy - ring_radius - 2),
    (cx + 8, cy - ring_radius + 4),
    (cx, cy - ring_radius + 4),
    (cx - 8, cy - ring_radius + 4),
    (cx - 12, cy - ring_radius - 2),
    (cx - 10, cy - ring_radius - 12),
]
draw.polygon(flame_pts, fill=(255, 67, 101, 255))
inner_flame = [
    (cx, cy - ring_radius - 20),
    (cx + 5, cy - ring_radius - 8),
    (cx + 4, cy - ring_radius + 2),
    (cx - 4, cy - ring_radius + 2),
    (cx - 5, cy - ring_radius - 8),
]
draw.polygon(inner_flame, fill=(245, 158, 11, 255))

# Label
lbl_center = "Current Streak"
bbox_lbl_center = draw.textbbox((0, 0), lbl_center, font=font_streak_label)
w_lbl_center = bbox_lbl_center[2] - bbox_lbl_center[0]
draw.text((cx - w_lbl_center // 2, 280), lbl_center, font=font_streak_label, fill=(255, 67, 101, 255))

# Subtext
sub_center = "Active Engineering Sync"
bbox_sub_center = draw.textbbox((0, 0), sub_center, font=font_subtext)
w_sub_center = bbox_sub_center[2] - bbox_sub_center[0]
draw.text((cx - w_sub_center // 2, 320), sub_center, font=font_subtext, fill=(139, 148, 158, 255))


# --- RIGHT PANEL: Longest Streak ---
num_right = "1,617"
bbox_num_right = draw.textbbox((0, 0), num_right, font=font_number)
w_num_right = bbox_num_right[2] - bbox_num_right[0]
draw.text((1333 - w_num_right // 2, 170), num_right, font=font_number, fill=(255, 255, 255, 255))

lbl_right = "Longest Streak"
bbox_lbl_right = draw.textbbox((0, 0), lbl_right, font=font_label)
w_lbl_right = bbox_lbl_right[2] - bbox_lbl_right[0]
draw.text((1333 - w_lbl_right // 2, 250), lbl_right, font=font_label, fill=(255, 255, 255, 255))

sub_right = "2025 Full-Year Matrix"
bbox_sub_right = draw.textbbox((0, 0), sub_right, font=font_subtext)
w_sub_right = bbox_sub_right[2] - bbox_sub_right[0]
draw.text((1333 - w_sub_right // 2, 295), sub_right, font=font_subtext, fill=(139, 148, 158, 255))

out_path = r"C:\Users\tarun\.gemini\antigravity\scratch\tarun1790\github_streak_summary.png"
img.save(out_path, "PNG")
print(f"Rendered streak PNG to {out_path}")
