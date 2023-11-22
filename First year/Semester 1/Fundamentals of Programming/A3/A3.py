import random


def generate_list():
    print("How many elements should the list have?")
    number_of_elements = int(input("Enter a natural number representing the number of elements of the list: "))
    list_of_random_numbers = []
    for _ in range(0, number_of_elements):
        list_of_random_numbers.append(random.randint(0, 100))
    return list_of_random_numbers


def gen_list_for_timing(number_of_elements, type_of_list):
    """"
    if type_of_list = 1, it generates a list for the best case
    if type_of_list = 2 it generates a list for the average case
    if type_of_list = 3 it generates a list for the worst case
    (for gnome and cocktail sort)
    """
    import random
    list_of_random_numbers = []
    for i in range(0, number_of_elements):
        list_of_random_numbers.append(i)
    if type_of_list == 2:
        random.shuffle(list_of_random_numbers)
    elif type_of_list == 3:
        list_of_random_numbers.reverse()
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


def time(list):
    import timeit
    print("For list of " + str(len(list)) + " elements")
    print("The time using cocktail sort:")
    print(timeit.timeit(lambda: sorting_list_using_cocktail_sort(list), number=1))
    print("The time using gnome sort:")
    print(timeit.timeit(lambda: sorting_list_using_gnome_sort(list), number=1))


def start():
    list_of_natural_numbers = []
    while True:
        print("1. Generate a list of random natural numbers")
        print("2. Sort the list using the first algorithm (cocktail sort)")
        print("3. Sort the list using the second algorithm (gnome sort)")
        print("4. Sort for the best case")
        print("5. Sort for the average case")
        print("6. Sort for the worst case")
        print("0. Exit")
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
        elif opt == 4:
            list1 = gen_list_for_timing(500, 1)
            list2 = gen_list_for_timing(1000, 1)
            list3 = gen_list_for_timing(2000, 1)
            list4 = gen_list_for_timing(4000, 1)
            list5 = gen_list_for_timing(8000, 1)
            time(list1)
            time(list2)
            time(list3)
            time(list4)
            time(list5)
        elif opt == 5:
            list1 = gen_list_for_timing(500, 2)
            list2 = gen_list_for_timing(1000, 2)
            list3 = gen_list_for_timing(2000, 2)
            list4 = gen_list_for_timing(4000, 2)
            list5 = gen_list_for_timing(8000, 2)
            time(list1)
            time(list2)
            time(list3)
            time(list4)
            time(list5)
        elif opt == 6:
            list1 = gen_list_for_timing(500, 3)
            list2 = gen_list_for_timing(1000, 3)
            list3 = gen_list_for_timing(2000, 3)
            list4 = gen_list_for_timing(4000, 3)
            list5 = gen_list_for_timing(8000, 3)
            time(list1)
            time(list2)
            time(list3)
            time(list4)
            time(list5)
        elif opt == 0:
            return
        else:
            print("Bad command :(")


start()
