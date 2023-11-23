import functions
def decode_command(command):
    command_word = ''
    product_name = ''
    quantity = 0
    item_price = 0
    ok = True
    index = 0
    while command[index] != ' ' and index< len(command):
        command_word = command_word + command[index]
        index +=1
    index += 1
    if command_word == 'add':
        while command[index] != ' ' and index< len(command):
            product_name = product_name + command[index]
            index += 1
        index += 1
        while command[index] != ' ' and index < len(command):
            digit = int(command[index])
            quantity = quantity*10+digit
            index+=1
        index += 1
        while index <len(command):
            digit = int(command[index])
            item_price = item_price*10 + digit
            index+=1
        parameters = [product_name, quantity, item_price]
        return command_word, parameters
    if command_word == 'remove<' or command_word == 'remove>':
        number_to_compare_to = 0
        while index<len(command) and (command[index] <= '9' and command[index] >='0'):
            digit = int(command[index])
            number_to_compare_to = number_to_compare_to*10 + digit
            index+= 1
        return command_word, number_to_compare_to
    if command_word == 'list':
        parameter = ''
        while index<len(command):
            parameter = parameter + command[index]
            index+=1
        return command_word, parameter
    if command_word == 'end':
        return command_word, 0
def main_menu():
    list_of_contents = []
    list_of_contents = functions.create_contents(list_of_contents)
    while True:
        print(list_of_contents)
        command = input(">")
        command_word, parameters = decode_command(command)

        if command_word == 'add':
            list_of_contents = functions.add_new_contest_to_list(list_of_contents, parameters[0], parameters[1], parameters[2])
        if command_word == 'remove<':
            list_of_contents = functions.remove_less_than(list_of_contents, parameters)
        if command_word == 'remove>':
            list_of_contents = functions.remove_greater_than(list_of_contents, parameters)
        if command_word == 'list' and parameters == 'price':
            new_list = []
            for i in range(0, len(list_of_contents)):
                new_list.append(list_of_contents[i])
            new_list = functions.sort_in_ascending_order_by_price(new_list)
            print("The sorted list by prce is:")
            print(new_list)
        if command_word == 'list' and parameters == 'quantity':
            new_list = []
            for i in range(0, len(list_of_contents)):
                new_list.append(list_of_contents[i])
            new_list = functions.sort_in_ascending_order_by_quantity(new_list)
            print("The sorted list by quantity is:")
            print(new_list)
        if command_word == 'end':
            return



main_menu()

