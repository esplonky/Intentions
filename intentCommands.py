import time
import os
from turtle import Screen, width
from unicodedata import name
import csv
from matplotlib import font_manager



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


