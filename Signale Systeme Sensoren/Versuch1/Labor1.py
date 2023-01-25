# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

def readCSV(filename):
    """
    This function reads CSV data into 2D Array
    """
    data = np.genfromtxt(filename,delimiter=',',usecols=(3,4))

    for i in range(1200):                       #delete first 1200lines
        data = np.delete(data, (0), axis=0)
    for i in range(650):                    
        data = np.delete(data, (650), axis=0)   #delete last 650lines    
    data = np.delete(data,0,1)
    return data

def meanOfVoltData(data):
    return np.mean(data)
def stdOfVoltData(data):
    return np.std(data)

def steigung(Xdata,Ydata):
    XdataMean = np.mean(Xdata)
    YdataMean = np.mean(Ydata)
    up = 0
    down = 0
    for i in range(21):
        up = up + ((Xdata[i] - XdataMean) * (Ydata[i] - YdataMean))
        down = down + (Xdata[i]-XdataMean)**2
    return up/down


#######################################################

dataM1 = readCSV('m1.csv')
dataM2 = readCSV('m2.csv')
dataM3 = readCSV('m3.csv')
dataM4 = readCSV('m4.csv')
dataM5 = readCSV('m5.csv')
dataM6 = readCSV('m6.csv')
dataM7 = readCSV('m7.csv')
dataM8 = readCSV('m8.csv')
dataM9 = readCSV('m9.csv')
dataM10= readCSV('m10.csv')
dataM11= readCSV('m11.csv')
dataM12= readCSV('m12.csv')
dataM13= readCSV('m13.csv')
dataM14= readCSV('m14.csv')
dataM15= readCSV('m15.csv')
dataM16= readCSV('m16.csv')
dataM17= readCSV('m17.csv')
dataM18= readCSV('m18.csv')
dataM19= readCSV('m19.csv')
dataM20= readCSV('m20.csv')


dataMean = np.array([meanOfVoltData(dataM1),        #Mittelwerte in V 
                     meanOfVoltData(dataM2),
                     meanOfVoltData(dataM3),
                     meanOfVoltData(dataM4),
                     meanOfVoltData(dataM5),
                     meanOfVoltData(dataM6),
                     meanOfVoltData(dataM7),
                     meanOfVoltData(dataM8),
                     meanOfVoltData(dataM9),
                     meanOfVoltData(dataM10),
                     meanOfVoltData(dataM11),
                     meanOfVoltData(dataM12),
                     meanOfVoltData(dataM13),
                     meanOfVoltData(dataM14),
                     meanOfVoltData(dataM15),
                     meanOfVoltData(dataM16),
                     meanOfVoltData(dataM17),
                     meanOfVoltData(dataM18),
                     meanOfVoltData(dataM19),
                     meanOfVoltData(dataM20)])

dataStd = np.array([stdOfVoltData(dataM1),          #Standardabweichung in V
                     stdOfVoltData(dataM2),
                     stdOfVoltData(dataM3),
                     stdOfVoltData(dataM4),
                     stdOfVoltData(dataM5),
                     stdOfVoltData(dataM6),
                     stdOfVoltData(dataM7),
                     stdOfVoltData(dataM8),
                     stdOfVoltData(dataM9),
                     stdOfVoltData(dataM10),
                     stdOfVoltData(dataM11),
                     stdOfVoltData(dataM12),
                     stdOfVoltData(dataM13),
                     stdOfVoltData(dataM14),
                     stdOfVoltData(dataM15),
                     stdOfVoltData(dataM16),
                     stdOfVoltData(dataM17),
                     stdOfVoltData(dataM18),
                     stdOfVoltData(dataM19),
                     stdOfVoltData(dataM20)])

distance = np.arange(10,32,3)
distance = np.append(distance,[33])
distance = np.append(distance,np.arange(36,67,3))

'''
plt.plot(distance, dataMean)             #X in sec & Y in Volts
plt.title('Mittelwerte aus 1-20.csv')
plt.xlabel('Länge in cm')
plt.ylabel('Spannung in V')
plt.ylim(0.3,1.5)
plt.xlim(8,72)
plt.show()
'''

plt.errorbar(distance, dataMean, yerr=dataStd, linestyle='solid',
             marker='.', capsize=3)
plt.title('Mittelwerte aus 1-20.csv mit Standardabweichung')
plt.xlabel('Länge in cm')
plt.ylabel('Spannung in V')
plt.ylim(0.3,1.5)
plt.xlim(8,72)
plt.show()


