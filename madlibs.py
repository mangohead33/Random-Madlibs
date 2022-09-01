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
  print(f"The kingdom of {nameOfKingdom}, ruled by the {adjective1} {nameOfMonarch} and the fair {nameOfSpouse} has run into a little problem.\n The land of {nameOfKingdom} has been plagued with {nameOfProblem} and it has turned the citizens {adjective2} and {adjective3}.\n The wise {nameOfMonarch} decided to best fix the problem, they will {action1} the {nameOfProblem} and {action2} the people.\n")

def sciFiThemed():
  currentYear = input("Enter a random year: ")
  nameOfAlien = input("Enter a silly name: ")
  adjective1 = input("Enter an adjective: ")
  adjective2 = input("Enter an adjective: ")
  action1 = input("Enter an action ending with ed: ")
  yourName = input("Enter your name: ")
  action2 = input("Enter an action: ")
  result = input("Enter a result ex(success, failure, unknown...): ")
  verb = input("Enter a verb: ")
  place = input("Enter name of place: ")
  print(f"It is the year {currentYear} and alien race known as the {nameOfAlien}s have invaded earth.\n The aliens are a race of {adjective1}, and {adjective2} creatures and they wish to {action1} the people of Earth.\n Thankfully {yourName} is in charge dealing with the aliens, and you plan to {action2} them.\n The plan was a  huge {result} and the {nameOfAlien}s have decided to {verb} and they went to {place} instead.\n")

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

