#include "ui.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

Ui* createUi(Service* service) {
	Ui* newUi = malloc(sizeof(Ui));
	if (newUi == NULL)
		return NULL;
	newUi->service = service;
	return newUi;
}

void destroy_ui(Ui* ui) {
	free(ui->service);
	free(ui);
}

int verify_if_user_input_is_valid(char category_of_the_product[], int month_of_expiration, int day_of_expiration) {
	if (strcmp(category_of_the_product, "dairy") != 0 && strcmp(category_of_the_product, "sweets") != 0 && strcmp(category_of_the_product, "fruit") != 0 && strcmp(category_of_the_product, "meat") != 0)
		return 0;
	if (month_of_expiration < 1 || month_of_expiration > 12)
		return 0;
	if (day_of_expiration < 1 || day_of_expiration > 30)
		return 0;
	return 1;

}

void dispay_products_with_given_property(Ui* ui, int length_of_products, Product* products_with_given_property[]) {
	for (int product_index = 0; product_index < length_of_products; product_index++) {
		Product* current_product = products_with_given_property[product_index];
		printf("%s - %s - %d - date of expiration %d:%d:%d\n", current_product->name, current_product->category, current_product->quantity, current_product->date_of_expiration.day, current_product->date_of_expiration.month, current_product->date_of_expiration.year);
	}
	printf("\n");
}

void print_the_array_of_products(Ui* ui) {
	int size_of_the_array_of_products = get_size_of_the_array_of_products_service(ui->service);
	Product* array_of_products[100];
	get_array_of_products_service(ui->service, array_of_products, size_of_the_array_of_products);
	for (int index = 0; index < size_of_the_array_of_products; index++) {
		printf("%s - %s - %d - date of expiration %d:%d:%d\n", array_of_products[index]->name, array_of_products[index]->category, array_of_products[index]->quantity, array_of_products[index]->date_of_expiration.day, array_of_products[index]->date_of_expiration.month, array_of_products[index]->date_of_expiration.year);
	}
	printf("\n");
}

void add_entries(Ui* ui) {
	add_product_service(ui->service, "apples", "fruit", 30, 2023, 10, 17,1);
	add_product_service(ui->service, "pears", "fruit", 20, 2023, 10, 9,1);
	add_product_service(ui->service, "chicken", "meat", 15, 2023, 5, 13,1);
	add_product_service(ui->service, "milk", "dairy", 25, 2023, 3, 23,1);
	add_product_service(ui->service, "cheese", "dairy", 35, 2023, 4, 1,1);
	add_product_service(ui->service, "bluberries", "fruit", 100, 2023, 5, 15,1);
	add_product_service(ui->service, "tiramisu", "sweets", 1, 2025, 3, 24,1);
	add_product_service(ui->service, "pork", "meat", 10, 2023, 5, 7,1);
	add_product_service(ui->service, "beef", "meat", 5, 2023,8, 2,1);
	add_product_service(ui->service, "watermelon", "fruit", 1, 2023, 7, 15,1);
}

void add_product_ui(Ui* ui) {
	char name_of_the_product[50], category_of_the_product[50];
	printf("Give the name of the product: ");
	scanf("%s", name_of_the_product);
	printf("Give the category of the product (meat, dairy, sweets, fruit): ");
	scanf("%s", category_of_the_product);
	int quantity_of_the_product;
	printf("Give the quantity of the product: ");
	scanf("%d", &quantity_of_the_product);
	int index = is_product_already_added_service(ui->service, category_of_the_product, name_of_the_product);
	if (index != -1) {
		update_quantity_of_the_product_service(ui->service, index, quantity_of_the_product, 1);
		print_the_array_of_products(ui);

	}
	else {
		int month_of_expiration, year_of_expiration, day_of_expiration;
		printf("Give the year of expiration: ");
		scanf("%d", &year_of_expiration);
		printf("Give the month of expiration: ");
		scanf("%d", &month_of_expiration);
		printf("Give the day of expiration: ");
		scanf("%d", &day_of_expiration);
		int is_user_input_valid = verify_if_user_input_is_valid(category_of_the_product, month_of_expiration, day_of_expiration);
		if (is_user_input_valid == 0) {
			printf("The input is not correct\n\n");
		}
		else {
			add_product_service(ui->service, name_of_the_product, category_of_the_product, quantity_of_the_product, year_of_expiration, month_of_expiration, day_of_expiration, 1);
			printf("Product added\n");
			int size_of_the_array_of_products = get_size_of_the_array_of_products_service(ui->service);
			print_the_array_of_products(ui);
		}
	}
}

