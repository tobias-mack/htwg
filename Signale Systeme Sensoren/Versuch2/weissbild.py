#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 06:59:17 2021

@author: twobeers
"""
import cv2
import numpy as np
import math
#bildgröße
rows= 480
columns= 640
# das Weißbild muss in der gleichen Entfernung wie das 
# zu korrigierende Bild aufgenommen werden
# die Belichtung auf 30-50% der Hellsättigung einzustellen.
gkPath = r'home/twobeers/Downloads/SSS/testbild.png'
graukeil = cv2.imread(gkPath)
whiteFramesAsArray = []
#Liste mit den Framenamen anlegen
whiteFrames = ["whiteFrames0.png", "whiteFrames1.png",
                 "whiteFrames2.png", "whiteFrames3.png",
                 "whiteFrames4.png", "whiteFrames5.png",
                 "whiteFrames6.png", "whiteFrames7.png",
                 "whiteFrames8.png", "whiteFrames9.png"]
# belichtungspar. müssen gleich sein wie das zu korrigierende Bild
cap = cv2.VideoCapture(0)
#Belichtungsparameter setzen
cap.set(10, 150)
cap.set(11,128)
cap.set(12,64)
cap.set(14,-1)
cap.set(15,156)
cap.set(17,-1)

while(True):
    ret, frame = cap.read()
    
    #mit cvtColor kann man die Aufnahme in ein anderen
    #Farbraum konvertieren
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('Weissbild', frame)

    #mit q das Foto aufnehmen
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #Wegen der for-Schleife werden automatisch
        #10 Aufnahmen erstellt
        #und in float32 umwandeln
        for i in range(0,10):
            frame = frame.astype('float32')
            cv2.imwrite(whiteFrames[i], frame)
        break;

for i in range(10):
    img_path = r'/home/twobeers/Downloads/SSS/' + whiteFrames[i]      #path of pictures
    src2 = cv2.imread(img_path)
    whiteFramesAsArray.append(cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY))

meanArray = np.zeros((rows,columns))
for i in range(rows):
    for j in range(columns):
        for k in range(10):
            tmp = np.zeros((0))
            tmp = np.append(tmp,whiteFramesAsArray[k][i][j])        #speichern der zehn ij pixelwerte aus den 10 weissbildern
        meanAtPixelij = np.mean(tmp)                               # mittelwert des Pixelwertes ij der 10 weissbilder
        meanArray[i][j] = meanAtPixelij                            # mittelwert weissbild-Matrix
print("it worked")
cv2.imwrite('Weißbild.png',meanArray)
# Einlesen des Graukeils 
img_path = r'/home/twobeers/Downloads/SSS/korrigiertDunkel.png'                 #Pfad der Dunkelbildkorrektur
graukeil = cv2.imread(img_path)
graukeil.astype('float32')
graukeil = cv2.cvtColor(graukeil, cv2.COLOR_BGR2GRAY)

# Normieren des Weissbildes
meanofWeiss = np.mean(meanArray)
normWeiss = np.divide(meanArray,meanofWeiss)

# dividieren des norm. weissbildes vom Graukeil + Speichern des korrigierten Bildes
korrigiert = np.divide(graukeil,normWeiss)
cv2.imwrite('korrigiertweiss.png', korrigiert)
# weissbild konstrastmaximiert darstellen
weissContrastMax = cv2.imread(r'/home/twobeers/Downloads/SSS/Weißbild.png')
alpha = 3 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)
weissContrastMax = cv2.convertScaleAbs(weissContrastMax, alpha=alpha, beta=beta)
cv2.imwrite('weissContrastMax.png', weissContrastMax)

cap.release()
cv2.destroyAllWindows()
    
    
    
    