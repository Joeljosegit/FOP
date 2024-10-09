from creature import Puppy, Cat
import numpy as np
import matplotlib.pyplot as plt
import random
import time
def plot_yard(ax, p):
    ax.imshow(p)

def plot_smells(ax, smells):
    ax.imshow(smells)
    


def build_yard(dims):
    
    plan = np.zeros(dims)
    return plan
   
def update_smells(smells, creatures):
    np.where(smells>0, smells-1, 0)
    for c in creatures:
        pos = c.get_pos()
        smells[pos[0], pos[1]] += 5

def main():
    size = (30,30)
    yard = build_yard(size)
    smells = np.zeros(size)
    creatures = []
    snoopy = Puppy("Snoopy", "white/black", (5,15))
    creatures.append(snoopy)
    ASAP = Puppy("ASAP", "white/black", (19,15))
    creatures.append(ASAP)
    for i in range(7):
        a = random.randint(5,20)
        b = random.randint(5,20)
        rocky = Puppy("Rocky", "red/brown", (a,b))
        creatures.append(rocky)
    cat1 = Cat("Oogie", "grey/grey", (17,7))
    creatures.append(cat1)
    


    

    for timestep in range(10):
        fig, ax = plt.subplots(figsize=(30,15))
        for c in creatures:
            c.step_change() #1.2.2 method to move circles north/east/west/south
            c.plot_me(ax, size) #1.2.1 method to plot cat's as circles


        update_smells(smells, creatures)
        
        ax.set_title(f"Timestep: {timestep+1}")
        plot_yard(ax, yard)


        
        fig.savefig("task1.png")
        plt.pause(4)
        plt.clf()

if __name__ == "__main__":
    main()
