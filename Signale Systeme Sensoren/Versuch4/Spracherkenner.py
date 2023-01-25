# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:37:05 2021

@author: tobias-mack
"""

from re import match

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
from scipy.fftpack import fft, fftshift


import wave

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 48000      #Abtastrate
FRAMESIZE = 1024
NOFFRAMES = 220
CHANNELS = 1
CHUNK = NOFFRAMES*FRAMESIZE     #SignallÃ¤nge M?
p = pyaudio.PyAudio()
print('running')
frames = []


stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=SAMPLEFREQ, input=True,
                frames_per_buffer=FRAMESIZE)
data = stream.read(CHUNK)

decoded = np.frombuffer(data, 'int16')    #Erstellen eines int16 Arrays der zuvor eingelesenen Daten
frames.append(data)
stream.stop_stream()
stream.close()
p.terminate()
# Write and Close the File
decoded = np.frombuffer(data, dtype=int)

np.savetxt('messungandere4.txt',decoded,delimiter=',')



'''
================
    Task 1
================
'''

'''
a) Audio record 
'''

'''
b) Signal editing
#=>     Trigger cut at 0  
#=>     remaining runtime 1000ms
#=>     missing samples filed with zeros
#=>     plot result
'''
csvData = np.genfromtxt("messungandere4.txt", dtype=float, encoding=None, skip_header=0)

print(csvData)
c = 0
for i in csvData:
    c = c + 1
    if i > 100000000:
        csvData2 = np.genfromtxt("messungandere4.txt", dtype=float, encoding = None,skip_header= c - 5)
        break

c = csvData2.size
c = 0
for i in np.flip(csvData2):
    c = c - 1
    if (i > 50000000):
        break
    csvData2[c] = 0

np.flip(csvData2)
signalLength = 29696
csvData2 = csvData2[0:signalLength]

decodedRaw2 = csvData2
np.savetxt('HochTest21.txt',csvData2,delimiter=',')
print("csvData2")
print(csvData2)
"""
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(csvData)
ax2.plot(csvData2)                         #Ploten der Daten
#ax1.plot(csvData)
#ax2.plot(csvData2)
plt.xlabel("Abtastung")
plt.ylabel("f(t)")
ax1.title.set_text('Raw signal')
ax2.title.set_text('Edited signal')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)
fig.show()
"""

'''
c) Amplitude spectrum 
#=>     calculating Amplitude spectrum (Prog.Code L3_21)
#=>     plot result
'''

    #Erstellen eines int16 Arrays der zuvor eingelesenen Daten
decodedRaw = np.genfromtxt("Rechts5.txt", dtype=float, encoding = None)                     #Erstellen einer Kopie
csvData3 = np.genfromtxt("Rechts5.txt", dtype=float, encoding = None)

TiefTest1 = np.genfromtxt("HochTest21.txt", dtype=float, encoding = None)

Rechts1 = np.genfromtxt("Rechts1.txt", dtype=float, encoding = None)
Rechts2 = np.genfromtxt("Rechts2.txt", dtype=float, encoding = None)
Rechts3 = np.genfromtxt("Rechts3.txt", dtype=float, encoding = None)
Rechts4 = np.genfromtxt("Rechts4.txt", dtype=float, encoding = None)
Rechts5 = np.genfromtxt("Rechts5.txt", dtype=float, encoding = None)

Links1 = np.genfromtxt("Links5.txt", dtype=float, encoding = None)
Links2 = np.genfromtxt("Links5.txt", dtype=float, encoding = None)
Links3 = np.genfromtxt("Links5.txt", dtype=float, encoding = None)
Links4 = np.genfromtxt("Links5.txt", dtype=float, encoding = None)
Links5 = np.genfromtxt("Links5.txt", dtype=float, encoding = None)

Hoch1 = np.genfromtxt("Hoch1.txt", dtype=float, encoding = None)
Hoch2 = np.genfromtxt("Hoch2.txt", dtype=float, encoding = None)
Hoch3 = np.genfromtxt("Hoch3.txt", dtype=float, encoding = None)
Hoch4 = np.genfromtxt("Hoch4.txt", dtype=float, encoding = None)
Hoch5 = np.genfromtxt("Hoch5.txt", dtype=float, encoding = None)

Tief1 = np.genfromtxt("Tief1.txt", dtype=float, encoding = None)
Tief2 = np.genfromtxt("Tief2.txt", dtype=float, encoding = None)
Tief3 = np.genfromtxt("Tief3.txt", dtype=float, encoding = None)
Tief4 = np.genfromtxt("Tief4.txt", dtype=float, encoding = None)
Tief5 = np.genfromtxt("Tief5.txt", dtype=float, encoding = None)

fftData = np.zeros(512)
fftDataTT1 = np.zeros(512)

fftDataT1 = np.zeros(512)
fftDataT2 = np.zeros(512)
fftDataT3 = np.zeros(512)
fftDataT4 = np.zeros(512)
fftDataT5 = np.zeros(512)

fftDataH1 = np.zeros(512)
fftDataH2 = np.zeros(512)
fftDataH3 = np.zeros(512)
fftDataH4 = np.zeros(512)
fftDataH5 = np.zeros(512)

fftDataL1 = np.zeros(512)
fftDataL2 = np.zeros(512)
fftDataL3 = np.zeros(512)
fftDataL4 = np.zeros(512)
fftDataL5 = np.zeros(512)

fftDataR1 = np.zeros(512)
fftDataR2 = np.zeros(512)
fftDataR3 = np.zeros(512)
fftDataR4 = np.zeros(512)
fftDataR5 = np.zeros(512)

fftDataLL= np.square(abs(np.fft.fft(Links1))   )

csvData2 = abs(np.fft.fft(csvData2))         #Berechnung der Fouriertransformation
power_decoded = np.square(csvData2)
frequency = np.linspace(0, SAMPLEFREQ/2, len(power_decoded))
print("FFT Complete")


fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(Links1)
ax2.plot(frequency/2, fftDataLL, 'r')
plt.axis([0, 1000, 0, max(fftDataLL)])
ax1.title.set_text('Links Raw signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()

#Plot des Signals und Amplitudenspektrums
"""
fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(decodedRaw2)
ax2.plot(frequency/2, power_decoded, 'r')
plt.axis([0, 1000, 0, max(power_decoded)])
ax1.title.set_text('Edited signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()
"""

'''
d) Windowing

#=>     local fft in each window
#=>     Amplitude spectrum
#=>     compare this plot with testPlot c)
#=>     transforming the Signal into 512ms Sections
        #with 50% overlap
#=>     Wighting of Sections with Gaussian Window function
        #window width = 4 * Std
'''




#window = signal.gaussian(512, std=128)
window = np.kaiser(512, 4)
#window = np.blackman(512)
print("csvData3.size")
print(csvData3.size)

#window = 1
i=0
print("window Complete")
while i < (signalLength/256)-1:
    #print(abs(np.fft.fft(csvData3[(i*256):(512 + (i * 256))] * window)))
    fftData[0:512] = (abs(np.fft.fft(csvData3[(i*256):(512 + (i * 256))] )) + fftData[0:512])
    fftDataTT1[0:512] = abs(np.fft.fft(TiefTest1[(i * 256):(512 + (i * 256))])) + fftDataTT1[0:512]

    fftDataT1[0:512] = abs(np.fft.fft(Tief1[(i * 256):(512 + (i * 256))])) + fftDataT1[0:512]
    fftDataT2[0:512] = abs(np.fft.fft(Tief2[(i * 256):(512 + (i * 256))])) + fftDataT2[0:512]
    fftDataT3[0:512] = abs(np.fft.fft(Tief3[(i * 256):(512 + (i * 256))])) + fftDataT3[0:512]
    fftDataT4[0:512] = abs(np.fft.fft(Tief4[(i * 256):(512 + (i * 256))])) + fftDataT4[0:512]
    fftDataT5[0:512] = abs(np.fft.fft(Tief5[(i * 256):(512 + (i * 256))])) + fftDataT5[0:512]
#
    fftDataH1[0:512] = abs(np.fft.fft(Hoch1[(i * 256):(512 + (i * 256))])) + fftDataH1[0:512]
    fftDataH2[0:512] = abs(np.fft.fft(Hoch2[(i * 256):(512 + (i * 256))])) + fftDataH2[0:512]
    fftDataH3[0:512] = abs(np.fft.fft(Hoch3[(i * 256):(512 + (i * 256))])) + fftDataH3[0:512]
    fftDataH4[0:512] = abs(np.fft.fft(Hoch4[(i * 256):(512 + (i * 256))])) + fftDataH4[0:512]
    fftDataH5[0:512] = abs(np.fft.fft(Hoch5[(i * 256):(512 + (i * 256))])) + fftDataH5[0:512]
#
    fftDataR1[0:512] = abs(np.fft.fft(Rechts1[(i * 256):(512 + (i * 256))])) + fftDataR1[0:512]
    fftDataR2[0:512] = abs(np.fft.fft(Rechts2[(i * 256):(512 + (i * 256))])) + fftDataR2[0:512]
    fftDataR3[0:512] = abs(np.fft.fft(Rechts3[(i * 256):(512 + (i * 256))])) + fftDataR3[0:512]
    fftDataR4[0:512] = abs(np.fft.fft(Rechts4[(i * 256):(512 + (i * 256))])) + fftDataR4[0:512]
    fftDataR5[0:512] = abs(np.fft.fft(Rechts5[(i * 256):(512 + (i * 256))])) + fftDataR5[0:512]
#
    fftDataL1[0:512] = abs(np.fft.fft(Links1[(i * 256):(512 + (i * 256))])) + fftDataL1[0:512]
    fftDataL2[0:512] = abs(np.fft.fft(Links2[(i * 256):(512 + (i * 256))])) + fftDataL2[0:512]
    fftDataL3[0:512] = abs(np.fft.fft(Links3[(i * 256):(512 + (i * 256))])) + fftDataL3[0:512]
    fftDataL4[0:512] = abs(np.fft.fft(Links4[(i * 256):(512 + (i * 256))])) + fftDataL4[0:512]
    fftDataL5[0:512] = abs(np.fft.fft(Links5[(i * 256):(512 + (i * 256))])) + fftDataL5[0:512]

    print(i)
    i = i+1

fftDataH = (fftDataH1+fftDataH2+fftDataH3+fftDataH4+fftDataH5 / (10496 / 256)) / 5
fftDataH = fftDataH * window

fftDataT = (fftDataT1+fftDataT2+fftDataT3+fftDataT4+fftDataT5 / (10496 / 256)) / 5
fftDataT = fftDataT * window

fftDataL = (fftDataL1+fftDataL2+fftDataL3+fftDataL4+fftDataL5 / (10496 / 256)) / 5
fftDataL = fftDataL * window

fftDataR = (fftDataR1+fftDataR2+fftDataR3+fftDataR4+fftDataR5 / (10496 / 256)) / 5
fftDataR = fftDataR * window
#fftData = fftData/(signalLength / 256)
fftData = fftData/(10496 / 256)
fftData = fftData * window

fftDataTT1 = fftDataTT1/(10496 / 256)
fftDataTT1 = fftDataTT1 * window

#print(fftData)
#csvData3 = np.fft.rfft(csvData3)
power_decoded = fftData
power_decodedH = fftDataH
power_decodedT = fftDataT
power_decodedL = fftDataL
power_decodedR = fftDataR

power_decodedTT1 = fftDataTT1
#power_decoded = np.square(fftData)
#frequency = np.linspace(0, SAMPLEFREQ/2, len(csvData3))
frequency = np.linspace(0, SAMPLEFREQ/2, len(power_decoded))
print("0 Test")

yAxis = 1000
#scipy.stats.pearsonr(x, y)

KoeffT = sp.stats.pearsonr(fftDataT,fftDataTT1)
KoeffH = sp.stats.pearsonr(fftDataH,fftDataTT1)
KoeffL = sp.stats.pearsonr(fftDataL,fftDataTT1)
KoeffR = sp.stats.pearsonr(fftDataR,fftDataTT1)
print("koeffizient T:")
print(KoeffT[0])
print(KoeffH[0])
print(KoeffL[0])
print(KoeffR[0])
maxkoef= max(KoeffT[0], KoeffH[0], KoeffL[0], KoeffR[0])*100
print(max(KoeffT[0], KoeffH[0], KoeffL[0], KoeffR[0])*100)

if (KoeffT[0] * 100 == maxkoef):
    print("Tief mit ", maxkoef, "%")

if (KoeffH[0] * 100 == maxkoef):
    print("Hoch mit ", maxkoef, "%")

if (KoeffR[0] * 100 == maxkoef):
    print("Rechts mit ", maxkoef, "%")

if (KoeffL[0] * 100 == maxkoef):
    print("Links mit ", maxkoef, "%")


fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(decodedRaw2)
ax2.plot(frequency/2, power_decoded, 'r')
plt.axis([0, yAxis, 0, max(power_decoded)])
ax1.title.set_text('Edited signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()

fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(Hoch1)
ax2.plot(frequency/2, power_decodedH, 'r')
plt.axis([0, yAxis, 0, max(power_decodedH)])
ax1.title.set_text('Hoch signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()

fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(Tief1)
ax2.plot(frequency/2, power_decodedT, 'r')
plt.axis([0, yAxis, 0, max(power_decodedT)])
ax1.title.set_text('Tief signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()

fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(Rechts1)
ax2.plot(frequency/2, power_decodedR, 'r')
plt.axis([0, yAxis, 0, max(power_decodedR)])
ax1.title.set_text('Rechts signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()

fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(Links1)
ax2.plot(frequency/2, power_decodedL, 'r')
plt.axis([0, yAxis, 0, max(power_decodedL)])
ax1.title.set_text('Links signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()

fig.show()

fig, (ax1, ax2) = plt.subplots(2)
ax1.set(xlabel="Abtastung", ylabel="f(t)")
ax2.set(xlabel="Hz", ylabel="|f(t)|")
ax1.plot(TiefTest1)
ax2.plot(frequency/2, power_decodedTT1, 'r')
plt.axis([0, yAxis, 0, max(power_decodedTT1)])
ax1.title.set_text('TiefTest1 signal')
ax2.title.set_text('Amplitude spectrum ')
plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.5)

fig.show()

#sample1 = csvData2[0:512]
#sample2 = csvData2[261:773]
n = 512
p = 261





'''
window = signal.gaussian(512, std=4)                 #Std 4
plt.plot(window)
A = fft(window, 2048) / (len(window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
plt.plot(freq, response)
plt.axis([-0.5, 0.5, -120, 0])
plt.title(r"Frequency response of the Gaussian window ($\sigma$=7)")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
'''
'''
================
    Task 2
================
'''

'''
a) Recording + Reference spectrum's
#=>     recording 5 times, sound signals of "Hoch”, ”Tief”, ”Links” and ”Rechts”
#=>     creating each spectrum using Method of Task 1
#=>     calculate each reference spectrum
'''

'''
b) Recording
#=>     recording 5 times, sound signals of "Hoch”, ”Tief”, ”Links” and ”Rechts” with another voice
'''

'''
c) calculate Correlation coefficients 
#=>     calc covariance 
        µf =  int_{-∞}^∞
#=>     calculate Correlation coefficients (Bravis-Pearson)
        rfg =σfg/(σf·σg)
#=>     comparing reference spectrum
        if (spectrum1 == spectrum2) 1 else 0
'''

'''
d) Recording
#=>     implementing architecture 
#=>     testing with all Records
#=>     print Detection rate in percent 
#=>     print Error rate in percent 
'''

#wf = wave.open("output.wav", 'rb')        #öffnen des zuvor aufgenommenen Signals
#erstellen eines Streams
#stream = p.open(format=FORMAT, channels=wf.getnchannels(), rate=SAMPLEFREQ, input=True, frames_per_buffer=FRAMESIZE)
#data = wf.readframes(480)                 #Einlesen von 480 Abtastungen (10 ms)



