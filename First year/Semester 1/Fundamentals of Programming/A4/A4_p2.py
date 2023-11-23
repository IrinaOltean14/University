"""
Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k.
For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14
"""


def search_for_a_subset_with_the_given_sum(set_of_positive_integers, number_of_elements, sum_to_search_for):
    intermediate_sum_values_matrix = [[]]
    intermediate_sum_values_matrix = [[False for i in range(sum_to_search_for + 1)] for j in range(number_of_elements)]
    for i in range(number_of_elements):
        intermediate_sum_values_matrix[i][0] = True
    if set_of_positive_integers[0] <= sum_to_search_for:
        intermediate_sum_values_matrix[0][set_of_positive_integers[0]] = True
    for i in range(1, number_of_elements):
        for j in range(0, sum_to_search_for + 1):
            if set_of_positive_integers[i] <= j:
                intermediate_sum_values_matrix[i][j] = (intermediate_sum_values_matrix[i - 1][j] or intermediate_sum_values_matrix[i - 1][j - set_of_positive_integers[i]])
            else:
                intermediate_sum_values_matrix[i][j] = intermediate_sum_values_matrix[i - 1][j]
    for i in range(0, number_of_elements):
        print(intermediate_sum_values_matrix[i])
    return intermediate_sum_values_matrix


def print_subset_having_the_given_sum(intermediate_sum_values_matrix, set_of_positive_integers, number_of_elements, sum_to_search_for, answer_list, found_answer):
    if found_answer == 0:
        if number_of_elements == 0 and sum_to_search_for != 0 and intermediate_sum_values_matrix[0][sum_to_search_for]:
            answer_list.append(set_of_positive_integers[number_of_elements])
            answer_list.reverse()
            print(answer_list)
            found_answer = 1
            return
        if number_of_elements == 0 and sum_to_search_for == 0:
            answer_list.reverse()
            print(answer_list)
            found_answer = 1
            return
        if intermediate_sum_values_matrix[number_of_elements - 1][sum_to_search_for]:
            new_list = []
            new_list.extend(answer_list)
            print_subset_having_the_given_sum(intermediate_sum_values_matrix, set_of_positive_integers, number_of_elements - 1, sum_to_search_for, new_list, found_answer)
        if sum_to_search_for >= set_of_positive_integers[number_of_elements]:
            if intermediate_sum_values_matrix[number_of_elements - 1][sum_to_search_for - set_of_positive_integers[number_of_elements]]:
                answer_list.append(set_of_positive_integers[number_of_elements])
                print_subset_having_the_given_sum(intermediate_sum_values_matrix, set_of_positive_integers, number_of_elements - 1, sum_to_search_for - set_of_positive_integers[number_of_elements], answer_list, found_answer)
    else:
        return


def input_problem_data():
    number_of_elements = (int(input("Enter the number of elements: ")))
    set_of_positive_integers = []
    for i in range(0, number_of_elements):
        set_of_positive_integers.append(int(input("Enter the element at position " + str(i) + ": ")))
    given_sum = int(input("Enter the sum to search for in the set: "))
    answer_matrix = search_for_a_subset_with_the_given_sum(set_of_positive_integers, number_of_elements, given_sum)
    if not answer_matrix[number_of_elements-1][given_sum]:
        print("There are no subsets with the given sum")
    else:
        print_subset_having_the_given_sum(answer_matrix, set_of_positive_integers, number_of_elements-1, given_sum, [], 0)


input_problem_data()
