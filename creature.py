"""
creatures.py - class definitions for the creatures in FOP Assignment, Sem 1 2024

Written by : Joel Jose
Student ID : 21745625

Includes:
    Puppy

Versions:
    - initial version supplied 1/4/24
"""
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def flip_coords(pos, LIMITS):
    return((pos[1],pos[0]))

class Puppy():
    type = "Dog"
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos, hunger, boredom):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.time_duration = 0
        self.hunger = hunger
        self.boredom = boredom

    def get_pos(self):
        return self.pos

    def step_change(self):
        validmoves = [(-1,0),(1,0),(0,1),(0,-1)]
        move = random.choice(validmoves)
        print(move)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
                
    def pause(self,creatures,ax):
        for c in creatures:
            for i,d in enumerate(creatures):
                if c.type == "Dog" and d.type == "Squirrel" and (d.pos[0]-c.pos[0]) <= 3:
                    c.time_duration += 1
                    if  c.time_duration <  2:
                        c.pos = (c.pos[0],c.pos[1])
                        ax.text(28,98,"Bark!",fontsize = 5, color = "blue")
                    else:
                        c.pos = (c.pos[0]-2,c.pos[1])
                    
                    c.pos = (c.pos[0]-2,c.pos[1])
                elif d.type == "Dog" and c.type == "Squirrel" and (c.pos[0] - d.pos[0]) <= 3:
                        d.time_duration += 1
                        if d.time_duration < 2:
                            d.pos = (c.pos[0],c.pos[1])
                            ax.text(28,98,"Bark!Bark!",fontsize = 5, color = "blue")

                        else:
                            d.pos = (d.pos[0]-2,d.pos[1])
        

    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]-0.3), height=1.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]-0.3), height=1.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        ax.text(fpos[0]-1,fpos[1]+1,self.name,ha = 'center', va = 'top', fontsize = 5)

    def playful_move(self,creatures):
        for c in creatures:
            move = [(0,1),(0,-1),(1,0),(-1,0)]
            for i in range(4):
                c.pos = (c.pos[0] + move[i][0], c.pos[1] + move[i][1])
            
                
    def toy_carry(self,creatures,toys):
        for c in creatures:
            for t in toys:
                if c.type != "Squirrel" and c.boredom_level() == "very bored" and t.pos == (c.pos[0]-1 or c.pos[0]+1, c.pos[1]) or t.pos == (c.pos[0],c.pos[1]-1 or c.pos[1]+1):
                    while c.boredom_level() == "very bored":
                        t.pos = (c.pos[0],c.pos[1])
                        c.boredom -= 3
                        last_bored_position = (c.pos[0],c.pos[1])
                    if last_bored_position is not None:
                        t.pos = (c.pos[0],c.pos[1]-1)
                    else: 
                        pass
                else:
                    pass

    def play(self,friends,creatures):
        for h in friends:
            for c in creatures:
                if c.type != "Squirrel" and (((h.get_pos()[0] == c.get_pos()[0]+1 or h.get_pos()[0] == c.get_pos()[0]-1) and h.get_pos()[1] == c.get_pos()[1]) or ((h.get_pos()[1] == c.get_pos()[1]-1 or h.get_pos()[1] ==  c.get_pos()[1]+1) and h.get_pos()[0] == c.get_pos()[0])):
                        c.playful_move(creatures)
                        c.boredom -= 3
                else:
                    c.step_change()
    def play_toy(self,creatures,toys):
        for c in creatures:
            for t in toys:
                if c.type != "Squirrel" and (((t.get_pos()[0] == c.get_pos()[0]+1 or t.get_pos()[0] == c.get_pos()[0]-1) and t.get_pos()[1] == c.get_pos()[1]) or ((t.get_pos()[1] == c.get_pos()[1]-1 or t.get_pos()[1] ==  c.get_pos()[1]+1) and t.get_pos()[0] == c.get_pos()[0])) and c.boredom_level() == "very bored":
                    c.toy_carry(creatures,toys)
                else:
                    c.step_change()

    def change_step(self,creatures,friends,hungry):
        for c in creatures:
            for h in friends:
                for j in hungry:
                    if c.name == j.name and c.type != "Squirrel":
                        c.pos = (c.get_pos()[0] +((h.get_pos()[0]-c.get_pos()[0])//2),c.get_pos()[1]+((h.get_pos()[1]-c.get_pos()[1])//2))
                    else:
                        c.pos = c.pos


    def chase(self,creatures,strangers,friends):
        for c in creatures:
            for h in friends:
                for s in strangers:
                    if c.type != "Squirrel":
                        if s.type == "Stranger" and ((h.pos[0] == c.pos[0]-3 or h.pos[0] == c.pos[0]+3) and h.pos[1] == c.pos[1] or (h.pos[0] == c.pos[0] and (h.pos[1] == c.pos[1]-3 or h.pos[1] == c.pos[1]+3))):
                            if c.pos[0] == h.pos[0] -3 or c.pos[0] == h.pos[0] +3:
                                if c.pos[0] == h.pos[0] -3:
                                    c.pos = (min(105,c.pos[0]+2),c.pos[1])
                                elif c.pos[0] == h.pos[0] +3:
                                    c.pos = (max(5,c.pos[0]-2),c.pos[1])
                            elif c.pos[0] == h.pos[0] -2 or c.pos[0] == h.pos[0] +2:
                                if c.pos[0] == h.pos[0] -2:
                                    c.pos = (min(105,c.pos[0] +1), c.pos[1])
                                elif c.pos[0] == h.pos[0] +2:
                                    c.pos = (max(5,c.pos[0]-1),c.pos[1])
                            elif c.pos[0] == h.pos[0] -1 or c.pos[0] == h.pos[0] +1:
                                if c.pos[0] == h.pos[0] -1:
                                    c.pos = (min(105,c.pos[0] +1), c.pos[1])
                                elif c.pos[0] == h.pos[0] +1:
                                    c.pos = (max(5,c.pos[0] -1), c.pos[1])
                            elif c.pos[0] == h.pos[0]:
                                c.pos = (c.pos[0],c.pos[1])
                            elif c.pos[1] == h.pos[1] -3 or c.pos[1] == h.pos[1] +3:
                                if c.pos[1] == h.pos[1] -3:
                                    c.pos = (c.pos[0],min(87,c.pos[1]+2))
                                elif c.pos[1] == h.pos[1] +3:
                                    c.pos = (c.pos[0],max(5,c.pos[1]-2))
                            elif c.pos[1] == h.pos[1] -2 or c.pos[1] == h.pos[1] +2:
                                if c.pos[1] == h.pos[1] -2:
                                    c.pos = (c.pos[0], min(87,c.pos[1]+1))
                                elif c.pos[1] == h.pos[1] +2:
                                    c.pos = (c.pos[0],max(5,c.pos[1]-1))
                            elif c.pos[1] == h.pos[1] -1 or c.pos[1] == h.pos[1] +1:
                                if c.pos[1] == h.pos[1] -1:
                                    c.pos = (c.pos[0], min(87,c.pos[1]+1))
                                elif c.pos[1] == h.pos[1] +1:
                                    c.pos = (c.pos[0], max(5,c.pos[1]-1))
                            elif c.pos[1] == h.pos[1]:
                                c.pos = (c.pos[0],c.pos[1])
                        else:
                            pass
                    else:
                        pass
    def recognise(self,creatures,friends,strangers):
        for c in creatures:
            for s in strangers:
                for h in friends:
                    if c.type != "Squirrel":
                        if s.type == "Stranger" and ((h.pos[0] == c.pos[0]-3 or h.pos[0] == c.pos[0]+3) and h.pos[1] == c.pos[1] or (h.pos[0] == c.pos[0] and (h.pos[1] == c.pos[1]-3 or h.pos[1] == c.pos[1]+3))):
                            c.chase(creatures,strangers)
                        elif h.type == "Friends":
                            c.play(creatures,friends)
                            c.boredom -= 3
                    else:
                        pass

    def boundaries(self,creatures):
        for c in creatures:
            if c.pos[0] <= 0:
                c.pos = ((c.pos[0] - (0-c.pos[0])) +5, c.pos[1])
            elif c.pos[0] >= 110:
                c.pos = ((c.pos[0] - (c.pos[0]-110)) -5, c.pos[1])
            elif c.pos[1] <= 0:
                c.pos = (c.pos[0],(c.pos[1]-(0-c.pos[1]))+5)
            elif c.pos[1] >= 89:
                c.pos = (c.pos[0],(c.pos[1] - (c.pos[1]-89))-5)
            for i in range(0,20):
                for j in range(1,4):
                    if c.pos == (80 - j or 80 + j, i):
                        if c.pos[0] == 80 - j:
                            c.pos = (c.pos[0]-3,c.pos[1])
                        elif c.pos[0] == 80 + j:
                            c.pos = (c.pos[0] +3, c.pos[1])
                    else:
                        pass
            for h in range(70,90):
                for k in range(1,4):
                    if c.pos == (80 + k or 80 - k, h):
                        if c.pos[0] == 80 - k:
                            c.pos = (c.pos[0] - 3, c.pos[1])
                        elif c.pos[0] == 80 + k:
                            c.pos = (c.pos[0] + 3, c.pos[1])
                    else:
                        pass
            for l in range(20,60):
                if c.pos == (20,i):
                    c.pos = (c.pos[0] -2, c.pos[1])
            for n in range(20,90):
                if c.pos == (n,20):
                    c.pos = (c.pos[0],c.pos[1]-2)
                elif c.pos == (n,70):
                    c.pos = (c.pos[0],c.pos[1]+2)
            for o in range(20,70):
                if c.pos == (90,o):
                    c.pos = (c.pos[0]+2,c.pos[1])
                elif c.pos[0] == 20 < c.pos[0] <= 55 and c.pos[1] == o:
                    c.pos = (c.pos[0]-(c.pos[0]-20),c.pos[1])
                elif c.pos[0] == 55 < c.pos[0] < 90 and c.pos[1] == o:
                    c.pos = (c.pos[0] + (90-c.pos[0]),c.pos[1])
                                                        
            

    def collissions(self,creatures,friends,ax):
        for c in creatures:
            for f in friends:
                if c.pos == f.pos:
                    c.pos = (c.pos[0],c.pos[1]+1)
                    c.boredom -= 2
                    f.pos = (f.pos[0],f.pos[1])
                elif c.pos == (f.pos[0]-1 or f.pos[0]+1,f.pos[1]):
                    if c.pos == (f.pos[0] -1, f.pos[1]):
                        c.boredom -= 2
                        c.pos = (c.pos[0],c.pos[1]+1)
                    elif c.pos == (f.pos[0]+1,f.pos[1]):
                        c.boredom -= 2
                        c.pos = (c.pos[0], c.pos[1] -1)
                elif c.pos == (f.pos[0],f.pos[1]-1 or f.pos[1]+1):
                    if c.pos == (f.pos[0],f.pos[1]-1):
                        c.boredom -= 2
                        c.pos = (c.pos[0]-1,c.pos[1])
                    elif c.pos == (f.pos[0],f.pos[1]+1):
                        c.boredom -= 2 
                        c.pos = (c.pos[0]+1,c.pos[1])
                else:
                    pass

    def cat_dog(self,creatures,ax):
        for c in creatures:
            for i,d in enumerate(creatures):
                if c.pos[0] > d.pos[0] and (c.pos[0] - d.pos[0]) <= 3  and c.name != d.name or c.pos[0] < d.pos[0] and (d.pos[0] - c.pos[0]) <= 3  and c.name != d.name:
                    if c.type == "Dog" and d.type == "Cat":
                        ax.text(c.pos[1],c.pos[0]+2,"BARK!", color="red", fontsize=5)
                        d.pos = (d.pos[0]+2,d.pos[1]+2)
                    elif d.type == "Dog" and c.type == "Cat":
                        ax.text(d.pos[1],d.pos[0]+2,"BARK!", color= "red", fontsize= 5)
                        c.pos = (c.pos[0]+2,c.pos[1]+2)
                else:
                    pass


    def hunger_fill(self):
        self.hunger += 1
        return self.hunger
    def hunger_level(self):
        if 0 <= self.hunger < 6:
            return "full"
        elif 6 <= self.hunger < 12:
            return "moderate"
        elif 12 <= self.hunger < 18:
            return "hungry"
    def boredom_fill(self):
        self.boredom += 1
        return self.boredom
    def boredom_level(self):
        if 0 <= self.boredom < 6:
            return "not bored"
        elif 6 <= self.boredom < 12:
            return "mild boredom"
        elif 12 <= self.boredom < 18:
            return "very bored"
    def plot_hunger_boredom(self,creatures,ax):
        for c in creatures:
            if c.hunger_level() == "full":
                colour = "green"
            elif c.hunger_level() == "moderate":
                colour = "orange"
            elif c.hunger_level() == "hungry":
                colour = "red"
            elif c.boredom_level() == "not bored":
                colour = "blue"
            elif c.boredom_level() == "mild boredom":
                colour = "yellow"
            elif c.boredom_level() == "very bored":
                colour = "pink"
            ax.scatter(c.pos[1],c.pos[0],color = colour, s = 100, label= f"{c.name}-{c.type}")

        legend_elements = [
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Full",markerfacecolor = "green", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Moderate",markerfacecolor = "orange", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Hungry",markerfacecolor = "red", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Not Bored",markerfacecolor = "blue", markersize = 15),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Mild Boredom",markerfacecolor = "yellow", markersize = 15),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Very Bored",markerfacecolor = "pink", markersize = 15)
        ]

        ax.legend(handles = legend_elements, loc = 'upper right')
        ax.set_title("Hunger and Boredom Tracker")
        
    
    def terrain_change(self,creatures,friends,creatures_house,friends_house):
        creatures_to_move = []
        friends_to_move = []
        for f in friends:
            for c in creatures:
                for i in range(60,70):
                    if c.type != 'Squirrel' and c.pos == (20,i) or f.pos == (20,i):
                        if c.pos == (20,i):
                            creatures_to_move.append(c)
                            creatures.remove(c)
                            
                        
                        elif f.pos == (20,i):
                            friends_to_move.append(f)
                            friends.remove(f)
                        for cm in creatures_to_move:
                            creatures_house.append(cm)
                            cm.pos == (110,45)
                        for fm in friends_to_move:
                            friends_house.append(fm)
                            fm.pos == (110,50)
                        creatures_to_move.clear()
                        friends_to_move.clear()
                    else:
                        pass


    def house_boundaries(self,creatures_house):
        creatures_to_move = []
        for ch in creatures_house:
            for i in range(15,70):
                if ch.pos[0] == 0 < ch.pos[0] <= 10 and ch.pos[1] == i:
                    ch.pos = (ch.pos[0]+((10-ch.pos[0])+2),ch.pos[1])
                elif ch.pos[0] <= 0:
                    ch.pos = ((ch.pos[0] - (0-ch.pos[0])) +5, ch.pos[1])
                elif ch.pos[0] >= 120:
                    creatures_to_move.append(ch)
                    creatures_house.remove(ch)
                    creatures.append(ch)
                    ch.pos == (22,62)
                    creatures_to_move.remove(ch)
                elif ch.pos[1] <= 0:
                    ch.pos = (ch.pos[0],(ch.pos[1]-(0-ch.pos[1]))+5)
                elif ch.pos[1] >= 89:
                    ch.pos = (ch.pos[0],(ch.pos[1] - (ch.pos[1]-89))-5)
                else:
                    pass




