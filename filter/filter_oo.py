"""
Script to evaluate the correspondence between a frequency and its position on the Fourier plane.
"""

import matplotlib.pyplot as plot
import numpy
import os
from filter_module import Aperture, image_filter

output_path = "output"

frequency_scale = 10 #2pi equals to frequency_scale * 2pi
width = 20*int(frequency_scale*2*numpy.pi) #allow multiple repetitions for better spectrum
height = width

# Create sin wave with superposition of multiple waves
aperture = Aperture(width, height, frequency_scale)
# aperture.add_wave(1, direction="x", dc=100)
# aperture.add_wave(2, direction="x")
# aperture.add_wave(1, direction="y")
# aperture.add_wave(2, direction="y")
aperture.add_grid(50, 100)

# Unmodified wave
plot.subplot(141)
plot.imshow(aperture.canvas, cmap='gray')

# FFT2
plot.subplot(142)
fourier = numpy.fft.fftshift(numpy.fft.fft2(aperture.canvas))
plot.imshow(abs(fourier), cmap='gray', vmax = 6e7)
x_width = 50
y_width = 50
plot.xlim(int(width/2 - x_width), int(width/2 + x_width))
plot.ylim(int(height/2 - y_width), int(height/2 + y_width))

# FFT2 after filter
plot.subplot(143)
image_fourier_lowpass = image_filter(fourier, 30, highpass=True)
plot.imshow(abs(image_fourier_lowpass), cmap="gray", vmax = 6e7)
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
