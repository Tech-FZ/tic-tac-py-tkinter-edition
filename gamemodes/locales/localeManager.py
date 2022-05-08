import locale
import os

def scanForLanguages(ticTacPyApp):
    languagesFound = os.listdir(os.path.join("gamemodes/locales/languages"))
    
    for languages in languagesFound:
        if languages == "en_GB.py":
            ticTacPyApp.languagesAvailable.append("English (United Kingdom)")
        
        elif languages == "en_US.py":
            ticTacPyApp.languagesAvailable.append("English (United States)")
        
        elif languages == "en_CA.py":
            ticTacPyApp.languagesAvailable.append("English (Canada)")
        
        elif languages == "en_AU.py":
            ticTacPyApp.languagesAvailable.append("English (Australia)")
        
        elif languages == "de_DE.py":
            ticTacPyApp.languagesAvailable.append("Deutsch (Deutschland)")
        
        elif languages == "de_AT.py":
            ticTacPyApp.languagesAvailable.append("Deitsch (Österreich)")
        
        elif languages == "de_CH.py":
            ticTacPyApp.languagesAvailable.append("Switzerdütsch")
        
        elif languages == "ja_JP.py":
            ticTacPyApp.languagesAvailable.append("日本語")

        elif languages == "fr_FR.py":
            ticTacPyApp.languagesAvailable.append("Français (France)")

        elif languages == "fr_CA.py":
            ticTacPyApp.languagesAvailable.append("Français (Canada)")

        elif languages == "uk_UA.py":
            ticTacPyApp.languagesAvailable.append("українська")

def determineLang(ticTacPyApp):
    def englishUS(ticTacPyApp):
        import gamemodes.locales.languages.en_US
        gamemodes.locales.languages.en_US.setLanguage(ticTacPyApp)
    
    def englishGB(ticTacPyApp):
        try:
            import gamemodes.locales.languages.en_GB
            gamemodes.locales.languages.en_GB.setLanguage(ticTacPyApp)

        except ImportError:
            englishUS(ticTacPyApp)
    
    def englishCA(ticTacPyApp):
        try:
            import gamemodes.locales.languages.en_CA
            gamemodes.locales.languages.en_CA.setLanguage(ticTacPyApp)

        except ImportError:
            englishCA(ticTacPyApp)
    
    def englishAU(ticTacPyApp):
        try:
            import gamemodes.locales.languages.en_AU
            gamemodes.locales.languages.en_AU.setLanguage(ticTacPyApp)

        except ImportError:
            englishUS(ticTacPyApp)
    
    def germanDE(ticTacPyApp):
        try:
            import gamemodes.locales.languages.de_DE
            gamemodes.locales.languages.de_DE.setLanguage(ticTacPyApp)

        except ImportError:
            englishUS(ticTacPyApp)
    
    def germanAT(ticTacPyApp):
        try:
            import gamemodes.locales.languages.de_AT
            gamemodes.locales.languages.de_AT.setLanguage(ticTacPyApp)

        except ImportError:
            germanDE(ticTacPyApp)
    
    def germanCH(ticTacPyApp):
        try:
            import gamemodes.locales.languages.de_CH
            gamemodes.locales.languages.de_CH.setLanguage(ticTacPyApp)

        except ImportError:
            germanDE(ticTacPyApp)
        
    def japanese(ticTacPyApp):
        try:
            import gamemodes.locales.languages.ja_JP
            gamemodes.locales.languages.ja_JP.setLanguage(ticTacPyApp)

        except ImportError:
            englishUS(ticTacPyApp)

    def frenchFR(ticTacPyApp):
        try:
            import gamemodes.locales.languages.fr_FR
            gamemodes.locales.languages.fr_FR.setLanguage(ticTacPyApp)

        except ImportError:
            englishUS(ticTacPyApp)

    def frenchCA(ticTacPyApp):
        try:
            import gamemodes.locales.languages.fr_CA
            gamemodes.locales.languages.fr_CA.setLanguage(ticTacPyApp)

        except ImportError:
            frenchFR(ticTacPyApp)

    def ukrainian(ticTacPyApp):
        try:
            import gamemodes.locales.languages.uk_UA
            gamemodes.locales.languages.uk_UA.setLanguage(ticTacPyApp)

        except ImportError:
            frenchFR(ticTacPyApp)

    # Detecting system language
    locTuple = locale.getlocale()
    langofSystem = locTuple[0]

    options = open("gamemodes/options/options.tictacpy", "r")
    content = options.readlines()
    lang = content[0]
    options.close()

    if lang == "/lang en_GB":
        englishGB(ticTacPyApp)
    
    elif lang == "/lang en_US":
        englishUS(ticTacPyApp)
    
    elif lang == "/lang en_CA":
        englishCA(ticTacPyApp)
    
    elif lang == "/lang en_AU":
        englishAU(ticTacPyApp)
    
    elif lang == "/lang de_DE":
        germanDE(ticTacPyApp)
    
    elif lang == "/lang de_AT":
        germanAT(ticTacPyApp)
    
    elif lang == "/lang de_CH":
        germanCH(ticTacPyApp)
    
    elif lang == "/lang ja_JP":
        japanese(ticTacPyApp)

    elif lang == "/lang fr_FR":
        frenchFR(ticTacPyApp)

    elif lang == "/lang fr_CA":
        frenchCA(ticTacPyApp)

    elif lang == "/lang uk_UA":
        ukrainian(ticTacPyApp)

    else:
        # British English
        if langofSystem == "en_GB":
            englishGB(ticTacPyApp)
        
        # Canadian English
        elif langofSystem == "en_CA":
            englishCA(ticTacPyApp)
        
        # Australian English
        elif langofSystem == "en_AU":
            englishAU(ticTacPyApp)
    
        # German German/Deutsches Deutsch
        elif langofSystem == "de_DE":
            germanDE(ticTacPyApp)
        
        # Austrian German/Österreichisches Deutsch
        elif langofSystem == "de_AT":
            germanAT(ticTacPyApp)
        
        # Swiss German/Switzerdütsch
        elif langofSystem == "de_CH":
            germanCH(ticTacPyApp)
        
        elif langofSystem == "ja_JP":
            japanese(ticTacPyApp)

        elif langofSystem == "fr_FR":
            frenchFR(ticTacPyApp)

        elif langofSystem == "fr_CA":
            frenchCA(ticTacPyApp)

        elif langofSystem == "uk_UA":
            ukrainian(ticTacPyApp)

        # American English (if primary language not working or being American English)
        else:
            englishUS(ticTacPyApp)