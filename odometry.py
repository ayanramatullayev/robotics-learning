
import math

wheel_diameter = 0.1  # meters
ticks_per_revolution = 360

# Encoder measurements
encoder_ticks = 3600

# Calculate distance
revolutions = encoder_ticks / ticks_per_revolution
distance = revolutions * math.pi * wheel_diameter

print("Revolutions:", revolutions)
print("Distance:", round(distance, 2), "meters")
