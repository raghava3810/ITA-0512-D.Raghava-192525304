import cv2

# Read image
img = cv2.imread("image.jpg")

# Rotate image by 180 degrees
rotated = cv2.rotate(img, cv2.ROTATE_180)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("180 Degree Rotation", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()