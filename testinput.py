"""
snoo.py - base simulation for the FOP assingment, Sem1 2024
Written by: Joel Jose
Student ID: 21745625

Usage:
Versions:
    - initial version supplied 15/4/24
"""
from creature import *
import numpy as np
import matplotlib.pyplot as plt
import random
import time
def plot_yard(ax, p):
    ax.imshow(p, cmap = "nipy_spectral")

def plot_smells(ax, smells):
    ax.imshow(smells, cmap = "hot")
    
def plot_house(ax,p):
    ax.imshow(p, cmap = "nipy_spectral")

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


def build_house(dims):
    blueprint = np.ones(dims) * 10
    blueprint[20:90,20:70] = 4
    blueprint[20:90,80:90]= 2
    blueprint[20:90, 0:10] = 2
    blueprint[0:10, 15:70] = 0
    blueprint[100:120,30:60] = 9
    return blueprint
   
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
    house = build_house(size)
    smells = np.zeros(size)
    creatures = []
    creatures_house = []
    friends = []
    friends_house = []
    toys = []
    foods = []
    strangers = []
    hungry = []
    toys.append(Toy("Ball","blue",(75,30), True))
    a = random.randint(10,70)
    b = random.randint(10,70)
#8.1 Input staements so that user can customise how they want the simulation to look like. They can customised how many characters, if they want puppies, cats , squirrels or friends and strangers and select how many of each, and the colour and name of each.
    print("\n\033[1mHello, Welcome to the Pets Simulation!\033[0m\n")

    try:
        start = input("\n\033[96mWould You like to Begin? (Y/N)\033[0m\n")

        while start.upper() == "Y":
            animal = input("What animal would you like to add to the Simulation? (Puppy, Cat, Squirrel): ")
            if animal == "Puppy":
                name = input("What should its name be? ")
                colour = input("What colour should it be? ")
                hunger = int(input("Enter its hunger level (0-18): "))
                boredom = int(input("Enter its boredom level (0-18): "))
                terrain = input("Where would you like it to be, in the house or in the yard? ")

                if terrain.lower() == "yard":
                    creatures.append(Puppy(name, colour, (a, b), hunger, boredom))
                elif terrain.lower() == "house":
                    creatures_house.append(Puppy(name, colour, (a, b), hunger, boredom))

            elif animal == "Cat":
                name = input("What should its name be? ")
                colour = input("What colour should it be? ")
                hunger = int(input("Enter its hunger level (0-18): "))
                boredom = int(input("Enter its boredom level (0-18): "))
                terrain = input("Where would you like it to be, in the house or in the yard? ")

                if terrain.lower() == "yard":
                    creatures.append(Cat(name, colour, (a, b), hunger, boredom))
                elif terrain.lower() == "house":
                    creatures_house.append(Cat(name, colour, (a, b), hunger, boredom))

            elif animal == "Squirrel":
                name = input("What should its name be? ")
                colour = input("What colour should it be? ")
                creatures.append(Squirrel(name, colour, (100,30)))

            again = input("Would you like to add another animal? (Y/N): ")
            if again.upper() == "Y":
                animal = input("What animal would you like to add to the Simulation? (Puppy, Cat, Squirrel): ")
            else:
                humans = input("Would you like to add Humans to the Simulation? (Y/N): ")
                while humans.upper() == "Y":
                    human_type = input("What type of human, a Stranger or a Friend? ").lower()
                    if human_type == "friend":
                        name = input("What should its name be? ")
                        colour = input("What colour should it be? ")
                        terrain = input("Where would you like it to be, in the house or in the yard? ")

                        if terrain.lower() == "yard":
                            friends.append(Friend(name, colour, (a, b)))
                        elif terrain.lower() == "house":
                            friends_house.append(Friend(name, colour, (a, b)))
                    elif human_type == "stranger":
                        colour = input("What colour should it be? ")
                        strangers.append(Stranger("-", colour, (a, b)))

                    humans = input("Would you like to add another human? (Y/N): ")

                        
                        
                start = input("Would you like to add more animals...")

        print("Time to start!")                    




    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


    


    

    for timestep in range(10):
        fig, ax = plt.subplots(1, 4, figsize=(30,15))
        for c in creatures:
                c.step_change()
                c.pause(creatures,ax[0])
                c.hunger_fill()
                c.boredom_fill()
                c.hunger_level()
                c.boredom_level()
                c.play(creatures,friends)
                c.play_toy(creatures,toys)
                c.change_step(creatures,friends,hungry)
                c.collissions(creatures,friends,ax[0])
                c.cat_dog(creatures,ax[0])
                c.recognise(creatures,friends,strangers)
                c.chase(creatures,strangers)
                c.boundaries(creatures)
                c.terrain_change(creatures,friends,creatures_house,friends_house)
                c.plot_me(ax[0],size)
                c.plot_hunger_boredom(creatures,ax[2])
                    

        for t in toys:
            t.plot_me(ax[0],size)
        for f in foods:
            f.check_hungry(creatures,hungry)
            f.check_available_food(foods,friends,hungry)
            f.feed(foods,friends,hungry)
            f.plot_me(ax[0],size)
        for h in friends:
            h.step_change()
            h.collissions(creatures,friends)
            if len(hungry) > 0:
                h.bring_food(hungry,friends,foods)
            else:
                h.step_change() 
            h.boundaries(friends)
            h.terrain_change(creatures,friends,creatures_house,friends_house)
            h.plot_me(ax[0],size)
        for s in strangers:
            s.run(creatures,strangers)
            s.boundaries(strangers)
            s.plot_me(ax[0],size)
        for ch in creatures_house:
            ch.step_change()
            ch.hunger_fill()
            ch.boredom_fill()
            ch.hunger_level()
            ch.boredom_level()
            ch.collissions(creatures_house,friends_house,ax[3])
            ch.house_boundaries(creatures_house)
            ch.plot_me(ax[3],size)
        for fh in friends_house:
            fh.step_change()
            fh.house_boundaries(friends_house)
            fh.plot_me(ax[3],size)

        


        
                


    
                    

        update_smells(smells, creatures, toys, foods,friends,strangers)
        
        ax[0].set_title(f"Day: {timestep+1}")
        ax[1].set_title(f"Day: {timestep+1}")
        ax[3].set_title(f"Day: {timestep+1}")
        plot_yard(ax[0], yard)
        plot_house(ax[3],house)


        
        plot_smells(ax[1],smells)
        fig.savefig("task1.png")
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
