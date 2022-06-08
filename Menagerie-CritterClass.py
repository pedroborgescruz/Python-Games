"""
Critter class.
Pedro Cruz
04/22/2022
"""
from random import *

class Critter(object):
    def __init__(self, name, desc, pers, px, diet):
        self.name = name
        self.desc = desc
        self.pers = pers
        self.px = px
        self.diet = diet
        self.fed = 0
        self.petted = 0
        self.played = 0

    def get_name(self):
        return self.name

    def __str__(self):       
        if (self.petted > 0):
            humor = "happy"
        else:
            humor  = "sad"
        if (self.played > 0):
            disp = "playful"
        else:
            disp = "bored"
        if (self.fed > 0):
            fed = "well-fed"
            if (self.fed > 2):
                fed = "overfull"
        else:
            fed = "hungry"
        
        myStr = ("%s is %s" %(self.name, self.desc))
        myStr += ("; %s looks %s, %s, and %s." %(self.pers, fed, disp, humor))

        return myStr
    
    def pet(self):
        self.petted += 1
        print("%s is %s, and enjoys %s pets!" %(self.name, self.desc, self.px))
    
    def feed(self):
        if self.fed < 2:
            self.fed += 1
            print("%s happily eats %s %s!" %(self.name, self.px, self.diet))
        else:
            print("%s is overfull, and doesn't eat %s " %(self.name, self.px)
                    + "%s" %(self.diet))

    def play(self):
        self.played += 1
        print("%s playfully chases %s toy!" %(self.name, self.px))

    def sleep(self):
        print("Goodnight!")
        atts = [self.petted, self.fed, self.played]
        
        if self.petted != 0:
            self.petted = self.petted - 1
        else:
            self.petted = 0
        if self.fed != 0:
            self.fed = self.fed - 1
        else: 
            self.fed = self.fed - 1
        if self.played != 0:
            self.played = self.played - 1
        else:
            self.played = 0
