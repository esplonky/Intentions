import time
from tkinter import *
from turtle import Screen, width
from unicodedata import name
import pygame
import csv
from pygame.locals import *

master = Tk()
master.geometry("200x200")

def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("Preferences")
    newWindow.geometry("200x200")
    label = Label(newWindow, "Preferences!").pack()
    label.pack(pady = 10)
    
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

myCsvData = importCsv('test.csv')
print(myCsvData)

pygame.init()
pygame.font.init()

displayWidth = 800
displayHeight = 600
surfWidth = displayWidth - 1
surfHeight = displayHeight - 1
surfDim = (displayWidth, displayHeight)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
brightRed = (255,0,0)
brightGreen = (0,255,0)

def mainLoop():
    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
    intentFont = pygame.font.SysFont('Calibri', 32, bold=True)
    mainSurface = pygame.Surface(surfDim)
    pygame.display.set_caption("Intentions")
    gameExit = False
    while not gameExit:

        gameDisplay.fill(white)
        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE  :
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    gameDisplay.fill(white)
                    gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                if event.key == pygame.K_DOWN:
                    gameDisplay.fill(white)
                    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
       
        for i in myCsvData:
            pygame.draw.rect(gameDisplay, white, pygame.Rect(270,270,1000,90))
            dataToString = str(i)
            nameCache = intentFont.render(i[0], False, black)
            numCache = intentFont.render(i[1], False, black)
            addrCache = intentFont.render(i[2], False, black)
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
            gameDisplay.blit(nameCache, namePos)
            gameDisplay.blit(numCache, numPos)
            gameDisplay.blit(addrCache, addrPos)
            pygame.display.flip()
            time.sleep(2)
              
mainLoop()