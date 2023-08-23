# import filter_module
import matplotlib.pyplot as plt
import numpy as np
from filter_module import image_filter
import os


class OptOutput:
    def __init__(self, aperture, output_path):
        self.aperture = aperture
        self.width = self.aperture.width
        self.height = self.aperture.height
        self.output_path = output_path

    def show(self,
             name,
             x_width=100,
             y_width=100,
             vmax=6e7,
             omega=30,
             highpass=True):

        pltfigure(name)
        pltrcParams.update({'font.size': 16})

        middle_x = self.width/2
        middle_y = self.height/2

        # Grayscale image of aperture
        pltsubplot(141)
        pltimshow(self.aperture.canvas, cmap='gray')

        # FFT2, with configurable vmax, height and width
        pltsubplot(142)
        fourier = np.fft.fftshift(np.fft.fft2(self.aperture.canvas))
        pltimshow(abs(fourier), cmap='gray', vmax=vmax)
        pltxlim(int(middle_x - x_width/2), int(middle_x + x_width/2))
        pltylim(int(middle_y - y_width/2), int(middle_y + y_width/2))

        # FFT2 after filter
        pltsubplot(143)
        image_fourier_lowpass = image_filter(fourier, omega, highpass=highpass)
        pltimshow(abs(image_fourier_lowpass), cmap="gray", vmax=vmax)
        pltxlim(int(middle_x - x_width/2), int(middle_x + x_width/2))
        pltylim(int(middle_y - y_width/2), int(middle_y + y_width/2))

        # Reconstructed image
        pltsubplot(144)
        image_reconstructed_lowpass = np.fft.ifft2(image_fourier_lowpass)
        pltimshow(abs(image_reconstructed_lowpass), cmap="gray")
  
        # Create output folder structure if necessary
        if not os.path.isdir(self.output_path):
            os.makedirs(self.output_path)

        # Final actions
        pltsavefig(os.path.join(self.output_path.strip(), name), dpi=300)
