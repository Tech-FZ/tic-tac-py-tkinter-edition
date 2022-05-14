from tkinter import *
import platform

def creditArts(ticTacPyApp):
    creditArtsWin = Toplevel()
    creditArtsWin.geometry()
    creditArtsWin.resizable(height=0, width=0)
    creditArtsWin.title(ticTacPyApp.creditTitle)
    
    if platform.system() == "Windows":
        creditArtsWin.iconbitmap("ttpicon.ico")

    header = Label(creditArtsWin, text=f"{ticTacPyApp.creditTxt} - {ticTacPyApp.creditArts}", font=("Arial", 16))
    header.pack()

    placeholder0 = Label(creditArtsWin, text="", font=("Arial", 2))
    placeholder0.pack()

    contribs = Text(creditArtsWin, height=4, width=45, font=("Arial", 8))
    contribs.insert(END, "Nicolas Lucien/Tech-FZ\n")
    contribs.config(state="disabled")
    contribs.pack()

    placeholder1 = Label(creditArtsWin, text="", font=("Arial", 2))
    placeholder1.pack()

    closeBtn = Button(creditArtsWin, text=ticTacPyApp.close, font=("Arial", 14))
    closeBtn["command"] = creditArtsWin.destroy
    closeBtn.pack()

    placeholder2 = Label(creditArtsWin, text="", font=("Arial", 2))
    placeholder2.pack()