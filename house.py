"""
snoo.py - base simulation for the FOP assingment, Sem1 2024
Written by: Joel Jose
Student ID: 21745625

Usage:
Versions:
    - initial version supplied 15/4/24
"""
from creature import Puppy, Cat
import numpy as np
import matplotlib.pyplot as plt
import random
import time
def plot_yard(ax, p):
    ax.imshow(p, cmap = "nipy_spectral")
#5.1.2 - This method is used to plot the yard array with all it's intialised values.


def build_yard(dims):
    #5.1.1 - This Method is used to intialise the values that correspond to the colours needed for the yard grid, to resemble a bird's eye view of a house with grass, house, and fences and gates. 
    
    plan = np.zeros(dims)
    plan[0:110,:] = 5
    plan[100:110,:] = 10
    plan[20:90,20:70] =7
    plan[80,0:20] = 0
    plan[80,70:90] = 0
    plan[:,0] = 0
    plan[:,89] = 0
    plan[0,:] = 0
    return plan
   

def main():
    size = (120,90)
    yard = build_yard(size)
    smells = np.zeros(size)
    creatures = []
    snoopy = Puppy("Snoopy", "white/black", (5,15))
    creatures.append(snoopy)
    ASAP = Puppy("ASAP", "white/black", (19,15))
    creatures.append(ASAP)
    for i in range(7):
        a = random.randint(10,70)
        b = random.randint(10,70)
        rocky = Puppy("Rocky", "red/brown", (a,b))
        creatures.append(rocky)
    cat1 = Cat("Oogie", "grey/grey", (17,7))
    creatures.append(cat1)
    cat2 = Cat("Kendrick", "orange/white", (25,50))
    creatures.append(cat2)
    cat3 = Cat("King", "green/blue", (30,15))
    creatures.append(cat3)
    cat4 = Cat("Drake", "purple/black", (60,10))
    creatures.append(cat4)
    


    

    for timestep in range(10):
        fig, ax = plt.subplots(figsize=(30,15))
        for c in creatures:
            c.step_change()
            c.plot_me(ax[0], size)


        
        ax[0].set_title(f"Timestep: {timestep+1}")
        ax[1].set_title(f"Timestep: {timestep+1}")
        plot_yard(ax[0], yard)


        
        fig.savefig("task1.png")
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
