"""
Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to n, such that
between any two numbers on consecutive positions, the difference in absolute value is at least m. If there is no
solution, display a message.
Iterative
"""
answer_list = []


def min_difference_between_consecutive_elements(last_of_element_of_stack, min_diff, element_to_add):
    difference = element_to_add - answer_list[last_of_element_of_stack - 1]
    if difference < 0:
        difference = difference * (-1)
    if difference < min_diff:
        return False
    return True


def is_already_in_list(last_element_of_stack, element_to_add):
    for i in range(0, last_element_of_stack):
        if element_to_add == answer_list[i]:
            return False
    return True


def display_all_solutions_having_the_min_difference_between_elements(min_difference, number_of_elements_in_answer):
    number_of_solutions = 0
    for i in range(1, number_of_elements_in_answer+1):
        answer_list.append(i)
        last_number = 0
        while len(answer_list) > 0:
            append_any_number_to_stack = False
            for j in range(last_number+1, number_of_elements_in_answer+1):
                if i != j and min_difference_between_consecutive_elements(len(answer_list), min_difference, j) and is_already_in_list(len(answer_list), j):
                    answer_list.append(j)
                    print(answer_list)
                    last_number = 0
                    number_of_solutions += 1
                    append_any_number_to_stack = True
                    break
            if not append_any_number_to_stack:
                last_number = answer_list.pop()
    return number_of_solutions


min_difference_in_absolute_value = int(input("Enter m: "))
max_number = int(input("Enter n: "))
number_of_solution = display_all_solutions_having_the_min_difference_between_elements(min_difference_in_absolute_value, max_number)
if number_of_solution == 0:
    print("There are no solutions")
