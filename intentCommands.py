import time
import os
from turtle import Screen, width
from unicodedata import name
import csv
from matplotlib import font_manager

def paddingSize(fontSize):
    match fontSize:
        case 8:
            size = 2
            return size
        case 9:
            size = 4
            return size
        case 10:
            size = 6
            return size
        case 11:
            size = 8
            return size
        case 12:
            size = 10
            return size
        case 13:
            size = 12
            return size
        case 14:
            size = 14
            return size
        case 15:
            size = 16
            return size
        case 16:
            size = 18
            return size
        case 18:
            size = 22
            return size
        case 20:
            size = 26
            return size
        case 22:
            size = 30
            return size
        case 24:
            size = 24
            return size
        case 38:
            size = 38
            return size
        case 36:
            size = 38
            return size
        case 48:
            size = 40
            return size
        case 72:
            size = 60
            return size
        case _:
            size = 45
            return size

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

gridYPos=25

gridPositions1 = [[25,gridYPos],[150,gridYPos],[275,gridYPos],[300,gridYPos],[425,gridYPos]]
