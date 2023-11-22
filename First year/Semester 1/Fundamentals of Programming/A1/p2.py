# Solve the problem from the second set here
# 8.Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2],
# for n > 2, larger than the given natural number n. (e.g. for n = 6, m = 8).
def find_fibonacci_number_larger_than_n(second_to_last, last, given_number):
    # The function calculates the Fibonacci numbers until it finds the first one (the smallest one)
    # that is larger than the given number
    current_fibonacci_number = second_to_last+last
    while current_fibonacci_number <= given_number:
        second_to_last = last
        last = current_fibonacci_number
        current_fibonacci_number = second_to_last+last
    return current_fibonacci_number

# def find_fibonacci_number_recv(second_to_last, last, given_number):
#     # same as above but using recursive
#     current_fibonacci_number = second_to_last + last
#     print(second_to_last, last, current_fibonacci_number)
#     if current_fibonacci_number > given_number:
#         return current_fibonacci_number
#     else:
#         return find_fibonacci_number_recv(last, current_fibonacci_number, given_number)


my_number = int(input("Enter a natural number (greater than 2): "))
print("The smallest number from the Fibonacci sequence larger than the given number is: ",
      str(find_fibonacci_number_larger_than_n(1, 1, my_number)))
# print("[[RECV]] The smallest number from the Fibonacci sequence larger than the given number is: ",
#       str(find_fibonacci_number_recv(1, 1, my_number)))
