import random
from random import choice
import string
import json
import pyodbc
from datetime import datetime
from database import Database

class GamePlay:

    def __init__(self, colourAmount, positionAmount, gameMode):
        # genereer de game adhv de input variabelen
        self.colourAmount = colourAmount
        self.positionAmount = positionAmount
        self.gameMode = gameMode
        self.ctr = 0
        self.allColours = ['Green', 'Yellow', 'Blue', 'Red', 'Orange','Purple','Pink', 'Brown', 'Silver', 'Aquamarine' ]
        self.db = Database()
        self.lastGuess = 0
        if (colourAmount >= 6 and colourAmount <= 10 and positionAmount >= 4 and positionAmount <= 10):
            # genereer random getal in opgegeven range
            s = ""
            if gameMode == "Hard":
                for x in range(4):
                    s = s + str(random.randint(0, colourAmount-1))
                print(s)
                self.num = s
            if gameMode == "Easy":
                randomNumber = []
                for x in range(4):
                    randomNumber.append(choice([i for i in range(colourAmount) if i not in randomNumber])) # random getal opslaan in array en voorkomen dat deze er dubbel in voorkomt
                    s = s + str(randomNumber[x])
                print(s)
                self.num = s

        else:
            print('foute invoer')

    def setGuessedColours(self, n=0000):
        # input voor testen
        returnArray = ['Empty', 'Empty', 'Empty', 'Empty']
        self.ctr += 1
        # Als input gelijk is aan ingegeven waarde
        if (n == self.num):
            print("Great! You guessed the number! You're a Mastermind!")
            returnArray = ['Zwart', 'Zwart', 'Zwart', 'Zwart']
        else:
            # initializeer counter

            count = 0

            # explicit type conversion of an integer to
            # a string in order to ease extraction of digits
            n = str(n)

            # explicit type conversion of a string to an integer
            self.num = str(self.num)

            # correct[] list stores digits which are correct
            correct = []

            # for loop draait de lengte
            for i, digit in enumerate(n):
                if (digit == self.num[i]):
                    # aantal goed geraden cijfers wordt opgehoogd
                    count += 1
                    # goede cijfer opgeslagen in array
                    correct.append(digit)


            guessedArray = [char for char in str(n)]
            correctArray = [char for char in str(self.num)]
            booleanCorrect = False #boolean that checks for a matching number
            countCorrectNumber = 0 #houdt overeenkomende getallen die niet op dezelfde positie staan bij
            for j in range(0, 4): #telt het aantal overeenkomende getallen
                booleanCorrect = False
                for i in correctArray:
                    if i == guessedArray[j] and booleanCorrect == False:
                        countCorrectNumber += 1
                        booleanCorrect = True #only one number may be correct

            countCorrectNumber = countCorrectNumber-count
            print(countCorrectNumber)


            if n == self.num:
                print("You've become a Mastermind!")
                print("It took you only", self.ctr, "tries.")
            if count >0:
                for i in range(0, count):
                    returnArray[i] = 'Zwart'
            if countCorrectNumber > 0:
                for i in range(count,count+countCorrectNumber):
                    returnArray[i] = 'Wit'
        return returnArray, self.ctr

if __name__ == "__main__":
    #for i in range(500):
    #    game = GamePlay(6, 6, 'Easy')
    #    if game.num < 1000:
    #        print(game.num)
    #        break
    #print('de main werkt')
    g = GamePlay(6, 4, "Hard")
    #d = Database()
    #d.addGame("Leon", 22)
    test = ['Empty', 'Empty', 'Empty', 'Empty']
    while (test!=['Zwart', 'Zwart', 'Zwart', 'Zwart']):
        test, aantalPogingen = g.setGuessedColours(str(input("Guess the colour combination:")))
        print(test)
      #  print(aantalPogingen)
      #  print(d.getNames())
