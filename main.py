

from source import plot_sphere, sample_spherical, energy
from path import run
from detector import detectorPlot, plotFull, setThings, just

# User interface


def main():
    
    print ("Run the code for the source")
    det = 1000    # for user input
    det = int (input ("How many points do you want the source to generate? \n"))
    
    plot_sphere(det)
    
    
main()
    
