from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Create 4K black canvas
width, height = 3840, 2160
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

# === Draw Bicycle Only ===
# Wheel centers and radius
wheel_radius = 180
wheel_thickness = 18
left_wheel_center = (int(width * 0.35), int(height * 0.78))
right_wheel_center = (int(width * 0.65), int(height * 0.78))

# Wheels
for center in [left_wheel_center, right_wheel_center]:
    draw.ellipse([
        (center[0] - wheel_radius, center[1] - wheel_radius),
        (center[0] + wheel_radius, center[1] + wheel_radius)
    ], outline="white", width=wheel_thickness)

# Frame points
pedal = (int(width * 0.47), int(height * 0.78))                 # center axis
seat_post = (int(width * 0.44), int(height * 0.60))             # seat
front_joint = (int(width * 0.61), int(height * 0.65))           # fork frame joint
handle = (int(width * 0.64), int(height * 0.55))                # handle top

# Frame lines
draw.line([left_wheel_center, pedal], fill="white", width=10)
draw.line([pedal, right_wheel_center], fill="white", width=10)
draw.line([pedal, seat_post], fill="white", width=10)
draw.line([pedal, front_joint], fill="white", width=10)
draw.line([seat_post, front_joint], fill="white", width=10)

# Seat
draw.line([seat_post[0]-40, seat_post[1], seat_post[0]+40, seat_post[1]], fill="white", width=10)

# Front fork and handlebar
draw.line([right_wheel_center, front_joint], fill="white", width=10)
draw.line([front_joint, handle], fill="white", width=10)
draw.line([handle[0]-30, handle[1], handle[0]+30, handle[1]], fill="white", width=10)

# Pedal (crank)
draw.ellipse([
    (pedal[0] - 25, pedal[1] - 25),
    (pedal[0] + 25, pedal[1] + 25)
], fill="white")

# === Show only the bicycle ===
plt.figure(figsize=(16, 9))
plt.imshow(image)
plt.axis("off")
plt.title("Bicycle", fontsize=20)
plt.show()
