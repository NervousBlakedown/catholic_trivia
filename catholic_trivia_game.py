# Trivia Game N'at.  O what fun it is.
import random

class QA:
    def __init__(self, question, correctAnswer, otherAnswers, difficulty):
        self.question = question
        self.corrAnsw = correctAnswer
        self.otherAnsw = otherAnswers
        self.difficulty = difficulty

# Enhanced Intro Text
print("\nWelcome to Blake's Catholic Trivia! Choose a category and test your knowledge. Let's begin.\n")

# Questions and answers
qaList = {
    'Virtues': [
        QA("What are the three theological virtues?", "Faith, Hope, Charity", ["Love, Wisdom, Gentleness", "Diversity, Inclusion, Anti-Racism", "Christ-esque behavior, Being a good person, Being vaguely nice"], 'Easy'),
        QA("What are the four cardinal virtues?", "Justice, Prudence, Temperance, Fortitude", ["Love, Tolerance, Kindness, Compassion", "Matthew, Mark, Luke, John", "Wisdom, Peace, Patience, Self-Control"], 'Medium')
    ],
    'Saints': [
        QA("Which saint is deemed 'The First Martyr'?", "Saint Stephen", ["Saint Iranaeus", "Saint Paul", "Saint John", "Saint Peter"], 'Easy')
    ],
    'Papacy': [
        QA("This pope had/has the longest-lasting pontificate in papal history.", "Pope Pius IX", ["Pope John Paul II", "Pope Leo XIII", "Pope Pius VI", "Pope Francis"], 'Hard'),
        QA("What two colors comprise the papal flag?", "White and Yellow", ["Black and Yellow", "Red and White", "Roy G. Biv"], 'Medium'),
        QA("Which of these popes was killed by a fallen ceiling?", "John XXI", ["Benedict VI","Lucius II", "John Paul I", "John VIII"], 'Hard')
    ]
}

# Scoring System
points = {'Easy': 10, 'Medium': 20, 'Hard': 30}
total_score = 0

# Category Selection
print("Categories:")
for idx, category in enumerate(qaList, 1):
    print(f"{idx}. {category}")
category_choice = int(input("Choose a category by number: "))
selected_category = list(qaList.keys())[category_choice - 1]

# Shuffle Questions
random.shuffle(qaList[selected_category])
for qaItem in qaList[selected_category]:
    print(f"\n{qaItem.question} (Difficulty: {qaItem.difficulty})")
    possible = qaItem.otherAnsw + [qaItem.corrAnsw]
    random.shuffle(possible)
    
    for idx, option in enumerate(possible, 1):
        print(f"{idx}: {option}")
    
    userAnsw = int(input("\nSelect your number and press enter: "))
    if possible[userAnsw-1] == qaItem.corrAnsw:
        print("Correct!")
        total_score += points[qaItem.difficulty]
    else:
        print("Incorrect. The correct answer was: " + qaItem.corrAnsw)

# Results and Finale
print(f"\nYour total score is: {total_score} points.")
print("\nThanks for playing!")
