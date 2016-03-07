class Quiz:
    def __init__(self):
        self.punkte = 0
        self.questions = []
        self.answers = []
        self.correct_answers = []
    def new_question(self, question, answers, correct_answers):
        self.questions.append(question)
        self.answers.append(answers)
        self.correct_answers.append(correct_answers)
    def ask(self):
        index = 0
        for i in self.questions:
            print(i)
            for j in self.answers[index]:
                print(j)
            answer = input("Your Answer")
            if answer == self.correct_answers[index]:
                self.points += 1
            else:
                self.points -= 1
            index += 1
    def get_points(self):
        return(self.points)
if __name__ == "__main__":
    quiz1 = Quiz()
    quiz1.new_question("Who are the three main characters of Harry Potter?",
    ["A: Ginny Weasley, Ron Weasly and Percy Weasly",
    "B: Harry Potter, Ron Weasly and Ginny Weasly",
    "C: Harry Potter, Ron Weasly and Hermine Granger"],
    "C")
    quiz1.new_question("Who is the Headmaster of Hogwarts in the first book?",
    ["A: Severus Snape"
    "B: Tom Marvolo Riddle"
    "C: Albus Dumbledore"],
    "C")
    quiz1.new_question("Who is Lord Voldemord?",
    ["A: Draco Malfoy",
    "B: Harry Potter",
    "C: Tom Marvolo Riddle"],
    "C")
    quiz1.new_question("Who killed Dumbledore?",
    [" A = Severus Snape",
    "B = Draco Malfoy",
    "C = Ginny Weasly"],
    "B")
