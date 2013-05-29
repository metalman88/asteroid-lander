from game.Constants import IRON, GOLD, COPPER, NONE
import pygame
from pygame.sprite import Sprite


class ShipPhysics(Sprite):

    def __init__(self):
        self.extra_weight = 0.01
  
    
    def updateWeight(self, fuel):
        return 0.4 + (0.4*(1-(fuel/1000))) - self.extra_weight
        
    def updateFuelBasedOnOre(self, ore):
        if ore== GOLD: self.extra_weight += .3
        if ore== IRON: self.extra_weight += .2
        if ore== COPPER: self.extra_weight += .1
        if ore== NONE: self.extra_weight = 0
        print "THE EXTRA WEIGHT IS " + str(self.extra_weight)