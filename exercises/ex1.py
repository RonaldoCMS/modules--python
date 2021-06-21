import time
#Calcolare la media di n numeri.

def insertMaxNumber():
    try:
        max = int(input("insert N number:\t"))
    except:
        print("Error, don't insert number")
    return max

def insertNumbers(max):
    list = []

    for index in range(max):
        try:
            temp = int(input("insert number\t"))
            list.append(temp)
        except:
            list.append(0)

    return list

def outAverage(myList):
    max = 0
    for index in myList:
        max = max + index
    
    return max / len(myList)

if __name__ == '__main__':
    max = insertMaxNumber()
    list = insertNumbers(max)
    average = outAverage(list)
    time.sleep(3)
    print("Result:\t", average)
    time.sleep(3)
    print("Thanks!")