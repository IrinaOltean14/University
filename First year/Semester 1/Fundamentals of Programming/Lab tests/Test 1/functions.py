
def create_contents(list_of_contents):
    list_of_contents.append(['Servetele_de_nas', 5, 123])
    list_of_contents.append(['Paine_200g', 3, 50])
    list_of_contents.append(['Suc_natural', 10, 78])
    return list_of_contents


def add_new_contest_to_list(list_of_contents, name, quantity, price):

    list_of_contents.append([name, quantity, price])
    return list_of_contents


def remove_less_than(list_of_contents, minimum_price):
    length = len(list_of_contents)
    i = 0
    while (i< length):
        #print(i)
        if i>= length:
            break
        if list_of_contents[i][1] < minimum_price:
            list_of_contents.remove(list_of_contents[i])
            i -= 1
            length -= 1
        #print(i)
        ##print(length)
        #print(list_of_contents)
        i+=1
    return list_of_contents


def remove_greater_than(list_of_contents, minimum_price):
    length = len(list_of_contents)
    i = 0
    while (i< length):
        #print(i)
        if i>= length:
            break
        if list_of_contents[i][1] > minimum_price:
            list_of_contents.remove(list_of_contents[i])
            i -= 1
            length -= 1
        #print(i)
        ##print(length)
        #print(list_of_contents)
        i+=1
    return list_of_contents

"""
def remove_greater_than(list_of_contents, maximum_price):
    for i in range(0, len(list_of_contents) ):
        if list_of_contents[i][1] > maximum_price:
            list_of_contents.remove(list_of_contents[i])
            i -= 1
    return list_of_contents
"""


def sort_in_ascending_order_by_price(list_to_be_sorted):
    for i in range(0, len(list_to_be_sorted)):
        for j in range(i+1, len(list_to_be_sorted)):
            if list_to_be_sorted[i][1] > list_to_be_sorted[j][1]:
                list_to_be_sorted[i], list_to_be_sorted[j] = list_to_be_sorted[j], list_to_be_sorted[i]
    return list_to_be_sorted


def sort_in_ascending_order_by_quantity(list_to_be_sorted):
    for i in range(0, len(list_to_be_sorted)):
        for j in range(i+1, len(list_to_be_sorted)):
            if list_to_be_sorted[i][2] > list_to_be_sorted[j][2]:
                list_to_be_sorted[i], list_to_be_sorted[j] = list_to_be_sorted[j], list_to_be_sorted[i]
    return list_to_be_sorted
