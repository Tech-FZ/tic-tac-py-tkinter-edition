from tkinter import *
import platform

def creditProgramming(ticTacPyApp):
    creditDevWin = Toplevel()
    creditDevWin.geometry()
    creditDevWin.resizable(height=0, width=0)
    creditDevWin.title(ticTacPyApp.creditTitle)
    
    if platform.system() == "Windows":
        creditDevWin.iconbitmap("ttpicon.ico")

    header = Label(creditDevWin, text=f"{ticTacPyApp.creditTxt} - {ticTacPyApp.creditDev}", font=("Arial", 16))
    header.pack()

    placeholder0 = Label(creditDevWin, text="", font=("Arial", 2))
    placeholder0.pack()

    contribs = Text(creditDevWin, height=4, width=45, font=("Arial", 8))
    contribs.insert(END, "Nicolas Lucien/Tech-FZ\n")
    contribs.config(state="disabled")
    contribs.pack()

    placeholder1 = Label(creditDevWin, text="", font=("Arial", 2))
    placeholder1.pack()

    closeBtn = Button(creditDevWin, text=ticTacPyApp.close, font=("Arial", 14))
    closeBtn["command"] = creditDevWin.destroy
    closeBtn.pack()

    placeholder2 = Label(creditDevWin, text="", font=("Arial", 2))
    placeholder2.pack()