# Trivia Game N'at.  O what fun it is.
import random

class QA:
    def __init__(self, question, correctAnswer, otherAnswers, difficulty):
        self.question = question
        self.corrAnsw = correctAnswer
        self.otherAnsw = otherAnswers
        self.difficulty = difficulty

# Enhanced Intro Text
print("\nWelcome to Blake's Catholic Trivia! Choose a category and test your knowledge. Let us begin.\n")

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
        QA("This pope was killed by a fallen ceiling.", "John XXI", ["Benedict VI","Lucius II", "John Paul I", "John VIII"], 'Hard')
    ]
}

# Add new categories and questions here
qaList.update({
    'Liturgy': [
        QA("What liturgical season is dedicated to preparation for Easter?", "Lent", ["Advent", "Ordinary Time", "Christmas"], 'Medium'),
        QA("What color is typically worn by priests during Lent?", "Purple", ["Green", "White", "Red"], 'Easy')
    ],
    'Sacraments': [
        QA("How many sacraments does the Catholic Church recognize?", "Seven", ["Five", "Six", "Eight"], 'Easy'),
        QA("Which sacrament is considered the 'source and summit of the Christian life'?", "Eucharist", ["Baptism", "Confirmation", "Holy Orders"], 'Medium')
    ],
    'Bible': [
        QA("Who betrayed Jesus for thirty pieces of silver?", "Judas Iscariot", ["Pontius Pilate", "King Herod", "Peter"], 'Easy'),
        QA("In which book of the Bible is the story of the Exodus found?", "Exodus", ["Genesis", "Leviticus", "Numbers"], 'Medium')
    ],
    'Church History': [
        QA("Which council defined the Nicene Creed?", "First Council of Nicaea", ["Council of Trent", "First Vatican Council", "Second Vatican Council"], 'Hard'),
        QA("Who founded the Benedictine Order?", "Saint Benedict of Nursia", ["Saint Francis of Assisi", "Saint Dominic", "Saint Ignatius of Loyola"], 'Medium')
    ]
})

# Scoring System
points = {'Easy': 10, 'Medium': 20, 'Hard': 30}
total_score = 0

def get_user_input(prompt, max_choice):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            user_choice = int(user_input)
            if 1 <= user_choice <= max_choice:
                return user_choice
            else:
                print(f"Please enter a number between 1 and {max_choice}.")
        else:
            print("That was not a valid number. Please try again.")

def ask_question(category):
    global total_score
    random.shuffle(qaList[category])
    for qaItem in qaList[category]:
        print(f"\n{qaItem.question} (Difficulty: {qaItem.difficulty})")
        possible = qaItem.otherAnsw + [qaItem.corrAnsw]
        random.shuffle(possible)
        
        for idx, option in enumerate(possible, 1):
            print(f"{idx}: {option}")
        
        userAnsw = get_user_input("\nSelect your number and press enter: ", len(possible))
        if possible[userAnsw-1] == qaItem.corrAnsw:
            print("Correct!")
            total_score += points[qaItem.difficulty]
        else:
            print("Incorrect. The correct answer was: " + qaItem.corrAnsw)
        break  # Break after one question to return to category selection

# Game loop
while True:
    print("\nCategories:")
    for idx, category in enumerate(qaList, 1):
        print(f"{idx}. {category}")
    print(f"{len(qaList) + 1}. Exit")
    
    category_choice = get_user_input("Choose a category by number or exit: ", len(qaList) + 1)
    
    if category_choice == len(qaList) + 1:
        break  # Exit the game
    
    selected_category = list(qaList.keys())[category_choice - 1]
    ask_question(selected_category)

# Results and Finale
print(f"\nYour total score is: {total_score} points.")
print("\nThanks for playing!")
