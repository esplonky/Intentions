import tkinter as tk
import intentCommands
import main


def writeToFile(fileName, fontStyle):
    prefsFile = open(fileName, 'w')
    prefsFile.write("FONT=" + "'" + fontStyle + "'" + '\n')
    prefsFile.close()

fontList = intentCommands.getListOfFonts()
root = tk.Tk()
root.title("Preferences")
root.geometry("600x800")
valueInside = tk.StringVar(root)
valueInside.set("Calibri")
fontValue = valueInside.get()
optionsList = tk.OptionMenu(root, valueInside, *fontList)
optionsList.after(0, writeToFile('CONFIG.py', fontValue))
optionsList.pack()


root.mainloop()
