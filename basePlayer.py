# -*- coding: utf-8 -*-
"""
Created on Sun May 15 18:40:51 2022

@author: Bryant's
"""

import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, xCoor, yCoor, screenMap):
        pygame.sprite.Sprite.__init__(self)
        screenMap.setMapValue(xCoor, yCoor, "P")
        
    
        