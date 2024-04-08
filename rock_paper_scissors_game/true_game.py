"""
This is an adaptation of the rockpaper scissors game in a way
"""
from time import sleep

"""
Well if you are familiar with the avatar movie this game is a python implementation
of the four elements(water, earth, fire and air) battling each other.

It is played between two participants
"""

class Participant:
    def __init__(self):
        name = input("🛡     Welcome Bender, What is you Name?__")
        print("""
            You are strong bender up against each other! 
            Every element:
            Water💧, Earth🌋, Fire🔥, Air💨 
            Is Available to you in combat\n
            """)
        self.name = name
        self.choice = ""
        self.points = 0


    def choose(self):
        sleep(0.5)
       
        self.choice = False
        while not self.choice in ["w","e","f","a"]:
            print("""
                Press W for Water💧,
                Press E for Earth🌋,
                Press F for Fire🔥,
                Press A for Air💨.........
                """)
            sleep(0.5)
            self.choice = input(f"{self.name} please choose one: Water💧, Earth🌋, Fire🔥 and Air💨: ").lower()

            if not self.choice in ["w", "e", "f", "a"]:
                sleep(1)
                print("Invalid element try again!")
                sleep(0.5)
            else:
                print("Move unleashed.....")
                return self.choice
        
    def increase_point(self):
        self.points +=1
       

    def to_numerical(self):
        convert = {
            "w": 0,
            "e": 1,
            "f": 2,
            "a": 3
        }
        return convert[self.choice]
    
    
    


class GameRound:
    def __init__(self,p1,p2):
        self.rules = [
            [0,1,1,-1],
            [-1,0,-1,1],
            [-1,1,0,1],
            [1,-1,-1,0]
        ]

        p1.choose()
        p2.choose()

        result = self.comparechoices(p1,p2)
        
        print(f"The result of the round is {self.roundresult(result)}") 

        if result > 0:
            p1.increase_point()
        elif result < 0:
            p2.increase_point()



    def comparechoices(self,p1,p2):
        return self.rules[p1.to_numerical()][p2.to_numerical()]


    def roundresult(self,result):
        convert ={
            0: "Draw",
            1: "Win",
            -1: "Loss"
        }
        return convert[result]
    
class Game:
    def __init__(self):
        self.EndGame = False
        self.particpant = Participant()
        self.particpant_two = Participant()


    def start(self):
        while not self.EndGame:
            gameround = GameRound(self.particpant, self.particpant_two)
            self.check_end()

    
    def check_end(self):
        end_check = input("Would you like to continue to a new round:\n Y/N:").lower()
        
        if end_check == 'y':
            print("Continuing Game.....\n")
            sleep(0.3)
            self.start()
        elif end_check == 'n':
            print("Ending game..........\n")
            self.EndGame = True
            self.determine_winner()
        else:
            print("Invalid Input! TRY AGAIN! ")
            self.determine_winner()
            

    def determine_winner(self):
        final_verdict = f"Game ends as a draw {self.particpant.name} had {self.particpant.points} and {self.particpant_two.name} had {self.particpant_two.points}"  

        if self.particpant.points > self.particpant_two.points:
            final_verdict = f"{self.particpant.name} wins!🥇 with {self.particpant.points} as against {self.particpant_two.name}'s {self.particpant_two.points}" 

        elif self.particpant.points < self.particpant_two.points:
            final_verdict = f"{self.particpant_two.name} wins!🥇 with {self.particpant_two.points} as againts {self.particpant.name}'s {self.particpant.points}"  

        print(final_verdict)


game = Game()
game.start()  