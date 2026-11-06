
import cv2
from pupil_apriltags import Detector

# Create AprilTag detector
detector = Detector(families="tag36h11")

# Open webcam
camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find AprilTags
    tags = detector.detect(gray)

    for tag in tags:
        tag_id = tag.tag_id

        print("Detected AprilTag:", tag_id)

        # Draw marker outline
        corners = tag.corners.astype(int)

        for i in range(4):
            p1 = tuple(corners[i])
            p2 = tuple(corners[(i + 1) % 4])
            cv2.line(frame, p1, p2, (0, 255, 0), 2)

        # Decide what robot should do
        if tag_id == 1:
            action = "GO LEFT"
        elif tag_id == 2:
            action = "GO CENTER"
        elif tag_id == 3:
            action = "GO RIGHT"
        else:
            action = "UNKNOWN TAG"

        print("Robot action:", action)

        x, y = map(int, tag.center)
        cv2.putText(
            frame, action, (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 255, 0), 2
        )

    cv2.imshow("FTC AprilTag Detection", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
