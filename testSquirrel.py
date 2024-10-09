import matplotlib.pyplot as plt
import numpy
from creature import Squirrel

def main():
    size = (30,30)
    yard = np.zeros(size)
    rrocks = Squirrel("Ball1","green",(20,5))
    fig,ax = plt.figure(figsize=(15,15))
    for timestep in range(5):
        rrocks.step_change() #1.1.1 Method to move the squirrel. 
        plt.imshow(yard, cmap = "Blues_r")
        ax = plt.axes()
        rocky.plot_me(ax) #1.1.2 Method to plot squirrels as circles on the grid.
        plt.pause(1)
        plt.clf()
if __name__ == "__main__":
    main()
~              
