import numpy


class SinWave:
    def __init__(self, width, height, frequency_scale) -> None:
        self.width = width
        self.height = height
        self.frequency_scale = frequency_scale
        self.canvas = numpy.zeros((self.height, self.width), dtype=numpy.uint8)

    def add(self, frequency, direction="x", dc=0, amplitude=50):
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

            case default:
                raise ValueError(
                    f"Direction has to be x or y but is {direction}")


def image_filter(image, radius, highpass=True):
    image_modified = image.copy()
    size_x, size_y = image_modified.shape
    position_x = size_x / 2 - 0.5
    position_y = size_y / 2 - 0.5

    for x in range(size_x):
        for y in range(size_y):
            distance = numpy.sqrt((position_x - x)**2 + (position_y - y)**2)
            if (highpass == False and radius < distance) or (highpass == True and radius >= distance):
                image_modified[x][y] = 0

    return image_modified
