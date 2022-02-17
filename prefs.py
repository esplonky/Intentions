from dataclasses import field
from msilib.schema import RadioButton
from multiprocessing.sharedctypes import Value
import tkinter as tk
import intentCommands
import asyncio
import subprocess
from tkinter import StringVar, Variable, filedialog
import threading
from configparser import ConfigParser


fontList = intentCommands.getListOfFonts()


import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

configObject = ConfigParser()
fontSizes = [8,9,10,11,12,14,16,18,20,22,24,26,28,36,48,72]

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "prefsApp.ui"

def mainLoop():
    subprocess.Popen("main.py", shell=True)

def browse_button():
    fieldCsvLocation.delete(0, 'end')
    csvFilename = filedialog.askopenfilename(title="Browse...", filetypes = (("CSV files", "*.csv"), ("All files", "*")))
    fieldCsvLocation.insert(tk.END, csvFilename)
    return csvFilename

def saveSettings():
    fontVal = "'" + str(insideValue.get()) + "'"
    sizeVal = "'" + str(insideValueNum.get()) + "'"
    fileVal = "'" + str(fieldCsvLocation.get()) + "'"
    gridVal = "'" + gridVar.get() + "'"
    configObject["MAIN"]={
        "FONT": fontVal,
        "FONTSIZE": sizeVal,
        "FILE": fileVal,
        "GRID": gridVal
    }
    confFile = open('CONFIG.ini', 'w')
    configObject.write(confFile)
    
root = tk.Tk()
root.resizable(False,False)



buttonBrowse = ttk.Button(root)
buttonBrowse.configure(text='Browse...', command=browse_button)
buttonBrowse.grid(column='1', row='1', sticky='nw')

fieldCsvLocation = ttk.Entry(root)
fieldCsvLocation.grid(column='0', row='1', sticky='nw')

button3 = ttk.Button(root)
button3.configure(text='Launch')
button3.grid(column='0', row='2', sticky='nw')
button3.configure(command=mainLoop)

insideValue = tk.StringVar(root)
insideValue.set("Calibri")
combobox1 = ttk.OptionMenu(root, insideValue, *fontList)
combobox1.grid(column='0', row='0')
fontStyle = insideValue.get()

buttonSave = ttk.Button(root)
buttonSave.configure(text='Apply')
buttonSave.grid(column='1', row='2', sticky='nw')
buttonSave.configure(command=saveSettings)

insideValueNum = tk.IntVar(root)
insideValueNum.set(14)

combobox2 = ttk.OptionMenu(root, insideValueNum, *fontSizes)
combobox2.grid(column='1', row='0')

fiveByFour = ttk.Radiobutton(root)
gridVar = tk.StringVar(value='54')
fiveByFour.configure(text='5x4', value='54', variable=gridVar)
fiveByFour.grid(column='0', row='3')
sixByFive = ttk.Radiobutton(root)
sixByFive.configure(text='6x5', value='65', variable=gridVar)
sixByFive.grid(column='1', row='3')

root.configure(height='600', width='800')
#root.configure(height='600', width='800')
    # Main widget
    
root.mainloop()






