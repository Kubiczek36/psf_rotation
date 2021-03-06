import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

fileName = 'imgs/2.tiff'

def imgRead(name, trashold):
    im = Image.open(name).convert('LA')
    imarray = np.array(im)[:,:,0]
    trasholdImArray = (imarray > trashold) * imarray
    return trasholdImArray

def getPSF(ImArray, size):
    cg = ndimage.measurements.center_of_mass(ImArray) ## najde těžiště
    cg = np.array([cg[0], cg[1]]).astype(int)
    ImArray[cg[0], cg[1]] = 255 ### dávat?
    PSF = ImArray[(cg[0]-(size//2)):(cg[0]+(size//2)), (cg[1]-(size//2)):(cg[1]+(size//2))]
    plt.imshow(PSF)
    return PSF, cg

def getBinaryPSF(ImArray, size, trashold):
    cg = ndimage.measurements.center_of_mass(ImArray) ## najde těžiště
    cg = np.array([cg[0], cg[1]]).astype(int)
    ImArray[cg[0], cg[1]] = 255 ### dávat?
    PSF = ImArray[(cg[0]-(size//2)):(cg[0]+(size//2)), (cg[1]-(size//2)):(cg[1]+(size//2))]
    PSF = (PSF > trashold) * 1
    plt.imshow(PSF)
    return PSF, cg


trshld = 30 #trešhold vole!
PSFsize = 40//2