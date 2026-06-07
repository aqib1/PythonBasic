if __name__ == '__main__':
    first_name = 'Aqib'
    print(first_name)

    number = 12
    print(number)
    print(type(number))
    print(number * 10)

    float_number = 12.11
    print(float_number)
    print(type(float_number))

    is_playing = True
    print(is_playing)

    list_data = [1, 2, 3, [2, 'a', 3.4], [True, False], (1, 2, 3)]
    print(list_data)
    print(type(list_data))
    print(list_data[0])
    print(list_data[3])
    print(list_data[4][1])
    print(list_data[-1][1])
    print(type(list_data[-1]))

    list_data[1] += 10
    print(list_data)

    print("Length of list :", len(list_data))