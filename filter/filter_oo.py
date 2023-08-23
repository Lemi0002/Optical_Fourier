"""
Script to evaluate the correspondence between a frequency and its
position on the Fourier plane.
"""

import matplotlib.pyplot as plt
import numpy
import os
from filter_module import Aperture, image_filter

output_path = "output"

frequency_scale = 10  # 2pi equals to frequency_scale * 2pi
width = 20*int(frequency_scale*2*numpy.pi)  # repetitions for better spectrum
height = width

# Create sin wave with superposition of multiple waves
aperture = Aperture(width, height, frequency_scale)
aperture.add_wave(1, direction="x", dc=100)
# aperture.add_wave(2, direction="x")
# aperture.add_wave(1, direction="y")
# aperture.add_wave(2, direction="y")
aperture.add_grid(50, 100)

# Unmodified wave
# plt.rcParams.update({'font.size': 18})
plt.subplot(141)
plt.imshow(aperture.canvas, cmap='gray')

# FFT2
plt.subplot(142)
fourier = numpy.fft.fftshift(numpy.fft.fft2(aperture.canvas))
plt.imshow(abs(fourier), cmap='gray', vmax=6e7)
x_width = 100
y_width = 100
plt.xlim(int(width/2 - x_width/2), int(width/2 + x_width/2))
plt.ylim(int(height/2 - y_width/2), int(height/2 + y_width/2))

# FFT2 after filter
plt.subplot(143)
image_fourier_lowpass = image_filter(fourier, 30, highpass=False)
plt.imshow(abs(image_fourier_lowpass), cmap="gray", vmax=6e7)
plt.xlim(int(width/2 - x_width/2), int(width/2 + x_width/2))
plt.ylim(int(height/2 - y_width/2), int(height/2 + y_width/2))

# Reconstructed image
plt.subplot(144)
image_reconstructed_lowpass = numpy.fft.ifft2(image_fourier_lowpass)
plt.imshow(abs(image_reconstructed_lowpass), cmap="gray")

# Create output folder structure if necessary
if not os.path.isdir(output_path):
    os.makedirs(output_path)

# Final actions
plt.savefig(os.path.join(output_path, "sine_superposition.png"), dpi=300)
plt.show()
