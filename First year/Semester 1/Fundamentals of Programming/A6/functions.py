#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print
# statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import random


def construct_list():
    list_with_participants_results = []
    for i in range(0,10):
        problem1 = random.randint(0,10)
        problem2 = random.randint(0,10)
        problem3 = random.randint(0,10)
        list_with_participants_results.append([problem1, problem2, problem3])
    return list_with_participants_results
def remove_if_average_score_less_than_a_value(list_with_participant_result, average_score_list, parameters):
    if len(parameters) != 1:
        raise ValueError("The number of parameters given is not correct (1 needed)")
    value = parameters[0]
    for i in range(0, len(average_score_list)):
        if average_score_list[i] < value:
            list_with_participant_result[i][0] = 0
            list_with_participant_result[i][1] = 0
            list_with_participant_result[i][2] = 0
    return list_with_participant_result


def remove_if_average_score_greater_than_a_value(list_with_participant_result, average_score_list, parameters):
    if len(parameters) != 1:
        raise ValueError("The number of parameters given is not correct (1 needed)")
    value = parameters[0]
    for i in range(0, len(average_score_list)):
        if average_score_list[i] > value:
            list_with_participant_result[i][0] = 0
            list_with_participant_result[i][1] = 0
            list_with_participant_result[i][2] = 0
    return list_with_participant_result


def create_top_based_on_average_score(list_with_participants_results, average_score_list, parameters):
    if len(parameters) != 1:
        raise ValueError("The number of parameters given is not correct (1 needed)")
    if parameters[0] > len(list_with_participants_results) - 1:
        raise ValueError("There are not enough participants to create the top (give a smaller number)")
    top_list = []
    for i in range(0, len(list_with_participants_results)):
        top_list.append(list_with_participants_results[i])
    for i in range(0, len(average_score_list)):
        for j in range(i, len(average_score_list)):
            if average_score_list[i] < average_score_list[j]:
                average_score_list[i], average_score_list[j] = average_score_list[j], average_score_list[i]
                top_list[i] , top_list[j] = top_list[j], top_list[i]
    #print(list_with_participants_results)
    return top_list


def create_list_with_each_participants_average_score(list_with_participants_results):
    average_score_list = []
    for i in range(0, len(list_with_participants_results)):
        average = (list_with_participants_results[i][0]+list_with_participants_results[i][1]+ list_with_participants_results[i][2])/3
        average_score_list.append(average)
    return average_score_list


def replace_the_score_obtained_by_a_participant_at_certain_problem(list_with_participants, parameters):
    if len(parameters) != 3:
        raise ValueError("The number of parameters given is not correct (3 needed)")
    if parameters[0] < 0 or parameters[0] > len(list_with_participants):
        raise ValueError("The first parameter is not a valid participant (parameter too small or too big)")
    if parameters[1] < 1 or parameters[1] > 3:
        raise ValueError("The second parameter is not a valid problem number (must be between 1 and 3)")
    if parameters[2] < 0 or parameters[2] > 10:
        raise ValueError("The third parameter is not a valid problem score (must be between o and 10)")
    participant = parameters[0]
    number_of_problem = parameters[1]
    replacement = parameters[2]
    list_with_participants[participant][number_of_problem-1] = replacement
    return list_with_participants


def test_replace_the_score_obtained_by_a_participant_at_a_certain_problem():
    list_with_participants = construct_list()
    try:
        parameters = [1, 2, 3, 4,5]
        replace_the_score_obtained_by_a_participant_at_certain_problem(list_with_participants, parameters)
        assert False
    except ValueError:
        assert True
    try:
        parameters = [15,2,9]
        replace_the_score_obtained_by_a_participant_at_certain_problem(list_with_participants, parameters)
        assert False
    except ValueError:
        assert True

    try:
        parameters = [7,7,8]
        replace_the_score_obtained_by_a_participant_at_certain_problem(list_with_participants, parameters)
        assert False
    except ValueError:
        assert True
    try:
        parameters = [7, 2, 11]
        replace_the_score_obtained_by_a_participant_at_certain_problem(list_with_participants, parameters)
        assert False
    except ValueError:
        assert True
    try:
        parameters = [7, 2, 9]
        replace_the_score_obtained_by_a_participant_at_certain_problem(list_with_participants, parameters)
        assert True
    except ValueError:
        assert False

