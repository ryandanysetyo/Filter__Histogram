import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('wwim.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)    #rumus equalization

cv2.imshow('Gambar Asli',img)
cv2.imshow('Grayscale',gray)
cv2.imshow('Histogram Equalization', equ)

plt.figure('Histogram Equalization')
plt.subplot(2,1,1),plt.hist(gray.ravel(),256,[0,256]),plt.title('Histogram awal')
plt.subplot(2,1,2),plt.hist(equ.ravel(),256,[0,256]),plt.title('Histogram hasil equalization')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()