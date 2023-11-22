
import random


def generate_list():
    print("How many elements should the list have?")
    number_of_elements = int(input("Enter a natural number representing the number of elements of the list: "))
    list_of_random_numbers = []
    for _ in range(0, number_of_elements):
        list_of_random_numbers.append(random.randint(0, 100))
    return list_of_random_numbers


def sorting_list_using_cocktail_sort(list_to_sort):
    length_of_list = len(list_to_sort)
    beginning = 0
    end = length_of_list
    indicator_of_list_order = True
    while indicator_of_list_order:
        indicator_of_list_order = False
        for i in range(beginning, end - 1):
            if list_to_sort[i] > list_to_sort[i+1]:
                x = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i+1]
                list_to_sort[i+1] = x
                indicator_of_list_order = True
        if not indicator_of_list_order:
            break
        indicator_of_list_order = False
        end = end - 1
        for i in range(end-1, beginning-1, -1):
            if list_to_sort[i] > list_to_sort[i+1]:
                x = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i+1]
                list_to_sort[i+1] = x
                indicator_of_list_order = True
        beginning = beginning + 1
    return list_to_sort


def sorting_list_using_gnome_sort(list_to_sort):
    index = 0
    n = len(list_to_sort)
    while index < n:
        if index == 0:
            index = 1
        elif list_to_sort[index] >= list_to_sort[index-1]:
            index = index + 1
        else:
            x = list_to_sort[index]
            list_to_sort[index] = list_to_sort[index-1]
            list_to_sort[index-1] = x
            index = index - 1
    return list_to_sort


def start():
    list_of_natural_numbers = []
    while True:
        print("1. Generate a list of random natural numbers")
        print("2. Sort the list using the first algorithm (cocktail sort)")
        print("3. Sort the list using the second algorithm (gnome sort)")
        print("0. Exit")
        sorted_list1 = []
        sorted_list2 = []
        opt = int(input("Enter your option: "))
        if opt == 1:
            list_of_natural_numbers = generate_list()
            print(list_of_natural_numbers)
        elif opt == 2:
            sorted_list1 = sorting_list_using_cocktail_sort(list_of_natural_numbers)
            print(sorted_list1)
        elif opt == 3:
            sorted_list2 = sorting_list_using_gnome_sort(list_of_natural_numbers)
            print(sorted_list2)
        elif opt == 0:
            return
        else:
            print("Bad command :(")


start()
