def second_nm(numbers):
    for i in range(len(numbers)):
        if (i % 2 != 0):
            print(numbers[i])


second_nm(range(10, 20))
