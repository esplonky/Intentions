import time
import os
from turtle import Screen, width
from unicodedata import name
import pygame
import csv
from pygame.locals import *
from matplotlib import font_manager
import asyncio
import pathlib
import pygubu



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


gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))


def quit_callback():
  global Done
  Done = True

def getListOfFonts():
    fontStorage = []

    for x in font_manager.win32InstalledFonts():
        x=x[::-1]
        dot = x.find('.')
        slash = x.find('\\')
        x = x[slash-1:dot:-1]
        fontStorage += [x]
    fontStorage.sort()
    return(fontStorage)

fontList = getListOfFonts()


