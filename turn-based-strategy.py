# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:28:35 2022

@author: Bryant's
"""

import pygame
from map import Map
from basePlayer import Player


background_colour = (0,0,0)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1000, 600))
  
# Set the caption of the screen
pygame.display.set_caption('Geeksforgeeks')
  
# Fill the background colour to the screen
screen.fill(background_colour)
  
# Update the display using flip
pygame.display.flip()
  
# Variable to keep our game loop running
running = True

screenMap = Map(screen)
character = Player(4, 4, screenMap)
  
# game loop
while running:
    # for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_colour)
               
    
    screenMap.drawMap()
    
    pygame.display.flip()   
    
pygame.quit()