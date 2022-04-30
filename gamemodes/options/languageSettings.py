from tkinter import *
from gamemodes.locales.localeManager import *
import platform

def langSettingMenu(ticTacPyApp):
    def applyFunction():
        options = open("gamemodes/options/options.tictacpy", "r")
        content = options.readlines()
        lang = content[0]
        options.close()

        options = open("gamemodes/options/options.tictacpy", "w")
        for line in content:
            if languageSelector.selection_get() == "English (United States)":
                options.write(line.replace(lang, "/lang en_US"))
            
            elif languageSelector.selection_get() == "English (United Kingdom)":
                options.write(line.replace(lang, "/lang en_GB"))
            
            elif languageSelector.selection_get() == "English (Australia)":
                options.write(line.replace(lang, "/lang en_AU"))
            
            elif languageSelector.selection_get() == "English (Canada)":
                options.write(line.replace(lang, "/lang en_CA"))
            
            elif languageSelector.selection_get() == "Deutsch (Deutschland)":
                options.write(line.replace(lang, "/lang de_DE"))
            
            elif languageSelector.selection_get() == "Deutsch (Österreich)":
                options.write(line.replace(lang, "/lang de_AT"))

            elif languageSelector.selection_get() == "Switzerdütsch":
                options.write(line.replace(lang, "/lang de_CH"))
            
            elif languageSelector.selection_get() == "日本語":
                options.write(line.replace(lang, "/lang ja_JP"))
            
            elif languageSelector.selection_get() == ticTacPyApp.default:
                options.write(line.replace(lang, "/lang std"))

        options.close()
        
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

    for languages in ticTacPyApp.languagesAvailable:
        languageSelector.insert(END, languages)
    
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