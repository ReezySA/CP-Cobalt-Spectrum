# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:01:13 2019

@author: rivan
"""

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

#creates random points on a sphere
def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

#creates random energy values
def energy(npoints):
    
    vals = np.random.rand(npoints)
    for i in range(npoints):

        if (vals[i]<0.5):
            vals[i] = 1173
                
        else:
            vals[i] = 1332
        #print(vals[i])
    return vals
    
#plots the sphere to check that it is isotropic  
def plot_sphere(n_emissions ):

    phi = np.linspace(0, np.pi, 20)
    theta = np.linspace(0, 2 * np.pi, 40)
    x = np.outer(np.sin(theta), np.cos(phi))
    y = np.outer(np.sin(theta), np.sin(phi))
    z = np.outer(np.cos(theta), np.ones_like(phi))
    
    
    xi, yi, zi = sample_spherical(n_emissions)
    Ei = energy(n_emissions)
    
    fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'equal'})
    #ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1)
    ax.scatter(xi, yi, zi, s=1, c='r', zorder=10)
    plt.show()
    #print (x)
    
if (__name__ == '__main__'):
    print ("source")
    plot_sphere(10000)
