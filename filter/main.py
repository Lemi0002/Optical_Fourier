"""
Script to evaluate the correspondence between a frequency and its position on the Fourier plane.
"""

import matplotlib.pyplot as plot
import numpy


def create_sin_wave(width, height, frequency):
    """
    Create an image containing a sine wave with a given frequency
    """
    canvas = numpy.zeros((height, width), dtype=numpy.uint8)

    for x in range(width):
        intensity = int(127 + 127 * numpy.sin(2 * numpy.pi * frequency * x / 10))
        canvas[:, x] = intensity

    return canvas


if __name__ == "__main__":
    width = 1200
    height = 600

    frequencies = [0.01, 0.02, 0.1, 10]

    waves = [create_sin_wave(width, height, freq) for freq in frequencies]
 
    plot.figure(1)

    baseNumber = 100*2 + 10*len(waves) + 1

    for index, wave in enumerate(waves):
        plot.subplot(baseNumber + index)
        plot.imshow(wave, cmap='gray', vmin=0, vmax=255)

        plot.subplot(baseNumber + index + len(waves))
        fourier = numpy.fft.fftshift(numpy.fft.fft2(wave))
        plot.imshow(numpy.log(abs(fourier), where=abs(fourier) > 0), cmap='gray')

    plot.show()
