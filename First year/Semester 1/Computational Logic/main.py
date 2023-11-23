def convert_result_list_to_result_string(result_list):
    # This function transforms a list (the elements represent the digits of the result) into a string representing
    # the result
    result_string = ''
    index = len(result_list) - 1
    while result_list[index] == 0 and index > 0:
        result_list.pop()
        index -= 1
    index = len(result_list) - 1
    while index >= 0:
        digit = result_list[index]
        if digit > 9:
            digit_str = chr(digit + 55)
        else:
            digit_str = str(digit)
        result_string += digit_str
        index -= 1
    return result_string


def power_of_two(base):
    # This function checks if a given base is a power of 2 (2, 4, 8 or 16)
    if base == 2 or base == 4 or base == 8 or base == 16:
        return True
    return False


def division_of_two_numbers_in_a_base_p(dividend, divisor, base):
    # This function performs the division of a number and a digit in a given base
    # The division is performed like on paper
    result_list = []
    length_of_dividend = len(dividend)
    transport = 0
    if divisor >= 'A' and divisor <= 'Z':
        divisor_int = ord(divisor) - 55
    else:
        divisor_int = int(divisor)
    for index in range(0, length_of_dividend):
        current_digit = dividend[index]
        if current_digit >= 'A' and current_digit <= 'Z':
            current_digit_int = ord(current_digit) - 55
        else:
            current_digit_int = int(current_digit)
        result_digit = (base * transport + current_digit_int) // divisor_int
        transport = (base * transport + current_digit_int) % divisor_int
        result_list.append(result_digit)
    result_list.reverse()
    return convert_result_list_to_result_string(result_list), transport


def multiplication_of_two_numbers_in_a_base_p(number1, number2, base):
    result_list = []
    length_of_number = len(number1) - 1
    if number2 >= 'A' and number2 <= 'Z':
        number2_int = ord(number2) - 55
    else:
        number2_int = int(number2)
    transport = 0
    while length_of_number >= 0:
        last_digit_of_number = number1[length_of_number]
        if last_digit_of_number >= 'A' and last_digit_of_number <= 'Z':
            last_digit_of_number_int = ord(last_digit_of_number) - 55
        else:
            last_digit_of_number_int = int(last_digit_of_number)
        current_product = transport + number2_int * last_digit_of_number_int
        quotient = current_product // base
        remainder = current_product % base
        result_list.append(remainder)
        transport = quotient
        length_of_number -= 1
    if transport:
        result_list.append(transport)
    return convert_result_list_to_result_string(result_list)


def difference_of_two_numbers_in_a_base_p(minuend, subtrahend, base):
    result_list = []
    length_of_minuend = len(minuend) - 1
    length_of_subtrahend = len(subtrahend) - 1
    borrow = 0
    while length_of_minuend >= 0:
        if length_of_subtrahend >= 0:
            last_digit_of_minuend = minuend[length_of_minuend]
            last_digit_of_subtrahend = subtrahend[length_of_subtrahend]
            if last_digit_of_minuend >= 'A' and last_digit_of_minuend <= 'Z':
                last_digit_of_minuend_int = ord(last_digit_of_minuend) - 55
            else:
                last_digit_of_minuend_int = int(last_digit_of_minuend)
            if last_digit_of_subtrahend >= 'A' and last_digit_of_subtrahend <= 'Z':
                last_digit_of_subtrahend_int = ord(last_digit_of_subtrahend) - 55
            else:
                last_digit_of_subtrahend_int = int(last_digit_of_subtrahend)
            if borrow == -1:
                last_digit_of_minuend_int += borrow
                borrow = 0
            if last_digit_of_minuend_int < last_digit_of_subtrahend_int:
                borrow = -1
                last_digit_of_minuend_int += base
            difference_of_digits = last_digit_of_minuend_int - last_digit_of_subtrahend_int
            result_list.append(difference_of_digits)
            length_of_subtrahend -= 1
        else:
            last_digit_of_minuend = minuend[length_of_minuend]
            if last_digit_of_minuend >= 'A' and last_digit_of_minuend <= 'Z':
                last_digit_of_minuend_int = ord(last_digit_of_minuend) - 55
            else:
                last_digit_of_minuend_int = int(last_digit_of_minuend)
            if borrow == -1:
                if last_digit_of_minuend_int < 1:
                    borrow = -1
                    last_digit_of_minuend_int += base - 1
                else:
                    last_digit_of_minuend_int -= 1
                    borrow = 0
            result_list.append(last_digit_of_minuend_int)
        length_of_minuend -= 1
    return convert_result_list_to_result_string(result_list)


def addition_of_two_numbers_in_a_base_p(number1, number2, base):
    result_list = []
    carry = 0
    length_of_first_number = len(number1) - 1
    length_of_second_number = len(number2) - 1
    if length_of_second_number > length_of_first_number:
        number1, number2 = number2, number1
        length_of_second_number, length_of_first_number = length_of_first_number, length_of_second_number
    while length_of_first_number >= 0:
        if length_of_second_number >= 0:
            last_digit_of_first_number = number1[length_of_first_number]
            last_digit_of_second_number = number2[length_of_second_number]
            if last_digit_of_first_number >= 'A' and last_digit_of_first_number <= 'Z':
                last_digit_of_first_number_int = ord(last_digit_of_first_number) - 55
            else:
                last_digit_of_first_number_int = int(last_digit_of_first_number)
            if last_digit_of_second_number >= 'A' and last_digit_of_second_number <= 'Z':
                last_digit_of_second_number_int = ord(last_digit_of_second_number) - 55
            else:
                last_digit_of_second_number_int = int(last_digit_of_second_number)
            sum_of_digits = last_digit_of_first_number_int + last_digit_of_second_number_int + carry
            if sum_of_digits >= base:
                carry = 1
                sum_of_digits = sum_of_digits - base
            else:
                carry = 0
            result_list.append(sum_of_digits)
            length_of_first_number -= 1
            length_of_second_number -= 1
        else:
            last_digit_of_first_number = number1[length_of_first_number]
            if last_digit_of_first_number >= 'A' and last_digit_of_first_number <= 'Z':
                last_digit_of_first_number_int = ord(last_digit_of_first_number) - 55
            else:
                last_digit_of_first_number_int = int(last_digit_of_first_number)
            sum_of_digits = last_digit_of_first_number_int + carry
            if sum_of_digits >= base:
                carry = 1
                sum_of_digits = sum_of_digits - base
            else:
                carry = 0
            result_list.append(sum_of_digits)
            length_of_first_number -= 1
    if carry == 1:
        result_list.append(1)
    return convert_result_list_to_result_string(result_list)


