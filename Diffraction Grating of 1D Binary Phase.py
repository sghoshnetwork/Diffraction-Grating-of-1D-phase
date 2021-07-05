#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Diffraction Grating of 1D phase
# Illuminated by a uniform plane wave with a wavelength of 1 um.
# Using a Fourier lens has a focal length of 7 cm
# Codes by Subham Ghosh (JIS College of Engineering, WB, India)

import matplotlib.pyplot as plt
import numpy as np

# Number of sample points for one period.
N = 2**10

# Period in um
L = 10

# Sampling period
delta_x = L/N

# Plot one period

x_element = delta_x * np.linspace(0,N-1,N)

y_element = np.zeros(N)

# Thckiness of the grating element in um
d = 1

for i in range(N):
    if x_element[i] < L/2: 
        y_element[i] = d
        
plt.figure(1)
plt.plot(x_element,y_element)
plt.xlabel('x (um)')
plt.ylabel('Height (um)')
plt.title('Grating Phase Element')
plt.grid()
plt.show()

# Posit, we have 10 period of gratings.

y_grating = np.tile(y_element, 10)
N_grating = 10*N
x_grating = delta_x * np.linspace(-N_grating/2,N_grating/2-1,N_grating) + L/4

plt.figure(2)
plt.plot(x_grating,y_grating)
plt.xlabel('x (um)')
plt.ylabel('Height (um)')
plt.title('1D Phase Grating')
plt.grid()
plt.show()

# An on-axis plane wave illumination with a wavelength of 1um
wl = 1

# Refractive index at 1um
n = 1.5

# Phase delay
phase_delay = (2*np.pi/wl) * (n-1) * d

# Assume a unifom plane wave illumation, we only illuminate part of the grating.

y_amp = np.zeros(N_grating)

for i in range(N_grating):
    if x_grating[i] > -4*L -L/4 and x_grating[i] < 4*L + L/4: 
        y_amp[i] = 1
        
plt.figure(3)
plt.plot(x_grating,y_amp,'r', linewidth=5)
plt.plot(x_grating,y_grating,'b')
plt.xlabel('x (um)')
plt.ylabel('Amplitude (a.u.)')
plt.title('Uniform Illumination')
plt.grid()
plt.show()

# Phase delay of for this illimination

y_phase = y_grating * phase_delay

plt.figure(4)
plt.plot(x_grating,y_phase,'g')
plt.xlabel('x (um)')
plt.ylabel('Phase (rad)')
plt.title('Phase')
plt.grid()
plt.show()

# Amplitude PSF is the FFT of the pupil mask

y = y_amp*np.exp(1j*y_phase)

# Pad zeros

m = 2**14

y = np.pad(y, (m,m), 'constant', constant_values=(0,0))

yShift = np.fft.fftshift(y)
fftyShift = np.fft.fft(yShift)
yf = np.fft.fftshift(fftyShift)

# Normalise the intensity
y_intensity = (np.abs(yf))**2
y_intensity = y_intensity/np.max(y_intensity)


# Define x cooridnate in the image plane

# A Fourier lens has a focal length of 7 cm
f = 7
u = np.linspace(-(N_grating+2*m)/2,(N_grating+2*m)/2-1,N_grating+2*m)/(delta_x*(N_grating+2*m))
xf = u*(wl*f)

# Ploting of diffraction pattern
plt.figure(5)
plt.plot(xf,y_intensity)
plt.xlim(-7,7)
plt.xlabel('u (cm)')
plt.ylabel('Intensity (a.u.)')
plt.title('Diffraction Grating of 1D phase')
plt.grid()


# In[ ]:




