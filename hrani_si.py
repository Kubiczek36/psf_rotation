import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

fileName0 = 'imgs/0.tiff'
fileName1 = 'imgs/2.tiff'
fileName_1 = 'imgs/-2.tiff'
fileName2 = 'imgs/4.tiff'

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

def condition(difference, refPlus, refMinus): ### Podmínka posunu
    return (max(refPlus, refMinus)/2 < difference)

class PSF:
    def __init__(self, path, trashold = 30):
        self.path = path
        self.img = Image.open(self.path).convert('LA')
        imarray = np.array(self.img)[:,:,0]
        self.tArray = (imarray > trashold) * imarray
        self.PSFArray, self.cg = getBinaryPSF(self.tArray)
    def compare(self, second):
        plt.imshow(self.PSFArray - second.PSFArray)
        return np.sum(abs(self.PSFArray - second.PSFArray))
       

refer = PSF(fileName0)
referPlus = PSF(fileName1)
referMinus = PSF(fileName_1)

# stage.move(+1)
stepPlus = refer.compare(referPlus)
# stage.move(-2)
stepMinus = refer.compare(referMinus)
# stage.move(+1)

directionOfMovenment

def evaluation(ref, plus, minus, direction):
    stepDif = np.mean(plus, minus)
    # current = PSF(camera.getImg())
    current = PSF(fileName2)
    dif0 = ref.compare(current)
    while condition(dif0, plus, minus):
        movenment = dif0/stepDif
        print(movenment)
        # stage.move(direction*movenment)
        # current = PSF(camera.getImg())
        dif = ref.compare(current)
        if dif0<dif:
            direction*=(-1)
        dif0 = dif

def evaluation1(ref, step, direction):
    # current = PSF(camera.getImg())
    current = PSF(fileName2)
    dif0 = ref.compare(current)
    while condition(dif0, plus, minus):
        print(step)
        # stage.move(direction*step)
        # current = PSF(camera.getImg())
        dif = ref.compare(current)
        if dif0<dif:
            direction*=(-1)
        dif0 = dif


"""
zkusit dorovnat na přesno, ale když to bude dlouho pendlovat a bude to jakž takž v mezi tak to nechat
"""
    else:
        print('Asi OK. rozdíl obrázků dif = ', dif)

array1 = imgRead(fileName1)
#arr1 = plt.imshow(array1)
PSF1, cg1 = getBinaryPSF(array1)
#PSF1im = plt.imshow(PSF1)
print(fileName1)
print("souradnice1:", cg1)

array2 = imgRead(fileName0)
#plt.imshow(array2)
PSF2, cg2 = getBinaryPSF(array2)
#plt.imshow(PSF2)
print(fileName0)
print("--------------- \n souradnice2:", cg2)

plt.imshow(PSF1 - PSF2)
print(np.sum(abs(PSF1 - PSF2)))