class Cat:
    type = "Cat"
    def __init__(self, name, colour, pos, hunger, boredom):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.time_duration = 0
        self.hunger = hunger
        self.boredom = boredom

    def get_pos(self):
        return self.pos

    def step_change(self):
        validmoves = [(-1,0),(1,0),(0,-1),(0,1)]
        print(validmoves)
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]-0.3), height=1.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]-0.3), height=1.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        ax.text(fpos[0]-1,fpos[1]+1,self.name,ha = 'center', va = 'top',fontsize = 5)

    def playful_move(self,creatures):
        for c in creatures:
            move = [(0,1),(0,-1),(1,0),(-1,0)]
            for i in range(4):
                c.pos = (c.pos[0] + move[i][0], c.pos[1] + move[i][1])
    def toy_carry(self,creatures,toys):
        for c in creatures:
            for t in toys:
                if c.type != "Squirrel" and c.boredom_level() == "very bored" and t.pos == (c.pos[0]-1 or c.pos[0]+1, c.pos[1]) or t.pos == (c.pos[0],c.pos[1]-1 or c.pos[1]+1):
                    while c.boredom_level() == "very bored":
                        t.pos = (c.pos[0],c.pos[1])
                        c.boredom -= 3
                        last_bored_position = (c.pos[0],c.pos[1])
                    if last_bored_position is not None:
                        t.pos = (c.pos[0],c.pos[1]-1)
                    else:
                        pass
                else:
                    pass
    def play(self,friends,creatures):
        for h in friends:
            for c in creatures:
                if c.type != "Squirrel" and (((h.get_pos()[0] == c.get_pos()[0]+1 or h.get_pos()[0] == c.get_pos()[0]-1) and h.get_pos()[1] == c.get_pos()[1]) or ((h.get_pos()[1] == c.get_pos()[1]-1 or h.get_pos()[1] ==  c.get_pos()[1]+1) and h.get_pos()[0] == c.get_pos()[0])):
                    c.playful_move(creatures)
                    c.boredom -= 3
                else:
                    c.step_change()
    def play_toy(self,creatures,toys):
        for c in creatures:
            for t in toys:
                if c.type != "Squirrel" and (((t.get_pos()[0] == c.get_pos()[0]+1 or t.get_pos()[0] == c.get_pos()[0]-1) and t.get_pos()[1] == c.get_pos()[1]) or ((t.get_pos()[1] == c.get_pos()[1]-1 or t.get_pos()[1] ==  c.get_pos()[1]+1) and t.get_pos()[0] == c.get_pos()[0])) and c.boredom_level() == "very bored":
                    c.toy_carry(creatures,toys)
                else:
                    c.step_change()

    def change_step(self,creatures,friends,hungry):
        for c in creatures:
            for h in friends:
                for j in hungry:
                    if c.name == j.name and c.type != "Squirrel":
                        c.pos = (c.get_pos()[0] +((h.get_pos()[0]-c.get_pos()[0])//2),c.get_pos()[1]+((h.get_pos()[1]-c.get_pos()[1])//2))
                    else:
                        c.pos = c.pos

    def pause(self,creatures,ax):
        pass


    def chase(self,creatures,strangers):
        for c in creatures:
            for h in strangers:
                if c.type != "Squirrel":
                    if h.type == "Stranger" and ((h.pos[0] == c.pos[0]-3 or h.pos[0] == c.pos[0]+3) and h.pos[1] == c.pos[1] or (h.pos[0] == c.pos[0] and (h.pos[1] == c.pos[1]-3 or h.pos[1] == c.pos[1]+3))):
                        if c.pos[0] == h.pos[0] -3 or c.pos[0] == h.pos[0] +3:
                            if c.pos[0] == h.pos[0] -3:
                                c.pos = (min(105,c.pos[0]+2),c.pos[1])
                            elif c.pos[0] == h.pos[0] +3:
                                c.pos = (max(5,c.pos[0]-2),c.pos[1])
                        elif c.pos[0] == h.pos[0] -2 or c.pos[0] == h.pos[0] +2:
                            if c.pos[0] == h.pos[0] -2:
                                c.pos = (min(105,c.pos[0] +1), c.pos[1])
                            elif c.pos[0] == h.pos[0] +2:
                                c.pos = (max(5,c.pos[0]-1),c.pos[1])
                        elif c.pos[0] == h.pos[0] -1 or c.pos[0] == h.pos[0] +1:
                            if c.pos[0] == h.pos[0] -1:
                                c.pos = (min(105,c.pos[0] +1), c.pos[1])
                            elif c.pos[0] == h.pos[0] +1:
                                c.pos = (max(5,c.pos[0] -1), c.pos[1])
                        elif c.pos[0] == h.pos[0]:
                            c.pos = (c.pos[0],c.pos[1])
                        elif c.pos[1] == h.pos[1] -3 or c.pos[1] == h.pos[1] +3:
                            if c.pos[1] == h.pos[1] -3:
                                c.pos = (c.pos[0],min(87,c.pos[1]+2))
                            elif c.pos[1] == h.pos[1] +3:
                                c.pos = (c.pos[0],max(5,c.pos[1]-2))
                        elif c.pos[1] == h.pos[1] -2 or c.pos[1] == h.pos[1] +2:
                            if c.pos[1] == h.pos[1] -2:
                                c.pos = (c.pos[0], min(87,c.pos[1]+1))
                            elif c.pos[1] == h.pos[1] +2:
                                c.pos = (c.pos[0],max(5,c.pos[1]-1))
                        elif c.pos[1] == h.pos[1] -1 or c.pos[1] == h.pos[1] +1:
                            if c.pos[1] == h.pos[1] -1:
                                c.pos = (c.pos[0], min(87,c.pos[1]+1))
                            elif c.pos[1] == h.pos[1] +1:
                                c.pos = (c.pos[0], max(5,c.pos[1]-1))
                        elif c.pos[1] == h.pos[1]:
                            c.pos = (c.pos[0],c.pos[1])
                    else:
                        pass
                else:
                    pass

    def recognise(self,creatures,friends,strangers):
        for c in creatures:
            for s in strangers:
                for h in friends:
                    if c.type != "Squirrel": 
                        if s.type == "Stranger" and ((h.pos[0] == c.pos[0]-3 or h.pos[0] == c.pos[0]+3) and h.pos[1] == c.pos[1] or (h.pos[0] == c.pos[0] and (h.pos[1] == c.pos[1]-3 or h.pos[1] == c.pos[1]+3))):
                            c.chase(creatures,strangers)
                        elif h.type == "Friends":
                            c.play(creatures,friends)
                    else:
                        pass


    def boundaries(self,creatures):
        for c in creatures:
            if c.pos[0] <= 0:
                c.pos = ((c.pos[0] - (0-c.pos[0])) +5, c.pos[1])
            elif c.pos[0] >= 110:
                c.pos = ((c.pos[0] - (c.pos[0]-110)) -5, c.pos[1])
            elif c.pos[1] <= 0:
                c.pos = (c.pos[0],(0-c.pos[1])+5)
            elif c.pos[1] >= 89:
                c.pos = (c.pos[0], (c.pos[1]-89)-5)
            for i in range(0,20):
                for j in range(1,4):
                    if c.pos == (80 - j or 80 + j, i):
                        if c.pos[0] == 80 - j:
                            c.pos = (c.pos[0]-3,c.pos[1])
                        elif c.pos[0] == 80 + j:
                            c.pos = (c.pos[0] +3, c.pos[1])
                    
            for h in range(70,90):
                for k in range(1,4):
                    if c.pos == (80 + k or 80 - k, h):
                        if c.pos[0] == 80 - k:
                            c.pos = (c.pos[0] - 3, c.pos[1])
                        elif c.pos[0] == 80 + k:
                            c.pos = (c.pos[0] + 3, c.pos[1])
                    else:
                        pass
                for l in range(20,60):
                    if c.pos == (20,i):
                        c.pos = (c.pos[0] -2, c.pos[1])
                for n in range(20,90):
                    if c.pos == (n,20):
                        c.pos = (c.pos[0],c.pos[1]-2)
                    elif c.pos == (n,70):
                        c.pos = (c.pos[0],c.pos[1]+2)
                for o in range(20,70):
                    if c.pos == (90,o):
                        c.pos = (c.pos[0]+2,c.pos[1])
                    elif c.pos[0] == 20 < c.pos[0] <= 55 and c.pos[1] == o:
                        c.pos = (c.pos[0]-(c.pos[0]-20),c.pos[1])
                    elif c.pos[0] == 55 < c.pos[0] < 90 and c.pos[1] == o:
                        c.pos = (c.pos[0] + (90-c.pos[0]),c.pos[1])
            else:
                pass


    def collissions(self,creatures,friends,ax):
        for c in creatures:
            for f in friends:
                if c.pos == f.pos:
                    c.pos = (c.pos[0],c.pos[1]+1)
                    f.pos = (f.pos[0],f.pos[1])
                elif c.pos == (f.pos[0]-1 or f.pos[0]+1,f.pos[1]):
                    if c.pos == (f.pos[0] -1, f.pos[1]):
                        c.boredom -= 2
                        c.pos = (c.pos[0],c.pos[1]+1)
                    elif c.pos == (f.pos[0]+1,f.pos[1]):
                        c.boredom -= 2
                        c.pos = (c.pos[0], c.pos[1] -1)
                elif c.pos == (f.pos[0],f.pos[1]-1 or f.pos[1]+1):
                    if c.pos == (f.pos[0],f.pos[1]-1):
                        c.boredom -= 2
                        c.pos = (c.pos[0]-1,c.pos[1])
                    elif c.pos == (f.pos[0],f.pos[1]+1):
                        c.boredom -= 2
                        c.pos = (c.pos[0]+1,c.pos[1])
                else:
                    pass
    def cat_dog(self,creatures,ax):
        for c in creatures:
            for i,d in enumerate(creatures):
                if c.pos[0] > d.pos[0] and (c.pos[0] - d.pos[0]) <= 3  and c.name != d.name or c.pos[0] < d.pos[0] and (d.pos[0] - c.pos[0]) <= 3  and c.name != d.name:
                    if c.type == "Dog" and d.type == "Cat":
                        ax.text(c.pos[1],c.pos[0]+2,"BARK!", color="red", fontsize=5)
                        d.pos = (d.pos[0]+2,d.pos[1]+2)
                    elif d.type == "Dog" and c.type == "Cat":
                        ax.text(d.pos[1],d.pos[0]+2,"BARK!", color= "red", fontsize= 5)
                        c.pos = (c.pos[0]+2,c.pos[1]+2)
                else:
                    pass
    def hunger_fill(self):
        self.hunger += 2
        return self.hunger
    def hunger_level(self):
        if 0 <= self.hunger < 6:
            return "full"
        elif 6 <= self.hunger < 12:
            return "moderate"
        elif 12 <= self.hunger < 18:
            return "hunger"
    def boredom_fill(self):
        self.boredom += 1
        return self.boredom
    def boredom_level(self):
        if 0 <= self.boredom < 6:
            return "not bored"
        elif 6 <= self.boredom < 12:
            return "mild boredom"
        elif 12 <= self.boredom < 18:
            return "very bored"
    def plot_hunger_boredom(self,creatures,ax):
        for c in creatures:
            if c.hunger_level() == "full":
                colour = "green"
            elif c.hunger_level() == "moderate":
                colour = "orange"
            elif c.hunger_level() == "hungry":
                colour = "red"
            elif c.boredom_level() == "not bored":
                colour = "blue"
            elif c.boredom_level() == "mild boredom":
                colour = "yellow"
            elif c.boredom_level() == "very bored":
                colour = "pink"
            ax.scatter(c.pos[1],c.pos[0],color = colour, s = 100, label= f"{c.name}-{c.type}")

        legend_elements = [
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Full",markerfacecolor = "green", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Moderate",markerfacecolor = "orange", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Hungry",markerfacecolor = "red", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Not Bored",markerfacecolor = "blue", markersize = 15),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Mild Boredom",markerfacecolor = "yellow", markersize = 15),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Very Bored",markerfacecolor = "pink", markersize = 15)
                ]

        ax.legend(handles = legend_elements, loc = 'upper right')
        ax.set_title("Hunger and Boredom Tracker")
        
    def terrain_change(self,creatures,friends,creatures_house,friends_house):
        creatures_to_move = []
        friends_to_move = []
        for f in friends:
            for c in creatures:
                for i in range(60,70):
                    if c.type != 'Squirrel' and c.pos == (20,i) or f.pos == (20,i):
                        if c.pos == (20,i):
                            creatures_to_move.append(c)
                            creatures.remove(c)


                        elif f.pos == (20,i):
                            friends_to_move.append(f)
                            friends.remove(f)
                        for cm in creatures_to_move:
                            creatures_house.append(cm)
                            cm.pos == (110,45)
                        for fm in friends_to_move:
                            friends_house.append(fm)
                            fm.pos == (110,50)
                        creatures_to_move.clear()
                        friends_to_move.clear()
                    else:
                        pass

    def house_boundaries(self,creatures_house):
        for ch in creatures_house:
            for i in range(15,70):
                if ch.pos[0] == 0 < ch.pos[0] <= 10 and ch.pos[1] == i:
                    ch.pos = (ch.pos[0]+((10-ch.pos[0])+2),ch.pos[1])
                elif ch.pos[0] <= 0:
                    ch.pos = ((ch.pos[0] - (0-ch.pos[0])) +5, ch.pos[1])
                elif ch.pos[0] >= 120:
                    creatures_to_move.append(ch)
                    creatures_house.remove(ch)
                    creatures.append(ch)
                    ch.pos == (22,62)
                    creatures_to_move.remove(ch)
                elif ch.pos[1] <= 0:
                    ch.pos = (ch.pos[0],(ch.pos[1]-(0-ch.pos[1]))+5)
                elif ch.pos[1] >= 89:
                    ch.pos = (ch.pos[0],(ch.pos[1] - (ch.pos[1]-89))-5)
                else:
                    pass

