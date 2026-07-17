from pathlib import Path

import cv2

img_path = Path(__file__).parent / "challenge" / "home" / "ctf-player" / "drop-in" / "flag.png"
img = cv2.imread(str(img_path))

detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(img)

print(data)
