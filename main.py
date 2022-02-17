import time
import os
import tkinter as tk
from tkinter import *
from turtle import Screen, width
from unicodedata import name
import pygame
import csv
from pygame.locals import *
import pygame_gui
from pyparsing import col
#import CONFIG
import intentCommands
from configparser import ConfigParser

configObject = ConfigParser()

 #Import CSV with a filename as its parameter, parse it, and add it to a list
def importCsv(fileName):
    file = open(fileName)
    csvData = csv.reader(file)
    header = []
    header = next(csvData)
    rows = []
    for row in csvData:
        rows.append(row)
    file.close()
    return rows
configObject.read("CONFIG.ini")
settings = configObject["MAIN"]
#Import and Print contents of 'test.csv'
csvName = settings["FILE"].strip("'")
myCsvData = importCsv(csvName)
#print(myCsvData)
timeFormula = len(myCsvData)/30
print(timeFormula)

#Initialize display parameters and colors
displayWidth = 800
displayHeight = 600
surfWidth = displayWidth - 1
surfHeight = displayHeight - 1
surfDim = (displayWidth, displayHeight)
halfWid = displayWidth / 2
halfHei = displayHeight / 2
posWid = halfWid - 100
namePosHei = halfHei - 20
numPosHei = namePosHei + 25
addrPosHei = numPosHei + 25
topCor = (0,0)
namePos = (posWid, namePosHei)
numPos = (posWid, numPosHei)                
addrPos = (posWid, addrPosHei)
fontPadding = 25
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
brightRed = (255,0,0)
brightGreen = (0,255,0)
transparent = (0,0,0,128)
#Pygame Init
pygame.init()
pygame.font.init()

#switch for Tk window
def quit_callback():
  global Done
  Done = True
  

def create_text_box(font, text, text_color, box_color, margin_x, margin_y):
    text_surf = font.render(text, True, text_color)
    box_surf = pygame.Surface(text_surf.get_rect().inflate(margin_x, margin_y).size)
    box_surf.fill(box_color)
    box_surf.blit(text_surf, text_surf.get_rect(center = box_surf.get_rect().center))
    return box_surf

def mainLoop():
    #Setting up our display and initializing our font styles
    #gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

    mainSurface = pygame.Surface(surfDim)
    pygame.display.set_caption("Intentions")
    gameExit = False
    

    ##################
    #Main Pygame Loop#
    ##################
    while not gameExit:
        
        gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        screenInfo = pygame.display.Info()
        screenWid = screenInfo.current_w
        screenHei = screenInfo.current_h
        fontPadY = 25
        namePosHei = screenHei / 2
        numPosHei = namePosHei + fontPadY
        addrPosHei = numPosHei + fontPadY
        posWid = (screenWid / 2) - 155
        namePos = (posWid, namePosHei)
        numPos = (posWid, numPosHei)                
        addrPos = (posWid, addrPosHei)
        gameDisplay.fill(white)
        #Fill the background with white
        gameDisplay.fill(white)
        #For each piece of data in myCsvData
        grid=[]
        for i in myCsvData:
                      
            configObject.read("CONFIG.ini")
            settings = configObject["MAIN"]
            fontSizeStrip = settings["FONTSIZE"].strip("'")
            fontSizeInt = int(fontSizeStrip)
            fontStrip = settings["FONT"].strip("'")
            #intentCommands.paddingSize()
            screenInfo = pygame.display.Info()
            screenWid = screenInfo.current_w
            screenHei = screenInfo.current_h
            namePosHei = screenHei / 2
            numPosHei = namePosHei + fontPadY
            addrPosHei = numPosHei + fontPadY
            posWid = (screenWid / 2) - 80
            namePos = (posWid, namePosHei)
            numPos = (posWid, numPosHei)                
            addrPos = (posWid, addrPosHei)

            intentFont = pygame.font.SysFont(fontStrip, fontSizeInt)
            #Store our text data as Strings
            dataToString = str(i)
            nameCache = intentFont.render(i[0], True, black)
            numCache = intentFont.render(i[1], True, black)
            addrCache = intentFont.render(i[2], True, black)
            
            ######################
            #Pygame Event Handler#
            ######################
            for event in pygame.event.get():
                #If 'X' button is clicked, exit gracefully
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #If Pygame detects a keypress
                if event.type == pygame.KEYDOWN:
                    #####################
                    #Escape = Exit      #
                    #Space = Fullscreen #
                    #Down = Windowed    #
                    #P = Open Prefs     #
                    #####################
                    if event.key == pygame.K_ESCAPE  :
                        pygame.quit()
                        quit()

            #Draws a white rectangle where the name goes
            pygame.draw.rect(gameDisplay, white, pygame.Rect(posWid,namePosHei,1000,90))
            #Display the text on screen
            for row in range(4):
                grid.append([])
                for column in range(3):
                    
                    gridX=intentCommands.gridPositions1
                    grid[row].append(gridX[column])
                    nameTextBox = create_text_box(intentFont, i[0], black, white, 0,0)
                    numTextBox = create_text_box(intentFont, i[1], black, white, 0,0)
                    addressTextBox = create_text_box(intentFont, i[2], black, white, 0,0)
                    print(grid[row][column])
                    gameDisplay.blit(nameTextBox, grid[row][column])
                    intentCommands.gridYPos+=100
                    gameDisplay.blit(numTextBox, grid[row][column])
                    intentCommands.gridYPos+=100
                    gameDisplay.blit(addressTextBox, grid[row][column])
            #Draw Screen
            pygame.display.flip()
            #wait for 2 seconds
            time.sleep(timeFormula)
mainLoop()