class Squirrel():
    """
    Holds information and behaviour of squirrel creature
    """
    type = "Squirrel"
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.time_duration = 0
        self.hunger = 0
        self.boredom = 0

    def get_pos(self):
        return self.pos

    def step_change(self):
        pass

    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)
        ax.text(fpos[0]-1,fpos[1]+1,self.name,ha = 'center', va = 'top',fontsize = 5)

    def change_step(self,creatures,friends,hungry):
        for c in creatures:
            for h in friends:
                for j in hungry:
                    if c.name == j.name and c.type != "Squirrel":
                        c.pos = (c.get_pos()[0] +((h.get_pos()[0]-c.get_pos()[0])//2),c.get_pos()[1]+((h.get_pos()[1]-c.get_pos()[1])//2))
                    else:
                        c.pos = c.pos



    def chase(self,creatures,strangers,friends):
        for c in creatures:
            for h in friends:
                for s in strangers:
                    if c.type != "Squirrel":
                        if s.type == "Stranger" and ((h.pos[0] == c.pos[0]-3 or h.pos[0] == c.pos[0]+3) and h.pos[1] == c.pos[1] or (h.pos[0] == c.pos[0] and (h.pos[1] == c.pos[1]-3 or h.pos[1] == c.pos[1]+3))):
                            if c.pos[0] == h.pos[0] -3 or c.pos[0] == h.pos[0] +3:
                                if c.pos[0] == h.pos[0] -3:
                                    c.pos = (min(105,c.pos[0]+2),c.pos[1])
                                elif c.pos[0] == h.pos[0] +3:
                                    c.pos = (max(5,c.pos[0]-2),c.pos[1])
                            elif c.pos[0] == h.pos[0] -2 or c.pos[0] == h.pos[0] +2:
                                if c.pos[0] == h.pos[0] -2:
                                    c.pos = (min(105,c.pos[0] +1), c.pos[1])
                                elif c.pos[0] == h.pos[0] +2:
                                    c.pos = (max(5,c.pos[0]-1),c.pos[1])
                            elif c.pos[0] == h.pos[0] -1 or c.pos[0] == h.pos[0] +1:
                                if c.pos[0] == h.pos[0] -1:
                                    c.pos = (min(105,c.pos[0] +1), c.pos[1])
                                elif c.pos[0] == h.pos[0] +1:
                                    c.pos = (max(5,c.pos[0] -1), c.pos[1])
                            elif c.pos[0] == h.pos[0]:
                                c.pos = (c.pos[0],c.pos[1])
                            elif c.pos[1] == h.pos[1] -3 or c.pos[1] == h.pos[1] +3:
                                if c.pos[1] == h.pos[1] -3:
                                    c.pos = (c.pos[0],min(87,c.pos[1]+2))
                                elif c.pos[1] == h.pos[1] +3:
                                    c.pos = (c.pos[0],max(5,c.pos[1]-2))
                            elif c.pos[1] == h.pos[1] -2 or c.pos[1] == h.pos[1] +2:
                                if c.pos[1] == h.pos[1] -2:
                                    c.pos = (c.pos[0],min(87, c.pos[1]+1))
                                elif c.pos[1] == h.pos[1] +2:
                                    c.pos = (c.pos[0],max(5,c.pos[1]-1))
                            elif c.pos[1] == h.pos[1] -1 or c.pos[1] == h.pos[1] +1:
                                if c.pos[1] == h.pos[1] -1:
                                    c.pos = (c.pos[0], min(87,c.pos[1]+1))
                                elif c.pos[1] == h.pos[1] +1:
                                    c.pos = (c.pos[0], max(5,c.pos[1]-1))
                            elif c.pos[1] == h.pos[1]:
                                c.pos = (c.pos[0],c.pos[1])
                        else:
                            pass
                    else:
                        pass


    def recognise(self,creatures,friends,strangers):
        for c in creatures:
            for h in friends:
                for s in strangers:
                    if c.type != "Squirrel": 
                        if s.type == "Stranger" and ((h.pos[0] == c.pos[0]-3 or h.pos[0] == c.pos[0]+3) and h.pos[1] == c.pos[1] or (h.pos[0] == c.pos[0] and (h.pos[1] == c.pos[1]-3 or h.pos[1] == c.pos[1]+3))):
                            c.chase(creatures,strangers)
                        elif h.type == "Friends":
                            c.play(creatures,friends)
                    else:
                        pass
    
    def boundaries(self,creatures):
        for c in creatures:
            if c.pos[0] <= 0:
                c.pos = ((c.pos[0] - (0-c.pos[0])) +5, c.pos[1])
            elif c.pos[0] >= 110:
                c.pos = ((c.pos[0] - (c.pos[0]-110)) -5, c.pos[1])
            elif c.pos[1] <= 0:
                c.pos = (c.pos[0],(c.pos[1]-(0-c.pos[1]))+5)
            elif c.pos[1] >= 89:
                c.pos = (c.pos[0],(c.pos[1] - (89-c.pos[1]))-5)
            for i in range(0,20):
                for j in range(1,4):
                    if c.pos == (80 - j or 80 + j, i):
                        if c.pos[0] == 80 - j:
                            c.pos = (c.pos[0]-3,c.pos[1])
                        elif c.pos[0] == 80 + j:
                            c.pos = (c.pos[0] +3, c.pos[1])
                    else:
                        pass
            for h in range(70,90):
                for k in range(1,4):
                    if c.pos == (80 + k or 80 - k, h):
                        if c.pos[0] == 80 - k:
                            c.pos = (c.pos[0] - 3, c.pos[1])
                        elif c.pos[0] == 80 + k:
                            c.pos = (c.pos[0] + 3, c.pos[1])
                    else:
                        pass
            for l in range(20,60):
                if c.pos == (20,i):
                    c.pos = (c.pos[0] -2, c.pos[1])
            for n in range(20,90):
                if c.pos == (n,20):
                    c.pos = (c.pos[0],c.pos[1]-2)
                elif c.pos == (n,70):
                    c.pos = (c.pos[0],c.pos[1]+2)
            for o in range(20,70):
                if c.pos == (90,o):
                    c.pos = (c.pos[0]+2,c.pos[1])
            



    def collissions(self,creatures,friends,ax):
        pass
    def pause(self,creatures,ax):
        for c in creatures:
            if c.type == "Dog":
                for k in range(90,96):
                    for j in range(20,26):
                        if c.pos == (k,j):
                            self.time_duration += 1
                            c.pos = (c.pos[0],c.pos[1])
                            ax.text(98,28,"Bark!Bark!", color = "red", fontsize=5)
                        elif c.time_duration >= 2 or c.pos != (k,j):
                            pass
            else:
                pass

    def playful_move(self,creatures):
        for c in creatures:
            move = [(0,1),(0,-1),(1,0),(-1,0)]
            for i in range(4):
                c.pos = (c.pos[0] + move[i][0], c.pos[1] + move[i][1])
    def toy_carry(self,creatures,toys):
        for c in creatures:
            for t in toys:
                if c.type != "Squirrel" and c.boredom_level() == "very bored" and t.pos == (c.pos[0]-1 or c.pos[0]+1, c.pos[1]) or t.pos == (c.pos[0],c.pos[1]-1 or c.pos[1]+1):
                    while c.boredom_level() == "very bored":
                        t.pos = (c.pos[0],c.pos[1])
                        c.boredom -= 3
                        last_bored_position = (c.pos[0],c.pos[1])
                    if last_bored_position is not None:
                        t.pos = (c.pos[0],c.pos[1]-1)
                    else:
                        pass
                else:
                    pass
    def play(self,friends,creatures):
        for h in friends:
            for c in creatures:
                if c.type != "Squirrel" and (((h.get_pos()[0] == c.get_pos()[0]+1 or h.get_pos()[0] == c.get_pos()[0]-1) and h.get_pos()[1] == c.get_pos()[1]) or ((h.get_pos()[1] == c.get_pos()[1]-1 or h.get_pos()[1] ==  c.get_pos()[1]+1) and h.get_pos()[0] == c.get_pos()[0])):
                    c.playful_move(creatures)
                else: 
                    c.step_change()
    def play_toy(self,creatures,toys):
        for c in creatures:
            for t in toys:
                if c.type != "Squirrel" and (((t.get_pos()[0] == c.get_pos()[0]+3 or t.get_pos()[0] == c.get_pos()[0]-3) and t.get_pos()[1] == c.get_pos()[1]) or ((t.get_pos()[1] == c.get_pos()[1]-3 or t.get_pos()[1] ==  c.get_pos()[1]+3) and t.get_pos()[0] == c.get_pos()[0])) and c.boredom_level() == "very bored":
                    c.toy_carry(creatures,toys)

                else:
                    c.step_change()


    def hunger_fill(self):
        self.hunger += 2
        return self.hunger
    def hunger_level(self):
        if 0 <= self.hunger < 6:
            return "full"
        elif 6 <= self.hunger < 12:
            return "moderate"
        elif 12 <= self.hunger < 18:
            return "hungry"
    def boredom_fill(self):
        self.boredom += 1
        return self.boredom
    def boredom_level(self):
        if 0 <= self.boredom < 6:
            return "not bored"
        elif 6 <= self.boredom < 12:
            return "mild boredom"
        elif 12 <= self.boredom < 18:
            return "very bored"
    def plot_hunger_boredom(self,creatures,ax):
        for c in creatures:
            if c.hunger_level() == "full":
                colour = "green"
            elif c.hunger_level() == "moderate":
                colour = "orange"
            elif c.hunger_level() == "hungry":
                colour = "red"
            elif c.boredom_level() == "not bored":
                colour = "blue"
            elif c.boredom_level() == "mild boredom":
                colour = "yellow"
            elif c.boredom_level() == "very bored":
                colour = "pink"
            ax.scatter(c.pos[1],c.pos[0],color = colour, s = 100, label= f"{c.name}-{c.type}")

        legend_elements = [
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Full",markerfacecolor = "green", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Moderate",markerfacecolor = "orange", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Hungry",markerfacecolor = "red", markersize = 10),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Not Bored",markerfacecolor = "blue", markersize = 15),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Mild Boredom",markerfacecolor = "yellow", markersize = 15),
                plt.Line2D([0],[0],marker = 'o', color = 'w', label = "Very Bored",markerfacecolor = "pink", markersize = 15)
                ]
            

        ax.legend(handles = legend_elements, loc = 'upper right')
        ax.set_title("Hunger and Boredom Tracker")

    def terrain_change(self,creatures,friends,creatures_house,friends_house):
        creatures_to_move = []
        friends_to_move = []
        for f in friends:
            for c in creatures:
                for i in range(60,70):
                    if c.type != 'Squirrel' and c.pos == (20,i) or f.pos == (20,i):
                        if c.pos == (20,i):
                            creatures_to_move.append(c)
                            creatures.remve(c)


                        elif f.pos == (20,i):
                            friends_to_move.append(f)
                            friends.remove(f)
                        for cm in creatures_to_move:
                            creatures_house.append(cm)
                            cm.pos == (110,45)
                        for fm in friends_to_move:
                            friends_house.append(fm)
                            fm.pos == (110,50)
                        creatures_to_move.clear()
                        friends_to_move.clear()
                    else:
                        pass

        

class Toy:
    def __init__(self,name,colour,pos,vis):
        self.name = name
        self.colour = colour
        self.pos = pos
        self.visible = vis
    def get_pos(self):
        return self.pos
    def plot_me(self,ax, LIMITS):
        if self.visible ==True:
            fpos = flip_coords(self.pos, LIMITS)
            patch = pat.Circle(fpos, radius = 0.5, color = self.colour)
            ax.add_patch(patch)
        else:
            ax.annotate("X",self.pos, color = self.colour)

class Food:
    def __init__(self,colour,pos):
        csplit = colour.split('/')
        self.colour1 = csplit[0]
        if len(csplit)==2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)
    def get_pos(self):
        return self.pos


    def check_hungry(self,creatures,hungry):
        for c in creatures:
            for i, h in enumerate(hungry):
                if c.name != h.name and c.hunger_level == "moderate" or c.hunger_level == "very hungry":
                    hungry.append(c)
                else:
                    pass

    def check_available_food(self, foods, friends,hungry):
        for f in friends:
            if len(hungry) > 0 and len(foods) == 0:
                for i in range(8):
                    foods.append(Food("red",f.pos))
            else:
                pass
    def feed(self, foods, friends, hungry):
        for f in friends:
            for food in foods:
                for j in hungry:
                    if ((j.get_pos()[0] == f.get_pos()[0]-1 or f.get_pos()[0]+1) and (j.get_pos()[1] == f.get_pos()[1])) or ((j.get_pos()[1] == f.get_pos()[1]-1 or f.get_pos()[1]+1) and (j.get_pos()[0] == f.get_pos()[0])):
                        foods.remove(food)
                        j.hunger -= 5
                        if j.hunger < 6:
                            hungry.remove(j)
                        else:
                            pass



