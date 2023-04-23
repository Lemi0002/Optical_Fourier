"""
Script to evaluate the correspondence between a frequency and its position on the Fourier plane.
"""

import matplotlib.pyplot as plot
import numpy
import os
from filter_module import SinWave, image_filter

output_path = "output"

frequency_scale = 10 #2pi equals to frequency_scale * 2pi
width = 20*int(frequency_scale*2*numpy.pi) #allow multiple repetitions for better spectrum
height = width

# Create sin wave with superposition of multiple waves
wave = SinWave(width, height, frequency_scale)
wave.add(1, direction="x", dc=100)
wave.add(2, direction="x")
wave.add(1, direction="y")
wave.add(2, direction="y")

# Unmodified wave
plot.subplot(141)
plot.imshow(wave.canvas, cmap='gray')

# FFT2
plot.subplot(142)
fourier = numpy.fft.fftshift(numpy.fft.fft2(wave.canvas))
plot.imshow(numpy.log(abs(fourier),
        where=abs(fourier) > 0), cmap='gray')
x_width = 50
y_width = 50
plot.xlim(int(width/2 - x_width), int(width/2 + x_width))
plot.ylim(int(height/2 - y_width), int(height/2 + y_width))

# FFT2 after filter
plot.subplot(143)
image_fourier_lowpass = image_filter(fourier, 22, highpass=False)
plot.imshow(abs(image_fourier_lowpass), cmap="gray")
plot.xlim(int(width/2 - x_width), int(width/2 + x_width))
plot.ylim(int(height/2 - y_width), int(height/2 + y_width))

# Reconstructed image
plot.subplot(144)
image_reconstructed_lowpass = numpy.fft.ifft2(image_fourier_lowpass)
plot.imshow(abs(image_reconstructed_lowpass), cmap="gray")

# Create output folder structure if necessary
if not os.path.isdir(output_path):
    os.makedirs(output_path)

# Final actions
plot.savefig(os.path.join(output_path, "sine_superposition.png"), dpi=300)
plot.show()
