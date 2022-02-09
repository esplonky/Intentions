import time
import os
import tkinter as tk
from tkinter import *
from turtle import Screen, width
from unicodedata import name
import pygame
import csv
from pygame.locals import *
from matplotlib import font_manager
import asyncio
import pathlib
import pygubu
import tkinter.ttk as ttk

root = tk.Tk()

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


#def openPreferences():
    
    
async def sleepTimer(seconds):
    time.sleep(2)
    return True

