
# Simplified FTC Autonomous
# Python-style pseudocode, not directly runnable on FTC Control Hub

# Hardware
left_drive = Motor("left_drive")
right_drive = Motor("right_drive")

left_lift = Motor("left_lift")
right_lift = Motor("right_lift")

claw_servo = Servo("claw")

odometry = Odometry()

# 1. Drive forward using odometry
odometry.reset()

target_distance = 1.0  # meters

while odometry.get_distance() < target_distance:
    left_drive.set_power(0.4)
    right_drive.set_power(0.4)

left_drive.set_power(0)
right_drive.set_power(0)

# 2. Lift with two motors
left_lift.reset_encoder()
right_lift.reset_encoder()

target_lift_ticks = 1500

while (
    left_lift.get_ticks() < target_lift_ticks
    or right_lift.get_ticks() < target_lift_ticks
):
    left_lift.set_power(0.5)
    right_lift.set_power(0.5)

left_lift.set_power(0)
right_lift.set_power(0)

# 3. Release cone
claw_servo.set_position(1.0)

print("Autonomous complete!")
