import math

left_distance = 0.2
right_distance = 0.6
wheel_distance = 0.4

# Calculate robot movement
distance = (left_distance + right_distance) / 2
delta_theta = (right_distance - left_distance) / wheel_distance

print("Distance:", round(distance, 2), "m")
print("Rotation:", round(math.degrees(delta_theta), 2), "degrees")