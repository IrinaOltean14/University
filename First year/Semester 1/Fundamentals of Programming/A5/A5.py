"""
Set A: Length and elements of a longest subarray of numbers having the same modulus.
Set B: The length and elements of a longest increasing subsequence, when considering each number's modulus
"""


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
    complex_number_tuple = (real_part, imaginary_part)
    return complex_number_tuple

# The following functions are used for the list representation


def create_new_list_with_each_number_modulus(list_of_complex_numbers):
    list_with_each_numbers_modulus = []
    for i in range(len(list_of_complex_numbers)):
        real_part = list_of_complex_numbers[i][0]
        imaginary_part = list_of_complex_numbers[i][1]
        list_with_each_numbers_modulus.append(real_part*real_part + imaginary_part*imaginary_part)
    return list_with_each_numbers_modulus


def print_the_longest_increasing_subsequence(intermediate_length_of_longest_increasing_subsequence, list_of_complex_numbers, end_index_of_subsequence):
    answer_list = []
    answer_list.append(represent_complex_number_to_string(list_of_complex_numbers[end_index_of_subsequence]))
    index_in_complex_numbers_list = end_index_of_subsequence - 1
    if intermediate_length_of_longest_increasing_subsequence[end_index_of_subsequence] == 0:
        print("The length of the longest increasing subsequence when considering a number's modulus is " + str(len(answer_list)))
        print("The longest increasing subsequence is:")
        print(answer_list)
        return
    while True:
        if intermediate_length_of_longest_increasing_subsequence[index_in_complex_numbers_list] == intermediate_length_of_longest_increasing_subsequence[end_index_of_subsequence] - 1:
            answer_list.append(represent_complex_number_to_string(list_of_complex_numbers[index_in_complex_numbers_list]))
            if intermediate_length_of_longest_increasing_subsequence[index_in_complex_numbers_list] == 0:
                answer_list.reverse()
                print("The length of the longest increasing subsequence when considering a number's modulus is " + str(len(answer_list)))
                print("The longest increasing subsequence is:")
                print(answer_list)
                return
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
    print_the_longest_increasing_subsequence(intermediate_length_of_longest_increasing_subsequence,list_of_complex_numbers, last_element_in_the_longest_increasing_subsequence)


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


def represent_complex_number_to_string(complex_number):
    return f"{complex_number[0]}+{complex_number[1]}i"


def print_the_longest_subarray_of_elements_having_the_same_modulus(list_of_complex_numbers, start_index_of_subarray, length_of_subarray):
    print("The length of the longest subarray with the same modulus is: " + str(length_of_subarray))
    print("The elements of the subarray are:")
    for i in range(start_index_of_subarray, start_index_of_subarray + length_of_subarray):
        print(represent_complex_number_to_string(list_of_complex_numbers[i]))


def add_complex_number_in_list(complex_number_tuple, list_of_complex_numbers):
    list_of_complex_numbers.append(complex_number_tuple)
    return list_of_complex_numbers

# Here the functions for the list representation end
# The following functions are used for the dictionary representation


def calculate_modulus(complex_number):
    complex_number_tuple = extract_the_parts_of_the_complex_number(complex_number)
    real_part = complex_number_tuple[0]
    imaginary_part = complex_number_tuple[1]
    return real_part*real_part+imaginary_part*imaginary_part


def print_the_longest_subarray_of_elements_having_the_same_modulus_dict(dictionary_of_complex_numbers, start_index_of_subarray, length_of_subarray):
    print("The length of the longest subarray with the same modulus is: " + str(length_of_subarray))
    print("The elements of the subarray are:")
    for i in range(start_index_of_subarray, start_index_of_subarray + length_of_subarray):
        print(dictionary_of_complex_numbers[i])


def find_the_length_of_a_longest_subarray_of_numbers_with_the_same_modulus_dict(dictionary_of_complex_numbers):
    start_index_of_maximum_subarray = 0
    start_index_of_current_subarray = 0
    previous_modulus = calculate_modulus(dictionary_of_complex_numbers[0])
    length_of_current_subarray = 1
    length_of_maximum_subarray = 1
    for i in range(1, len(dictionary_of_complex_numbers)):
        current_modulus = calculate_modulus(dictionary_of_complex_numbers[i])
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
    print_the_longest_subarray_of_elements_having_the_same_modulus_dict(dictionary_of_complex_numbers, start_index_of_maximum_subarray, length_of_maximum_subarray)


