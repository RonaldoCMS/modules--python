#Lettura e scrittura di un vettore o di una matrice.

def maxLenghtArray():
    return int(input('Insert max lenght:\t'))

def writeArray(max):
    arr = []
    i = 0
    while i < max:
        value = int(input('write in array:\t'))
        arr.append(value)
        i+=1
    return arr

if __name__ == '__main__':
    max = maxLenghtArray()
    arr = writeArray(max)
    print(arr)
    