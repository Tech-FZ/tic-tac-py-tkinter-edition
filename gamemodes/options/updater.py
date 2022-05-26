import platform
import webbrowser
import requests
from tkinter import *

def checkForUpdates(ticTacPyApp, manually):
    try:
        # For stable releases, commented out here, DO NOT REMOVE
        #url = "https://raw.githubusercontent.com/Tech-FZ/tic-tac-py-tkinter-edition/main/ttpupdatefile.tictacpy"

        # For Version 1.1.0 pre-releases
        url = "https://raw.githubusercontent.com/Tech-FZ/tic-tac-py-tkinter-edition/v1.1.0-workspace/ttpupdatefile.tictacpy"
        
        rq = requests.get(url, allow_redirects=True)
        newVer = open("ttpupdatefile.tictacpy", "wb+")
        newVer.write(rq.content)
        newVer.close()

        newVer = open("ttpupdatefile.tictacpy", "r+")
        newVerContent = newVer.readlines()
        newMajor = newVerContent[0].replace("/newest-major ", "")
        newMajor = newMajor.replace("\n", "")
        newMinor1 = newVerContent[1].replace("/newest-minor1 ", "")
        newMinor1 = newMinor1.replace("\n", "")
        newMinor2 = newVerContent[2].replace("/newest-minor2 ", "")
        newMinor2 = newMinor2.replace("\n", "")

        if int(newMajor) > ticTacPyApp.majorVer:
            updateAvailable(ticTacPyApp, newMajor, newMinor1, newMinor2)

        elif int(newMinor1) > ticTacPyApp.minorVer1:
            if int(newMajor) >= ticTacPyApp.majorVer:
                updateAvailable(ticTacPyApp, newMajor, newMinor1, newMinor2)

        elif int(newMinor2) > ticTacPyApp.minorVer2:
            if int(newMajor) >= ticTacPyApp.majorVer and int(newMinor1) >= ticTacPyApp.minorVer1:
                updateAvailable(ticTacPyApp, newMajor, newMinor1, newMinor2)

            else:
                if manually == True:
                    isNewestVer(ticTacPyApp)

        else:
            if manually == True:
                isNewestVer(ticTacPyApp)

        newVer.close()

    except:
        if manually == True:
            noInternetConnection(ticTacPyApp)

def updateAvailable(ticTacPyApp, newMajor, newMinor1, newMinor2):
    def prepUpdRedirect():
        updateRedirect()
        updater.destroy()

    updater = Toplevel()
    updater.title("Tic Tac Py Updater")
    updater.geometry()
    updater.resizable(width=0, height=0)

    if platform.system() == "Windows":
        updater.iconbitmap("ttpicon.ico")

    placeholder0 = Label(updater, text="", font=("Arial", 2))
    placeholder0.grid(row=0, column=0)

    placeholder1 = Label(updater, text="", font=("Arial", 2))
    placeholder1.grid(row=0, column=4)

    placeholder2 = Label(updater, text="", font=("Arial", 2))
    placeholder2.grid(row=5, column=4)

    header = Label(updater, text=ticTacPyApp.txtUpdateAvailable, font=("Arial", 16))
    header.grid(row=0, column=1, columnspan=3)

    currVer = Label(
        updater, 
        text=f"{ticTacPyApp.txtCurrentVer} {ticTacPyApp.majorVer}.{ticTacPyApp.minorVer1}.{ticTacPyApp.minorVer2}", 
        font=("Arial", 14)
        )

    currVer.grid(row=1, column=1, columnspan=3)

    newVer = Label(
        updater, 
        text=f"{ticTacPyApp.txtNewVer} {newMajor}.{newMinor1}.{newMinor2}", 
        font=("Arial", 14)
        )

    newVer.grid(row=2, column=1, columnspan=3)

    updateQuestion = Label(updater, text=ticTacPyApp.updateQuestion, font=("Arial", 14))
    updateQuestion.grid(row=3, column=1, columnspan=3)

    yesBtn = Button(updater, text=ticTacPyApp.yes, font=("Arial", 12))
    yesBtn["command"] = prepUpdRedirect
    yesBtn.grid(row=4, column=1)

    noBtn = Button(updater, text=ticTacPyApp.no, font=("Arial", 12))
    noBtn["command"] = updater.destroy
    noBtn.grid(row=4, column=3)

def updateRedirect():
    webbrowser.open("https://github.com/Tech-FZ/tic-tac-py-tkinter-edition/releases")

def isNewestVer(ticTacPyApp):
    updater = Toplevel()
    updater.title("Tic Tac Py Updater")
    updater.geometry()
    updater.resizable(width=0, height=0)

    if platform.system() == "Windows":
        updater.iconbitmap("ttpicon.ico")

    placeholder2 = Label(updater, text="", font=("Arial", 2))
    placeholder2.grid(row=2, column=2)

    header = Label(updater, text=ticTacPyApp.txtIsNewest, font=("Arial", 16))
    header.grid(row=0, column=0, columnspan=3)

    okBtn = Button(updater, text=ticTacPyApp.okay, font=("Arial", 12))
    okBtn["command"] = updater.destroy
    okBtn.grid(row=1, column=1)

def noInternetConnection(ticTacPyApp):
    updater = Toplevel()
    updater.title("Tic Tac Py Updater")
    updater.geometry()
    updater.resizable(width=0, height=0)

    if platform.system() == "Windows":
        updater.iconbitmap("ttpicon.ico")

    placeholder2 = Label(updater, text="", font=("Arial", 2))
    placeholder2.grid(row=2, column=2)

    header = Label(updater, text=ticTacPyApp.noInternet, font=("Arial", 16))
    header.grid(row=0, column=0, columnspan=3)

    okBtn = Button(updater, text=ticTacPyApp.okay, font=("Arial", 12))
    okBtn["command"] = updater.destroy
    okBtn.grid(row=1, column=1)