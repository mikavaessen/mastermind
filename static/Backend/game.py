from datetime import datetime

class Game():
    def __init__(self, guesses):
        self.guesses = guesses
        self.time = datetime.now()