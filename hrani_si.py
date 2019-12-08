import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

fileName1 = 'imgs/6.tiff'
fileName2 = 'imgs/-2.tiff'

def imgRead(name, trashold = 30):
    im = Image.open(name).convert('LA')
    imarray = np.array(im)[:,:,0]
    trasholdImArray = (imarray > trashold) * imarray
    return trasholdImArray

def getPSF(ImArray, size = 50):
    cg = ndimage.measurements.center_of_mass(ImArray) ## najde těžiště
    cg = np.array([cg[0], cg[1]]).astype(int)
#    ImArray[cg[0], cg[1]] = 255 ### dávat?
    PSF = ImArray[(cg[0]-(size//2)):(cg[0]+(size//2)), (cg[1]-(size//2)):(cg[1]+(size//2))]
    plt.imshow(PSF)
    return PSF

def getBinaryPSF(ImArray, size = 50, trashold = 30):
    cg = ndimage.measurements.center_of_mass(ImArray) ## najde těžiště
    cg = np.array([cg[0], cg[1]]).astype(int)
#    ImArray[cg[0], cg[1]] = 255 ### dávat?
    PSF = ImArray[(cg[0]-(size//2)):(cg[0]+(size//2)), (cg[1]-(size//2)):(cg[1]+(size//2))]
    PSF = (PSF > trashold) * 1
    #plt.imshow(PSF)
    return PSF, cg


array1 = imgRead(fileName1)
#arr1 = plt.imshow(array1)
PSF1, cg1 = getBinaryPSF(array1)
#PSF1im = plt.imshow(PSF1)
print(fileName1)
print("souradnice1:", cg1)

array2 = imgRead(fileName2)
#plt.imshow(array2)
PSF2, cg2 = getBinaryPSF(array2)
#plt.imshow(PSF2)
print(fileName2)
print("--------------- \n souradnice2:", cg2)

plt.imshow(PSF1 - PSF2)
print(np.sum(abs(PSF1 - PSF2)))