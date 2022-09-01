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
  nameOfAction = input("Enter an action: ")
  nameOfAction2 = input("Enter second Action: ")
  print(f"The kingdom of {nameOfKingdom}, ruled by the {adjective1} {nameOfMonarch} and the fair {nameOfSpouse} has run into a little problem.\n The land of {nameOfKingdom} has been plagued with {nameOfProblem} and it has turned the citizens {adjective2} and {adjective3}.\n The wise {nameOfMonarch} decided to best fix the problem, they will {nameOfAction} the {nameOfProblem} and {nameOfAction2} the people.\n")

def sciFiThemed():
  alienName = input("Enter a silly name: ")
  verb = input("Enter a Verb: ")
  action = input("Enter an action: ")
  print(f"blah blah")

def romanceThemed():
  adjective = input("Enter an Adjective: ")
  verb = input("Enter a Verb: ")
  action = input("Enter an action: ")
  print(f"blah blah blah")

storyList =[fantasyThemed, sciFiThemed, romanceThemed]

def generateStory():
  story = random.choice(storyList)
  story()

generateStory()

