
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Robot parameters
x = 0.0
y = 0.0
theta = 0.0

left_speed = 1.0
right_speed = 1.0
wheel_distance = 0.4
dt = 0.1

v = (left_speed + right_speed) / 2
omega = (right_speed - left_speed) / wheel_distance

x_positions = [x]
y_positions = [y]

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 1.8)
ax.set_aspect("equal")
ax.grid()
ax.set_title("Robot Animation")

line, = ax.plot([], [], "b-")
robot, = ax.plot([], [], "ro", markersize=10)

def update(frame):
    global x, y, theta

    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += omega * dt

    x_positions.append(x)
    y_positions.append(y)

    line.set_data(x_positions, y_positions)
    robot.set_data([x], [y])

    return line, robot

ani = FuncAnimation(
    fig,
    update,
    frames=100,
    interval=100,
    repeat=False
)

plt.show()
