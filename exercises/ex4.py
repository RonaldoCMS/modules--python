#Preso in input un numero a, vogliamo visualizzare se si tratta di un numero maggiore o uguale di zero oppure negativo.

if __name__ == '__main__':
    value = 0

    if value < 0:
        print('negative')
    elif value > 0:
        print('positive')
    else:
        print('neutral')