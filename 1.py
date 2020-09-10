#simple program to read and show image using opencv and matsploit
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('OpenCV Basics/dog.png')#read an image
#by default opencv uses bgr color spaces. se we convert back into rgb colorspaces
newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img) #plot the image
plt.show()
plt.imshow(newImg)
plt.show()
print(img)
