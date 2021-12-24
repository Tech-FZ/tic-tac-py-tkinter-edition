from tkinter import *
import gamemodes.comDifficulty.easy
import gamemodes.comDifficulty.hard

def chooseDifficulty(ticTacPyApp):
    def easyChosen():
        gamemodes.comDifficulty.easy.playerVsComputer(ticTacPyApp)
    
    def hardChosen():
        gamemodes.comDifficulty.hard.playerVsComputer(ticTacPyApp)

    difficultyWindow = Toplevel()
    difficultyWindow.title(ticTacPyApp.difficultyTxt)
    difficultyWindow.geometry()
    difficultyWindow.resizable(width=0, height=0)

    difficultyQuestionLabel = Label(difficultyWindow, text=ticTacPyApp.difficultyQuestion, font=("Arial", 16))
    difficultyQuestionLabel.pack()

    easyButton = Button(difficultyWindow, text=ticTacPyApp.easyTxt, font=("Arial", 12))
    easyButton["command"] = easyChosen
    easyButton.pack()

    placeholder0 = Label(difficultyWindow, text="", font=("Arial", 2))
    placeholder0.pack()

    hardButton = Button(difficultyWindow, text=ticTacPyApp.hardTxt, font=("Arial", 12))
    hardButton["command"] = hardChosen
    hardButton.pack()

    placeholder2 = Label(difficultyWindow, text="", font=("Arial", 2))
    placeholder2.pack()

    cancelButton = Button(difficultyWindow, text=ticTacPyApp.abortButtonText, font=("Arial", 12))
    cancelButton["command"] = difficultyWindow.destroy
    cancelButton.pack()

    placeholder1 = Label(difficultyWindow, text="", font=("Arial", 2))
    placeholder1.pack()