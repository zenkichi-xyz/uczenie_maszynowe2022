def every_second_number(numbers):
    for i in range(len(numbers)):
        if (i % 2 != 0):
            print(numbers[i])


print('\nZadanie d')
every_second_number(range(0, 10))
