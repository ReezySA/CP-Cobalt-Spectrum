
from detector import inDetector, runDet
import numpy as np


# travelling path, glorified book keeping class


x_start, y_start, z_start = 0,0,0
vecx, vecy, vecz = 0,0,0
energy = 0

# keeping track of when and how the interaction occurs
eLost = []     
eLoc = []
eTime = []

def setParam(param):
    print ("")
    
    
def getParam():
    print ("")

def energyLost():
    print ("")

def path(param):
    print ("start thread")

def run(en, xi, yi, zi):
    
    R = np.sqrt(xi**2 + yi**2)
    r = np.sqrt(xi**2 + yi**2 + zi**2)
    theta = np.arccos(zi/r)
    phi = np.arcsin(yi/R)
    
    height = R
    if height >= 20 or zi <= 0: # outside the detector
        return 0
    r0 = [en, theta, phi]
    r1 = [height, phi, 0.1]
    print ("get here")
    runDet(r0, r1)
