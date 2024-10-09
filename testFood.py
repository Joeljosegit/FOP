"""
snoo.py - base simulation for the FOP assingment, Sem1 2024
Written by: Joel Jose
Student ID: 21745625

Usage:
Versions:
    - initial version supplied 15/4/24
"""
from creature import Puppy, Cat, Squirrel, Toy, Food
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
   
def update_smells(smells, creatures, toys, foods):
    np.where(smells>0, smells-1, 0)
    for c in creatures:
        pos = c.get_pos()
        smells[pos[0], pos[1]] += 10
    for t in toys:
        pos = t.get_pos()
        smells[pos[0],pos[1]] += 10
    for f in foods:
        pos = f.get_pos()
        smells[pos[0],pos[1]] += 10






def main():
    size = (120,90)
    yard = build_yard(size)
    smells = np.zeros(size)
    creatures = []
    toys = []
    foods = []
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
    s1 = Squirrel("Scrat","red/orange",(100,30))
    creatures.append(s1)
    toy1 = Toy("Ball1","green",(90,40),True)
    toy2 = Toy("Ball2","red",(20,20),False)
    toys.append(toy1)
    toys.append(toy2)
    food1 = Food("Meat","red",s1.get_pos())
    foods.append(food1)
    
    


    

    for timestep in range(10):
        fig, ax = plt.subplots(1, 2, figsize=(30,15))

        for f in foods:
            f.check_hungry(creatures,hungry) #3.1.2 - checks if there are any hungry creatures.
            f.check_available_food(foods,friends,hungry) #3.1.3 - if there is not enough food, it adds more food to the supply
            f.feed(foods,friends,hungry) #3.1.4 - food gets depleted when consumed by creature
            f.plot_me(ax[0],size) #3.1.1 - food is plotted onto the grid using plot_me()



        update_smells(smells, creatures, toys, foods)
        
        ax[0].set_title(f"Timestep: {timestep+1}")
        ax[1].set_title(f"Timestep: {timestep+1}")
        plot_yard(ax[0], yard)


        
        plot_smells(ax[1],smells)
        fig.savefig("task1.png")
        plt.pause(4)
        plt.clf()

if __name__ == "__main__":
    main()
