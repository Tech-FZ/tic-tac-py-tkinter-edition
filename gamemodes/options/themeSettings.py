from tkinter import *
from themes.thememgr import *
import platform

def langSettingMenu(ticTacPyApp):
    def themeInfoPrep():
        themeSelected = languageSelector.selection_get()
        i = 0

        while i < len(themelist):
            if themelist[i][2] == themeSelected:
                count = i
                break

            i += 1

        themeInfo(themelist[count])

    def themeInfo(themeToGetMoreInfoAbout):
        creditArtsWin = Toplevel()
        creditArtsWin.geometry()
        creditArtsWin.resizable(height=0, width=0)
        creditArtsWin.title(ticTacPyApp.settingTitleBar)
    
        if platform.system() == "Windows":
            creditArtsWin.iconbitmap("ttpicon.ico")

        header = Label(creditArtsWin, text=f"{ticTacPyApp.getThemeInfoTxt}", font=("Arial", 16))
        header.pack()

        placeholder0 = Label(creditArtsWin, text="", font=("Arial", 2))
        placeholder0.pack()

        themeInfoBox = Text(creditArtsWin, height=4, width=45, font=("Arial", 8))
        themeInfoBox.insert(END, f"{themeToGetMoreInfoAbout[2]}\n")
        themeInfoBox.insert(END, f"{ticTacPyApp.themeAuthorMadeBy} {themeToGetMoreInfoAbout[4]}\n")
        themeInfoBox.insert(END, f"{themeToGetMoreInfoAbout[3]}\n")
        themeInfoBox.insert(END, f"{ticTacPyApp.themeLicenseTxt} {themeToGetMoreInfoAbout[5]}\n")

        if int(themeToGetMoreInfoAbout[1]) != ticTacPyApp.ttpVersionGroup:
            if int(themeToGetMoreInfoAbout[1]) < ticTacPyApp.ttpVersionGroup:
                themeInfoBox.insert(END, f"\n{ticTacPyApp.themeForOlderVer}\n")

            elif int(themeToGetMoreInfoAbout[1]) > ticTacPyApp.ttpVersionGroup:
                themeInfoBox.insert(END, f"\n{ticTacPyApp.themeForNewerVer}\n")

            themeInfoBox.insert(END, f"\n{ticTacPyApp.themeCompatibilityWarning}\n")

        themeInfoBox.config(state="disabled")
        themeInfoBox.pack()

        placeholder1 = Label(creditArtsWin, text="", font=("Arial", 2))
        placeholder1.pack()

        closeBtn = Button(creditArtsWin, text=ticTacPyApp.close, font=("Arial", 14))
        closeBtn["command"] = creditArtsWin.destroy
        closeBtn.pack()

        placeholder2 = Label(creditArtsWin, text="", font=("Arial", 2))
        placeholder2.pack()

    def prepareApplyOne():
        themeSelected = languageSelector.selection_get()
        i = 0

        while i < len(themelist):
            if themelist[i][2] == themeSelected:
                count = i
                break

            i += 1

        prepareApplyTwo(count)

    def prepareApplyTwo(index):
        applyFunction(themelist[index][0])

    def applyFunction(themeToSet):
        options = open("gamemodes/options/options.tictacpy", "r")
        content = options.readlines()
        themeReplaced = content[1]
        options.close()

        ticTacPyApp.themedir = f"themes/{themeToSet}"

        options = open("gamemodes/options/options.tictacpy", "w")
        for line in content:
            options.write(line.replace(themeReplaced, f"/theme \"{ticTacPyApp.themedir}\""))

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

    themelist = []

    languageSettingsMenu = Toplevel(ticTacPyApp.settingsMenu)
    languageSettingsMenu.geometry()
    languageSettingsMenu.title(ticTacPyApp.settingTitleBar)
    languageSettingsMenu.resizable(width=0, height=0)

    if platform.system() == "Windows":
        languageSettingsMenu.iconbitmap("ttpicon.ico")

    languageLabel = Label(languageSettingsMenu, text=ticTacPyApp.themeSetTxt, font=("Arial", 16))
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

    infoButton = Button(languageSettingsMenu, text=ticTacPyApp.getThemeInfoTxt, font=("Arial", 14))
    infoButton["command"] = themeInfoPrep
    infoButton.pack()

    okButton = Button(languageSettingsMenu, text=ticTacPyApp.okay, font=("Arial", 14))
    okButton["command"] = prepareApplyOne
    okButton.pack()

    abortButton = Button(languageSettingsMenu, text=ticTacPyApp.abortButtonText, font=("Arial", 14))
    abortButton["command"] = languageSettingsMenu.destroy
    abortButton.pack()

    placeholder1 = Label(languageSettingsMenu, text=" ", font=("Arial", 2))
    placeholder1.pack()