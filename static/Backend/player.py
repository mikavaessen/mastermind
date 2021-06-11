from static.Backend.game import Game

class Player():
    def __init__(self, name):
        self.name = name
        self.games = list(Game)

    def __str__(self):
        return self.name
        
    def addGame(self, guesses):
        game = Game(guesses)
        self.games.append(game)


