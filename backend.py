import random

if __name__ == "__main__":
    print('de main werkt')
    
class: GamePlay
    def __init__(self, colourAmount, positionAmount, gameMode):
        #genereer de game adhv de input variabelen
        self.colourAmount = colourAmount
        self.positionAmount = positionAmount
        self.gameMode = gameMode
        self.ctr = 0
        if(colourAmount>=6 and colourAmount<=10 and positionAmount>=4 and positionAmount<=10):
            
            self.num = random.randrange(10**(colourAmount-1),10**colourAmount) 
            return 1
        else:
            return 0

    def setGuessedColours(self)

        #input voor testen                    
        n = int(input("Guess the "self.colourAmount" colour combination:")) 

        
        # Als input gelijk is aan ingegeven waarde
        if(n == self.num):             
            print("Great! You guessed the number! You're a Mastermind!")
        else:
            # initializeer counter
              
        

            while(n!=self.num):
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
                correct=[]        
        
                # for loop runs 4 times since the number has 4 digits.     
                for i in range(0,self.colourAmount): 
                    # checking for equality of digits
                    if(n[i] == self.num[i]): 
                        # number of digits guessed correctly increments
                        count += 1    
                        # hence, the digit is stored in correct[].
                        correct.append(n[i])     
                    else:
                        continue
        
                # when not all the digits are guessed correctly.
                if (count < self.colourAmount) and (count != 0):     
                    print("Not quite the number. But you did get ",count," digit(s) correct!")
                    print("Also these numbers in your input were correct.")
                        
                    for k in correct:
                        print(k, end=' ')
        
                    print('\n')
                    print('\n')
                    n = int(input("Enter your next choice of numbers: "))
        
                # when none of the digits are guessed correctly.
                elif(count == 0):         
                    print("None of the numbers in your input match.")
                    n=int(input("Enter your next choice of numbers: ")) 
        
            if n==self.num:                
                print("You've become a Mastermind!")
                print("It took you only",self.ctr,"tries.")
class: User