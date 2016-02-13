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
loesung1=input("""9/11 was a
A = terrorist action
B = fatal accident 
C = airline
D = company
E = island
F = game
Deine Antwort: """)
ueberpruefen("A", "a", loesung1)
loesung2=input("""Who started World War II?
A = The US
B = Canada
C = Russia
D = Stalingrad
E = Stalin
F = Hitler/Germany
Deine Antwort: """)
ueberpruefen("F", "f", loesung2)
loesung3=input("""Who is Putin?
A = President of the US
B = President of Canada
C = Dictator of Russia
Deine Antwort: """)
ueberpruefen("C", "c", loesung3)
loesung4=input("""When did the US declare Independence
A = 1990
B = 16th century
C = 1776
Deine Antwort: """)
ueberpruefen("C", "c", loesung4)
print("Du hast", punkte, "Punkte ereicht.")

