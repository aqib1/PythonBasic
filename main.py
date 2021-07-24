# Hello world example

f = "hi there"


def setfunction():
    global f
    f = 23
    print(f)
    s = "Hi there "
    print(s.upper() + str(f).join(" sdhjgdj"))


def add(val1, val2=0):
    return val1 + val2


def mul(va1, val2=1):
    return va1*val2


def main():
    print(mul(22, 2))
    print(add(1))
    # print(setfunction is setfunction)
    # print(setfunction() is None)
    # setfunction()
    # print(f)
    # del f
    # temp = -2
    # print(temp)
    # del temp
    # print(temp)
    # print(f) f is deleted
    # name = input("What is your name ?")
    # print(name)


if __name__ == "__main__":
    main()
