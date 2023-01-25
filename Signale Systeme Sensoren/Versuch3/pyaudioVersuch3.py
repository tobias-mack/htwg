# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:28:19 2021

@author: Twobeers
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100              #Abtastfrequenz ?
FRAMESIZE = 1024                #
NOFFRAMES = 2                   #
CHUNK = NOFFRAMES*FRAMESIZE     #Signallänge M?
p = pyaudio.PyAudio()
print('running')

stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,input=True,
                frames_per_buffer=FRAMESIZE)
data = stream.read(CHUNK)
decoded = np.frombuffer(data, dtype=int);
#np.savetxt('messungandere.csv',decoded,delimiter=',')

stream.stop_stream()
stream.close()
p.terminate()
print('done')

fig, (ax1,ax2) = plt.subplots(2)
fig.suptitle('Audioaufnahme')
ax1.plot(decoded)


fourier_transform = np.fft.fft(decoded)
abs_fourier_transform = np.abs(fourier_transform)
power_spectrum = np.square(abs_fourier_transform)
frequency = np.linspace(0, SAMPLEFREQ/2, len(power_spectrum))
ax2.plot(frequency,power_spectrum)