class Person:
    type = "Person"
    def __init__(self,name,colour,pos):
        self.name = name
        csplit = colour.split('/')
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
    def step_change(self):
        validmoves = [(1,0),(-1,0),(0,-1),(0,1)]
        print(validmoves)
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
    def plot_me(self,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=2, color=self.colour1)
        ax.add_patch(patch)
        ax.text(fpos[0]-1,fpos[1]+1,self.type,ha = 'center', va = 'top',fontsize = 5)








class Friend(Person):
    type = "Friend"

    def __init__(self,name,colour,pos):
        super().__init__(name,colour,pos)

    def get_pos(self):
        return self.pos
    def bring_food(self,hungry,friends,foods):
        for h in hungry:
            for j in friends:
                    for f in foods:
                        if j.get_pos()[1] > h.get_pos()[1]+1:
                            j.pos = (j.get_pos()[0],j.get_pos()[1]-1)
                        elif j.get_pos()[1] < h.get_pos()[1]-1:
                            j.pos = (j.get_pos()[0],j.get_pos()[1]+1)
                        elif j.get_pos()[0] > h.get_pos()[0]+1:
                            j.pos = (j.get_pos()[0]-1,j.get_pos()[1])
                        elif j.get_pos()[0] < h.get_pos()[0]-1:
                            j.pos = (j.get_pos()[0] +1 , j.get_pos()[1])
                        f.pos = j.pos
    def playful_move(self,creatures):
        pass
    def boredom_level(self):
        pass
    
    
    def boundaries(self,friends):
        for h in friends:
            if h.pos[0] <= 0:
                h.pos = ((h.pos[0] - (0-h.pos[0])) +5, h.pos[1])
            elif h.pos[0] >= 110:
                h.pos = ((h.pos[0] - (h.pos[0]-110)) -5, h.pos[1])
            elif h.pos[1] <= 0:
                h.pos = (h.pos[0],(0-h.pos[1])+5)
            elif h.pos[1] >= 89:
                h.pos = (h.pos[0],(h.pos[1]-89)-5)
            for i in range(0,20):
                for j in range(1,4):
                    if h.pos == (80 - j or 80 + j, i):
                        if h.pos[0] == 80 - j:
                            h.pos = (h.pos[0]-3,h.pos[1])
                        elif h.pos[0] == 80 + j:
                            h.pos = (h.pos[0] +3, h.pos[1])
                    else:
                        pass
            for q in range(70,90):
                for k in range(1,4):
                    if h.pos == (80 + k or 80 - k, q):
                        if h.pos[0] == 80 - k:
                            h.pos = (h.pos[0] - 3, h.pos[1])
                        elif h.pos[0] == 80 + k:
                            h.pos = (h.pos[0] + 3, h.pos[1])
                
            for l in range(20,60):
                if h.pos == (20,i):
                    h.pos = (h.pos[0] -2, h.pos[1])
            for n in range(20,90):
                if h.pos == (n,20):
                    h.pos = (h.pos[0],h.pos[1]-2)
                elif h.pos == (n,70):
                    h.pos = (h.pos[0],h.pos[1]+2)
            for o in range(20,70):
                if h.pos == (90,o):
                    h.pos = (h.pos[0]+2,h.pos[1])
                elif h.pos[0] == 20 < h.pos[0] <= 55 and h.pos[1] == o:
                    h.pos = (h.pos[0]-(h.pos[0]-20),h.pos[1])
                elif h.pos[0] == 55 < h.pos[0] < 90 and h.pos[1] == o:
                    h.pos = (h.pos[0] + (90-h.pos[0]),h.pos[1])


    def collissions(self,creatures,friends):
        for c in creatures:
            for f in friends:
                if c.pos == f.pos:
                    c.pos = (c.pos[0],c.pos[1]+1)
                    f.pos = (f.pos[0],f.pos[1])
                else:
                    pass
                for i,d in enumerate(creatures):
                    if c.pos == d.pos and c.type != d.type:
                        if d.type == "Dog":
                            c.pos = (c.pos[0]+1,c.pos[1])
                        elif d.type == "Cat":
                            c.pos = (c.pos[0]-1,c.pos[1])
                        elif d.type == "Squirrel":
                            c.pos = (c.pos[0],c.pos[1]-1)


    def terrain_change(self,creatures,friends,creatures_house,friends_house):
        creatures_to_move = []
        friends_to_move = []
        for f in friends:
            for c in creatures:
                for i in range(60,70):
                    if c.type != 'Squirrel' and c.pos == (20,i) or f.pos == (20,i):
                        if c.pos == (20,i):
                            creatures_to_move.append(c)
                            creatures.remove(c)


                        elif f.pos == (20,i):
                            friends_to_move.append(f)
                            friends.remove(f)
                        for cm in creatures_to_move:
                            creatures_house.append(cm)
                            cm.pos == (110,45)
                        for fm in friends_to_move:
                            friends_house.append(fm)
                            fm.pos == (110,50)
                        creatures_to_move.clear()
                        friends_to_move.clear()
                    else:
                        pass
    def house_boundaries(self,friends_house):
        for fh in friends_house:
            for i in range(15,70):
                if fh.pos[0] == 0 < fh.pos[0] <= 10 and fh.pos[1] == i:
                    fh.pos = (fh.pos[0]+((10-fh.pos[0])+2),fh.pos[1])
                elif fh.pos[0] <= 0:
                    fh.pos = ((fh.pos[0] - (0-fh.pos[0])) +5, fh.pos[1])
                elif fh.pos[0] >= 120:
                    friends_to_move.append(fh)
                    friends_house.remove(fh)
                    friends.append(fh)
                    fh.pos == (22,62)
                    friends_to_move.remove(fh)
                elif fh.pos[1] <= 0:
                    fh.pos = (fh.pos[0],(fh.pos[1]-(0-fh.pos[1]))+5)
                elif fh.pos[1] >= 89:
                    fh.pos = (fh.pos[0],(fh.pos[1] - (fh.pos[1]-89))-5)
                else:
                    pass



