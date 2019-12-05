import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

im = Image.open('imgs/2.tiff').convert('LA')

trashold = 30

imarray = np.array(im)[:,:,0]

trasholdImArray = (imarray > trashold) * imarray

cg = ndimage.measurements.center_of_mass(trasholdImArray) ## najde těžiště

cg = np.array([cg[0], cg[1]]).astype(int)

#psf = grayscale[]

"""
size = np.shape(grayscale)


crd = np.zeros([size[0], size[1], 2]) # cordinates

massCentre = np.array([0, 0])

vaha = np.array([0,0])

for i in range(size[0]):
    for j in range(size[1]):
        #crd [i,j] += [i, j]
        vaha += [i,j]
        if grayscale[i, j] > trashold:
            massCentre = massCentre + np.array([grayscale[i, j] * i, grayscale[i, j] * j])




massCentre = np.round(massCentre/size)

grayscale[floor(x,y)] = 255

im.show()

self.red = (self.red > self.trashold) * self.red
použít zápis viz výše
"""
