# Python programe to illustrate 
# arithmetic operation of
# addition of two images
    
# organizing imports 
import cv2 
import numpy as np 
    
# path to input images are specified and  
# images are loaded with imread command 
image1 = cv2.imread('C:\\Users\mick.kelly\\OneDrive - ENTEKRA\\Documents\\Phyton\\1-500x250-3.jpg') 
image2 = cv2.imread('C:\\Users\\mick.kelly\\OneDrive - ENTEKRA\\Documents\\Phyton\\2-500x250-2.jpg')
image3 = cv2.imread('C:\\Users\\mick.kelly\\OneDrive - ENTEKRA\\Pictures\\2021-04-08_20h13_07.png')
  
# cv2.addWeighted is applied over the
# image inputs with applied parameters
weightedSum = cv2.addWeighted(image1, 1, image2, 0.9, 100)
  
# the window showing output image
# with the weighted sum 
cv2.imshow('Weighted Image', weightedSum)
  
# De-allocate any associated memory usage  
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 