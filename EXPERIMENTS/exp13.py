import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([[50,50],[200,50],[50,200]])

# Destination points
pts2 = np.float32([[10,100],[200,50],[100,250]])

# Affine matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply transformation
result = cv2.warpAffine(img, M, (cols, rows))

# Display
cv2.imshow("Original", img)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()