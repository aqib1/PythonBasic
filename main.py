# Hello world example
from Math import Math

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
    return va1 * val2


def power(val, r=1):
    result = 1

    for i in range(r):
        result *= val

    return result


def multi_add(*args):
    result = 0

    for i in args:
        result += i

    return result





def main():
    math = Math()
    print(math.add(1, 2, 3))
    print(math.mul(1, 2, 4))

    # days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    # for i, day in enumerate(days):
    #     if day == "sunday":
    #         print("She took weed everyday ", i, day)
    # loops
    # x = 1
    # while x <= 10:
    #     print(x)
    #     x += 1

    # for i in range(5, 10):
    #     print(i)

    # condition = "This is ok for me" if(multi_add(1, 2, 3, 4, 5) == 11) else "Its not ok form me"
    # print(condition)
    # if multi_add(11, 2, 3, 4) == 10:
    #     print("ok")
    # elif multi_add(11, 12) == 23:
    #     print("Equal")
    # else:
    #     print("Not OK")
    # print(power(r=2, val=3))
    # print(mul(22, 2))
    # print(add(1))
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
