punkte=0
def punktzahl(pluspunkte):
    punkte = punkte + pluspunkte
    global punkte
def ueberpruefen(antwort1,antwort2,benutzerantwort):
    if benutzerantwort != antwort1 and benutzerantwort!= antwort2:
        punktzahl(-1)
        print("Das war die falsche Antwort. Die richtige Antwort war", antwort1)
    else:
        punktzahl(1)
        print("Das war die richtige Antwort")
a=input("Password: ")
if a!="Mayday" and a != "mayday":
    a=input("Password: ")
loesung1=input("""Bei einer Airline explpdierte das Triebwerk eines Airbus A380. Welche Airline war das?
A = United Airlines
B = US Airways
C = Lufthansa
D = Air Canada
E = Quantas
F = Qantas
Deine Antwort: """)
ueberpruefen("F", "f", loesung1)
loesung2=input("""Ein Flugzeug setzte mitten über New York zur Notlandung an. Welche Airline und welcher Flug war das?
A = United Airlines Flug 232
B = Air Canada Flug 149
C = US Airways Flug 232
D = Quantas Flug 32
E = US Airways Flug 1459
F = US Airways Flug 1549
Deine Antwort: """)
ueberpruefen("F", "f", loesung2)
loesung3=input("""Aus welcher Baureihe stammt das Flugzeug?
A = Airbus A320
B = Boeing 747
C = Boeing 767
Deine Antwort: """)
ueberpruefen("C", "c", loesung3)
loesung4=input("""Wie heißt der Pilot?
A = Alfred Haynes
B = Alfred Hitchcooc
C = Chesley Sullenberger
Deine Antwort: """)
ueberpruefen("C", "c", loesung4)
print("Du hast", punkte, "Punkte ereicht.")

