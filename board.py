# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:29:36 2020

@author: HuJaMing
"""
import cv2 
import numpy as np

img = cv2.imread('C:\\Users\\HuJaMing\\Desktop\\board.jpg', 1) #利用灰階讀圖
cv2.namedWindow('result', 0)
cv2.resizeWindow('result', 640, 480)

'''
cv2.imshow('result', morph_o)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#%%
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite('gray.jpg', gray)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)  #19-19+canny0-90感覺消很多
#cv2.imwrite('blurred.jpg', blurred)
canny = cv2.Canny(blurred, 0, 20)

'''
ret, thresh = cv2.threshold(canny, 200, 255, cv2.THRESH_BINARY)
cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, cnts, -1, (0, 255, 0), thickness=2)
'''

kernel = np.ones((1, 20), np.uint8) #設定卷積核 (高, 寬)
dilation = cv2.dilate(canny,kernel,iterations = 1)
#cv2.imwrite('dilation1.jpg', dilation)

dst = 255 - dilation #反白
#cv2.imwrite('dst.jpg', dst)

#cv2.imshow('result', dst)


kernel = np.ones((50,50), np.uint8) 
morph_o = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel) #影象開運算-去除躁點
#cv2.imwrite('morph_o.jpg', morph_o)

kernel = np.ones((1, 300), np.uint8) #設定卷積核 (高, 寬)
dilation = cv2.dilate(morph_o,kernel,iterations=1)
#cv2.imwrite('dilation2.jpg', dilation)

#morph_c = cv2.morphologyEx(morph_o, cv2.MORPH_GRADIENT, kernel) #影象閉運算
#ret, thresh = cv2.threshold(morph_o, 127, 255, 0)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for i in contours:
    cnt=i
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,255,0),10)
'''
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]
x,y,w,h = cv2.boundingRect(cnt)
'''
c = max(contours, key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),20)
    

cv2.namedWindow('result2', 0)
cv2.resizeWindow('result2', 640, 480)
result = np.hstack([morph_o,dilation])
cv2.imshow('result2', img)
#cv2.imwrite('result.jpg', img)

cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()