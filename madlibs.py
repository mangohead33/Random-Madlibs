# when file is ran random madlib story should be selected
# user is prompted to enter inputs for the story
# afterall inputs have been added a story will be generated

# then ask if the user wishes to do it again? However it would be best if the user doesn't receive the same story twice

import random

def fantasyThemed():
  nameOfKingdom = input("Enter the name of a fictional place: ")
  nameOfMonarch = input("Enter your name: ")
  adjective1 = input("Enter an adjective: ")
  nameOfSpouse = input("Enter the name of your partner: ")
  nameOfProblem = input("Enter something that you hate: ")
  adjective2 = input("Enter an adjective: ")
  adjective3 = input("Enter an adjective: ")
  action1 = input("Enter an action: ")
  action2 = input("Enter second Action: ")
  print(f"The kingdom of {nameOfKingdom}, ruled by the {adjective1} {nameOfMonarch} and the fair {nameOfSpouse} has run into a little problem.\nThe land of {nameOfKingdom} has been plagued with {nameOfProblem} and it has turned the citizens {adjective2} and {adjective3}.\nThe wise {nameOfMonarch} decided to best fix the problem, they will {action1} the {nameOfProblem} and {action2} the people.\n")

def sciFiThemed():
  currentYear = input("Enter a random year: ")
  nameOfAlien = input("Enter a silly name: ")
  adjective1 = input("Enter an adjective: ")
  adjective2 = input("Enter an adjective: ")
  action1 = input("Enter an action: ")
  yourName = input("Enter your name: ")
  action2 = input("Enter an action: ")
  result = input("Enter a a type of result: ")
  verb = input("Enter a verb: ")
  place = input("Enter name of place: ")
  print(f"It is the year {currentYear} and alien race known as the {nameOfAlien}s have invaded earth.\nThe aliens are a race of {adjective1}, and {adjective2} creatures and they wish to {action1} the people of Earth.\nThankfully {yourName} is in charge dealing with the aliens, and you plan to {action2} them.\nThe plan was a huge {result} and the {nameOfAlien}s have decided to {verb} and they went to {place} instead.\n")

def horrorThemed():
  nameOfPlace = input("Enter the name of a restaraunt: ")
  mascotName = input("Enter a funny name: ")
  nameOfAnimal = input("Enter an animal species: ")
  food = input("Enter a food: ")
  height = input("Enter a number: ")
  weight = input("Enter a number: ")
  action1 = input("Enter a violent action: ")
  item = input("Enter an item you find useful: ")
  print(f"You're stuck in a haunted {nameOfPlace} and the mascot has come alive and is out for blood.\n {mascotName} the {nameOfAnimal}, is {height} ft tall and weighs {weight}kg, was struck by lightning and has turned evil.\n You  were hungry for {food} and you had the misfortune to be trapped in {nameOfPlace} with {mascotName}.\n To survive you grab a {item} and you use it to {action1} {mascotName}.  ")

storyList =[fantasyThemed, sciFiThemed, horrorThemed]

def generateStory():
  story = random.choice(storyList)
  story()

generateStory()

