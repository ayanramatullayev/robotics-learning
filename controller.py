
target_angle = 90
current_angle = 110

error = target_angle - current_angle

if error > 0:
    print("Turn LEFT")
elif error < 0:
    print("Turn RIGHT")
else:
    print("Target reached!")

print("Error:", error, "degrees")
