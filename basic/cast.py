if __name__ == '__main__':
    x = 5
    y = "John"
    z = input('Insert number:\t')
 
    try:
        j = int(input('Insert other number:\t'))
    except ValueError:
        j = 0

    print(type(x)) #class int
    print(type(y)) #class str
    print(type(z)) #class str
    print(type(j)) #class int