def conversion_using_substitution_method(number, base1, base2):
    power = '1'
    number_in_base2 = '0'
    length_of_number = len(number) - 1
    if base1 > 9:
        base1_str = chr(base1 + 55)
    else:
        base1_str = str(base1)
    while length_of_number >= 0:
        last_digit = number[length_of_number]
        if last_digit != '0':
            second_operand = multiplication_of_two_numbers_in_a_base_p(power, last_digit, base2)
            number_in_base2 = addition_of_two_numbers_in_a_base_p(number_in_base2, second_operand, base2)
        power = multiplication_of_two_numbers_in_a_base_p(power, base1_str, base2)
        length_of_number -= 1
    return number_in_base2


def conversions_using_the_method_of_successive_divisions(number, base1, base2):
    result_list = []
    if base2 > 9:
        base2_str = chr(base2 + 55)
    else:
        base2_str = str(base2)
    while True:
        number, remainder = division_of_two_numbers_in_a_base_p(number, base2_str, base1)
        result_list.append(remainder)
        if number == '0':
            break
    return convert_result_list_to_result_string(result_list)


def conversion_using_rapid_conversions(number, base1, base2):
    result_list = []
    if base1 != 2:
        number = conversions_using_the_method_of_successive_divisions(number, base1, 2)
    if base2 == 4:
        number_of_elements_in_group_of_digits = 2
    elif base2 == 8:
        number_of_elements_in_group_of_digits = 3
    else:
        number_of_elements_in_group_of_digits = 4
    if base2 == 2:
        return number
    length_of_number = len(number) - 1
    while length_of_number > 0:
        current_digit = ''
        if length_of_number + 1 < number_of_elements_in_group_of_digits:
            for i in range(0, number_of_elements_in_group_of_digits - length_of_number - 1):
                current_digit = current_digit + '0'
            for i in range(0, length_of_number):
                current_digit = current_digit + number[i]
        else:
            for i in range(length_of_number - number_of_elements_in_group_of_digits + 1, length_of_number + 1):
                current_digit = current_digit + number[i]
        current_digit_in_base2 = conversion_using_substitution_method(current_digit, 2, base2)
        result_list.append(current_digit_in_base2)
        length_of_number -= number_of_elements_in_group_of_digits
    result_list.reverse()
    number_in_base2 = ''
    for i in range(0, len(result_list)):
        number_in_base2 = number_in_base2 + result_list[i]
    return number_in_base2


def main_menu():
    # This function displays a menu-driven console to interact with the user (the user can pick different options)
    print("Project made by Oltean Irina-Stefania, from group 915")
    while True:
        print("Pick an option:")
        print("1. Arithmetic operations for positive integers")
        print("2. Conversions of natural numbers between two bases")
        print("3. End the program")
        option = int(input("Enter your option (1, 2 or 3): "))
        if option == 1:
            print("Pick an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication by one digit")
            print("4. Division by one digit")
            operation = int(input("Enter an operation (1, 2, 3 or 4): "))
            base = int(input("Enter a base in which the operation will be performed: "))
            if operation == 1:
                number1 = input("Enter the first operand: ")
                number2 = input("Enter the second operand: ")
                print("The result of the addition is: " + addition_of_two_numbers_in_a_base_p(number1, number2, base))
            if operation == 2:
                minuend = input("Enter the minuend: ")
                subtrahend = input("Enter the subtrahend: ")
                print("The result of the subtraction is: " + difference_of_two_numbers_in_a_base_p(minuend, subtrahend, base))
            if operation == 3:
                number1 = input("Enter the first operand: ")
                number2 = input("Enter the second operand (one digit): ")
                print("The result of the multiplication is: " + multiplication_of_two_numbers_in_a_base_p(number1, number2, base))
            if operation == 4:
                dividend = input("Enter the dividend: ")
                divisor = input("Enter the divisor (one digit): ")
                quotient, remainder = division_of_two_numbers_in_a_base_p(dividend, divisor, base)
                print("The quotient is: " + str(quotient))
                print("The remainder is: " + str(remainder))
        if option == 2:
            base1 = int(input("Enter the base of the number to be conversed: "))
            number = input("Enter the number to be conversed: ")
            base2 = int(input("Enter the base in which you want to converse the number: "))
            if power_of_two(base1) and power_of_two(base2) and base2 != 2:
                # We use rapid conversion
                print("The conversed number is: " + conversion_using_rapid_conversions(number, base1, base2))
            elif base1 < base2:
                # We use the substitution method
                print("The conversed number is: " + conversion_using_substitution_method(number, base1, base2))
            else:
                # We use the method of successive divisions
                print("The conversed number is: " + conversions_using_the_method_of_successive_divisions(number, base1, base2))
        if option == 3:
            print("End of program")
            break


main_menu()
