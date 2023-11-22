#
# Write the implementation for A5 in this file
#
import random


def generate_random_complex_numbers():
    real_part = random.randint(1,20)
    imaginary_part = random.randint(1,20)
    complex_number = complex(real_part, imaginary_part)
    return complex_number


def represent_complex_number_to_string(complex_number):
    return f"{int(complex_number.real)}+{int(complex_number.imag)}i"


def extract_the_parts_of_the_complex_number(string_representing_a_complex_number):
    index_in_string = 0
    real_part = 0
    imaginary_part = 0
    while string_representing_a_complex_number[index_in_string] != '+':
        real_part = real_part * 10 + int(string_representing_a_complex_number[index_in_string])
        index_in_string += 1
    index_in_string += 1
    while index_in_string < len(string_representing_a_complex_number) - 1:
        imaginary_part = imaginary_part * 10 + int(string_representing_a_complex_number[index_in_string])
        index_in_string += 1
    complex_number = complex(real_part, imaginary_part)
    return complex_number


# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def add_complex_number_to_list(complex_number, list_of_complex_numbers):
    list_of_complex_numbers.append(represent_complex_number_to_string(complex_number))
    return list_of_complex_numbers
#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def add_complex_number_to_dictionary(complex_number, dictionary_of_complex_numbers, key):
    dictionary_of_complex_numbers[key] = represent_complex_number_to_string(complex_number)
    return dictionary_of_complex_numbers

#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def create_new_list_with_each_number_modulus(list_of_complex_numbers):
    list_with_each_numbers_modulus = []
    for i in range(len(list_of_complex_numbers)):
        complex_number = extract_the_parts_of_the_complex_number(list_of_complex_numbers[i])
        real_part = int(complex_number.real)
        imaginary_part = int(complex_number.imag)
        list_with_each_numbers_modulus.append(real_part*real_part+imaginary_part*imaginary_part)
    return list_with_each_numbers_modulus


def find_the_length_of_a_longest_subarray_of_numbers_with_the_same_modulus(list_of_complex_numbers):
    list_with_each_numbers_modulus = create_new_list_with_each_number_modulus(list_of_complex_numbers)
    start_index_of_maximum_subarray = 0
    start_index_of_current_subarray = 0
    previous_modulus = list_with_each_numbers_modulus[0]
    length_of_current_subarray = 1
    length_of_maximum_subarray = 1
    for i in range(1, len(list_of_complex_numbers)):
        current_modulus = list_with_each_numbers_modulus[i]
        if current_modulus == previous_modulus:
            length_of_current_subarray += 1
        else:
            if length_of_current_subarray > length_of_maximum_subarray:
                start_index_of_maximum_subarray = start_index_of_current_subarray
                length_of_maximum_subarray = length_of_current_subarray
                length_of_current_subarray = 1
            previous_modulus = current_modulus
            start_index_of_current_subarray = i
    if length_of_current_subarray > length_of_maximum_subarray:
        start_index_of_maximum_subarray = start_index_of_current_subarray
        length_of_maximum_subarray = length_of_current_subarray
    print_the_longest_subarray_of_elements_having_the_same_modulus(list_of_complex_numbers, start_index_of_maximum_subarray, length_of_maximum_subarray)


def put_in_answer_the_longest_increasing_subsequence(intermediate_length_of_longest_increasing_subsequence, list_of_complex_numbers, end_index_of_subsequence):
    answer_list = []
    answer_list.append(list_of_complex_numbers[end_index_of_subsequence])
    index_in_complex_numbers_list = end_index_of_subsequence - 1
    if intermediate_length_of_longest_increasing_subsequence[end_index_of_subsequence] == 0:
        return answer_list
    while True:
        if intermediate_length_of_longest_increasing_subsequence[index_in_complex_numbers_list] == intermediate_length_of_longest_increasing_subsequence[end_index_of_subsequence] - 1:
            answer_list.append(list_of_complex_numbers[index_in_complex_numbers_list])
            if intermediate_length_of_longest_increasing_subsequence[index_in_complex_numbers_list] == 0:
                answer_list.reverse()
                return answer_list
            end_index_of_subsequence = index_in_complex_numbers_list
        index_in_complex_numbers_list -= 1


