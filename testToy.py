import matplotlib.pyplot as plt
import numpy as np
from creature import Toy

def main():
    size = (30,30)
    yard = np.zeros(size)
    toy1 = Toy("Ball1","green",(20,5),True) 
    toy2 = Toy("Ball2","green",(10,5),False)
    fig,ax = plt.figure(figsize=(15,15))

    plt.imshow(yard, cmap = "Blues_r")
    ax = plt.axes()
    toy1.plot_me(ax,size) #3.2.1.1 - plots toys on the grid/plot
    toy2.plot_me(ax,size)
    plt.show
if __name__ == "__main__":
    main()
