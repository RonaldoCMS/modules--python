#Realizzare un programma, che legga in input un voto rappresentato da un carattere tra A ed E e dopo ne stampi il significato.

def controllVote(vote):
    if vote.__eq__("A") or vote.__eq__("B") or vote.__eq__("C") or vote.__eq__("D") or vote.__eq__("E"):
        return True
    return False

def translatorVote(vote):
    if controllVote(vote):
        outConvertVote(vote)
    else:
        print('Error insert value')

def outConvertVote(vote):
    switcher = {
        "A": "Perfect",
        "B": "Nice",
        "C": "Good",
        "D": "sufficient",
        "E": "unsufficient"
    }

    print(vote, "\t", switcher[vote])

if __name__ == '__main__':
    translatorVote("E")

    
    