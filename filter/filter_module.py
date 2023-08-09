import numpy


class Aperture:
    def __init__(self, width, height, frequency_scale) -> None:
        self.width = width
        self.height = height
        self.frequency_scale = frequency_scale
        self.canvas = numpy.zeros((self.height, self.width), dtype=numpy.uint8)

    def add_wave(self, frequency, direction="x", dc=0, amplitude=50):
        """
        Add a sin wave to the canvas
        """

        match direction:
            case "x":
                for x in range(self.width):
                    intensity = dc + amplitude * \
                        numpy.sin(frequency * x / self.frequency_scale)
                    self.canvas[:, x] = self.canvas[:, x] + intensity

            case "y":
                for y in range(self.height):
                    intensity = dc + amplitude * \
                        numpy.sin(frequency * y / self.frequency_scale)
                    self.canvas[y, :] = self.canvas[y, :] + intensity

            case _:
                raise ValueError(
                    f"Direction has to be x or y but is {direction}")

    def add_grid(self, a, b):
        """
        Add a grid to the canvas
        a is the material, b is the void
        """

        period = a + b

        for x in range(self.width):
            if (x % period) > b:
                self.canvas[:, x] = 255

        for y in range(self.height):
            if (y % period) > b:
                self.canvas[y, :] = 255


def image_filter(image, radius, highpass=True):
    image_modified = image.copy()
    size_x, size_y = image_modified.shape
    position_x = size_x / 2 - 0.5
    position_y = size_y / 2 - 0.5

    for x in range(size_x):
        for y in range(size_y):
            distance = numpy.sqrt((position_x - x)**2 + (position_y - y)**2)
            if ((highpass is False and radius < distance) or
                    (highpass is True and radius >= distance)):
                image_modified[x][y] = 0

    return image_modified
