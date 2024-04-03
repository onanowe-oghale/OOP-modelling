"""
First Template still alot to work on here
"""

class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(f"{self.name}, please choose rock, paper or scissors: ")
        print(f"{self.name} has selected {self.choice}")



class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()

    def compareChoices(self):
        print("Implement choice check!")

    def awardPoints(self):
        print("Implement Points award")    

class Game:
    def __init__(self):
        self.Endgame = False
        self.participant = Participant("Spock")
        self.secondparticipant = Participant("Kirk")

    def start(self):
        game_round = GameRound(self.participant, self.secondparticipant)

    def checkEndCondition(self):
        print("Implement whether game should continue!")
    
    def determineWinner(self):
        print("Implement")


game = Game()
game.start()