def find_the_length_of_the_longest_increasing_subsequence(list_of_complex_numbers):
    list_with_each_numbers_modulus = create_new_list_with_each_number_modulus(list_of_complex_numbers)
    last_element_in_the_longest_increasing_subsequence = 0
    length_of_longest_increasing_subsequence = 0
    intermediate_length_of_longest_increasing_subsequence = []
    for i in range(len(list_with_each_numbers_modulus)):
        intermediate_length_of_longest_increasing_subsequence.append(0)
    for i in range(1, len(list_with_each_numbers_modulus)):
        for j in range(0, i):
            if list_with_each_numbers_modulus[i] >= list_with_each_numbers_modulus[j] and intermediate_length_of_longest_increasing_subsequence[i] < intermediate_length_of_longest_increasing_subsequence[j]+1:
                intermediate_length_of_longest_increasing_subsequence[i] = intermediate_length_of_longest_increasing_subsequence[j] + 1
                if intermediate_length_of_longest_increasing_subsequence[i] > length_of_longest_increasing_subsequence:
                    length_of_longest_increasing_subsequence = intermediate_length_of_longest_increasing_subsequence[i]
                    last_element_in_the_longest_increasing_subsequence = i
    answer_list = put_in_answer_the_longest_increasing_subsequence(intermediate_length_of_longest_increasing_subsequence, list_of_complex_numbers, last_element_in_the_longest_increasing_subsequence)
    return answer_list

#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#


def print_the_longest_subarray_of_elements_having_the_same_modulus(list_of_complex_numbers, start_index_of_subarray, length_of_subarray):
    print("The length of the longest subarray with the same modulus is: " + str(length_of_subarray))
    print("The elements of the subarray are:")
    for i in range(start_index_of_subarray, start_index_of_subarray + length_of_subarray):
        print(list_of_complex_numbers[i])


def read_complex_number_from_console():
    complex_number_string = str(input("Enter a complex number: "))
    complex_number = extract_the_parts_of_the_complex_number(complex_number_string)
    return complex_number


def write_complex_number_to_console(complex_number):
    print(represent_complex_number_to_string(complex_number))


def main_menu():
    list_of_complex_numbers = []
    dictionary_of_complex_numbers = {}
    while True:
        print("Options:")
        print("1.Generate 5 random complex numbers (these are added in the list and in the dictionary)")
        print("2.Add new complex numbers (to the list and to the dictionary)")
        print("3.Print the list of complex numbers")
        print("4.Print the dictionary of complex numbers")
        print("5.Print the length and elements of longest subarray of numbers having the same modulus")
        print("6.Print the length and elements of a longest increasing subsequence, when considering each number's modulus")
        option = int(input("Enter your option: "))
        if option == 1:
            for i in range(0,5):
                complex_number = generate_random_complex_numbers()
                list_of_complex_numbers = add_complex_number_to_list(complex_number, list_of_complex_numbers)
                dictionary_of_complex_numbers = add_complex_number_to_dictionary(complex_number, dictionary_of_complex_numbers, len(dictionary_of_complex_numbers))
        if option == 3:
            print()
            print("The list of complex numbers is")
            print(list_of_complex_numbers)
            print()
        if option == 4:
            print()
            print("The dictionary of complex numbers is")
            print(dictionary_of_complex_numbers)
            print()
        if option == 2:
            print()
            print("How many complex number do you want to add?")
            number_of_complex_elements = int(input("Enter the number of complex elements: "))
            for i in range(number_of_complex_elements):
                complex_number = read_complex_number_from_console()
                list_of_complex_numbers = add_complex_number_to_list(complex_number, list_of_complex_numbers)
                dictionary_of_complex_numbers = add_complex_number_to_dictionary(complex_number, dictionary_of_complex_numbers, len(dictionary_of_complex_numbers))
            print()
        if option == 5:
            print()
            find_the_length_of_a_longest_subarray_of_numbers_with_the_same_modulus(list_of_complex_numbers)
            print()
        if option == 6:
            print()
            answer_list = find_the_length_of_the_longest_increasing_subsequence(list_of_complex_numbers)
            print("The length of the longest increasing subsequence is: " + str(len(answer_list)))
            print("The elements of the longest increasing subsequence is:")
            print(answer_list)
            print()
        if option == 0:
            return


main_menu()
if __name__ == "__main__":
    print("Make magic happen")
