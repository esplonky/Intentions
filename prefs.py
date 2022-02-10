import tkinter as tk
import intentCommands
import main
from CONFIG import *
import asyncio

fontList = intentCommands.getListOfFonts()
root = tk.Tk()
root.title("Preferences")
root.geometry("600x800")
#valueInside = tk.StringVar(root)
#valueInside.set("Calibri")
#fontValue = valueInside.get()
#optionsList = tk.OptionMenu(root, valueInside, *fontList)
#optionsList.after(0, writeToFile('CONFIG.py', fontValue))
#optionsList.pack()


#root.mainloop()


import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "prefsApp.ui"

async def mainLoop():
    main.mainLoop()

def saveSettings():
    fontVal = insideValue.get()
    prefsFile = open("CONFIG.py", 'w')
    prefsFile.write("FONT=" + "'" + fontVal + "'" + '\n')
    prefsFile.close()

root = tk.Tk()
fieldCsvLocation = ttk.Entry(root)
fieldCsvLocation.grid(column='0', row='1', sticky='nw')
buttonBrowse = ttk.Button(root)
buttonBrowse.configure(text='Browse...')
buttonBrowse.grid(column='1', row='1', sticky='nw')
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


    #combobox2 = ttk.OptionMenu()
        #combobox2.grid(column='1', row='0')
root.configure(height='600', width='800')
    # Main widget
    
root.mainloop()






