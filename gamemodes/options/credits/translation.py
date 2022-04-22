from tkinter import *
import platform

def creditTranslation(ticTacPyApp):
    creditLangWin = Toplevel()
    creditLangWin.geometry()
    creditLangWin.resizable(height=0, width=0)
    creditLangWin.title(ticTacPyApp.creditTitle)
    
    if platform.system() == "Windows":
        creditLangWin.iconbitmap("ttpicon.ico")

    header = Label(creditLangWin, text=f"{ticTacPyApp.creditTxt} - {ticTacPyApp.creditArts}", font=("Arial", 16))
    header.pack()

    placeholder0 = Label(creditLangWin, text="", font=("Arial", 2))
    placeholder0.pack()

    contribs = Text(creditLangWin, height=4, width=45, font=("Arial", 8))
    contribs.insert(END, "English Translation\n")
    contribs.insert(END, "Nicolas Lucien/Tech-FZ\n\n")

    contribs.insert(END, "German Translation\n")
    contribs.insert(END, "Nicolas Lucien/Tech-FZ\n\n")

    contribs.config(state="disabled")
    contribs.pack()

    placeholder1 = Label(creditLangWin, text="", font=("Arial", 2))
    placeholder1.pack()

    closeBtn = Button(creditLangWin, text=ticTacPyApp.close, font=("Arial", 14))
    closeBtn["command"] = creditLangWin.destroy
    closeBtn.pack()

    placeholder2 = Label(creditLangWin, text="", font=("Arial", 2))
    placeholder2.pack()