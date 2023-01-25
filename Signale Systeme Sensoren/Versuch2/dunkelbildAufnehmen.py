import cv2
import numpy as np
#beim Dunkelbild muss man beachten, dass die Belichtungsparameter
#identisch eingestellt sind wie beim Graukeil

#bildgröße
rows= 480
columns= 640

cap = cv2.VideoCapture(0)
#array für bilder(einzelne Pixelwerte in bildgröße)
grayFramesAsArray = []
#Liste mit den Framenamen anlegen
grayDarkFrame = ["grayDarkFrame0.png", "grayDarkFrame1.png",
                 "grayDarkFrame2.png", "grayDarkFrame3.png",
                 "grayDarkFrame4.png", "grayDarkFrame5.png",
                 "grayDarkFrame6.png", "grayDarkFrame7.png",
                 "grayDarkFrame8.png", "grayDarkFrame9.png"]
# belichtungspar. setzen
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
    cv2.imshow('Dunkelbild', frame)

    #mit q das Foto aufnehmen
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #Wegen der for-Schleife werden automatisch
        #10 Aufnahmen erstellt
        #und in float32 umwandeln
        for i in range(0,10):
            frame = frame.astype('float32')
            cv2.imwrite(grayDarkFrame[i], frame)
        break;

for i in range(10):
    img_path = r'/home/twobeers/Downloads/SSS/' + grayDarkFrame[i]      #path of pictures
    src2 = cv2.imread(img_path)
    grayFramesAsArray.append(cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY))

meanArray = np.zeros((rows,columns))
for i in range(rows):
    for j in range(columns):
        for k in range(10):
            tmp = np.zeros((0))
            tmp = np.append(tmp,grayFramesAsArray[k][i][j])        #speichern der zehn ij pixelwerte aus den 10 dunkelbildern
        meanAtPixelij = np.mean(tmp)                               # mittelwert des Pixelwertes ij der 10 dunkelbilder
        meanArray[i][j] = meanAtPixelij                            # mittelwert Dunkelbild-Matrix
print("it worked")
cv2.imwrite('dunkelbildMeanMatrix.png',meanArray)
# Einlesen des Graukeils 
img_path = r'/home/twobeers/Downloads/SSS/testbild.png'                 #Pfad des Graukeilbildes
graukeil = cv2.imread(img_path)
graukeil.astype('float32')
graukeil = cv2.cvtColor(graukeil, cv2.COLOR_BGR2GRAY)
# subtrahieren des Dunkelbildes vom Graukeil
korrigiert = np.subtract(graukeil,meanArray)
# Speichern des korrigierten Bildes
cv2.imwrite('korrigiertDunkel.png', korrigiert)
# dunkelbild konstrastmaximiert darstellen
dunkelContrastMax = cv2.imread(r'/home/twobeers/Downloads/SSS/dunkelbildMeanMatrix.png')
alpha = 3 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)
dunkelContrastMax = cv2.convertScaleAbs(dunkelContrastMax, alpha=alpha, beta=beta)
cv2.imwrite('dunkelContrastMax.png', dunkelContrastMax)

cap.release()
cv2.destroyAllWindows()