def print_the_longest_increasing_subsequence_dict(intermediate_length_of_longest_increasing_subsequence, dictionary_of_complex_numbers, end_index_of_subsequence):
    answer_list = []
    answer_list.append(dictionary_of_complex_numbers[end_index_of_subsequence])
    index_in_complex_numbers_list = end_index_of_subsequence - 1
    if intermediate_length_of_longest_increasing_subsequence[end_index_of_subsequence] == 0:
        print("The length of the longest increasing subsequence when considering a number's modulus is " + str(len(answer_list)))
        print("The longest increasing subsequence is:")
        print(answer_list)
        return
    while True:
        if intermediate_length_of_longest_increasing_subsequence[index_in_complex_numbers_list] == intermediate_length_of_longest_increasing_subsequence[end_index_of_subsequence] - 1:
            answer_list.append(dictionary_of_complex_numbers[index_in_complex_numbers_list])
            if intermediate_length_of_longest_increasing_subsequence[index_in_complex_numbers_list] == 0:
                answer_list.reverse()
                print("The length of the longest increasing subsequence when considering a number's modulus is " + str(len(answer_list)))
                print("The longest increasing subsequence is:")
                print(answer_list)
                return
            end_index_of_subsequence = index_in_complex_numbers_list
        index_in_complex_numbers_list -= 1


def find_the_length_of_the_longest_increasing_subsequence_dict(dictionary_of_complex_numbers):
    last_element_in_the_longest_increasing_subsequence = 0
    length_of_longest_increasing_subsequence = 0
    intermediate_length_of_longest_increasing_subsequence = []
    for i in range(len(dictionary_of_complex_numbers)):
        intermediate_length_of_longest_increasing_subsequence.append(0)
    for i in range(1, len(dictionary_of_complex_numbers)):
        for j in range(0, i):
            modulus_i = calculate_modulus(dictionary_of_complex_numbers[i])
            modulus_j = calculate_modulus(dictionary_of_complex_numbers[j])
            if modulus_i >= modulus_j and intermediate_length_of_longest_increasing_subsequence[i] < intermediate_length_of_longest_increasing_subsequence[j]+1:
                intermediate_length_of_longest_increasing_subsequence[i] = intermediate_length_of_longest_increasing_subsequence[j] + 1
                if intermediate_length_of_longest_increasing_subsequence[i] > length_of_longest_increasing_subsequence:
                    length_of_longest_increasing_subsequence = intermediate_length_of_longest_increasing_subsequence[i]
                    last_element_in_the_longest_increasing_subsequence = i
    print_the_longest_increasing_subsequence_dict(intermediate_length_of_longest_increasing_subsequence,dictionary_of_complex_numbers, last_element_in_the_longest_increasing_subsequence)


def main_menu():
    print("How many complex numbers do you want to implement?")
    print("The complex numbers have to be given in the form: a+bi")
    number_of_complex_elements = int(input("Enter the number of complex elements: "))
    list_of_complex_numbers = []
    dictionary_of_complex_numbers = {}
    for i in range(number_of_complex_elements):
        complex_number_string = input("Enter the complex number at position " + str(i) + ": ")
        complex_number_tuple = extract_the_parts_of_the_complex_number(complex_number_string)
        add_complex_number_in_list(complex_number_tuple, list_of_complex_numbers)
        dictionary_of_complex_numbers[i] = complex_number_string
    print("The following results are obtained using the LIST representations of the complex numbers")
    print(list_of_complex_numbers)
    find_the_length_of_a_longest_subarray_of_numbers_with_the_same_modulus(list_of_complex_numbers)
    find_the_length_of_the_longest_increasing_subsequence(list_of_complex_numbers)
    print()
    print("The following results are obtained using the DICTIONARY representations of the complex numbers")
    print(dictionary_of_complex_numbers)
    find_the_length_of_a_longest_subarray_of_numbers_with_the_same_modulus_dict(dictionary_of_complex_numbers)
    find_the_length_of_the_longest_increasing_subsequence_dict(dictionary_of_complex_numbers)


main_menu()
