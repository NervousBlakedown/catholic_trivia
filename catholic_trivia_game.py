# Trivia Game N'at.  O what fun it is.
# Imports
import random


# Create class
class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers


# Intro text
print("\n")
print("Welcome to Blake's Catholic Trivia!  Let's begin.")
print()

# Questions and answers go here.  Modify as desired.
qaList = [
  QA("What are the three theological virtues?", 
      "Faith, Hope, Charity", 
        ["Love, Wisdom, Gentleness", "Diversity, Inclusion, Anti-Racism", "Christ-esque behavior, Being a good person, Being vaguely nice"]),
  QA("What are the four cardinal virtues?",
      "Justice, Prudence, Temperance, Fortitude", 
        ["Love, Tolerance, Kindness, Compassion", "Matthew, Mark, Luke, John", "Wisdom, Peace, Patience, Self-Control"]),
  QA("Which saint is deemed 'The First Martyr'?",
      "Saint Stephen", 
        ["Saint Iranaeus", "Saint Paul", "Saint John", "Saint Peter"]),
  QA("This pope had/has the longest-lasting pontificate in papal history.",
      "Pope Piux IX",
        ["Pope John Paul II", "Pope Leo XIII", "Pope Pius VI", "Pope Francis"]),
  QA("What two colors comprise the papal flag?",
      "White and Yellow",
        ["Black and Yellow", "Red and White", "Roy G. Biv"]),
  QA("Which of these popes was killed by a fallen ceiling?",
      "John XXI",
        ["Benedict VI","Lucius II", "John Paul I", "John VIII"])
]
# TODO: insert line break between answers and prompt

# Shuffle Everything
corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Select your number and press enter:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to an answer. Please enter an available number and press enter:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Correct.")
    corrCount += 1
  else:
    print("Incorrect.")
    print("The correct answer was: " + qaItem.corrAnsw)
  print()


# Results and Finale
correct_pct = (corrCount / len(qaList)) * 100
print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly, " + str(correct_pct) + " %.")
print()
print("Thanks for playing!")
print()