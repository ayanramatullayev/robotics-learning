
import math

# Initial pose
x = 0.0
y = 0.0
theta = 0.0

# Wheel movements (meters)
left_distance = 0.2
right_distance = 0.6
wheel_distance = 0.4

# Odometry
d = (left_distance + right_distance) / 2
delta_theta = (right_distance - left_distance) / wheel_distance

# Update pose
x += d * math.cos(theta + delta_theta / 2)
y += d * math.sin(theta + delta_theta / 2)
theta += delta_theta

print(f"X: {x:.2f} m")
print(f"Y: {y:.2f} m")
print(f"Angle: {math.degrees(theta):.1f}°")