#test_replace_the_score_obtained_by_a_participant_at_a_certain_problem()
def remove_the_score_of_several_participants(list_with_participants_results, positions):
    if len(positions) != 2:
        raise ValueError("The number of parameters given is not correct (2 needed)")
    if positions[0] < 0:
        raise ValueError("The first position is smaller than 0")
    if positions[1] > len(list_with_participants_results) - 1:
        raise ValueError("The second position is bigger than the number of participants")
    for i in range(positions[0], positions[1]+1):
        list_with_participants_results[i][0] = 0
        list_with_participants_results[i][1] = 0
        list_with_participants_results[i][2] = 0
    return list_with_participants_results


def test_remove_the_score_of_several_participants():
    list_with_participants = construct_list()
    try:
        positions = [1]
        remove_the_score_of_several_participants(list_with_participants, positions)
        assert False
    except ValueError:
        assert True
    try:
        positions = [1, 67]
        remove_the_score_of_several_participants(list_with_participants, positions)
        assert False
    except ValueError:
        assert True
    try:
        positions = [1,4]
        remove_the_score_of_several_participants(list_with_participants, positions)
        assert True
    except ValueError:
        assert True


#test_remove_the_score_of_several_participants()
def remove_the_score_of_a_participant(list_with_participants, position):
    if len(position) != 1:
        raise ValueError("The number of parameters given is not correct (1 needed)")
    if position[0] < 0 or position[0] > len(list_with_participants)-1:
        raise ValueError("The parameter given is not a position in the list")
    list_with_participants[position[0]][0] = 0
    list_with_participants[position[0]][1] = 0
    list_with_participants[position[0]][2] = 0
    return list_with_participants

def test_remove_the_score_of_a_participant():
    list_with_participants = construct_list()
    try:
        position = [1,2]
        remove_the_score_of_a_participant(list_with_participants, position)
        assert False
    except ValueError:
        assert True
    try:
        position = [25]
        remove_the_score_of_a_participant(list_with_participants, position)
        assert False
    except ValueError:
        assert True
    try:
        position = [7]
        remove_the_score_of_a_participant(list_with_participants, position)
        assert True
    except ValueError:
        assert True


#test_remove_the_score_of_a_participant()
def add_new_participant_to_list(list_with_participants_results, scores):
    if len(scores) != 3:
        raise ValueError("The number of scores is not correct")
    if scores[0] < 0 or scores[0] > 10:
        raise ValueError("The first score is not between 0 and 10")
    if scores[1] < 0 or scores[1] > 10:
        raise ValueError("The second score is not between 0 and 10")
    if scores[2] < 0 or scores[2] > 10:
        raise ValueError("The third score is not between 0 and 10")
    list_with_participants_results.append([scores[0], scores[1], scores[2]])
    return list_with_participants_results


def test_add_new_participant_to_list():
    list_with_participants = construct_list()
    try:
        scores = [11, 10, 99]
        add_new_participant_to_list(list_with_participants, scores)
        assert False
    except ValueError:
        assert True
    try:
        scores = [1,10,0]
        add_new_participant_to_list(list_with_participants, scores)
        assert list_with_participants[len(list_with_participants)-1] == scores
    except ValueError:
        assert False


def add_new_participant_at_certain_position(list_with_participant_results, parameters):
    if len(parameters) != 4:
        raise ValueError("The number of parameters given is not correct (4 needed)")
    if parameters[0] < 0 or parameters[0] > 10:
        raise ValueError("The first score is not between 0 and 10")
    if parameters[1] < 0 or parameters[1] > 10:
        raise ValueError("The second score is not between 0 and 10")
    if parameters[2] < 0 or parameters[2] > 10:
        raise ValueError("The third score is not between 0 and 10")
    if parameters[3] > len(list_with_participant_results) or parameters[3] < 0:
        raise ValueError("The position given is bigger than the length of participants list or smaller than 0 (insertion can not be made)")
    scores = [parameters[0], parameters[1], parameters[2]]
    position = parameters[3]
    list_with_participant_results.insert(position, [scores[0], scores[1], scores[2]])
    return list_with_participant_results


def test_add_new_participant_to_certain_position():
    list_with_participants = construct_list()
    try:
        parameters = [11, 9, 9, 5]
        add_new_participant_at_certain_position(list_with_participants, parameters)
        assert False
    except ValueError:
        assert True
    try:
        parameters = [2, 3, 4, 23]
        add_new_participant_at_certain_position(list_with_participants, parameters)
        assert False
    except ValueError:
        assert True
    try:
        parameters = [1, 7, 9, 6]
        add_new_participant_at_certain_position(list_with_participants, parameters)
        assert list_with_participants[parameters[3]] == [parameters[0], parameters[1], parameters[2]]
    except ValueError:
        assert False

#test_add_new_participant_to_certain_position()
