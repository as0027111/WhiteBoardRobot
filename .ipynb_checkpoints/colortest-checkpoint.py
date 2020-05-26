# -*- coding: utf-8 -*-
import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/green&blue.jpg', 1) #利用灰階讀圖
color =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#正常的顏色

HSVframe =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#%%blue
colorLow = np.array([100,43,46]) #blue(HSV)
colorHigh = np.array([124,255,255]) #blue(HSV)
mask = cv2.inRange(HSVframe, colorLow, colorHigh)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

c = max(contours, key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
cv2.rectangle(color,(x,y),(x+w,y+h),(0,0,255),20)
#%%green

colorLow = np.array([35,43,46]) #green(HSV)
colorHigh = np.array([90,255,255]) #green(HSV)
mask = cv2.inRange(HSVframe, colorLow, colorHigh)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for i in contours:
    cnt=i
    x,y,w,h = cv2.boundingRect(cnt)
    if w>50 and h>50:
        cv2.rectangle(color,(x,y),(x+w,y+h),(0,255,0),10)
'''
c = max(contours, key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),20)
'''
plt.imshow(color)