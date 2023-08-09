import os
import numpy
import matplotlib.pyplot as plot
import PIL as pil


def convertPattern(name, output_path="patternRecon/output"):
    print(f"Generation of {name} started")
    input_path = f"patternRecon/input/{name}.png"
    # Try to read the picture and convert it to grey scale
    try:
        image_input = pil.Image.open(input_path)
        image = image_input.convert("L")
        # image_rgb = image_input.convert("RGB")
    except FileNotFoundError as exception:
        print(exception)
        exit()

    # Create output folder structure if necessary
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    # Apply two dimensional fft
    image_fourier = numpy.fft.fftshift(numpy.fft.fft2(image))

    # Generate output files
    plot.imshow(image, cmap='gray')
    plot.savefig(os.path.join(output_path, f"input_{name}.png"))

    plot.imshow(numpy.log(abs(image_fourier),
                where=abs(image_fourier) > 0), cmap='gray')
    plot.savefig(os.path.join(output_path, f"fourier_{name}.png"))

    # Apply inverse fft to all pictures
    image_reconstructed = numpy.fft.ifft2(image_fourier)
    plot.imshow(abs(image_reconstructed), cmap='gray')
    plot.savefig(os.path.join(output_path, f"reconstructed_{name}.png"))


convertPattern("A")
convertPattern("A_moved")
convertPattern("B")
convertPattern("B_spiral")
convertPattern("B_dist")
