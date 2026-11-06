
target_angle = 90
current_angle = 30

Kp = 0.05

error = target_angle - current_angle
omega = Kp * error

print("Error:", error, "degrees")
print("Turn speed:", omega, "degrees/s")
