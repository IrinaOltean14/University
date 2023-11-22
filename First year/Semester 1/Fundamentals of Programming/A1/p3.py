# Solve the problem from the third set here
# Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,...
# obtained from the sequence of natural numbers by replacing composed numbers
# with their prime divisors, without memorizing the elements of the sequence.
import math


def is_prime(x):
    # checks if the number x is prime (returns True) or not (returns False)
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
    return True


def prime_divisors_of_composed_number(composed_number, count_element):
    # the function finds the prime divisors of a composed number and increases the number of elements in the sequence
    # it returns a list
    # if the first element of the list is 0, the n-th element has been found
    # and the n-th element is the second element of the list
    # if the first element of the list is 1, the n-th element has not been found yet
    # and the second element of the list represents the number of elements we have to find until the n-th element
    divisor = 2
    answer_list = [0, 0]
    while composed_number != 1:
        power = 0
        while composed_number % divisor == 0:
            power = 1
            composed_number //= divisor
        if power != 0:
            count_element -= 1
        if count_element == 0:
            answer_list = [0, divisor]
            return answer_list
        divisor += 1
    answer_list = [1, count_element]
    return answer_list


def determine_nth_element(nth_element):
    # determines and returns the element on the n-th position
    current_element = 0
    current_natural_number = 1
    count_elements = nth_element
    while count_elements != 0:
        if current_natural_number == 1:
            current_element = 1
            count_elements -= 1
        elif is_prime(current_natural_number):
            current_element = current_natural_number
            count_elements -= 1
        else:
            composed_number_list = prime_divisors_of_composed_number(current_natural_number, count_elements)
            if composed_number_list[0] == 0:
                return composed_number_list[1]
            else:
                count_elements = int(composed_number_list[1])

        current_natural_number += 1
    return current_element


n = int(input("Enter n, representing the number of the element to be determined: "))
print(determine_nth_element(n))
