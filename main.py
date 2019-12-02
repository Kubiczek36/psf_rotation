import numpy as np
# import matplotlib.pyplot as plt

from PIL import Image
im = Image.open('imgs/2.tiff')
im.show()

imarray = np.array(im)
grayscale = np.sum(imarray-255, 2)

size = np.shape(grayscale)

massCentre = np.array([0, 0])

for i in range(size[0]):
    for j in range(size[1]):
        massCentre = massCentre + np.array([grayscale[i, j] * i, grayscale[i, j] * j])

massCentre = massCentre/np.sum(imarray)

print(massCentre)
"""
self.red = (self.red > self.trashold) * self.red
použít zápis viz výše
"""
