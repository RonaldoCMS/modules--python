
def compilelist(index):
    lista = []
    for i in range(index):
        value = (input('Inserire il ' + str(i+1) + ' numero: '))
        lista.append(int(value))
     #array.insert(i,int(input('Inserire il ' + str(i+1) + ' numero: ')))



index = int(input('Quanti elementi vuoi inserire nella lista?: '))
lista = compilelist(index)

i = 0
while(index > i):
    print('\nNumero della cella ' + str(i) + ' = ' + lista[i])
    i+=1