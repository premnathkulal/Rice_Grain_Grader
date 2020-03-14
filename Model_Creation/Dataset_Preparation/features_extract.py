#https://docs.opencv2.org/3.4/dd/d49/tutorial_py_contour_features.html

import numpy as np
import cv2
from skimage import measure, data, io
import matplotlib.pyplot as plt
import  os
import csv
import shutil

def features_extract():

	shutil.rmtree('extracted_features')
	os.mkdir('extracted_features')

 
	#CORRRECT_GRAINS
	for f in os.listdir('CORRRECT_GRAINS'):
		img = cv2.imread('CORRRECT_GRAINS/'+f,0)
		ret,thresh = cv2.threshold(img,127,255,0)
		im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
		cnt = contours[0]
		M = cv2.moments(cnt)

		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])

		area = cv2.contourArea(cnt)

		perimeter = cv2.arcLength(cnt,True)

		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		radius = int(radius)

		ellipse = cv2.fitEllipse(cnt)
		img = cv2.ellipse(img,ellipse,(0,255,0),2)

		rect = cv2.minAreaRect(cnt)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		img = cv2.drawContours(img,[box],0,(255,255,255),2)

		width = ellipse[1][0]
		height = ellipse[1][1]
		aspect_ratio = width/height

		with open('extracted_features/test.csv', 'a', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([width,height,aspect_ratio,area,radius,perimeter,1])


	#FOR DAMAGED GRAINS
	for f in os.listdir('DAMAGED_GRAINS'):
		img = cv2.imread('DAMAGED_GRAINS/'+f,0)
		ret,thresh = cv2.threshold(img,127,255,0)
		im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
		cnt = contours[0]
		M = cv2.moments(cnt)

		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])

		area = cv2.contourArea(cnt)

		perimeter = cv2.arcLength(cnt,True)

		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		radius = int(radius)

		ellipse = cv2.fitEllipse(cnt)
		img = cv2.ellipse(img,ellipse,(0,255,0),2)

		rect = cv2.minAreaRect(cnt)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		img = cv2.drawContours(img,[box],0,(255,255,255),2)

		width = ellipse[1][0]
		height = ellipse[1][1]
		aspect_ratio = width/height

		with open('extracted_features/test.csv', 'a', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([width,height,aspect_ratio,area,radius,perimeter,0])

features_extract()

