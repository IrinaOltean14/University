
from src.domain import As
class Service:
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator

    def display_assign(self):
        return self._repo.display_assign()

    def add_assign(self, id, name, solution):
        assign = As(id, name, solution)
        # Verify if the assign to be added is a valid one
        self._validator.validate(assign, self._repo.display_assign())
        # If the assign is valid, the assign is added to the list
        self._repo.add_assign(assign)

    def dishonesty_check(self):
        assign_list = self._repo.display_assign()
        dishonesty_list = []
        for index1 in range(0, len(assign_list)):
            for index2 in range(index1+1, len(assign_list)):
                assign1 = assign_list[index1]
                assign2 = assign_list[index2]
                solution1 = assign1.solution
                solution2 = assign2.solution
                words1 = solution1.split(' ')
                words2 = solution2.split(' ')
                sim = 0
                for word1 in words1:
                    for word2 in words2:
                        word1 = word1.strip()
                        word2 = word2.strip()
                        #print(word1, word2)
                        if word1 == word2 and word1 != ' ':
                            sim += 1
                #print(sim)
                if len(words1) < len(words2):
                    percentage = (sim*100)/len(words1)
                    if percentage > 20:
                        dishonesty_list.append(assign1.name + ' ' + assign2.name+ ' ' + '(' + str(percentage) + '% of ' + assign1.name + "'s solution)")
                else:
                    percentage = (sim * 100) / len(words2)
                    if percentage > 20:
                        dishonesty_list.append(assign1.name + ' ' + assign2.name + ' ' + '(' + str(
                            percentage) + '% of ' + assign2.name + "'s solution)")
        return dishonesty_list


class ValidationError(Exception):
    pass


class AsValidator:
    def __init__(self):
        pass

    def validate(self, assign, assign_list):
        # This function checks if an assignment is valid
        error = ""
        id = assign.id
        ok = True
        # Check if id is integer
        try:
            val = int(id)
        except ValueError:
            error += 'Id is not an integer '
            ok = False
        # Check if id is unique
        if ok:
            for asi in assign_list:
                if asi.id == id:
                    error += 'Id is not unique '
        # Check if name has at least 3 characters
        if len(assign.name) <= 2:
            error += 'Name is too short '
        # Check if the solution is not empty
        if len(assign.solution) == 0:
            error += 'Solution can not be empty '

        if len(error) > 0:
            raise ValidationError(error)


