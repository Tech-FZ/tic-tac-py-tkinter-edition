import os

def themeInit(ticTacPyApp):
    themelist = os.listdir(os.path.join("themes"))
    i = 0

    while i < len(themelist):
        if themelist[i] == "thememgr.py":
            themelist.remove(themelist[i])

        else:
            try:
                themetest = os.listdir(os.path.join(f"themes/{themelist[i]}"))

                j = 0

                while j < len(themetest):
                    if themetest[j] == "themeinfo.tictacpy":
                        ticTacPyApp.themes.append(themelist[i])
                        break

                    j += 1

            except:
                pass

        i += 1