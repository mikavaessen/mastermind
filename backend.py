import random
from random import choice
import string


class GamePlay:

    def __init__(self, colourAmount, positionAmount, gameMode):
        # genereer de game adhv de input variabelen
        self.colourAmount = colourAmount
        self.positionAmount = positionAmount
        self.gameMode = gameMode
        self.ctr = 0
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
                    randomNumber.append(choice([i for i in range(0, colourAmount-1) if i not in randomNumber])) # random getal opslaan in array en voorkomen dat deze er dubbel in voorkomt
                    s = s + str(randomNumber[x])
                print(s)
                self.num = s

        else:
            print('foute invoer')

    def setGuessedColours(self, n=0000):
        # input voor testen

        # Als input gelijk is aan ingegeven waarde
        if (n == self.num):
            print("Great! You guessed the number! You're a Mastermind!")
        else:
            # initializeer counter

            # variable increments every time the loop
            # is executed, giving an idea of how many
            # guesses were made.
            self.ctr += 1

            count = 0

            # explicit type conversion of an integer to
            # a string in order to ease extraction of digits
            n = str(n)

            # explicit type conversion of a string to an integer
            self.num = str(self.num)

            # correct[] list stores digits which are correct
            correct = []

            # for loop draait de lengte
            for i in range(0, 4):
                # checking for equality of digits
                if (n[i] == self.num[i]):
                    # aantal goed geraden cijfers wordt opgehoogd
                    count += 1
                    # goede cijfer opgeslagen in array
                    correct.append(n[i])
                else:
                    continue

            # wanneer niet alles goed is geraden
            if (count < 4) and (count != 0):
                print("Not quite the number. But you did get ", count, " digit(s) correct!")
                print("Also these numbers in your input were correct.")

                for k in correct:
                    print(k, end=' ')

                print('\n')
                print('\n')

            guessedArray = [char for char in str(n)]
            correctArray = [char for char in str(self.num)]
            countCorrectNumber = 0 #houdt overeenkomende getallen die niet op dezelfde positie staan bij
            for j in range(0, 4): #telt het aantal overeenkomende getallen
                for i in correctArray:
                    if i == guessedArray[j]:
                        countCorrectNumber += 1
            # wanneer alles fout is geraden
            countCorrectNumber = countCorrectNumber-count
            print(countCorrectNumber)

            if (count == 0):
                print("None of the numbers in your input match.")
        if n == self.num:
            print("You've become a Mastermind!")
            print("It took you only", self.ctr, "tries.")
        returnArray = ['Empty','Empty','Empty','Empty']
        for i in range(0,count):
            returnArray[i] = 'Zwart'
        for i in range(count,count+countCorrectNumber):
            returnArray[i] = 'Zwart'


if __name__ == "__main__":
    print('de main werkt')
    g = GamePlay(6, 4, "Easy")
    while (1):
        g.setGuessedColours(int(input("Guess the colour combination:")))
