
from __future__ import division
import numpy as np
import numpy.random as ran

import matplotlib.pyplot as plt

# from path import setParam, getParam

crossSectionsFile = np.genfromtxt('./crossSections.txt',skip_header=2)

crossSections = {}
for i in crossSectionsFile:
    crossSections[i[0]] = {'cs': i[1], 'pe': i[2]}

xfit = []
yfit = []
for i in crossSectionsFile:
    xfit.append(i[0])
    yfit.append(i[1])

print xfit
print yfit
# csFunction = np.polyfit(xfit, yfit, 100)

# plt.plot(csFunction)
plt.scatter(xfit, yfit)
plt.show()

Alrho = 2.7         # density of Al (g/cm3)
AlmacCS = 5.482e-02          # mass attenuation coeff for Al at 1.25 MeV for Compton scattering
AlmacPE =  1.688e-05         # mass attenuation coeff for Al at 1.25 Mev for photoelectric absorption
NaIrho = 3.67
NaImacCS = 4.846e-02
NaImacPE = 2.240e-03
Al_thicc = 0.3      # mm, Al infront of the detector
det_r = 20          # mm, detector radius
det_h = 40          # mm, detector height
offset = 25         # mm, distance of detector from source, +z direction
sheild_thicc = 2    # mm, around the dectector
deadtime = 0.01     # s, optional? (non-trivial)
meandist = 1        # mm, mean distnce path travels in detector

EList = []

def comptonScatter(E):
    m_e = 0.5109989461   #MeV/c^2
    alpha = 1/137 #fine structure constant
    rc = 0.38616 #pm -> reduced Compton wavelength of an electron
    theta = np.arange(0,np.pi,0.01)   #range of possible theta angles (I beleive if we decrease 0.1 we will get a better resoultion)

    #probability for different scattering angles in Compton Effect is given by Klein-Nishina Forumula:

    P = 1/(1+(E/(m_e))*(1-np.cos(theta)))
    KN = (alpha**2)*(rc**2)*(P**2) * (P+ P**(-1) - (np.sin(theta)**2) )/2
    #return energy according to Compton Scatter Equation and randomly generated theta

    totalSigma = sum(KN)  #total cross section(barns) - by integrating under Klein-Nishma Dist.
    randomTheta = np.random.choice(theta, 1,p=KN/totalSigma)
    randomPhi = np.random.uniform(0,2*np.pi)
    
    #plot

    # plt.scatter(np.arange(0,np.pi,0.01), np.random.choice(theta, 315,p=KN/sum(KN)))
    #plt.plot(theta,KN)
    # plt.show()
    Eprime = E/(1+(E/(m_e))*(1-np.cos(randomTheta))) #energy of scattered photon
    # EList.append(Eprime[0])
    r = (Eprime[0],randomPhi,randomTheta)
    return r
    # return [Eprime,randomPhi,randomTheta] #return energy according to Compton Scatter Equation and randomly generated theta
    # inDetector(EList, r, r0)


def attentuate(mac, rho):      # calculate a distance x travelled by a photon through some medium before an interaction
    num = ran.rand()
    x = np.log(num)/(-rho*mac)
    return x


def maxDistance(r, r0):     # calculates the maximum allowed travel distance before exiting a volume. Should be compared to x from "attenuate" to determine if an interaction occrus
    return max(0, 40 - r0[2])


def enterDect(r):    # there is a chance of the path deflecting off the Al shielding (r is vector in spherical)
    rho = np.sqrt((25 * np.tan(r[1] * np.pi / 180)) ** 2 + (25 * np.tan(r[2] * np.pi / 180)) ** 2)
    phi = r[2]
    z = 25
    r0 = (rho, phi, z)
    maxx = maxDistance(r, r0)
    x = attentuate(AlmacCS+AlmacPE, Alrho)
    if x < maxx:
        print('photon goes home')
        return False
    return True


def inDetector(r, r0):   # photon is now in the scintillator
    maxx = maxDistance(r, r0)
    x = attentuate(NaImacCS + NaImacPE, NaIrho)
    if x < maxx:            # an interaction happens
        interval = (NaImacCS/NaImacPE) + 1
        num = ran.random()*interval
        if num < 1.:            # PE happens
            # print 'PE'
            EList.append(r[0])
            # return (EList, 0, 0)
            return
        else:                # sca
            # scattering happens
            # print 'scattering'
            comptr = comptonScatter(r[0])
            EList.append(r[0] - comptr[0])
            r01 = (r0[0], r0[1], r0[2] + x)
            # return (EList, comptr, r01)
            # return
            inDetector(comptr, r01)
    elif len(EList) > 0:        # x exceeds maximum x so return energy list if it has values
        # print 'compted'
        # return (EList, 0, 0)
        return
    else:           # no interactions happened, photon goes away
        return False




# def maxDistance(r, z, l):     # calculates the maximum allowed travel distance before exiting a volume. Should be compared to x from "attenuate" to determine if an interaction occrus
#     d = z
#     rho = np.sqrt((d*np.tan(r[1]* np.pi / 180))**2 + (d*np.tan(r[2]* np.pi / 180))**2)  # rho position of photon in cylindrical
#     magr = np.sqrt(d**2 + rho**2)   # distance travelled from origin
#     maxr = (magr/rho) * (det_r-rho)     # maximum allowed subsequent travel distance limited by radius of AL
#     maxl = (magr/d) * l     # maximum allowed subsequent travel distance limited by length of Al
#     maxx = min(maxr, maxl)
#     return maxx



def setgeometry(lst):  # optional
    print ("")

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


def do(r, r0):
    # l = []
    # E = inDetector(l, r, r0)
    inDetector(r, r0)
    # print EList
    # return E

r = (1.17,1,1)
r2 = (1.33,1,1)
r0 = (0,0,0)
# do(r, r0)

# fullList = []
# for i in range(10000):
#     num = ran.rand()
#     if num > 0.5:
#         do(r, r0)
#     else:
#         do(r2, r0)
#     for j in EList:
#         fullList.append(j)
#     EList = []

# print fullList

# plt.hist(fullList, bins=100)
# plt.show()