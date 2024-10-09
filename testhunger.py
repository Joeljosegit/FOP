"""
snoo.py - base simulation for the FOP assingment, Sem1 2024
Written by: Joel Jose
Student ID: 21745625

Usage:
Versions:
    - initial version supplied 15/4/24
"""
from creature import Puppy, Cat, Squirrel, Toy, Food, Friend, Stranger
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
   
def update_smells(smells, creatures, toys, foods,friends,strangers):
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
    for j in friends:
        pos = j.get_pos()
        smells[min(max(pos[0],0),99), min(max(pos[1],0),78)] += 10
    for h in strangers:
        pos = h.get_pos()
        smells[min(max(pos[0],0),99), min(max(pos[1],0),78)] += 10







def main():
    size = (120,90)
    yard = build_yard(size)
    smells = np.zeros(size)
    creatures = []
    toys = []
    foods = []
    friends = []
    strangers = []
    hungry = []
    snoopy = Puppy("Snoopy", "white/black", (15,88))
    creatures.append(snoopy)
    ASAP = Puppy("ASAP", "white/black", (19,15))
    creatures.append(ASAP)
    cat1 = Cat("Oogie", "grey/grey", (17,7))
    creatures.append(cat1)
    cat2 = Cat("Kendrick", "orange/white", (30,16))
    creatures.append(cat2)
    cat3 = Cat("King", "green/blue", (30,15))
    creatures.append(cat3)
    cat4 = Cat("Drake", "purple/black", (60,10))
    creatures.append(cat4)
    s1 = Squirrel("Scrat","red/orange",(100,30))
    creatures.append(s1)
    toy1 = Toy("Ball1","blue",(30,40),True)
    toy2 = Toy("Ball2","red",(20,20),False)
    toys.append(toy1)
    toys.append(toy2)
    human1 = Friend("Rick","yellow/blue",(30,20))
    friends.append(human1)
    food1 = Food("Meat","red",human1.get_pos())
    foods.append(food1)
    dog2 = Puppy("Test_Subject","white/yellow",(94,30))
    hungry.append(cat2)
    creatures.append(dog2)
    man = Stranger("Beep","black/white",(19,23))
    strangers.append(man)
    


    

    for timestep in range(10):
        fig, ax = plt.subplots(1, 3, figsize=(30,15))
        for c in creatures:
                c.step_change()
                c.pause(creatures,ax[0])
                c.hunger_fill() #7.0.1 - over time a creatures' hugner rises each time-step
                c.hunger_level() #7.0.2 - displays the creatures' hunger level as a label
                c.change_step(creatures,friends,hungry)
                c.collissions(creatures,friends)
                c.recognise(creatures,friends,strangers)
                c.boundaries(creatures)
                c.plot_me(ax[0],size)
                c.plot_hunger_boredom(creatures,ax[2]) 
                    

        for t in toys:
            t.plot_me(ax[0],size)
        for f in foods:
            f.plot_me(ax[0],size)
        for h in friends:
            h.step_change()
            h.collissions(creatures,friends)
            if len(hungry) > 0:
                h.bring_food(hungry,friends,foods)
                h.play(friends,creatures)
            else:
               h.step_change() 
            h.boundaries(friends)
            h.plot_me(ax[0],size)
        for s in strangers:
            s.run(creatures,strangers)
            s.boundaries(strangers)
            s.plot_me(ax[0],size)


        
                


            
        for f in foods:
            for h in friends:
                for j in hungry:
                    if ((j.get_pos()[0] == f.get_pos()[0]-1 or f.get_pos()[0]+1) and (j.get_pos()[1] == f.get_pos()[1])) or ((j.get_pos()[1] == f.get_pos()[1]-1 or f.get_pos()[1]+1) and (j.get_pos()[0] == f.get_pos()[0])):
                        foods.remove(f)
                        hungry.remove(j)
                    

        update_smells(smells, creatures, toys, foods,friends,strangers)
        
        ax[0].set_title(f"Day: {timestep+1}")
        ax[1].set_title(f"Day: {timestep+1}")
        plot_yard(ax[0], yard)


        
        plot_smells(ax[1],smells)
        fig.savefig("task1.png")
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
