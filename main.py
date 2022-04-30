from gamemodes.pvp import *
from gamemodes.pvcom import *
from tkinter import *
from gamemodes.locales.localeManager import *
from gamemodes.settings import *
from gamemodes.options.updater import *
from themes.thememgr import *
import platform

class App:
    def __init__(self):
        # Version definition system for the upcoming updater
        self.majorVer = 1
        self.minorVer1 = 99
        self.minorVer2 = 2
        self.ttpVersionGroup = 1
        self.gamemode = 0
        self.lang = "not defined"

        # Text for main
        self.alphaWarning = "not defined"
        self.welcome = "not defined"
        self.gamemodeQuestion = "not defined"
        self.pvpText = "not defined"
        self.pvcomText = "not defined"
        self.settingTextForMain = "not defined"

        # Text for entire game
        self.okay = "not defined"
        self.fieldFilledWarning = "not defined"
        self.playAgainQuestion = "not defined"
        self.yes = "not defined"
        self.no = "not defined"
        self.tieText = "not defined"
        self.close = "Close"

        # Text for PvCom
        self.playerLostText = "not defined"
        self.playerWonText = "not defined"
        self.nonsenseTextPlaceholder = "not defined"
        self.pvcomTitleBar = "not defined"

        # Text for PvP
        self.playerOneWonText = "not defined"
        self.playerTwoWonText = "not defined"
        self.playerOneTurnText = "not defined"
        self.playerTwoTurnText = "not defined"
        self.pvpTitleBar = "not defined"

        # For settings
        self.settingsMenu = ""
        self.settingTitleBar = "not defined"
        self.settingQuestion = "not defined"
        self.buttonToLang = "not defined"
        self.buttonToAboutBox = "not defined"
        self.settingMenuExit = "not defined"
        self.default = "not defined"
        self.applyButtonText = "not defined"
        self.abortButtonText = "not defined"
        self.updateTxt = "Check for updates"
        self.creditTxt = "Credits"
        self.themeSetTxt = "Theme Settings"

        # For lang
        self.langText = "not defined"
        self.langNotFoundText = "not defined"
        self.languagesAvailable = []

        # Text for About Box
        self.aboutTitleBar = "not defined"
        self.licenseText = "not defined"
        self.licenseButton = "not defined"

        # Text for restart advise
        self.restartText = "not defined"

        # Text for difficulty
        self.difficultyTxt = "not defined"
        self.difficultyQuestion = "not defined"
        self.easyTxt = "not defined"
        self.hardTxt = "not defined"

        # Text for updater
        self.txtUpdateAvailable = "New update released!"
        self.txtCurrentVer = "Your version:"
        self.txtNewVer = "Newest version:"
        self.updateQuestion = "Do you want to be redirected to the GitHub page\nto download the newest version?"
        self.txtIsNewest = "You're running the latest version already!"
        self.noInternet = "TTP Updater failed to connect to the GitHub repository\nservers of the game.\nPlease check your internet connection\nand try again."

        # Text for credits
        self.creditTitle = "Tic Tac Py - Credits"
        self.creditDev = "Programming"
        self.creditArts = "Arts"
        self.creditTranslation = "Translation"

        # Preparing for hard KI
        self.gridCopy = []

        # Preparing theme loading
        self.themedir = "themes/default"
        self.themes = []

        # Text for theme settings
        self.themeAuthorMadeBy = "Made by:"
        self.themeLicenseTxt = "License:"
        self.themeForOlderVer = "WARNING: This theme has been made for an older version of Tic Tac Py."
        self.themeForNewerVer = "WARNING: This theme has been made for a newer version of Tic Tac Py."
        self.themeCompatibilityWarning = "You may still use this theme, but issues will likely occur."
        self.getThemeInfoTxt = "About this theme"

    def gamemodeCheck(self):
        if self.gamemode.get() == 1:
            playerVsPlayer(ticTacPyApp)
    
        elif self.gamemode.get() == 2:
            chooseDifficulty(ticTacPyApp)
        
        elif self.gamemode.get() == 3:
            settingSet(ticTacPyApp)
    
ticTacPyApp = App()

print(f"Tic Tac Py, Tkinter Edition, Version {ticTacPyApp.majorVer}.{ticTacPyApp.minorVer1}.{ticTacPyApp.minorVer2}")

root = Tk()

determineLang(ticTacPyApp)
scanForLanguages(ticTacPyApp)
checkForUpdates(ticTacPyApp, False)
themeInit(ticTacPyApp)
ticTacPyApp.languagesAvailable.append(ticTacPyApp.default)
root.title("Tic Tac Py Tkinter Edition")
root.geometry()
root.resizable(width=0, height=0)

if platform.system() == "Windows":
    root.iconbitmap("ttpicon.ico")

#warningSentence = Label(text=ticTacPyApp.alphaWarning)
#warningSentence.config(font=("Arial", 12))
#warningSentence.grid(row=0, column=0, rowspan=2)

label1 = Label(text=ticTacPyApp.welcome, font=("Arial", 16))
label1.grid(row=2, column=0)

question = Label(root, text=ticTacPyApp.gamemodeQuestion, font=("Arial", 16))
question.grid(row=3, column=0)

ticTacPyApp.gamemode = IntVar()
gamemode1 = Radiobutton(text=ticTacPyApp.pvpText, variable=ticTacPyApp.gamemode, value=1, font=("Arial", 12))
gamemode1.select()
gamemode1.grid(row=4, column=0)
gamemode2 = Radiobutton(text=ticTacPyApp.pvcomText, variable=ticTacPyApp.gamemode, value=2, font=("Arial", 12))
gamemode2.select()
gamemode2.grid(row=5, column=0)
gamemode3 = Radiobutton(text=ticTacPyApp.settingTextForMain, variable=ticTacPyApp.gamemode, value=3, font=("Arial", 12))
gamemode3.select()
gamemode3.grid(row=6, column=0)

button = Button(root, text=ticTacPyApp.okay, font=("Arial", 14))
button["command"] = ticTacPyApp.gamemodeCheck
button.grid(row=7, column=0)

placeholder = Label(root, text="", font=("Arial", 2))
placeholder.grid(row=8, column=0)

root.mainloop()