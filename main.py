# Hello world example

f = "hi there"


def setfunction():
    global f
    f = 23
    print(f)
    s = "Hi there "
    print(s.upper() + str(f).join(" sdhjgdj"))


def main():
    setfunction()
    print(f)
    del f
    # print(f) f is deleted
    # name = input("What is your name ?")
    # print(name)


if __name__ == "__main__":
    main()
