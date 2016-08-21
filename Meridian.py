import random
def meridian(liste):
    liste.sort()
    if len(liste) % 2 == 1:
        return liste[int((len(liste)-1)/2)]
    else:
        return (liste[int(len(liste)/2-1)]+liste[int(len(liste)/2)])/2
if __name__ == "__main__":
    liste1 = []
    for i in range(random.randint(0, 100)):
        liste1.append(random.randint(0, 200))
        print(meridian(liste1))
