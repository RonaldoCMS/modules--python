
def youself(name, age, job, country):
    txt = "Hi, my name's {} and I am {} years old. I am {} and I from in {}"
    return "\n---------------------------\n " + txt.format(name, age, job, country) + "\n----------------------\n"
     
if __name__ == '__main__':
    print(youself("Fabio", 21, "Developer", "Nola"))
    print(youself("Vincenzo Fortezza", 10, "C++Man", "Carbonara di Nola"))
