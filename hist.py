import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import numpy.random as ran

from scipy.stats import cosine as cs 
from scipy.linalg import lu
from scipy.optimize import curve_fit # uses L-M algorithm through leastsq
from scipy.optimize import minimize
from scipy import integrate
from scipy.stats import poisson

import random
import math
import time


# making useful histgrams


def mk_hist(param):
    print ("")

