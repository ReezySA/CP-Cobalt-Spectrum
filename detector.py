

import numpy as np
import numpy.random as ran

import matplotlib.pyplot as plt

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
det_r = 40          # mm, detector radius
det_h = 40          # mm, detector height
offset = 25         # mm, distance of detector from source, +z direction
sheild_thicc = 2    # mm, around the dectector
deadtime = 0.01     # s, optional? (non-trivial)
meandist = 1        # mm, mean distnce path travels in detector


##################################################################
#general functions which can be called easily

def comptonScatter(E):

    m_e = 0.5109989461   #MeV/c^2
    c = 299792458 #m/s
    alpha = 1/137 #fine structure constant
    rc = 0.38616 #pm -> reduced Compton wavelength of an electron
    
    theta = np.arange(0,180,0.1)   #range of possible theta angles (I beleive if we decrease 0.1 we will get a better resoultion)

    P = 1/(1+(E/(m_e*c**2))*(1-np.cos(theta)))

    #probability for different scattering angles in Compton Effect is given by Klein-Nishina Forumula

    KN = (alpha**2)*(rc**2)*(P**2)* (P+ P**(-1) - (np.sin(theta)**2) )/2

    #choose a random scattering angle according to the Klein-Nishina distribution

    #total cross section(barns) - by integrating under Klein-Nishma Dist.
    
    
    print( np.random.choice(theta, 1,p=KN/sum(KN))) 

    plt.scatter(np.arange(0,180,0.1), np.random.choice(theta, 1800,p=KN/sum(KN)))

    plt.show()

comptonScatter(1.3)




##################################################################



def attentuate(mac, rho):      # calculate a distance x travelled by a photon through some medium before an interaction
    num = ran.rand()
    x = np.log(num)/(-rho*mac)
    return x

def setgeometry(lst):   # optional
    print ("")
    
def enterDect():    # there is a chance of the path deflecting off the Al shielding
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


