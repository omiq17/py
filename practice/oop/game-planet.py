from random import choice
from sys import exit

class Scene:
    def enter(self):
        pass

class Death(Scene):
    message = [
            "You have been messed up!",
            "Loser!",
            "Go Home Now!",
            "You have been killed!",
        ]
    def enter(self):
        print("\nWrong Answer!")    
        print(choice(self.message) + "\n" + "Game Over.\n")
        exit(1)

class RoundOne(Scene):
    def enter(self):
        print("\nWhat is planet?\n")
        print("1. An astronomical body")
        print("2. A star")
        print("3. A nuclear body\n")
        ans = input("> ")

        if ans == "1":
            return "round two"
        else:
            return "death"

class RoundTwo(Scene):
    def enter(self):
        print("\nWhat is the closest planet to the Sun and also the "\
                "smallest planet in the solar system?\n")
        print("1. Jupiter")
        print("2. Venus")
        print("3. Mercury\n")
        ans = input("> ")

        if ans == "3":
            return "win"
        else:
            return "death"

class Win(Scene):
    def enter(self):
        print("\nCongratulation!!!\nYou have successfully won the game.")
        exit(1)

class GameEngine:
    stages = {
        "play": RoundOne(),
        "round one": RoundOne(),
        "round two": RoundTwo(),
        "win" : Win(),
        "death": Death()
    }
    def __init__(self, startScene):
        self.scene = startScene
    def play(self):
        currentScene = self.stages.get(self.scene)

        while True:
            # going to next scene 
            nextScene = currentScene.enter()
            # storing result back to current scene
            currentScene = self.stages.get(nextScene)

def main():
    planet = GameEngine("play")
    planet.play()

main()
