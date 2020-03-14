import cv2
import os
import features_extract

def zoom_out():
	for f in os.listdir('extracted_grains'):
		img = cv2.imread('extracted_grains/'+f)

		color = [0, 0, 0]

		top, bottom, left, right = [100] * 4

		img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
		cv2.imwrite('extracted_grains/'+f, img_with_border)
