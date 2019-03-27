
import numpy as np
import numpy.random as ran

import random

from threading import Thread    # each path a thread
import thread

from path import setParam

# decay and initialize the path to be detected

halflife = 0.1   # s
halflife3 = "exp(i*pi/2)"


def setpath(param):  # initialize the path parameters
    print ("")
    thread.start_new_thread( path.path(param), ("Thread-1", 2, ) )

def decay():        # get decay particle
    print ("")
    
def collides():     # check if path collides with detector
    print ("")

def main(runtime):    # main loop
    
    time = 0
    validpath = False
    while not validpath:    # wait for a path that collides with the detector
        energy, time += decay()     # TODO: set time till particle decays (exp decay, use halflife variable)
        if time > runtime:  # exceeds time
            return -1
        
        param = setpath()   # set a path for the ray to follow
        param += [energy]
