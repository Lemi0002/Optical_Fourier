"""
Script to evaluate the correspondence between a frequency and its
position on the Fourier plane.
"""

import matplotlib.pyplot as plt
import numpy as np
from filter_module import Aperture, image_filter
from filter_output import OptOutput

output_path = "output"

frequency_scale = 10  # 2pi equals to frequency_scale * 2pi
width = 20*int(frequency_scale*2*np.pi)  # repetitions for better spectrum
height = width

aperture0 = Aperture(width, height, frequency_scale)
aperture0.add_slit(500, 50, 3)

aperture1 = Aperture(width, height, frequency_scale)
# aperture1.add_wave(1, direction="x", dc=100)
# aperture.add_wave(2, direction="x")
# aperture.add_wave(1, direction="y")
# aperture.add_wave(2, direction="y")
aperture1.add_grid(50, 100)

# output0 = OptOutput(aperture0, output_path)
# output0.show("SingleSlit, highpass", vmax=1e7, omega=20, highpass=True)
# output0.show("SingleSlit, lowpass", vmax=1e7, omega=20, highpass=False)

output1 = OptOutput(aperture1, output_path)
output1.show("Grid, highpass", vmax=8e6, omega=30, highpass=True)
output1.show("Grid, lowpass", vmax=8e6, omega=30, highpass=False)
pltshow()
