"""
trying to implement to rock paper scissor game learnt on my own
"""


class Participant:
    def __init__(self):
        name = input("What Is Your Name😁: ")
        self.name = name
        self.choice = ""
        self.points = 0


    def choose(self):
        choice_dict = {"R": "Rock🌚", "P":"Paper📄 ", "S":"Scissor ✂"} 
        for keys, values in choice_dict.items():
            print(f"Press {keys} To Choose {values}")

        self.choice = False

        while self.choice not in ["r","p","s"]:

            self.choice = input(f"{self.name} please choose one between between rock🌚, paper📄 and scissors✂: \n").lower()
        
            if self.choice not in ["r", "p", "s"]:
                print("Invalid input try again!❌ ")
            else:
                return self.choice
                
    def increment_point(self):
        self.points =+1

    def toNumerical(self):
        convert = {
            "r": 0,
            "p": 1,
            "s": 2
        }
        return convert[self.choice]

class Gameround:
    def __init__(self,p1,p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        
        p1.choose()
        p2.choose()

        result = self.compare_choice(p1,p2)
        print(f"The Round ended in a {self.res_as_str(result)} ⚔")

        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()

    def compare_choice(self,p1,p2):
        return self.rules[p1.toNumerical()][p2.toNumerical()]

    def res_as_str(self, result):
        res = {
            0: "Draw",
            1: "Win",
            -1: "Loss"
        }
        return res[result]
    

class Game:
    def __init__(self):
        self.EndGame = False
        self.participant = Participant()
        self.second_participant = Participant()


    def start(self):
        while not self.EndGame: 
            game_round = Gameround(self.participant,self.second_participant)
            self.check_continue()


    def check_continue(self):
        print("Game round completed! \n🚀")
        continue_cond = input("Would you like to continue? \n  Y/ N🤔: ").lower()

        if continue_cond == 'y':
            print("\nMoving To Next Gameround⚔.")
            self.start()
        elif continue_cond == 'n':
            print("Game ends \n")
            print("Determining winner.............🥇")
            self.EndGame = True
            self.determine_winner()
        else:
            print("Invalid Input! 🛡")
            self.check_continue()
            


    def determine_winner(self):
        verdict = f"It is a draw!🤝🏿 {self.participant.name} had {self.participant.points} and {self.second_participant.name} had {self.second_participant.points}"

        if self.participant.points > self.second_participant.points:
            verdict = (f"{self.participant.name} has {self.participant.points} and {self.second_participant.name} has {self.second_participant.points}")
            print(f"{self.participant.name}🥇 wins!🎊")
        elif self.participant.points < self.second_participant.points:
            verdict = (f"{self.second_participant.name} has {self.second_participant.points} and {self.participant.name} has {self.participant.points}")
            print(f"{self.second_participant.name}🥇 wins!🎊")
        
        print(verdict)


game = Game()
game.start()