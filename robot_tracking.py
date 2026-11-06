import math
import matplotlib.pyplot as plt

x = 0.0
y = 0.0
theta = 0.0

wheel_distance = 0.4
x_positions = [x]
y_positions = [y]

# Distance traveled by each wheel at every step
movements = [
    (1.0, 1.0),
    (1.0, 1.0),
    (0.2, 0.6),
    (1.0, 1.0),
    (1.0, 1.0)
]

for left, right in movements:
    d = (left + right) / 2
    delta_theta = (right - left) / wheel_distance

    x += d * math.cos(theta + delta_theta / 2)
    y += d * math.sin(theta + delta_theta / 2)
    theta += delta_theta
    x_positions.append(x)
    y_positions.append(y)

plt.plot(x_positions, y_positions, "b-o")
plt.scatter(x_positions[0], y_positions[0], color="green", s=100, label="Start")
plt.scatter(x, y, color="red", s=100, label="Finish")

plt.axis("equal")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.title("Robot Odometry Trajectory")
plt.legend()
plt.grid()
plt.show()
print(f"X: {x:.2f}, Y: {y:.2f}, Angle: {math.degrees(theta):.1f}°")
