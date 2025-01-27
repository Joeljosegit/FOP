from creature import Puppy
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
        

def main():
    size = (60,70)
    yard = build_yard(size)
    smells = np.zeros(size)
    creatures = []
    snoopy = Puppy("Snoopy", "white/black", (5,15))
    creatures.append(snoopy)
    ASAP = Puppy("ASAP", "white/black", (19,15))
    creatures.append(ASAP)
    for i in range(7):
        a = random.randint(10,50)
        b = random.randint(10,50)
        rocky = Puppy("Rocky", "red/brown", (a,b))
        creatures.append(rocky)
    


    

    for timestep in range(10):
        fig, ax = plt.subplots(figsize = (30,15))
        for c in creatures:
            c.step_change() #1.3.2 - Method to move dog
            c.plot_me(ax, size) #1.3.1 - Method to plot dogs as circles
            c.recognise(creatures,friends,strangers) #1.3.4 - method to determine whether human nearby is stranger or friend
            c.chase(creatures,strangers) #1.3.3 - method to chase after a stranger


        ax.set_title(f"Timestep: {timestep+1}")    
        plot_yard(ax, yard)


        
        fig.savefig("task1.png")
        plt.pause(4)
        plt.clf()

if __name__ == "__main__":
    main()
