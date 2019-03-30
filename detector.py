

import numpy as np
import numpy.random as ran

# from path import setParam, getParam

import time     # implementing dead time


# Have the dectector geometry 

Alrho = 2.7         # density of Al (g/cm3)
AlmacCS = 5.482e-02          # mass attenuation coeff for Al at 1.25 MeV for Compton scattering
AlmacPE =  1.688e-05         # mass attenuation coeff for Al at 1.25 Mev for photoelectric absorption
# NaIrho =
# NaImacCS =
# NaImacPE =
Al_thicc = 0.3      # mm, Al infront of the detector
det_r = 20          # mm, detector radius
det_h = 40          # mm, detector height
offset = 25         # mm, distance of detector from source, +z direction
sheild_thicc = 2    # mm, around the dectector
deadtime = 0.01     # s, optional? (non-trivial)
meandist = 1        # mm, mean distnce path travels in detector

def attentuate(mac, rho):      # calculate a distance x travelled by a photon through some medium before an interaction
    num = ran.rand()
    x = np.log(num)/(-rho*mac)
    return x

def maxDistance(z, l):     # calculates the maximum allowed travel distance before exiting a volume. Should be compared to x from "attenuate" to determine if an interaction occrus
    d = z
    rho = np.sqrt((d*np.tan(r[1]* np.pi / 180))**2 + (d*np.tan(r[2]* np.pi / 180))**2)  # rho position of photon in cylindrical
    magr = np.sqrt(d**2 + rho**2)   # distance travelled from origin
    maxr = (magr/rho) * (det_r-rho)     # maximum allowed subsequent travel distance limited by radius of AL
    maxl = (magr/d) * l     # maximum allowed subsequent travel distance limited by length of Al
    maxx = min(maxr, maxl)
    return maxx

def setgeometry(lst):   # optional
    print ("")
    
def enterDect(r):    # there is a chance of the path deflecting off the Al shielding (r is vector in spherical)
    z = 25
    maxx = maxDistance(z, Al_thicc)
    print maxx
    x = attentuate(AlmacCS+AlmacPE, Alrho)
    if x < maxx:
        print 'photon goes home'
        return False
    return True

def inDetector():   # photon is now in the scintillator

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

r = (1.17,1,1)
enterDect(r)
