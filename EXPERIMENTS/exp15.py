import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris Corner Detection
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate for better visibility
dst = cv2.dilate(dst, None)

# Mark corners in red
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Display
cv2.imshow("Harris Corner Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()