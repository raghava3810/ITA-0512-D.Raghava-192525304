import cv2

# Read image
img = cv2.imread("image.jpg")

# Rotate image 270° clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("270 Degree Clockwise Rotation", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()