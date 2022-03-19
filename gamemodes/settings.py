from tkinter import *
import gamemodes.options.languageSettings
import gamemodes.options.about
from gamemodes.options.updater import *

def settingSet(ticTacPyApp):
    def languageSettings():
        gamemodes.options.languageSettings.langSettingMenu(ticTacPyApp)

    
    def about():
        gamemodes.options.about.aboutBox(ticTacPyApp)

    def checkUpd():
        checkForUpdates(ticTacPyApp, True)
        

    ticTacPyApp.settingsMenu = Toplevel()
    ticTacPyApp.settingsMenu.geometry()
    ticTacPyApp.settingsMenu.resizable(width=0, height=0)
    ticTacPyApp.settingsMenu.title(ticTacPyApp.settingTitleBar)

    question = Label(ticTacPyApp.settingsMenu, text=ticTacPyApp.settingQuestion, font=("Arial", 16))
    question.grid(row=0, column=0, columnspan=7)

    placeholder0 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder0.grid(row=1, column=0, sticky=W)

    buttonForLangSettings = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.buttonToLang, font=("Arial", 14))
    buttonForLangSettings["command"] = languageSettings
    buttonForLangSettings.grid(row=1, column=1, sticky=W)

    placeholder1 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder1.grid(row=1, column=2, sticky=W)

    buttonForAboutBox = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.buttonToAboutBox, font=("Arial", 14))
    buttonForAboutBox["command"] = about
    buttonForAboutBox.grid(row=1, column=3, sticky=W)

    placeholder2 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder2.grid(row=1, column=4, sticky=W)

    buttonForExit = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.settingMenuExit, font=("Arial", 14))
    buttonForExit["command"] = ticTacPyApp.settingsMenu.destroy
    buttonForExit.grid(row=1, column=5, sticky=W)

    placeholder3 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder3.grid(row=1, column=6, sticky=W)

    buttonForUpdater = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.updateTxt, font=("Arial", 14))
    buttonForUpdater["command"] = checkUpd
    buttonForUpdater.grid(row=3, column=3, sticky=W)

    placeholder4 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder4.grid(row=2, column=0, sticky=W)

    placeholder4 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder4.grid(row=4, column=0, sticky=W)