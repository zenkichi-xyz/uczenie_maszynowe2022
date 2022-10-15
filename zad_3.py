def is_even(number: int) -> bool:
    return(number % 2 == 0)

valid = is_even(3)
if valid:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
