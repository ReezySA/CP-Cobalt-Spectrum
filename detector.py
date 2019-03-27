

import numpy as np
import numpy.random as ran

from path import setParam, getParam

import time     # implementing dead time


# Have the dectector geometry 


Al_thicc = 0.3      # mm, Al infront of the detector
det_r = 40          # mm, detector radius
det_h = 40          # mm, detector height
offset = 25         # mm, distance of detector from source, +z direction
sheild_thicc = 2    # mm, around the dectector
deadtime = 0.01     # s, optional? (non-trivial)
meandist = 1        # mm, mean distnce path travels in detector


def setgeometry(lst):   # optional
    print ("")
    
def enterDect():    # there is a chance of the path deflecting of the Al shielding
    print ("")
    return False
    
def inDetector():   # check if path is still in the detector
    print ("")
    return False

def energyLost():   # because of the deflection
    print ("")

def deflect():      # the path is deflected, set new path and energy lost
    print ("")
   
def distTrav(energy):     # distance the particle travels, take compton and photo effect into account, tempted to make another class for this
    print ("")
    return 0

def main():         # the path hits the dectector, deal with it here        # might not be needed
    print ("")
    
    if not enterDect(): # path is deflected by Al_thicc
        return -1
    
    indect = True   # short for in the detector
    while indect:
        dist_travelled = distTrav(energy)   # calculate this via the exp distribution using meandist (non-trivial)
        
        # calculate new particle position
        # check if it remains in the detector
            # if it remains, calculate energy lost
            # else see if it was deflected by the shielding around the detector
