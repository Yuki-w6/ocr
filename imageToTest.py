import cv2
import numpy as np
import pytesseract

# img = cv2.imread('../Pictures/invoice_1.png')
img = cv2.imread('../Pictures/invoice_2.png')
# img = cv2.imread('../Pictures/invoice_3.jpg')
height, width, channels = img.shape

gray_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# edged_img = cv2.Canny(blur_img, 75, 200)
# edged_img = cv2.Canny(blur_img, 50,150)
edged_img = cv2.Canny(blur_img, 1,50)

# cv2.imshow('edged', edged_img)
# cv2.waitKey(0)

coutours, hierarchy = cv2.findContours(edged_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

areas = [cv2.contourArea(c) for c in coutours]
max_index = np.argmax(areas)
# print(max_index)

epsilon = 0.1 * cv2.arcLength(coutours[max_index], True)
approx = cv2.approxPolyDP(coutours[max_index], epsilon, True)

# pts1 = np.float32(approx)
pts1 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (width, height))
# flip = cv2.flip(result, 1)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

text = pytesseract.image_to_string(result, lang='jpn')
print(text)