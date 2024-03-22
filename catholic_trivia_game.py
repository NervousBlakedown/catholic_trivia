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

# Expanding the existing qaList with more questions for each category

qaList['Virtues'].extend([
    QA("Which virtue is associated with moderation in action, thought, or feeling?", "Temperance", ["Justice", "Prudence", "Fortitude"], 'Medium'),
    QA("Prudence is also known as what?", "Wisdom", ["Courage", "Justice", "Charity"], 'Easy')
])

qaList['Saints'].extend([
    QA("Who is the patron saint of lost causes?", "Saint Jude", ["Saint Christopher", "Saint Michael", "Saint Anthony"], 'Medium'),
    QA("Which saint is known for her visions of Jesus and promoting the devotion to the Sacred Heart?", "Saint Margaret Mary Alacoque", ["Saint Teresa of Avila", "Saint Catherine of Siena", "Saint Joan of Arc"], 'Hard')
])

qaList['Papacy'].extend([
    QA("Who was the first pope?", "Saint Peter", ["Saint Paul", "Saint Andrew", "Saint James"], 'Easy'),
    QA("Which pope initiated the First Crusade in 1095?", "Pope Urban II", ["Pope Gregory VII", "Pope Alexander III", "Pope Innocent III"], 'Medium')
])

qaList['Liturgy'].extend([
    QA("During which liturgical season is the 'Gloria' omitted?", "Lent", ["Advent", "Easter", "Ordinary Time"], 'Medium'),
    QA("What is the liturgical color for Ordinary Time?", "Green", ["Purple", "White", "Red"], 'Easy')
])

qaList['Sacraments'].extend([
    QA("Which sacrament is administered to those who are ill or nearing death?", "Anointing of the Sick", ["Confirmation", "Holy Orders", "Matrimony"], 'Medium'),
    QA("In which sacrament do candidates receive the Gifts of the Holy Spirit?", "Confirmation", ["Baptism", "Eucharist", "Penance"], 'Easy')
])

qaList['Bible'].extend([
    QA("Who was the first king of Israel?", "Saul", ["David", "Solomon", "Samuel"], 'Medium'),
    QA("Which book comes immediately before Mark in the New Testament?", "Matthew", ["Luke", "John", "Acts"], 'Easy')
])

qaList['Church History'].extend([
    QA("In which year was the Second Vatican Council concluded?", "1965", ["1959", "1962", "1970"], 'Hard'),
    QA("Who composed the 'Summa Theologica'?", "Saint Thomas Aquinas", ["Saint Augustine", "Saint Anselm", "Saint Albert the Great"], 'Medium')
])

qaList['Virtues'].extend([
    QA("Which virtue allows one to give each his due?", "Justice", ["Faith", "Hope", "Charity"], 'Medium'),
    QA("What virtue is known as the 'mother of all virtues'?", "Prudence", ["Justice", "Temperance", "Fortitude"], 'Medium')
])

qaList['Saints'].extend([
    QA("Which saint is known for translating the Bible into Latin, known as the Vulgate?", "Saint Jerome", ["Saint Augustine", "Saint Gregory the Great", "Saint Ambrose"], 'Hard'),
    QA("Who is the patron saint of animals and the environment?", "Saint Francis of Assisi", ["Saint Dominic", "Saint Benedict", "Saint Ignatius of Loyola"], 'Easy')
])

qaList['Papacy'].extend([
    QA("Who was the first non-Italian pope after 455 years, elected in 1978?", "Pope John Paul II", ["Pope Paul VI", "Pope John XXIII", "Pope Benedict XVI"], 'Medium'),
    QA("Which pope convened the Council of Trent in 1545?", "Pope Paul III", ["Pope Leo X", "Pope Clement VII", "Pope Julius III"], 'Hard')
])

qaList['Liturgy'].extend([
    QA("What is the highest holy day in the Catholic Church?", "Easter", ["Christmas", "Pentecost", "All Saints' Day"], 'Easy'),
    QA("Which part of the Mass consists of the Liturgy of the Word and the Liturgy of the Eucharist?", "The Mass of the Faithful", ["The Introductory Rites", "The Concluding Rites"], 'Medium')
])

qaList['Sacraments'].extend([
    QA("Which sacrament is considered the last sacrament of initiation?", "Confirmation", ["Eucharist", "Baptism", "Penance"], 'Easy'),
    QA("Matrimony and Holy Orders are known as the Sacraments of what?", "Service", ["Healing", "Initiation", "Commitment"], 'Medium')
])

qaList['Bible'].extend([
    QA("Who was swallowed by a great fish, according to the Old Testament?", "Jonah", ["Noah", "Moses", "Elijah"], 'Easy'),
    QA("In which Gospel is the Sermon on the Mount found?", "Matthew", ["Mark", "Luke", "John"], 'Medium')
])

qaList['Church History'].extend([
    QA("Who led the Catholic Church during World War II?", "Pope Pius XII", ["Pope Pius XI", "Pope John XXIII", "Pope Paul VI"], 'Medium'),
    QA("The division between the Eastern Orthodox Church and the Roman Catholic Church in 1054 is known as what?", "The Great Schism", ["The Reformation", "The Crusades", "The Council of Trent"], 'Hard')
])


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
