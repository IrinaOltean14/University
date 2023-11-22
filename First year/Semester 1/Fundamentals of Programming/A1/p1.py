# Solve the problem from the first set here
# 4.For a given natural number n find the largest natural number written with the same digits. (e.g. n=3658, m=8653).

def decompose_my_number(given_number):
    """creates a frequency list of the digits of the entered number"""
    digits_of_my_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while given_number != 0:
        x = given_number % 10
        digits_of_my_number[x] += 1
        given_number //= 10
    return digits_of_my_number


def create_the_largest_natural_number_with_the_same_digits(digits_of_my_number):

    """"
    The frequency list is browsed in reverse (from 9 to 0) and depending on the number of occurrences of each digit,
    the required number (new number) is created
    """
    new_number = 0
    for i in range(9, -1, -1):
        if digits_of_my_number[i] != 0:
            for j in range(0, digits_of_my_number[i]):
                new_number = new_number*10+i
    return new_number


my_number = int(input("Enter a natural number n to find the largest natural number written with the same digits: "))
print("The largest natural number written with the same digits as the given number is "
      + str(create_the_largest_natural_number_with_the_same_digits(decompose_my_number(my_number))))
