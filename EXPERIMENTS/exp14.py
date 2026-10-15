import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])

# Destination points
pts2 = np.float32([[0,0],[300,0],[100,300],[300,300]])

# Perspective matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
result = cv2.warpPerspective(img, M, (cols, rows))

# Display
cv2.imshow("Original", img)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()