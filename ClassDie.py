import random

class Die(object):
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color

    def getColor(self):
        return self.color

    def getSides(self):
        return self.sides

    def roll(self):
        return random.randint(1, self.sides + 1)

    def changeColor(self, color):
        self.color = color

    def changeSides(self, sides):
        self.sides = sides

print("I just created a Dice Object. It has 6 sides and is red")
rome = Die(6, "red")
print("I rolled the dice object, and got the a ")
number = rome.roll()
print(number)

print("I'm going to change the number of sides to 999999999 so I can roll a higher number")
rome.changeSides(999999999)
print("Now I'm going to Roll the dice to see what I get")
print(rome.roll())

newColor = input("Please change the color of the die from " + rome.getColor())
rome.changeColor(newColor)

print("Congrats the new color is " + rome.getColor())