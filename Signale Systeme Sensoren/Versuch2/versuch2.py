#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:02:10 2021

@author: twobeers
"""

import numpy as np
import cv2

def readImg(img_path):
    src = cv2.imread(img_path)
    return cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cap = cv2.VideoCapture(0)
cap.set(10, 150)
cap.set(11,128)
cap.set(12,64)
cap.set(14,-1)
cap.set(15,156)
cap.set(17,-1)
print("framewidth:" + str(cap.get(3)))
print("frameheight:" + str(cap.get(4)))
print("--------------------------------")
print("brightness:" + str(cap.get(10)))
print("contrast:" + str(cap.get(11)))
print("saturation:" + str(cap.get(12)))
print("--------------------------------")
print("gain:" + str(cap.get(14)))
print("exposure:" + str(cap.get(15)))
print("--------------------------------")
print("whitebalance:" + str(cap.get(17)))
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("video capture", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("testbild.png",gray)           #beim schließen wird testbild gespeichert
        
        break;
cap.release()
cv2.destroyAllWindows()

image_path = r'/home/twobeers/Downloads/SSS/testbild.png'
img = readImg(image_path)           #graubild
cv2.imshow("graubild", img)