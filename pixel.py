import cv2

img = cv2.imread('../Pictures/invoice_2.png')

pixel_value = img[25, 75]
print(pixel_value)

img[25, 75] = 0
print(pixel_value)
