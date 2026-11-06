
import math
import matplotlib.pyplot as plt

# Initial robot position
x = 0.0
y = 0.0
theta = 0.0

# Robot parameters
left_speed = 1.0
right_speed = 1.0
wheel_distance = 0.4
dt = 0.1

# Robot velocities
v = (left_speed + right_speed) / 2
omega = (right_speed - left_speed) / wheel_distance

# Store trajectory
x_positions = [x]
y_positions = [y]

# Simulate 100 steps
for i in range(100):
    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += omega * dt

    x_positions.append(x)
    y_positions.append(y)

# Plot robot trajectory
plt.plot(x_positions, y_positions)
plt.scatter(x_positions[0], y_positions[0], label="Start")
plt.scatter(x, y, label="Finish")

plt.axis("equal")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.title("My First Robot Simulation")
plt.legend()
plt.grid()
plt.show()
