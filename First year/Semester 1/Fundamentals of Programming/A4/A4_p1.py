"""
Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to n, such that
between any two numbers on consecutive positions, the difference in absolute value is at least m. If there is no
solution, display a message.
Recursive
"""


def is_already_in_list(list_to_verify, element_to_verify):
    for i in range(0, element_to_verify):
        if list_to_verify[i] == list_to_verify[element_to_verify]:
            return False
    return True


def min_difference_between_consecutive_elements(list_to_verify, element_to_verify, min_difference):
    if element_to_verify == 0:
        return True
    last_element = list_to_verify[element_to_verify-1]
    difference = last_element - list_to_verify[element_to_verify]
    if difference < 0:
        difference *= (-1)
    if difference >= min_difference:
        return True
    return False


answer_list = []
there_is_at_least_one_solution = 0


def display_all_solutions_having_the_min_difference_between_elements(min_difference, maximum_number, current_element_in_answer):
    global there_is_at_least_one_solution
    for i in range(1, maximum_number+1):
        answer_list.append(i)
        if is_already_in_list(answer_list, current_element_in_answer) and min_difference_between_consecutive_elements(answer_list, current_element_in_answer, min_difference):
            if current_element_in_answer > 0:
                print(answer_list)
                there_is_at_least_one_solution += 1
            display_all_solutions_having_the_min_difference_between_elements(min_difference, maximum_number, current_element_in_answer + 1)
        answer_list.pop()
    return there_is_at_least_one_solution


min_difference_in_absolute_value = int(input("Enter m: "))
max_number = int(input("Enter n: "))
number_of_solution = display_all_solutions_having_the_min_difference_between_elements(min_difference_in_absolute_value, max_number, 0)
if number_of_solution == 0:
    print("There are no solutions")
