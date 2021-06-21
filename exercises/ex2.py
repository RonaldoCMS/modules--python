#Realizzare un convertitore, ad esempio lire/euro.

def insertEuroValue():
    return float(input('Insert euros:\t'))

def convertInLire(euro):
    return euro * 1936.27

if __name__ == '__main__':
    euro = insertEuroValue()
    print("Lire\t: ", convertInLire(euro))