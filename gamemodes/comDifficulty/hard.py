import gamemodes.assets.turnCounter
from random import randint
from tkinter import *

# Player is O, Computer is X.

def playerVsComputer(ticTacPyApp):
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def fieldFilled():
        notice = Toplevel(gamepvcom)
        notice.geometry()
        notice.resizable(width=0, height=0)
        notice.iconbitmap("ttpicon.ico")

        noticeText = Label(notice, text=ticTacPyApp.fieldFilledWarning, font=("Arial", 16))
        noticeText.pack()

        noticeButton = Button(notice, text=ticTacPyApp.okay, font=("Arial", 12))
        noticeButton["command"] = notice.destroy
        noticeButton.pack()

        placeholder7 = Label(notice, text="", font=("Arial", 2))
        placeholder7.pack()

    def playerWon():
        def effectOfYes():
            playerOnFirstPlace.destroy()
            wannaPlayMore()
        
        # Resetting the turns
        gamemodes.assets.turnCounter.playerOne = 0
        gamemodes.assets.turnCounter.playerTwo = 0

        playerOnFirstPlace = Toplevel(gamepvcom)
        playerOnFirstPlace.geometry()
        playerOnFirstPlace.resizable(width=0, height=0)
        playerOnFirstPlace.iconbitmap("ttpicon.ico")

        winnerText = Label(playerOnFirstPlace, text=f"{ticTacPyApp.playerWonText}\n{ticTacPyApp.playAgainQuestion}", font=("Arial", 16))
        winnerText.grid(row=0, column=0, columnspan=3)

        yesButton = Button(playerOnFirstPlace, text=ticTacPyApp.yes, font=("Arial", 12))
        yesButton["command"] = effectOfYes
        yesButton.grid(row=1, column=0)

        noButton = Button(playerOnFirstPlace, text=ticTacPyApp.no, font=("Arial", 12))
        noButton["command"] = doneWithPlaying
        noButton.grid(row=1, column=2)

        placeholder7 = Label(playerOnFirstPlace, text="", font=("Arial", 2))
        placeholder7.grid(row=2)
    
    def playerLost():
        def effectOfYes():
            playerOnSecondPlace.destroy()
            wannaPlayMore()

        # Resetting the turns
        gamemodes.assets.turnCounter.playerOne = 0
        gamemodes.assets.turnCounter.playerTwo = 0

        playerOnSecondPlace = Toplevel(gamepvcom)
        playerOnSecondPlace.geometry()
        playerOnSecondPlace.resizable(width=0, height=0)
        playerOnSecondPlace.iconbitmap("ttpicon.ico")

        loserText = Label(playerOnSecondPlace, text=f"{ticTacPyApp.playerLostText}\n{ticTacPyApp.playAgainQuestion}", font=("Arial", 16))
        loserText.grid(row=0, column=0, columnspan=3)

        yesButton = Button(playerOnSecondPlace, text=ticTacPyApp.yes, font=("Arial", 12))
        yesButton["command"] = effectOfYes
        yesButton.grid(row=1, column=0)

        noButton = Button(playerOnSecondPlace, text=ticTacPyApp.no, font=("Arial", 12))
        noButton["command"] = doneWithPlaying
        noButton.grid(row=1, column=2)

        placeholder7 = Label(playerOnSecondPlace, text="", font=("Arial", 2))
        placeholder7.grid(row=2)
    
    def nobodyWon():
        def effectOfYes():
            playerEqual.destroy()
            wannaPlayMore()

        # Resetting the turns
        gamemodes.assets.turnCounter.playerOne = 0
        gamemodes.assets.turnCounter.playerTwo = 0

        playerEqual = Toplevel(gamepvcom)
        playerEqual.geometry()
        playerEqual.resizable(width=0, height=0)
        playerEqual.iconbitmap("ttpicon.ico")

        equalText = Label(playerEqual, text=f"{ticTacPyApp.tieText}\n{ticTacPyApp.playAgainQuestion}", font=("Arial", 16))
        equalText.grid(row=0, column=0, columnspan=3)

        yesButton = Button(playerEqual, text=ticTacPyApp.yes, font=("Arial", 12))
        yesButton["command"] = effectOfYes
        yesButton.grid(row=1, column=0)

        noButton = Button(playerEqual, text=ticTacPyApp.no, font=("Arial", 12))
        noButton["command"] = doneWithPlaying
        noButton.grid(row=1, column=2)
        
        placeholder7 = Label(playerEqual, text="", font=("Arial", 2))
        placeholder7.grid(row=2)

    def doneWithPlaying():
        gamepvcom.destroy()

        # New code
        field[0][0] = " "
        field[0][1] = " "
        field[0][2] = " "
        field[1][0] = " "
        field[1][1] = " "
        field[1][2] = " "
        field[2][0] = " "
        field[2][1] = " "
        field[2][2] = " "
    
    def wannaPlayMore():
        # New code
        field[0][0] = " "
        field[0][1] = " "
        field[0][2] = " "
        field[1][0] = " "
        field[1][1] = " "
        field[1][2] = " "
        field[2][0] = " "
        field[2][1] = " "
        field[2][2] = " "

        # Hiding player marks
        buttonForCellZeroP.grid_forget()
        buttonForCellOneP.grid_forget()
        buttonForCellTwoP.grid_forget()
        buttonForCellThreeP.grid_forget()
        buttonForCellFourP.grid_forget()
        buttonForCellFiveP.grid_forget()
        buttonForCellSixP.grid_forget()
        buttonForCellSevenP.grid_forget()
        buttonForCellEightP.grid_forget()

        # Hiding computer marks
        buttonForCellZeroCom.grid_forget()
        buttonForCellOneCom.grid_forget()
        buttonForCellTwoCom.grid_forget()
        buttonForCellThreeCom.grid_forget()
        buttonForCellFourCom.grid_forget()
        buttonForCellFiveCom.grid_forget()
        buttonForCellSixCom.grid_forget()
        buttonForCellSevenCom.grid_forget()
        buttonForCellEightCom.grid_forget()

        # Placing empty cells back
        buttonForCellZero.grid(row=1, column=1)
        buttonForCellOne.grid(row=1, column=3)
        buttonForCellTwo.grid(row=1, column=5)
        buttonForCellThree.grid(row=3, column=1)
        buttonForCellFour.grid(row=3, column=3)
        buttonForCellFive.grid(row=3, column=5)
        buttonForCellSix.grid(row=5, column=1)
        buttonForCellSeven.grid(row=5, column=3)
        buttonForCellEight.grid(row=5, column=5)

    def checkState():
        # Checking rows

        if field[0][0] == field[0][1] == field[0][2]:
            if field[0][0] == "O":
                playerWon()

            elif field[0][0] == "X":
                playerLost()
        
        elif field[1][0] == field[1][1] == field[1][2]:
            if field[1][0] == "O":
                playerWon()

            elif field[1][0] == "X":
                playerLost()
                    
        elif field[2][0] == field[2][1] == field[2][2]:
            if field[2][0] == "O":
                playerWon()

            elif field[2][0] == "X":
                playerLost()
                    
        # Checking columns

        elif field[0][0] == field[1][0] == field[2][0]:
            if field[0][0] == "O":
                playerWon()

            elif field[0][0] == "X":
                playerLost()
                    
        elif field[0][1] == field[1][1] == field[2][1]:
            if field[0][1] == "O":
                playerWon()

            elif field[0][1] == "X":
                playerLost()
                    
        elif field[0][2] == field[1][2] == field[2][2]:
            if field[0][2] == "O":
                playerWon()

            elif field[0][2] == "X":
                playerLost()
                    
        # Checking diagonals (Sorry for my bad English, I primarily speak German. :( )

        elif field[0][0] == field[1][1] == field[2][2]:
            if field[0][0] == "O":
                playerWon()

            elif field[0][0] == "X":
                playerLost()
                    
        elif field[0][2] == field[1][1] == field[2][0]:
            if field[0][2] == "O":
                playerWon()

            elif field[0][2] == "X":
                playerLost()
                    
        # Checking if full

        elif field[0][0] != " " and field[0][1] != " " and field[0][2] != " " and field[1][0] != " ":
            if field[1][1] != " " and field[1][2] != " " and field[2][0] != " ":
                if field[2][1] != " " and field[2][2] != " ":
                    nobodyWon()

    # Here is the real game

    def fieldZeroPlayer():
        if field[0][0] == " ":
            field[0][0] = "O"
            buttonForCellZero.grid_forget()
            buttonForCellZeroP.grid(row=1, column=1)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()
            
    def fieldOnePlayer():
        if field[0][1] == " ":
            field[0][1] = "O"
            buttonForCellOne.grid_forget()
            buttonForCellOneP.grid(row=1, column=3)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldTwoPlayer():
        if field[0][2] == " ":
            field[0][2] = "O"
            buttonForCellTwo.grid_forget()
            buttonForCellTwoP.grid(row=1, column=5)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldThreePlayer():
        if field[1][0] == " ":
            field[1][0] = "O"
            buttonForCellThree.grid_forget()
            buttonForCellThreeP.grid(row=3, column=1)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldFourPlayer():
        if field[1][1] == " ":
            field[1][1] = "O"
            buttonForCellFour.grid_forget()
            buttonForCellFourP.grid(row=3, column=3)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldFivePlayer():
        if field[1][2] == " ":
            field[1][2] = "O"
            buttonForCellFive.grid_forget()
            buttonForCellFiveP.grid(row=3, column=5)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldSixPlayer():
        if field[2][0] == " ":
            field[2][0] = "O"
            buttonForCellSix.grid_forget()
            buttonForCellSixP.grid(row=5, column=1)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldSevenPlayer():
        if field[2][1] == " ":
            field[2][1] = "O"
            buttonForCellSeven.grid_forget()
            buttonForCellSevenP.grid(row=5, column=3)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldEightPlayer():
        if field[2][2] == " ":
            field[2][2] = "O"
            buttonForCellEight.grid_forget()
            buttonForCellEightP.grid(row=5, column=5)
            gamemodes.assets.turnCounter.playerOne += 1
            computerTurn()
            ticTacPyApp.gridCopy = field.copy()

    def fieldZeroComputer():
        if field[0][0] == " ":
            field[0][0] = "X"
            buttonForCellZero.grid_forget()
            buttonForCellZeroCom.grid(row=1, column=1)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()

        else:
            computerTurn()
            
    def fieldOneComputer():
        if field[0][1] == " ":
            field[0][1] = "X"
            buttonForCellOne.grid_forget()
            buttonForCellOneCom.grid(row=1, column=3)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()

        else:
            computerTurn()
            
    def fieldTwoComputer():
        if field[0][2] == " ":
            field[0][2] = "X"
            buttonForCellTwo.grid_forget()
            buttonForCellTwoCom.grid(row=1, column=5)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()

        else:
            computerTurn()
            
    def fieldThreeComputer():
        if field[1][0] == " ":
            field[1][0] = "X"
            buttonForCellThree.grid_forget()
            buttonForCellThreeCom.grid(row=3, column=1)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()

        else:
            computerTurn()
        
    def fieldFourComputer():
        if field[1][1] == " ":
            field[1][1] = "X"
            buttonForCellFour.grid_forget()
            buttonForCellFourCom.grid(row=3, column=3)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()

        else:
            computerTurn()
            
    def fieldFiveComputer():
        if field[1][2] == " ":
            field[1][2] = "X"
            buttonForCellFive.grid_forget()
            buttonForCellFiveCom.grid(row=3, column=5)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()

        else:
            computerTurn()
            
    def fieldSixComputer():
        if field[2][0] == " ":
            field[2][0] = "X"
            buttonForCellSix.grid_forget()
            buttonForCellSixCom.grid(row=5, column=1)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()
            
        else:
            computerTurn()
            
    def fieldSevenComputer():
        if field[2][1] == " ":
            field[2][1] = "X"
            buttonForCellSeven.grid_forget()
            buttonForCellSevenCom.grid(row=5, column=3)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()
            
        else:
            computerTurn()
            
    def fieldEightComputer():
        if field[2][2] == " ":
            field[2][2] = "X"
            buttonForCellEight.grid_forget()
            buttonForCellEightCom.grid(row=5, column=5)
            gamemodes.assets.turnCounter.playerTwo += 1
            checkState()
            
        else:
            computerTurn()
        
    def computerTurn():
        def getMove():
            if i == 0:
                fieldZeroComputer()

            elif i == 1:
                fieldOneComputer()
            
            elif i == 2:
                fieldTwoComputer()
            
            elif i == 3:
                fieldThreeComputer()
            
            elif i == 4:
                fieldFourComputer()
            
            elif i == 5:
                fieldFiveComputer()
            
            elif i == 6:
                fieldSixComputer()
            
            elif i == 7:
                fieldSevenComputer()
            
            elif i == 8:
                fieldEightComputer()

        checkState()
        if gamemodes.assets.turnCounter.playerOne != 0 and gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
            i = 0
            
            while i < len(ticTacPyApp.gridCopy):
                if ticTacPyApp.gridCopy[i] == " ":
                    gridWithNewMove = ticTacPyApp.gridCopy
                    gridWithNewMove[i] = "O"

                    if gridWithNewMove[0] == gridWithNewMove[1] == gridWithNewMove[2] == "O":
                        getMove()
                        break

                    elif gridWithNewMove[4] == gridWithNewMove[3] == gridWithNewMove[5] == "O":
                        getMove()
                        break

                    elif gridWithNewMove[7] == gridWithNewMove[8] == gridWithNewMove[6] == "O":
                        getMove()
                        break
                    
                    elif gridWithNewMove[0] == gridWithNewMove[3] == gridWithNewMove[6] == "O":
                        getMove()
                        break

                    elif gridWithNewMove[1] == gridWithNewMove[4] == gridWithNewMove[7] == "O":
                        getMove()
                        break

                    elif gridWithNewMove[2] == gridWithNewMove[5] == gridWithNewMove[8] == "O":
                        getMove()
                        break

                    elif gridWithNewMove[0] == gridWithNewMove[4] == gridWithNewMove[8] == "O":
                        getMove()
                        break
                    
                    elif gridWithNewMove[2] == gridWithNewMove[4] == gridWithNewMove[6] == "O":
                        getMove()
                        break
                
                i += 1
            
            i = 0
            
            if gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                while i < len(ticTacPyApp.gridCopy):
                    if ticTacPyApp.gridCopy[i] == " ":
                        gridWithNewMove = ticTacPyApp.gridCopy
                        gridWithNewMove[i] = "X"

                        if gridWithNewMove[0] == gridWithNewMove[1] == gridWithNewMove[2] == "X":
                            getMove()
                            break

                        elif gridWithNewMove[4] == gridWithNewMove[3] == gridWithNewMove[5] == "X":
                            getMove()
                            break

                        elif gridWithNewMove[7] == gridWithNewMove[8] == gridWithNewMove[6] == "X":
                            getMove()
                            break
                    
                        elif gridWithNewMove[0] == gridWithNewMove[3] == gridWithNewMove[6] == "X":
                            getMove()
                            break

                        elif gridWithNewMove[1] == gridWithNewMove[4] == gridWithNewMove[7] == "X":
                            getMove()
                            break

                        elif gridWithNewMove[2] == gridWithNewMove[5] == gridWithNewMove[8] == "X":
                            getMove()
                            break

                        elif gridWithNewMove[0] == gridWithNewMove[4] == gridWithNewMove[8] == "X":
                            getMove()
                            break

                        elif gridWithNewMove[2] == gridWithNewMove[4] == gridWithNewMove[6] == "X":
                            getMove()
                            break
                    
                    i += 1

            if gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                computer = randint(0, 8)
                if computer == 0:
                    fieldZeroComputer()
           
                elif computer == 1:
                    fieldOneComputer()
            
                elif computer == 2:
                    fieldTwoComputer()
            
                elif computer == 3:
                    fieldThreeComputer()
            
                elif computer == 4:
                    fieldFourComputer()
            
                elif computer == 5:
                    fieldFiveComputer()
            
                elif computer == 6:
                    fieldSixComputer()
            
                elif computer == 7:
                    fieldSevenComputer()
            
                elif computer == 8:
                    fieldEightComputer()
                
    gamepvcom = Toplevel()
    gamepvcom.geometry()
    gamepvcom.resizable(width=0, height=0)
        
    gamepvcom.title(ticTacPyApp.pvcomTitleBar)
    gamepvcom.iconbitmap("ttpicon.ico")

    # Placeholder between the left of the window and column 0
    placeholder0 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder0.grid(row=1, column=0)

    # Placeholder between the high of the window and row 0
    placeholder1 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder1.grid(row=0)

    # For cell 0 
    buttonForCellZero = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellZero["command"] = fieldZeroPlayer
    buttonForCellZero.grid(row=1, column=1)

    buttonForCellZeroP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellZeroP["command"] = fieldFilled

    buttonForCellZeroCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellZeroCom["command"] = fieldFilled

    # Placeholder between column 0 and 1
    placeholder2 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder2.grid(row=1, column=2)

    # For cell 1 
    buttonForCellOne = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellOne["command"] = fieldOnePlayer
    buttonForCellOne.grid(row=1, column=3)

    buttonForCellOneP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellOneP["command"] = fieldFilled

    buttonForCellOneCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellOneCom["command"] = fieldFilled

    # Placeholder between column 1 and 2
    placeholder3 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder3.grid(row=1, column=4)

    # For cell 2 
    buttonForCellTwo = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellTwo["command"] = fieldTwoPlayer
    buttonForCellTwo.grid(row=1, column=5)

    buttonForCellTwoP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellTwoP["command"] = fieldFilled

    buttonForCellTwoCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellTwoCom["command"] = fieldFilled

    # Placeholder between column 2 and the right of the window
    placeholder4 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder4.grid(row=1, column=6)

    # Placeholder between row 0 and 1
    placeholder5 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder5.grid(row=2, column=2)

    # For cell 3 
    buttonForCellThree = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellThree["command"] = fieldThreePlayer
    buttonForCellThree.grid(row=3, column=1)

    buttonForCellThreeP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellThreeP["command"] = fieldFilled

    buttonForCellThreeCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellThreeCom["command"] = fieldFilled

    # For cell 4 
    buttonForCellFour = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellFour["command"] = fieldFourPlayer
    buttonForCellFour.grid(row=3, column=3)

    buttonForCellFourP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellFourP["command"] = fieldFilled

    buttonForCellFourCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellFourCom["command"] = fieldFilled

    # For cell 5
    buttonForCellFive = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellFive["command"] = fieldFivePlayer
    buttonForCellFive.grid(row=3, column=5)

    buttonForCellFiveP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellFiveP["command"] = fieldFilled

    buttonForCellFiveCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellFiveCom["command"] = fieldFilled

    # Placeholder between row 1 and 2
    placeholder6 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder6.grid(row=4, column=2)

    # For cell 6
    buttonForCellSix = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellSix["command"] = fieldSixPlayer
    buttonForCellSix.grid(row=5, column=1)

    buttonForCellSixP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellSixP["command"] = fieldFilled

    buttonForCellSixCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellSixCom["command"] = fieldFilled

    # For cell 7
    buttonForCellSeven = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellSeven["command"] = fieldSevenPlayer
    buttonForCellSeven.grid(row=5, column=3)

    buttonForCellSevenP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellSevenP["command"] = fieldFilled

    buttonForCellSevenCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellSevenCom["command"] = fieldFilled

    # For cell 8
    buttonForCellEight = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellEight["command"] = fieldEightPlayer
    buttonForCellEight.grid(row=5, column=5)

    buttonForCellEightP = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellEightP["command"] = fieldFilled

    buttonForCellEightCom = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellEightCom["command"] = fieldFilled

    # Placeholder between row 2 and the low of the window
    placeholder8 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder8.grid(row=6, column=2)