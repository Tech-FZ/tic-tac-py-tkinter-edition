import gamemodes.assets.turnCounter
from tkinter import *

# Player is O, Computer is X.

def playerVsPlayer(ticTacPyApp):
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def fieldFilled():
        notice = Toplevel(gamepvcom)
        notice.geometry()
        notice.resizable(width=0, height=0)

        noticeText = Label(notice, text=ticTacPyApp.fieldFilledWarning, font=("Arial", 16))
        noticeText.pack()

        noticeButton = Button(notice, text=ticTacPyApp.okay, font=("Arial", 12))
        noticeButton["command"] = notice.destroy
        noticeButton.pack()

        placeholder7 = Label(notice, text="", font=("Arial", 2))
        placeholder7.pack()

    def playerOneWon():
        def effectOfYes():
            playerOneOnFirstPlace.destroy()
            wannaPlayMore()
        
        # Resetting the turns
        gamemodes.assets.turnCounter.playerOne = 0
        gamemodes.assets.turnCounter.playerTwo = 0

        playerOneOnFirstPlace = Toplevel(gamepvcom)
        playerOneOnFirstPlace.geometry()
        playerOneOnFirstPlace.resizable(width=0, height=0)

        winnerText = Label(playerOneOnFirstPlace, text=f"{ticTacPyApp.playerOneWonText}\n{ticTacPyApp.playAgainQuestion}", font=("Arial", 16))
        winnerText.grid(row=0, column=0, columnspan=3)

        yesButton = Button(playerOneOnFirstPlace, text=ticTacPyApp.yes, font=("Arial", 12))
        yesButton["command"] = effectOfYes
        yesButton.grid(row=1, column=0)

        noButton = Button(playerOneOnFirstPlace, text=ticTacPyApp.no, font=("Arial", 12))
        noButton["command"] = doneWithPlaying
        noButton.grid(row=1, column=2)

        placeholder7 = Label(playerOneOnFirstPlace, text="", font=("Arial", 2))
        placeholder7.grid(row=2)
    
    def playerOneLost():
        def effectOfYes():
            playerOneOnSecondPlace.destroy()
            wannaPlayMore()

        # Resetting the turns
        gamemodes.assets.turnCounter.playerOne = 0
        gamemodes.assets.turnCounter.playerTwo = 0

        playerOneOnSecondPlace = Toplevel(gamepvcom)
        playerOneOnSecondPlace.geometry()
        playerOneOnSecondPlace.resizable(width=0, height=0)

        loserText = Label(playerOneOnSecondPlace, text=f"{ticTacPyApp.playerTwoWonText}\n{ticTacPyApp.playAgainQuestion}", font=("Arial", 16))
        loserText.grid(row=0, column=0, columnspan=3)

        yesButton = Button(playerOneOnSecondPlace, text=ticTacPyApp.yes, font=("Arial", 12))
        yesButton["command"] = effectOfYes
        yesButton.grid(row=1, column=0)

        noButton = Button(playerOneOnSecondPlace, text=ticTacPyApp.no, font=("Arial", 12))
        noButton["command"] = doneWithPlaying
        noButton.grid(row=1, column=2)

        placeholder7 = Label(playerOneOnSecondPlace, text="", font=("Arial", 2))
        placeholder7.grid(row=2)
        
    def nobodyWon():
        def effectOfYes():
            playersEqual.destroy()
            wannaPlayMore()

        # Resetting the turns
        gamemodes.assets.turnCounter.playerOne = 0
        gamemodes.assets.turnCounter.playerTwo = 0

        playersEqual = Toplevel(gamepvcom)
        playersEqual.geometry()
        playersEqual.resizable(width=0, height=0)

        equalText = Label(playersEqual, text=f"{ticTacPyApp.tieText}!\n{ticTacPyApp.playAgainQuestion}", font=("Arial", 16))
        equalText.grid(row=0, column=0, columnspan=3)

        yesButton = Button(playersEqual, text=ticTacPyApp.yes, font=("Arial", 12))
        yesButton["command"] = effectOfYes
        yesButton.grid(row=1, column=0)
        
        noButton = Button(playersEqual, text=ticTacPyApp.no, font=("Arial", 12))
        noButton["command"] = doneWithPlaying

        noButton.grid(row=1, column=2)
        placeholder7 = Label(playersEqual, text="", font=("Arial", 2))
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

        # Hiding player 1 marks
        buttonForCellZeroP1.grid_forget()
        buttonForCellOneP1.grid_forget()
        buttonForCellTwoP1.grid_forget()
        buttonForCellThreeP1.grid_forget()
        buttonForCellFourP1.grid_forget()
        buttonForCellFiveP1.grid_forget()
        buttonForCellSixP1.grid_forget()
        buttonForCellSevenP1.grid_forget()
        buttonForCellEightP1.grid_forget()

        # Hiding player 2 marks
        buttonForCellZeroP2.grid_forget()
        buttonForCellOneP2.grid_forget()
        buttonForCellTwoP2.grid_forget()
        buttonForCellThreeP2.grid_forget()
        buttonForCellFourP2.grid_forget()
        buttonForCellFiveP2.grid_forget()
        buttonForCellSixP2.grid_forget()
        buttonForCellSevenP2.grid_forget()
        buttonForCellEightP2.grid_forget()

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

        try:
            playerTwoTurnText.grid_forget()
            playerOneTurnText.grid(row=0, column=0, columnspan=6)
            
        except:
            pass

    def checkState():
        # Checking rows

        if field[0][0] == field[0][1] == field[0][2]:
            if field[0][0] == "O":
                playerOneWon()

            elif field[0][0] == "X":
                playerOneLost()
        
        elif field[1][0] == field[1][1] == field[1][2]:
            if field[1][0] == "O":
                playerOneWon()

            elif field[1][0] == "X":
                playerOneLost()
                    
        elif field[2][0] == field[2][1] == field[2][2]:
            if field[2][0] == "O":
                playerOneWon()

            elif field[2][0] == "X":
                playerOneLost()
                    
        # Checking columns

        elif field[0][0] == field[1][0] == field[2][0]:
            if field[0][0] == "O":
                playerOneWon()

            elif field[0][0] == "X":
                playerOneLost()
                    
        elif field[0][1] == field[1][1] == field[2][1]:
            if field[0][1] == "O":
                playerOneWon()

            elif field[0][1] == "X":
                playerOneLost()
                    
        elif field[0][2] == field[1][2] == field[2][2]:
            if field[0][2] == "O":
                playerOneWon()

            elif field[0][2] == "X":
                playerOneLost()
                    
        # Checking diagonals (Sorry for my bad English, I primarily speak German. :( )

        elif field[0][0] == field[1][1] == field[2][2]:
            if field[0][0] == "O":
                playerOneWon()

            elif field[0][0] == "X":
                playerOneLost()
                    
        elif field[0][2] == field[1][1] == field[2][0]:
            if field[0][2] == "O":
                playerOneWon()

            elif field[0][2] == "X":
                playerOneLost()
                    
        # Checking if full

        elif field[0][0] != " " and field[0][1] != " " and field[0][2] != " " and field[1][0] != " ":
            if field[1][1] != " " and field[1][2] != " " and field[2][0] != " ":
                if field[2][1] != " " and field[2][2] != " ":
                    nobodyWon()

    # Here is the real game

    def fieldZeroPlayer():
        if field[0][0] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[0][0] = "O"
                buttonForCellZero.grid_forget()
                buttonForCellZeroP1.grid(row=1, column=1)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[0][0] = "X"
                buttonForCellZero.grid_forget()
                buttonForCellZeroP2.grid(row=1, column=1)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)
            
            checkState()
            
    def fieldOnePlayer():
        if field[0][1] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[0][1] = "O"
                buttonForCellOne.grid_forget()
                buttonForCellOneP1.grid(row=1, column=3)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[0][1] = "X"
                buttonForCellOne.grid_forget()
                buttonForCellOneP2.grid(row=1, column=3)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
            
    def fieldTwoPlayer():
        if field[0][2] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[0][2] = "O"
                buttonForCellTwo.grid_forget()
                buttonForCellTwoP1.grid(row=1, column=5)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[0][2] = "X"
                buttonForCellTwo.grid_forget()
                buttonForCellTwoP2.grid(row=1, column=5)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
        
    def fieldThreePlayer():
        if field[1][0] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[1][0] = "O"
                buttonForCellThree.grid_forget()
                buttonForCellThreeP1.grid(row=3, column=1)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[1][0] = "X"
                buttonForCellThree.grid_forget()
                buttonForCellThreeP2.grid(row=3, column=1)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
        
    def fieldFourPlayer():
        if field[1][1] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[1][1] = "O"
                buttonForCellFour.grid_forget()
                buttonForCellFourP1.grid(row=3, column=3)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[1][1] = "X"
                buttonForCellFour.grid_forget()
                buttonForCellFourP2.grid(row=3, column=3)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
        
    def fieldFivePlayer():
        if field[1][2] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[1][2] = "O"
                buttonForCellFive.grid_forget()
                buttonForCellFiveP1.grid(row=3, column=5)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[1][2] = "X"
                buttonForCellFive.grid_forget()
                buttonForCellFiveP2.grid(row=3, column=5)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
        
    def fieldSixPlayer():
        if field[2][0] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[2][0] = "O"
                buttonForCellSix.grid_forget()
                buttonForCellSixP1.grid(row=5, column=1)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[2][0] = "X"
                buttonForCellSix.grid_forget()
                buttonForCellSixP2.grid(row=5, column=1)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
        
    def fieldSevenPlayer():
        if field[2][1] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[2][1] = "O"
                buttonForCellSeven.grid_forget()
                buttonForCellSevenP1.grid(row=5, column=3)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[2][1] = "X"
                buttonForCellSeven.grid_forget()
                buttonForCellSevenP2.grid(row=5, column=3)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
        
    def fieldEightPlayer():
        if field[2][2] == " ":
            if gamemodes.assets.turnCounter.playerOne == gamemodes.assets.turnCounter.playerTwo:
                field[2][2] = "O"
                buttonForCellEight.grid_forget()
                buttonForCellEightP1.grid(row=5, column=5)
                gamemodes.assets.turnCounter.playerOne += 1
                playerOneTurnText.grid_forget()
                playerTwoTurnText.grid(row=0, column=0, columnspan=6)
            
            elif gamemodes.assets.turnCounter.playerOne > gamemodes.assets.turnCounter.playerTwo:
                field[2][2] = "X"
                buttonForCellEight.grid_forget()
                buttonForCellEightP2.grid(row=5, column=5)
                gamemodes.assets.turnCounter.playerTwo += 1
                playerTwoTurnText.grid_forget()
                playerOneTurnText.grid(row=0, column=0, columnspan=6)

            checkState()
                
    gamepvcom = Toplevel()
    gamepvcom.geometry()
    gamepvcom.resizable(width=0, height=0)
        
    gamepvcom.title(ticTacPyApp.pvpTitleBar)

    # This is to show the turns

    playerOneTurnText = Label(gamepvcom, text=ticTacPyApp.playerOneTurnText, font=("Arial", 12))
    playerOneTurnText.grid(row=0, column=0, columnspan=6)
    playerTwoTurnText = Label(gamepvcom, text=ticTacPyApp.playerTwoTurnText, font=("Arial", 12))

    # Placeholder between the left of the window and cell 0
    placeholder0 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder0.grid(row=1, column=0)

    # For cell 0 
    buttonForCellZero = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellZero["command"] = fieldZeroPlayer
    buttonForCellZero.grid(row=1, column=1)

    buttonForCellZeroP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellZeroP1["command"] = fieldFilled

    buttonForCellZeroP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellZeroP2["command"] = fieldFilled

    # Placeholder between cell 0 and 1
    placeholder1 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder1.grid(row=1, column=2)

    # For cell 1 
    buttonForCellOne = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellOne["command"] = fieldOnePlayer
    buttonForCellOne.grid(row=1, column=3)

    buttonForCellOneP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellOneP1["command"] = fieldFilled

    buttonForCellOneP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellOneP2["command"] = fieldFilled

    # Placeholder between cell 1 and 2
    placeholder2 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder2.grid(row=1, column=4)

    # For cell 2 
    buttonForCellTwo = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellTwo["command"] = fieldTwoPlayer
    buttonForCellTwo.grid(row=1, column=5)

    buttonForCellTwoP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellTwoP1["command"] = fieldFilled

    buttonForCellTwoP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellTwoP2["command"] = fieldFilled

    # Placeholder between cell 2 and the right of the window
    placeholder3 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder3.grid(row=1, column=6)

    # Placeholder between row 0 and 1
    placeholder4 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder4.grid(row=2, column=0)

    # For cell 3 
    buttonForCellThree = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellThree["command"] = fieldThreePlayer
    buttonForCellThree.grid(row=3, column=1)

    buttonForCellThreeP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellThreeP1["command"] = fieldFilled

    buttonForCellThreeP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellThreeP2["command"] = fieldFilled

    # For cell 4 
    buttonForCellFour = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellFour["command"] = fieldFourPlayer
    buttonForCellFour.grid(row=3, column=3)

    buttonForCellFourP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellFourP1["command"] = fieldFilled

    buttonForCellFourP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellFourP2["command"] = fieldFilled

    # For cell 5
    buttonForCellFive = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellFive["command"] = fieldFivePlayer
    buttonForCellFive.grid(row=3, column=5)

    buttonForCellFiveP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellFiveP1["command"] = fieldFilled

    buttonForCellFiveP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellFiveP2["command"] = fieldFilled

    # Placeholder between row 1 and 2
    placeholder5 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder5.grid(row=4, column=0)

    # For cell 6
    buttonForCellSix = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellSix["command"] = fieldSixPlayer
    buttonForCellSix.grid(row=5, column=1)

    buttonForCellSixP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellSixP1["command"] = fieldFilled

    buttonForCellSixP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellSixP2["command"] = fieldFilled

    # For cell 7
    buttonForCellSeven = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellSeven["command"] = fieldSevenPlayer
    buttonForCellSeven.grid(row=5, column=3)

    buttonForCellSevenP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellSevenP1["command"] = fieldFilled

    buttonForCellSevenP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellSevenP2["command"] = fieldFilled

    # For cell 8
    buttonForCellEight = Button(gamepvcom, text=" ", width=16, height=4, font=("Arial", 9))
    buttonForCellEight["command"] = fieldEightPlayer
    buttonForCellEight.grid(row=5, column=5)

    buttonForCellEightP1 = Button(gamepvcom, text="O", width=16, height=4, font=("Arial", 9))
    buttonForCellEightP1["command"] = fieldFilled

    buttonForCellEightP2 = Button(gamepvcom, text="X", width=16, height=4, font=("Arial", 9))
    buttonForCellEightP2["command"] = fieldFilled

    # Placeholder between row 2 and the low of the window
    placeholder6 = Label(gamepvcom, text="", font=("Arial", 2))
    placeholder6.grid(row=6, column=0)