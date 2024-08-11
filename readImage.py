import cv2

img = cv2.imread("../Pictures/invoice_1.png")

print(img.shape)

cv2.imshow("Invoice Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()