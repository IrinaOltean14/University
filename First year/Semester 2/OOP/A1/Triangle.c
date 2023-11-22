#include <stdio.h>


int factorial(int number_to_calculate_factorial_for)
{
	int result = 1;
	for (int number_to_be_multiplied_with = 2; number_to_be_multiplied_with <= number_to_calculate_factorial_for; number_to_be_multiplied_with++)
		result *= number_to_be_multiplied_with;
	return result;
}

void print_the_triangle(int number_of_rows)
{
	int line, column, current_number_to_be_printed;
	for (line = 0; line < number_of_rows; line++)
	{
		for (column = 0; column < number_of_rows - line; column++)
			printf(" ");
		for (column = 0; column <= line; column++)
		{
			current_number_to_be_printed = factorial(line) / (factorial(line - column) * factorial(column));
			printf("%d ", current_number_to_be_printed);
		}
		printf("\n");
	}
}

int check_if_a_number_is_prime(int number_to_be_checked)
{
	if (number_to_be_checked == 2)
		return 1;
	else if (number_to_be_checked < 2)
		return 0;
	for (int possible_divisor = 2; possible_divisor <= number_to_be_checked / 2; possible_divisor++)
		if (number_to_be_checked % possible_divisor == 0)
			return 0;
	return 1;
}

void print_longest_contiguos_subsequence_of_prime_numbers(int given_vector[], int start_of_sequence, int length_of_sequence)
{
	for (int index = start_of_sequence; index < start_of_sequence + length_of_sequence; index++)
		printf("%d ", given_vector[index]);
	printf("\n");
}

void find_the_longest_contiguos_subsequence_of_prime_numbers(int length, int given_vector[])
{
	int maximum_length = 0, current_length = 0, current_start_of_sequence, start_of_maximum_sequence=0;
	for (int index = 0; index < length; index++)
		if (check_if_a_number_is_prime(given_vector[index]) == 1)
		{
			if (current_length == 0)
				current_start_of_sequence = index;
			current_length ++;
			if (current_length > maximum_length)
			{
				maximum_length = current_length;
				start_of_maximum_sequence = current_start_of_sequence;
			}
		}
		else
		{
			current_length = 0;
		}
	print_longest_contiguos_subsequence_of_prime_numbers(given_vector, start_of_maximum_sequence, maximum_length);
	
}

int main()
{
	int option, ok = 1;
	while (ok) {
		printf("1 - Print the Pascal triangle of dimension n of all combinations C(m,k) of m objects taken by k, k = 0, 1, ..., m,for line m, where m = 1, 2, ..., n.\n");
		printf("2 - Given a vector of numbers, find the longest contiguous subsequence of prime numbers.\n");
		printf("0 - Exit the program.\n");
		printf("Enter your option: ");
		scanf("%d", &option);
		if (option == 1)
		{
			int number_of_rows;
			printf("Enter the numbers of rows for the triangle: ");
			scanf("%d", &number_of_rows);
			print_the_triangle(number_of_rows);
		}
		else if (option == 2)
		{
			int length_of_the_array, given_array[100];
			printf("Enter the length of the array: ");
			scanf("%d", &length_of_the_array);
			for (int index = 0; index < length_of_the_array; index++)
			{
				printf("Give the element at position %d: ", index);
				scanf("%d", &given_array[index]);
			}
			find_the_longest_contiguos_subsequence_of_prime_numbers(length_of_the_array, given_array);

		}
		else
			break;
	}
	
	char st[10];
	scanf("%s", &st);

	return 0;

}