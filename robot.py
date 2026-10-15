# My first robotics program

left_speed = 0.5
right_speed = 1.5
wheel_distance = 0.4

v = (left_speed + right_speed) / 2
omega = (right_speed - left_speed) / wheel_distance

print("Linear velocity:", v, "m/s")
print("Angular velocity:", omega, "rad/s")