########  Messergebnisse
distanceInCm = np.arange(10,71,3)
meanOfVoltage = np.array([1.435,1.305,1.143,1.029,0.9538,0.9182,
                 0.7863,0.785,0.7098,0.6926,0.6318,0.6118,
                 0.6044,0.5643,0.5442,0.5438,0.539,0.5037,
                 0.4868,0.4489,0.4678])


########  Plot distance and voltage
plt.plot(distanceInCm, meanOfVoltage)             #X in sec & Y in Volts
plt.title('Messergebnisse per Hand')
plt.xlabel('Länge in cm')
plt.ylabel('Spannung in V')
plt.ylim(0.3,1.5)
plt.xlim(8,72)
plt.show()




########  Task 2 Modellierung der Kennlinie - lin. Regression

########  ln of distance and voltage 
distanceLog = np.log(distanceInCm)
VoltageLog = np.log(meanOfVoltage)

########  plot ln  of csv files
plt.plot(np.log(distance),np.log(dataMean),label="csv Daten") 
plt.plot(distanceLog,VoltageLog,label="Messdaten")            #X in sec & Y in Volts
plt.title('Log von csv-files und eigenen Messungen')
plt.xlabel('log of distance')
plt.ylabel('log of voltage')
plt.legend(loc=3)

plt.show()

########  Plot ln of eigene Messungen
plt.plot(distanceLog,VoltageLog)             #X in sec & Y in Volts
plt.title('Log von eigenen Messungen')
plt.xlabel('log of distance')
plt.ylabel('log of voltage')
plt.show()


########  lin Reg of our data
a = steigung(VoltageLog,distanceLog)
b = np.mean(distanceLog) - a * np.mean(VoltageLog)

y = np.empty([21], dtype=float)
for i in range(21):
    y[i] = a * VoltageLog[i] + b
    
y2 = math.exp(b)*(meanOfVoltage**a)         #kennlinie e^b * x^aa

plt.plot(y2,meanOfVoltage)
plt.title('Kennlinie e^b * x^a')
plt.xlabel('Länge in cm')
plt.ylabel('Spannung in V')
plt.show()

plt.plot(distanceLog,VoltageLog,'bo',label="Messdaten")
plt.plot(y,VoltageLog,'r', label="Ausgleichsgerade")
plt.title('Ausgleichsgerade mit log von Daten')
plt.xlabel('log of distance')
plt.ylabel('log of voltage')
#plt.plot(meanOfVoltage,y2)

plt.legend(loc=3)
plt.show()

########  linear regression with seaborn lib
#sns.regplot(x = distanceInCm,y = meanOfVoltage)


#########################################################
########  FLÄCHENMESSUNG TEIL 3
#########################################################

dina4B = readCSV('dina4b.csv')
dina4L = readCSV('dina4l.csv')

mean4B = np.mean(dina4B)
mean4L = np.mean(dina4L)
std4B = np.std(dina4B)
std4L = np.std(dina4L)


lnL68min = a * -0.29029303022 + b
L68min = math.exp(lnL68min)
lnL68max = a * -0.33973963898 + b
L68max = math.exp(lnL68max)

lnL95min = a * -0.36349476511 + b
L95min = math.exp(lnL95min)
lnL95max = a * -0.26660422813 + b
L95max = math.exp(lnL95max)

lnB68min = a * -0.07906213383 + b
B68min = math.exp(lnB68min)
lnB68max = a * -0.11711579351 + b
B68max = math.exp(lnB68max)

lnB95min = a * -0.0612982658 + b
B95min = math.exp(lnB95min)
lnB95max = a * -0.13590903207 + b
B95max = math.exp(lnB95max)

L=0.7857
B=0.9727
#########68% sicherheit
Lmin = a*(np.log(L+std4L))+b
Lmin = math.exp(Lmin)

Lmax = a*(np.log(L-std4L))+b
Lmax = math.exp(Lmax)
#########95%sicherheit
Lmin1 = a*(np.log(L+1.96*std4L))+b
Lmin1 = math.exp(Lmin)

Lmax1 = a*(np.log(L-1.96*std4L))+b
Lmax1 = math.exp(Lmax)
############# BREITE
#########68% sicherheit
Bmin = a*(np.log(B+std4B))+b
Bmin = math.exp(Bmin)

Bmax = a*(np.log(B-std4B))+b
Bmax = math.exp(Bmax)
#########95%sicherheit
Bmin1 = a*(np.log(B+1.96*std4B))+b
Bmin1 = math.exp(Bmin1)

Bmax1 = a*(np.log(B-1.96*std4B))+b
Bmax1 = math.exp(Bmax1)

FlächeMax = Lmax * Bmax
FlächeMin = Lmin * Bmin


























