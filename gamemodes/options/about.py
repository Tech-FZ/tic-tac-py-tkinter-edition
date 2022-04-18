from tkinter import *
import platform

def aboutBox(ticTacPyApp):
    aboutApp = Toplevel(ticTacPyApp.settingsMenu)
    aboutApp.geometry()
    aboutApp.resizable(width=0, height=0)
    aboutApp.title(ticTacPyApp.aboutTitleBar)

    if platform.system() == "Windows":
        aboutApp.iconbitmap("ttpicon.ico")

    ttp = Label(
        aboutApp,
        text=f"Tic Tac Py - Tkinter Edition, Version {ticTacPyApp.majorVer}.{ticTacPyApp.minorVer1}.{ticTacPyApp.minorVer2}",
        font=("Arial", 16)
    )
    
    ttp.pack()

    licenseLabel = Label(aboutApp, text="BSD 3-Clause License\n\nCopyright (c) 2021-2022, Tech-FZ and Tic Tac Py contributors\nAll rights reserved."
        "\n\nRedistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met:"
        "\n\n1. Redistributions of source code must retain the above copyright notice, this\nlist of conditions and the following disclaimer."
        "\n\n2. Redistributions in binary form must reproduce the above copyright notice,\nthis list of conditions and the following disclaimer in the documentation\nand/or other materials provided with the distribution."
        "\n\n3. Neither the name of the copyright holder nor the names of its\ncontributors may be used to endorse or promote products derived from\nthis software without specific prior written permission."
        '\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"'
        "\nAND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE"
        "\nIMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE"
        "\nDISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE"
        "\nFOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL"
        "\nDAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR"
        "\nSERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER"
        "\nCAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,"
        "\nOR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE"
        "\nOF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.", font=("Arial", 14))
    
    licenseLabel.pack()

    button = Button(aboutApp, text=ticTacPyApp.okay, font=("Arial", 14))
    button["command"] = aboutApp.destroy
    button.pack()

    placeholder = Label(aboutApp, text="", font=("Arial", 2))
    placeholder.pack()
