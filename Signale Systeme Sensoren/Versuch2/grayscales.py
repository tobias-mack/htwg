#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:25:19 2021

@author: twobeers
"""

import numpy as np
import cv2

mainFrame = cv2.imread(r'/home/twobeers/Downloads/SSS/testbild.png')

#Stichpunkt Index Slicing
#0:350 ist die gesamte HÃ¶he vom Frame
#x:y ist jeweils die Teilbreite des Frames
#                     x:y
frame1 = mainFrame[0:479, 0:105,:]
cv2.imwrite('frame1.png', frame1)

frame2 = mainFrame[0:479, 107:247,:]
cv2.imwrite('frame2.png', frame2)

frame3 = mainFrame[0:479, 250:390,:]
cv2.imwrite('frame3.png', frame3)

frame4 = mainFrame[0:479, 395:533,:]
cv2.imwrite('frame4.png', frame4)

frame5 = mainFrame[0:479, 540:639,:]
cv2.imwrite('frame5.png', frame5)


frame1Mean = frame1.mean()
frame1Std = frame1.std()
print(frame1Mean)
print(frame1Std)
print("")

frame2Mean = frame2.mean()
frame2Std = frame2.std()
print(frame2Mean)
print(frame2Std)
print("")

frame3Mean = frame3.mean()
frame3Std = frame3.std()
print(frame3Mean)
print(frame3Std)
print("")

frame4Mean = frame4.mean()
frame4Std = frame4.std()
print(frame4Mean)
print(frame4Std)
print("")

frame5Mean = frame5.mean()
frame5Std = frame5.std()
print(frame5Mean)
print(frame5Std)
print("")
