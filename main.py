

from source import decay

# User interface


def main():
    print ("")
    detections = 100    # for user input
    
    lst = []    # collected energy loss
    run = True
    
    while run:
        
        tmp = decay(detections) # tmp is a list to remain flexible
        
        for i in range(len(tmp)):   # put the energy loss in lst
            if tmp[i] < 0:
                run = False
                break
            lst += [tmp[i]]
            
    # make histograms here i guess
    print (lst)
    
main()
    
