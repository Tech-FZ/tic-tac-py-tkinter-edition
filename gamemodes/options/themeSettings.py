from tkinter import *
from themes.thememgr import *
import platform
import os

def langSettingMenu(ticTacPyApp):
    def applyFunction():
        options = open("gamemodes/options/options.tictacpy", "r")
        content = options.readlines()
        theme = content[1]
        options.close()

        #options = open("gamemodes/options/options.tictacpy", "w")
        
        
        restartAdvise = Toplevel(languageSettingsMenu)
        restartAdvise.geometry()
        restartAdvise.title()
        restartAdvise.resizable(width=0, height=0)

        if platform.system() == "Windows":
            restartAdvise.iconbitmap("ttpicon.ico")

        restartLabel = Label(restartAdvise, text=ticTacPyApp.restartText, font=("Arial", 16))
        restartLabel.grid(row=0, column=0, columnspan=3)

        button = Button(restartAdvise, text=ticTacPyApp.okay, font=("Arial", 14))
        button["command"] = languageSettingsMenu.destroy
        button.grid(row=1, column=1)

        placeholder2 = Label(restartAdvise, text="", font=("Arial", 2))
        placeholder2.grid(row=2, column=0)

    themelist = []

    languageSettingsMenu = Toplevel(ticTacPyApp.settingsMenu)
    languageSettingsMenu.geometry()
    languageSettingsMenu.title(ticTacPyApp.settingTitleBar)
    languageSettingsMenu.resizable(width=0, height=0)

    if platform.system() == "Windows":
        languageSettingsMenu.iconbitmap("ttpicon.ico")

    languageLabel = Label(languageSettingsMenu, text=ticTacPyApp.langText, font=("Arial", 16))
    languageLabel.pack()

    languageSelector = Listbox(languageSettingsMenu)
    languageSelector.pack(side=LEFT, fill=BOTH)

    scrollbar = Scrollbar(languageSettingsMenu)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    for theme in ticTacPyApp.themes:
        try:
            themeDefList = []
            themeForVer = 0
            themeName = ""
            themeDesc = ""
            themeAuthor = ""
            themeCopyright = ""

            themeDef = open(f"themes/{theme}/themeinfo.tictacpy", "r")
            themeDefContent = themeDef.readlines()

            for line in themeDefContent:
                line = line.replace("\n", "")

                if line.startswith("/for-ttp-ver-code"):
                    tempVar = line.replace("/for-ttp-ver-code ", "")
                    themeForVer = int(tempVar)

                elif line.startswith("/theme-name"):
                    tempVar = line.replace("/theme-name \"", "")
                    themeName = tempVar.replace("\"", "")

                elif line.startswith("/theme-description"):
                    tempVar = line.replace("/theme-description \"", "")
                    themeDesc = tempVar.replace("\"", "")

                elif line.startswith("/theme-author"):
                    tempVar = line.replace("/theme-author \"", "")
                    themeAuthor = tempVar.replace("\"", "")

                elif line.startswith("/theme-copyright"):
                    tempVar = line.replace("/theme-copyright \"", "")
                    themeCopyright = tempVar.replace("\"", "")

            themeDefList = [theme, themeForVer, themeName, themeDesc, themeAuthor, themeCopyright]
            themelist.append(themeDefList)
            languageSelector.insert(END, themeDefList[2])
        
        except:
            pass
    
    languageSelector.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=languageSelector.yview)

    notFoundLabel = Label(languageSettingsMenu, text=ticTacPyApp.langNotFoundText, font=("Arial", 16))
    notFoundLabel.pack()

    okButton = Button(languageSettingsMenu, text=ticTacPyApp.okay, font=("Arial", 14))
    okButton["command"] = applyFunction
    okButton.pack()

    abortButton = Button(languageSettingsMenu, text=ticTacPyApp.abortButtonText, font=("Arial", 14))
    abortButton["command"] = languageSettingsMenu.destroy
    abortButton.pack()

    placeholder1 = Label(languageSettingsMenu, text=" ", font=("Arial", 2))
    placeholder1.pack()