"""
Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k.
For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.
"""


def search_for_a_subset_with_the_given_sum(set_of_positive_integers, number_of_elements, sum_to_search_for):
    if sum_to_search_for == 0:
        return True
    if number_of_elements == 0 and sum_to_search_for:
        return False
    if set_of_positive_integers[number_of_elements - 1] > sum_to_search_for:
        return search_for_a_subset_with_the_given_sum(set_of_positive_integers, number_of_elements - 1, sum_to_search_for)
    else:
        return search_for_a_subset_with_the_given_sum(set_of_positive_integers, number_of_elements - 1, sum_to_search_for - set_of_positive_integers[number_of_elements - 1]) or search_for_a_subset_with_the_given_sum(set_of_positive_integers, number_of_elements - 1, sum_to_search_for)


def print_subset_having_the_given_sum(set_of_positive__integers, number_of_elements, sum_to_search_for, answer_list, found_answer):
    if found_answer == 0:
        if sum_to_search_for == 0:
            found_answer = 1
            answer_list.reverse()
            print(answer_list)
            return
        if number_of_elements == 0 and sum_to_search_for:
            return
        if sum_to_search_for >= set_of_positive__integers[number_of_elements - 1]:
            new_list = []
            new_list.extend(answer_list)
            new_list.append(set_of_positive__integers[number_of_elements - 1])
            print_subset_having_the_given_sum(set_of_positive__integers, number_of_elements - 1, sum_to_search_for - set_of_positive__integers[number_of_elements - 1], new_list, found_answer)
        print_subset_having_the_given_sum(set_of_positive__integers, number_of_elements - 1, sum_to_search_for, answer_list, found_answer)
    else:
        return


def input_problem_data():
    number_of_elements = (int(input("Enter the number of elements: ")))
    set_of_positive_integers = []
    for i in range(0, number_of_elements):
        set_of_positive_integers.append(int(input("Enter the element at position " + str(i) + ": ")))
    given_sum = int(input("Enter the sum to search for in the set: "))
    if search_for_a_subset_with_the_given_sum(set_of_positive_integers, number_of_elements, given_sum):
        print("There is a subset with the given sum")
        print_subset_having_the_given_sum(set_of_positive_integers, number_of_elements, given_sum, [], 0)
    else:
        print("There is no subset with the given sum")



input_problem_data()