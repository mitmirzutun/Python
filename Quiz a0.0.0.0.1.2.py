punkte=0
def punktzahl(pluspunkte):
    punkte = punkte + pluspunkte
    global punkte
def ueberpruefen(antwort1,antwort2,benutzerantwort):
    if benutzerantwort != antwort1 and benutzerantwort!= antwort2:
        punktzahl(-1)
        print("That was the false answer. The correct answer was", antwort1)
    else:
        punktzahl(1)
        print("That was the right answer.")
loesung1=input("""Who are the three main characters of Harry Potter?
A: Ginny Weasley, Ron Weasly and Percy Weasly
B: Harry Potter, Ron Weasly and Ginny Weasly
C: Harry Potter, Ron Weasly and Hermine Granger
Your answer: """)
ueberpruefen("C", "c", loesung1)
loesung2=input("""Who is the Headmaster of Hogwarts in the first book?
A: Severus Snape
B: Tom Marvolo Riddle
C: Albus Dumbledore
Your answer: """)
ueberpruefen("C", "c", loesung2)
loesung3=input("""Who is Lord Voldemord?
A: Draco Malfoy
b: Harry Potter
C:  Tom Marvolo Riddle
Your Answer: """)
ueberpruefen("C", "c", loesung3)
loesung4=input("""Who killed Dumbledore?
A = Severus Snape
B = Draco Malfoy
C = Ginny Weasly
Your answer: """)
ueberpruefen("A", "a", loesung4)
print("You got", punkte, "Points.")

