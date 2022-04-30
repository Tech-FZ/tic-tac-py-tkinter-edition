from tkinter import *
import gamemodes.options.languageSettings
import gamemodes.options.about
from gamemodes.options.updater import *
from gamemodes.options.credits.menu import *
import gamemodes.options.themeSettings
import platform

def settingSet(ticTacPyApp):
    def languageSettings():
        gamemodes.options.languageSettings.langSettingMenu(ticTacPyApp)

    def themeSettings():
        gamemodes.options.themeSettings.langSettingMenu(ticTacPyApp)
    
    def about():
        gamemodes.options.about.aboutBox(ticTacPyApp)

    def checkUpd():
        checkForUpdates(ticTacPyApp, True)
        
    def creditMenuOpen():
        creditMenu(ticTacPyApp)

    ticTacPyApp.settingsMenu = Toplevel()
    ticTacPyApp.settingsMenu.geometry()
    ticTacPyApp.settingsMenu.resizable(width=0, height=0)
    ticTacPyApp.settingsMenu.title(ticTacPyApp.settingTitleBar)

    if platform.system() == "Windows":
        ticTacPyApp.settingsMenu.iconbitmap("ttpicon.ico")

    question = Label(ticTacPyApp.settingsMenu, text=ticTacPyApp.settingQuestion, font=("Arial", 16))
    question.grid(row=0, column=0, columnspan=7)

    placeholder0 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder0.grid(row=1, column=0)

    buttonForLangSettings = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.buttonToLang, font=("Arial", 14))
    buttonForLangSettings["command"] = languageSettings
    buttonForLangSettings.grid(row=1, column=1)

    placeholder1 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder1.grid(row=1, column=2)

    buttonForAboutBox = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.buttonToAboutBox, font=("Arial", 14))
    buttonForAboutBox["command"] = about
    buttonForAboutBox.grid(row=1, column=3)

    placeholder2 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder2.grid(row=1, column=4)

    buttonForExit = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.settingMenuExit, font=("Arial", 14))
    buttonForExit["command"] = ticTacPyApp.settingsMenu.destroy
    buttonForExit.grid(row=1, column=5)

    placeholder3 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder3.grid(row=1, column=6)

    buttonForUpdater = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.updateTxt, font=("Arial", 14))
    buttonForUpdater["command"] = checkUpd
    buttonForUpdater.grid(row=3, column=1)

    buttonForThemes = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.themeSetTxt, font=("Arial", 14))
    buttonForThemes["command"] = themeSettings
    buttonForThemes.grid(row=3, column=3)

    buttonForCredits = Button(ticTacPyApp.settingsMenu, text=ticTacPyApp.creditTxt, font=("Arial", 14))
    buttonForCredits["command"] = creditMenuOpen
    buttonForCredits.grid(row=3, column=5)

    placeholder4 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder4.grid(row=2, column=0)

    placeholder4 = Label(ticTacPyApp.settingsMenu, text="", font=("Arial", 2))
    placeholder4.grid(row=4, column=0)