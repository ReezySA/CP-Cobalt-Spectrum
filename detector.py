from __future__ import division
import numpy as np
import numpy.random as ran

import matplotlib.pyplot as plt

# from path import setParam, getParam

crossSectionsFile = np.genfromtxt('./crossSections.txt', skip_header=2)
crossSectionEnergies = []
crossSectionCS = []
crossSectionPE = []
for i in crossSectionsFile:
    crossSectionEnergies.append(i[0])
    crossSectionCS.append(i[1])
    crossSectionPE.append(i[2])


Alrho = 2.7         # density of Al (g/cm3)
AlmacCS = 5.482e-02          # mass attenuation coeff for Al at 1.25 MeV for Compton scattering
AlmacPE =  1.688e-05         # mass attenuation coeff for Al at 1.25 Mev for photoelectric absorption
NaIrho = 3.67
Al_thicc = 0.3      # mm, Al infront of the detector
det_r = 20          # mm, detector radius
det_h = 40          # mm, detector height
offset = 25         # mm, distance of detector from source, +z direction



def comptonScatter(E):
    m_e = 0.5109989461   #MeV/c^2
    rc = 0.38616 #pm -> reduced Compton wavelength of an electron
    # c = 3*(10**(8))
    # theta = np.arange(0,np.pi,0.01)   #range of possible theta angles (I beleive if we decrease 0.1 we will get a better resoultion)
    randomTheta=1
    e=(m_e/(m_e+E)*(1-np.cos(randomTheta)))
    # Z=64

    #probability for different scattering angles in Compton Effect is given by Klein-Nishina Forumula:

    # KN = np.pi* (rc**2)*(m_e/E)*Z*(1/e + e)*(1-(e*(np.sin(randomTheta)**2))/(1+e**2))
    e_0 = m_e/(m_e+2*E) #backward scatter(theta = pi)

    #combined composition (Monte Carlo Algorithm)

    alpha1 = np.log(1/e_0)
    alpha2 = (1-(e_0)**2)/2
    # def f1(e):
    #     f11 = 1/(alpha1*e)
    #     return f11
    # def f2(e):
    #     f22 = e/alpha2
    #     return f22
    def g(e,x):
        gg = 1-((e*x)/(1+e**2)) #Monte Carlo Rejection Function
        return gg

    #Monte Carlo Algorithm

    r = np.random.uniform(0,1,3) #generate 3 random numbers between 0 and 1
    t = m_e*(1-e)/(E*e)
    # f=0
    while(g(e,t*(2-t)) >= r[2]):
        r = np.random.uniform(0,1,3) #generate 3 random numbers between 0 and 1
        #selection process for f
        if (r[0] < alpha1/(alpha1+alpha2)):

            # f= f1(np.exp(-alpha1*r[1]))
            e =  np.exp(-alpha1*r[1])
        else:
            # f=f2((e_0)**2 + (1-(e_0)**2)*r[1])
            e = np.sqrt((e_0)**2 + (1-(e_0)**2)*r[1])
        t = m_e*(1-e)/(E*e)
    randomTheta = np.arccos(1-(m_e/(e*E))*(1-e))  #theta with accepted e
    EPrime = e*E
    randomPhi = np.random.uniform(0,2*np.pi)  #sandom phi between 0 and 2pi
    r = (EPrime,randomTheta,randomPhi)
    return r


def attenuate(sigma, density):      # calculate a distance x travelled by a photon through some medium before an interaction
    num = ran.rand()
    x = np.log(num)/(-density*sigma)*10     ## x in mm
    return x


def maxDistance(r, r0, x):     # calculates the maximum allowed travel distance before exiting a volume. Should be compared to x from "attenuate" to determine if an interaction occrus
    rho1 = r0[0]
    phi1 = r0[1]
    z1 = r0[2]
    oldtheta = np.arctan(rho1/z1)
    # print 'old theta', oldtheta
    rho2 = x*np.sin(r[1]+oldtheta)
    phi2 = r[2]
    z2 = x*np.cos(r[1]+oldtheta)
    rho3 = rho1 + rho2
    phi3 = phi1 + phi2
    z3 = z1 + z2
    # print 'v1 =', rho1, phi1, z1
    # print 'v2 = ', rho2, phi2, z2
    if (rho3 < det_r) & (z3 < det_h):
        return [True, (rho3,phi3,z3)]
    else:
        return [False, (rho3,phi3,z3)]


def enterDect(r):    # there is a chance of the path deflecting off the Al shielding (r is vector in spherical)
    rho = np.sqrt((25 * np.tan(r[1] * np.pi / 180)) ** 2 + (25 * np.tan(r[2] * np.pi / 180)) ** 2)
    phi = r[2]
    z = 25
    r0 = (rho, phi, z)
    x = attenuate(AlmacCS+AlmacPE, Alrho)
    maxx = maxDistance(r, r0, x)
    if maxx[0] == True:
        # print 'photon goes home'
        return False
    else:
        return True


def energyRes(E):
    if E == 0:
        return 0
    fwhm = 0.03*E
    sigma = fwhm/2.355
    Espread = ran.normal(E, sigma)
    return Espread


def inDetector(r, r0):   # photon is now in the scintillator
    sigmaCS = (np.interp(r[0], crossSectionEnergies, crossSectionCS))
    sigmaPE = np.interp(r[0], crossSectionEnergies, crossSectionPE)
    x = attenuate(sigmaCS + sigmaPE, NaIrho)
    # print 'x =', x
    maxx = maxDistance(r, r0, x)
    # print maxx[0]
    if maxx[0] == True:            # an interaction happens
        interval = (sigmaCS/sigmaPE) + 1
        num = ran.random()*interval
        if num < 1.:            # PE happens
            # print 'PE'
            EList.append(energyRes(r[0]))
            return
        else:                # scattering happens
            # print 'scattering'
            comptr = comptonScatter(r[0])
            EList.append(energyRes(r[0] - comptr[0]))
            r0new = maxx[1]
            # print 'new pos = ',r0new
            inDetector(comptr, r0new)
    elif len(EList) > 0:        # x exceeds maximum x so return energy list if it has values
        # print 'escaped'
        return
    else:           # no interactions happened, photon goes away
        return False


r = (1.17,0.1,0.1)
r2 = (1.33,0.1,0.1)
r0 = (0,0,0.1)

# inDetector(r, r0)
# print EList
# print sum(EList)

fullList = []
for i in range(100000):
    EList = []
    num = ran.rand()
    if num > 0.5:
        inDetector(r, r0)
    else:
        inDetector(r2, r0)
    deposit = np.sum(EList)
    if deposit > 0:
        fullList.append(deposit)


# print fullList

plt.hist(fullList, bins=1000, histtype='step')
plt.show()












def setgeometry(lst):  # optional
    print ("")


def energyLost():  # because of the deflection
    print ("")


def deflect():  # the path is deflected, set new path and energy lost
    print ("")


def distTrav(
        energy):  # distance the particle travels, take compton and photo effect into account, tempted to make another class for this
    print ("")
    return 0


def main():  # the path hits the dectector, deal with it here        # might not be needed
    print ("")

    if not enterDect():  # path is deflected by Al_thicc
        return -1

    indect = True  # short for in the detector
    while indect:
        dist_travelled = distTrav(energy)  # calculate this via the exp distribution using meandist (non-trivial)

        # calculate new particle position
        # check if it remains in the detector
        # if it remains, calculate energy lost
        # else see if it was deflected by the shielding around the detector

