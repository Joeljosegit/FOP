"""
snoo.py - base simulation for the FOP assingment, Sem1 2024
Written by: Joel Jose
Student ID: 21745625

Usage:
Versions:
    - initial version supplied 15/4/24
"""
from creature import Puppy, Cat, Squirrel, Toy, Food, Person, Friend, Stranger
import numpy as np
import matplotlib.pyplot as plt
import random
import time
def plot_yard(ax, p):
    ax.imshow(p, cmap = "nipy_spectral")

def plot_smells(ax, smells):
    ax.imshow(smells, cmap = "hot")
    


def build_yard(dims):
    
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
   
def update_smells(smells, creatures, toys, foods,humans):
    np.where(smells>0, smells-1, 0)
    for c in creatures:
        pos = c.get_pos()
        smells[min(max(pos[0],0),99), min(max(pos[1],0),78)] += 10
    for t in toys:
        pos = t.get_pos()
        smells[pos[0],pos[1]] += 10
    for f in foods:
        pos = f.get_pos()
        smells[pos[0],pos[1]] += 10
    for h in humans:
        pos = h.get_pos()
        smells[min(max(pos[0],0),99), min(max(pos[1],0),78)] += 10








def main():
    size = (120,90)
    yard = build_yard(size)
    smells = np.zeros(size)
    creatures = []
    toys = []
    foods = []
    humans = []
    hungry = []
    human1 = Person("Rick","yellow/blue",(30,20))
    humans.append(human1)
    
    


    

    for timestep in range(10):
        for h in humans:
            h.step_change() #2.1.1 - method to move humans
            h.plot_me(ax[0],size) #2.1.2 - method to plot humans


        
                


            

                    

        
        
        ax[0].set_title(f"Timestep: {timestep+1}")
        plot_yard(ax[0], yard)


        
        plot_smells(ax[1],smells)
        fig.savefig("task1.png")
        plt.pause(4)
        plt.clf()

if __name__ == "__main__":
    main()
