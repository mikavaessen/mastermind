import random
from random import choice
from database import Database

class GamePlay:

    def __init__(self, colourAmount, positionAmount, gameMode):
        # genereer de game adhv de input variabelen
        self.colourAmount = colourAmount
        self.positionAmount = positionAmount
        self.gameMode = gameMode
        self.ctr = 0
        self.allColours = ['Green', 'Yellow', 'Blue', 'Red', 'Orange', 'Purple', 'Pink', 'Brown', 'Silver', 'Aquamarine' ]
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
            returnArray = ['Zwart', 'Zwart', 'Zwart', 'Zwart']
        else:
            # initializeer counter

            count = 0
            # Converteerd int naar str
            n = str(n)
            self.num = str(self.num)
            #slaat goede getallen op
            correct = []

            # for loop draait de lengte
            for i, digit in enumerate(n):
                if (digit == self.num[i]):
                    # aantal goed geraden cijfers wordt opgehoogd
                    count += 1
                    # goede cijfer opgeslagen in array
                    correct.append(digit)

            #loop voor het tellen van overeenkomende getallen
            guessedArray = [char for char in str(n)]
            correctArray = [char for char in str(self.num)]
            countCorrectNumber = 0 #houdt overeenkomende getallen die niet op dezelfde positie staan bij
            for j in range(0, 4): #telt het aantal overeenkomende getallen
                booleanCorrect = False #zorgt ervoor dat er bij een correct getal maar 1 ophoging plaatsvindt
                for i in correctArray:
                    if i == guessedArray[j] and booleanCorrect == False:
                        countCorrectNumber += 1
                        booleanCorrect = True #only one number may be correct

            countCorrectNumber = countCorrectNumber-count
            print(countCorrectNumber)
            #controle gegenereerde waardes
            if n == self.num:
                print("Gefeliciteerd! je bent een Mastermind!")
                print("Je hebt er", self.ctr, "pogingen over gedaan.")
            #vullen output array
            if count >0:
                for i in range(0, count):
                    returnArray[i] = 'Zwart'
            if countCorrectNumber > 0:
                for i in range(count,count+countCorrectNumber):
                    returnArray[i] = 'Wit'
        return returnArray, self.ctr

