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

mainClock = pygame.time.Clock()


# Init code for Tkinter 
class App:
    def __init__(self, master) -> None:
  
        # Instantiating master i.e toplevel Widget
        self.master = master
  
        # Creating first Label i.e with default font-size
        Label(self.master, text="I have default font-size").pack(pady=20)
  
        # Creating second label
        # This label has a font-family of Arial
        # and font-size of 25
        Label(self.master,
              text="I have a font-size of 25",
  
              # Changing font-size here
              font=("Arial", 25)
              ).pack()
  
 
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

#Import and Print contents of 'test.csv'
myCsvData = importCsv('test.csv')
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
#Pygame Init
pygame.init()
pygame.font.init()

#switch for Tk window
def quit_callback():
  global Done
  Done = True


def mainLoop():
    #Setting up our display and initializing our font styles
    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
    intentFont = pygame.font.SysFont('Calibri', 14, bold=True)
    mainSurface = pygame.Surface(surfDim)
    pygame.display.set_caption("Intentions")
    gameExit = False

    ##################
    #Main Pygame Loop#
    ##################
    while not gameExit:
        screenInfo = pygame.display.Info()
        screenWid = screenInfo.current_w
        screenHei = screenInfo.current_h
        namePosHei = screenHei / 2
        numPosHei = namePosHei + 25
        addrPosHei = numPosHei + 25
        posWid = (screenWid / 2) - 155
        namePos = (posWid, namePosHei)
        numPos = (posWid, numPosHei)                
        addrPos = (posWid, addrPosHei)
        #Fill the background with white
        gameDisplay.fill(white)
        #For each piece of data in myCsvData
        for i in myCsvData:
            #Store our text data as Strings
            dataToString = str(i)
            nameCache = intentFont.render(i[0], False, black)
            numCache = intentFont.render(i[1], False, black)
            addrCache = intentFont.render(i[2], False, black)
            
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
                    if event.key == pygame.K_SPACE:
                        gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                        screenInfo = pygame.display.Info()
                        screenWid = screenInfo.current_w
                        screenHei = screenInfo.current_h
                        namePosHei = screenHei / 2
                        numPosHei = namePosHei + 25
                        addrPosHei = numPosHei + 25
                        posWid = (screenWid / 2) - 155
                        namePos = (posWid, namePosHei)
                        numPos = (posWid, numPosHei)                
                        addrPos = (posWid, addrPosHei)
                        gameDisplay.fill(white)
                    if event.key == pygame.K_DOWN:
                        gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
                        gameDisplay.fill(white)

            #Draws a white rectangle where the name goes
            pygame.draw.rect(gameDisplay, white, pygame.Rect(posWid,namePosHei,1000,90))
            #Display the text on screen
            gameDisplay.blit(nameCache, namePos)
            gameDisplay.blit(numCache, numPos)
            gameDisplay.blit(addrCache, addrPos)
            #Draw Screen
            pygame.display.flip()
            #wait for 2 seconds
            time.sleep(timeFormula)
mainLoop()