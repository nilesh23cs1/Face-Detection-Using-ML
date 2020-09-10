# Simple Program to read and show an image

import cv2

img = cv2.imread('OpenCV Basics/dog.png')#we didnot need to covert colorspace back into rgb
gray = cv2.imread('OpenCV Basics/dog.png',cv2.IMREAD_GRAYSCALE)#shows grayscale image

cv2.imshow('Dog Image',img)# dog title is 'Dog Image'
cv2.imshow('Gray Dog Image',gray)# dog title is 'Gray Dog Image'

cv2.waitKey(0) #parameter 0 is time means wait infinitely. Program will stop when any key is pressed
#cv2.waitKey(25) #it means wait for 25 millisecond befor all window get distroyed
cv2.destroyAllWindows()# it will destroy window after 25 millisecond