class Stranger(Person):
    type = "Stranger"

    def __init__(self,name,colour,pos):
        super().__init__(name,colour,pos)
        
    
    def get_pos(self):
        return self.pos
    



    def run(self,creatures,strangers):
        for c in creatures:
            for h in strangers:
                for i in range(5):
                    if (h.pos[0] == c.pos[0]-i or h.pos[0] == c.pos[0]+i) or (h.pos[1] == c.pos[1]-i or h.pos[1] == c.pos[1]+i):
                        if h.pos[0] <= 54:
                            h.pos = (max(0,h.pos[0]-7),h.pos[1])
                        elif h.pos[0] >= 55:
                            h.pos = (min(110,h.pos[0]+7),h.pos[1])
                        while h.pos[1] <= 0 or h.pos[1] >= 89:
                            if h.pos[0] <= 54:
                                while h.pos[0] != 0:
                                    h.pos = (max(0,h.pos[0] -7), h.pos[1])
                            elif h.pos[0] >= 55:
                                while h.pos[0] != 110:
                                    h.pos = (min(110,h.pos[0] +7), h.pos[1])
                    else:
                        h.pos = (h.get_pos()[0],h.get_pos()[1])

    def boundaries(self,strangers):
        for h in strangers:
            if h.pos[0] <= 0 or h.pos[0] >= 110 or h.pos[1] <= 0 or h.pos[1] >= 89:
                strangers.remove(h)
            else:
                pass