void test(Ui* ui) {
	add_product_service(ui->service, "mango", "fruit", 20, 2023, 10, 10, 1);
	assert(get_size_of_the_array_of_products_service(ui->service) == 11);
	remove_product_from_the_array_service(ui->service, 10, 1);
	assert(get_size_of_the_array_of_products_service(ui->service) == 10);
	update_product_service(ui->service, 0, 1, 1, 1, 1, 1);
	assert(get_quantity(ui->service, 0) == 1);
	update_product_service(ui->service, 0, 10, 10, 10, 10, 10);
	assert(get_quantity(ui->service, 0) == 10);
	update_product_service(ui->service, 0, 20, 20, 20, 20, 20);
	assert(get_quantity(ui->service, 0) == 20);
	update_product_service(ui->service, 0, 20, 2023, 10,11,1);
	assert(get_quantity(ui->service, 0) == 20);
	printf("Tests successfull\n");
}

void printMenu(Ui* ui) {
	int print_menu = 1;
	printf("The products that are already added: \n");
	print_the_array_of_products(ui);
	while (print_menu == 1) {
		printf("Choose an option: \n");
		printf("a. Add, delete or update a product\n");
		printf("b. Display all products whose name contains a given string or whose quantity is bigger than a given number (if the string is empty, all products from the refrigerator are considered), and show them sorted ascending by the existing quantity.");
		printf("c. Display all products of a given category (if the category is empty, all types of food will be considered) whose expiration dates are close (expire in the following X days, where the value of X is user-provided). \n");
		printf("d. Undo.\n");
		printf("e. Redo. \n");
		printf("Enter your option: ");
		char option[2];
		scanf("%s", option);

		if (strcmp(option, "a") == 0) {
			printf("What do you want to do? (add, remove, update) ");
			char command[10];
			scanf("%s", command);
			if (strcmp(command, "add") == 0) {
				add_product_ui(ui);
			}
			else if (strcmp(command, "remove") == 0) {
				char name_of_product[50], category_of_product[20];
				printf("Give the name of the product you want to remove: ");
				scanf("%s", name_of_product);
				printf("Give the category of the product you want to remove: ");
				scanf("%s", category_of_product);
				int is_product_in_array_of_products = is_product_already_added_service(ui->service, category_of_product, name_of_product);
				if (is_product_in_array_of_products == -1)
					printf("The product that you gave is not in the array \n");
				else {
					remove_product_from_the_array_service(ui->service, is_product_in_array_of_products, 1);
					printf("Product deleted successfully\n");
					print_the_array_of_products(ui);
				}

			}
			else if (strcmp(command, "update") == 0) {
				char name_of_product[50], category_of_product[20];
				printf("Give the name of the product you want to update: ");
				scanf("%s", name_of_product);
				printf("Give the category of the product you want to update: ");
				scanf("%s", category_of_product);
				int is_product_in_array_of_products = is_product_already_added_service(ui->service, category_of_product, name_of_product);
				if (is_product_in_array_of_products == -1)
					printf("The product that you gave is not in the array \n");
				else {
					int quantity_of_the_product;
					printf("Give the updated quantity of the product: ");
					scanf("%d", &quantity_of_the_product);
					int month_of_expiration, year_of_expiration, day_of_expiration;
					printf("Give the updated year of expiration: ");
					scanf("%d", &year_of_expiration);
					printf("Give the updated updated month of expiration: ");
					scanf("%d", &month_of_expiration);
					printf("Give the updated day of expiration: ");
					scanf("%d", &day_of_expiration);
					update_product_service(ui->service, is_product_in_array_of_products, quantity_of_the_product, year_of_expiration, month_of_expiration, day_of_expiration, 1);
					printf("Product updated successfully\n");
					print_the_array_of_products(ui);
				}
			}
			else {
				printf("Invalid command");
			}

		}
		else if (strcmp(option, "b") == 0) {
			printf("Do you want to filter with quantity or name? ");
			char filter[50];
			scanf("%s", filter);
			if (strcmp(filter, "name") == 0) {
				char string_to_search_for[20];
				printf("Enter the string you want to search for: ");
				gets(string_to_search_for);
				gets(string_to_search_for);
				if (strcmp(string_to_search_for, "") == 0) {
					Product* array_of_products[100];
					get_array_of_products(ui->service, array_of_products);
					sort_products_that_contain_the_given_string(get_size_of_the_array_of_products_service(ui->service), array_of_products);
					dispay_products_with_given_property(ui, get_size_of_the_array_of_products_service(ui->service), array_of_products);
				}
				else {
					struct Product* products_that_contain_the_given_string[100];
					int length_of_products_that_contain_the_given_string = search_products_that_contain_the_given_string(ui->service, string_to_search_for, products_that_contain_the_given_string);
					if (length_of_products_that_contain_the_given_string == 0)
						printf("There are no products whose names contain the given string\n");
					else {
						sort_products_that_contain_the_given_string(length_of_products_that_contain_the_given_string, products_that_contain_the_given_string);
						dispay_products_with_given_property(ui, length_of_products_that_contain_the_given_string, products_that_contain_the_given_string);
					}
				}
			}
			else if (strcmp(filter, "quantity") == 0) {
				int quantity;
				printf("Enter the quantity: ");
				scanf("%d", &quantity);
				Product* array_of_products[100];
				int length = search_products_above_given_quantity(ui->service, array_of_products, quantity);
				sort_products_that_contain_the_given_string(length, array_of_products);
				dispay_products_with_given_property(ui, length, array_of_products);

			}

		}
		else if (strcmp(option, "c") == 0) {
			char category_of_the_product[50];
			int number_of_days_until_expiration;
			printf("Enter the number of days until expiration: ");
			scanf("%d", &number_of_days_until_expiration);
			printf("Enter the category you want to search for (meat, sweets, fruit, dairy or null): ");
			gets(category_of_the_product);
			gets(category_of_the_product);
			if (strcmp(category_of_the_product, "dairy") == 0 || strcmp(category_of_the_product, "sweets") == 0 || strcmp(category_of_the_product, "fruit") == 0 || strcmp(category_of_the_product, "meat") == 0 || strcmp(category_of_the_product, "") == 0) {
				printf("Do you want descending sorting? ");
				char descending[10];
				scanf("%s", descending);
				Product* array_of_products_that_fulfill_the_requirements[100];
				int length_of_array = search_products_from_given_category_that_expire_in_next_days(ui->service, array_of_products_that_fulfill_the_requirements, category_of_the_product, number_of_days_until_expiration);
				if (strcmp(descending, "yes") == 0) {
					sort_descending_by_expiration(ui->service, array_of_products_that_fulfill_the_requirements, length_of_array);
				}
				dispay_products_with_given_property(ui, length_of_array, array_of_products_that_fulfill_the_requirements);
			}
			else
				printf("Invalid input\n");
		}
		else if (strcmp(option, "d") == 0){
			int is_it_possible_to_undo = undo(ui->service);
			if (is_it_possible_to_undo == 0)
				printf("It is not possible to undo\n");
			else {
				printf("Undo succesfull\n");
				print_the_array_of_products(ui);
			}
		}
		else if (strcmp(option, "e") == 0) {
			int is_it_possible_to_redo = redo(ui->service);
			if (is_it_possible_to_redo == 0)
				printf("It is not possible to redo\n");
			else {
				printf("Redo succesfull\n");
				print_the_array_of_products(ui);
			}
		}
		

	}
	char option1[100];
	scanf("%s", option1);
}



