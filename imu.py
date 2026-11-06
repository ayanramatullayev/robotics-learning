
import math

# Wheel odometry estimates
left_distance = 0.2
right_distance = 0.6
wheel_distance = 0.4

odom_angle = (right_distance - left_distance) / wheel_distance

# IMU gyroscope measurement
gyro_speed = 0.9  # rad/s
dt = 1.0          # seconds

imu_angle = gyro_speed * dt

print("Odometry:", round(math.degrees(odom_angle), 1), "degrees")
print("IMU:", round(math.degrees(imu_angle), 1), "degrees")
print("Difference:", round(math.degrees(odom_angle - imu_angle), 1), "degrees")
