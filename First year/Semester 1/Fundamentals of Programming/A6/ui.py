#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements)
# are found here
#
import functions


def process_command(user_command):
    # remove leading and trailing whitespace
    command_word = ''
    first_word = True
    parameters = []
    user_command = user_command.strip()
    i = 0
    while i < len(user_command):
        if user_command[i] == " ":
            pass
        elif user_command[i] >= '0' and user_command[i] <= '9':
            parameter = 0
            while user_command[i] >= '0' and user_command[i] <= '9':
                parameter = parameter * 10 + int(user_command[i])
                i += 1
                if i >= len(user_command):
                    break
            parameters.append(parameter)
            i -= 1
        elif (user_command[i] >= 'a' and user_command[i] <= 'z') or (user_command[i]>='A' and user_command[i]<='Z'):
            word = ''
            while (user_command[i] >= 'a' and user_command[i] <= 'z') or (user_command[i]>='A' and user_command[i]<='Z'):
                word = word + user_command[i]
                i += 1
                if i >= len(user_command):
                    break
            if first_word:
                command_word = word
                first_word = False
            else:
                command_word = command_word + ' ' + word
            i -= 1
        elif user_command[i] == '>' or user_command[i] == '<' or user_command[i] == '=':
            command_word = command_word + ' ' + user_command[i]
        i += 1
    return command_word, parameters


def start():
    list_with_participants_results = functions.construct_list()
    print(list_with_participants_results)
    list_history = []
    while True:
        valid_command = True
        user_command = input(">")
        command_word, parameters = process_command(user_command)
        previous_list = []
        for i in range(0, len(list_with_participants_results)):
            previous_list.append([list_with_participants_results[i][0], list_with_participants_results[i][1], list_with_participants_results[i][2]])
        if command_word == 'add':
            try:
                list_with_participants_results = functions.add_new_participant_to_list(list_with_participants_results, parameters)
            except ValueError as ve:
                print("Error: ", ve)
        elif command_word == 'insert at':
            try:
                list_with_participants_results = functions.add_new_participant_at_certain_position(list_with_participants_results, parameters)
            except ValueError as ve:
                print('Error: ', ve)
        elif command_word == 'remove':
            try:
                list_with_participants_results = functions.remove_the_score_of_a_participant(list_with_participants_results, parameters)
            except ValueError as ve:
                print('Error: ', ve)
        elif command_word == "remove to":
            try:
                list_with_participants_results = functions.remove_the_score_of_several_participants(list_with_participants_results, parameters)
            except ValueError as ve:
                print('Error: ', ve)
        elif command_word == 'replace P with':
            try:
                list_with_participants_results = functions.replace_the_score_obtained_by_a_participant_at_certain_problem(list_with_participants_results, parameters)
            except ValueError as ve:
                print('Error: ', ve)
        elif command_word == 'list':
            print(list_with_participants_results)
            valid_command = False
        elif command_word == 'list =':

            average = parameters[0]
            average_list = functions.create_list_with_each_participants_average_score(list_with_participants_results)
            for i in range(0, len(average_list)):
                if average_list[i] == average:
                    print(list_with_participants_results[i])
            valid_command = False
        elif command_word == 'list >':
            if len(parameters) != 1:
                print("Error: The number of parameters given is not correct")
            else:
                average = parameters[0]
                average_list = functions.create_list_with_each_participants_average_score(list_with_participants_results)
                for i in range(0, len(average_list)):
                    if average_list[i] > average:
                        print(list_with_participants_results[i])
            valid_command = False
        elif command_word == 'list <':
            if len(parameters) != 1:
                print("Error: The number of parameters given is not correct")
            else:
                average = parameters[0]
                average_list = functions.create_list_with_each_participants_average_score(list_with_participants_results)
                for i in range(0, len(average_list)):
                    if average_list[i] < average:
                        print(list_with_participants_results[i])
            valid_command = False
        elif command_word == 'top':
            average_list = functions.create_list_with_each_participants_average_score(list_with_participants_results)
            try:
                participants_in_top_list = functions.create_top_based_on_average_score(list_with_participants_results, average_list, parameters)
                print("The top is:")
                for i in range(0, parameters[0]):
                    print(participants_in_top_list[i])
            except ValueError as ve:
                print('Error: ', ve)
            valid_command = False
        elif command_word == 'remove >':
            average_list = functions.create_list_with_each_participants_average_score(list_with_participants_results)
            try:
                list_with_participants_results = functions.remove_if_average_score_greater_than_a_value(list_with_participants_results, average_list, parameters)
            except ValueError as ve:
                print('Error: ' , ve)
        elif command_word == 'remove <':
            average_list = functions.create_list_with_each_participants_average_score(list_with_participants_results)
            try:
                list_with_participants_results = functions.remove_if_average_score_less_than_a_value(list_with_participants_results, average_list, parameters)
            except ValueError as ve:
                print('Error: ', ve)
        elif command_word == 'end':
            return
        elif command_word == 'undo':
            list_with_participants_results = list_history[len(list_history) - 1]
            list_history.pop()
            valid_command = False
        else:
            print('Invalid command')
            valid_command = False
        if valid_command:
            list_history.append(previous_list)
        #print(list_history)
        print("The list is:")
        print(list_with_participants_results)


