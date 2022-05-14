from tkinter import *
import platform
from gamemodes.options.credits.programming import *
from gamemodes.options.credits.arts import *
from gamemodes.options.credits.translation import *

def creditMenu(ticTacPyApp):
    def programmingBtnFunc():
        creditProgramming(ticTacPyApp)

    def artBtnFunc():
        creditArts(ticTacPyApp)

    def langBtnFunc():
        creditTranslation(ticTacPyApp)

    creditMenuWin = Toplevel()
    creditMenuWin.geometry()
    creditMenuWin.resizable(height=0, width=0)
    creditMenuWin.title(ticTacPyApp.creditTitle)
    
    if platform.system() == "Windows":
        creditMenuWin.iconbitmap("ttpicon.ico")

    placeholder0 = Label(creditMenuWin, text="", font=("Arial", 2))
    placeholder0.grid(row=0, column=0)

    placeholder1 = Label(creditMenuWin, text="", font=("Arial", 2))
    placeholder1.grid(row=2, column=2)

    placeholder2 = Label(creditMenuWin, text="", font=("Arial", 2))
    placeholder2.grid(row=2, column=4)

    placeholder4 = Label(creditMenuWin, text="", font=("Arial", 2))
    placeholder4.grid(row=4, column=4)

    devBtn = Button(creditMenuWin, text=ticTacPyApp.creditDev, font=("Arial", 14))
    devBtn["command"] = programmingBtnFunc
    devBtn.grid(row=1, column=1)

    artsBtn = Button(creditMenuWin, text=ticTacPyApp.creditArts, font=("Arial", 14))
    artsBtn["command"] = artBtnFunc
    artsBtn.grid(row=1, column=3)

    translateBtn = Button(creditMenuWin, text=ticTacPyApp.creditTranslation, font=("Arial", 14))
    translateBtn["command"] = langBtnFunc
    translateBtn.grid(row=3, column=1)

    closeBtn = Button(creditMenuWin, text=ticTacPyApp.close, font=("Arial", 14))
    closeBtn["command"] = creditMenuWin.destroy
    closeBtn.grid(row=3, column=3)