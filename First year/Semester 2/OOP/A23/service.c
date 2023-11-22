#include "Service.h"
#include <string.h>
#include <stdlib.h>

Service* createService(Repository* repo, Undo* undo, Undo* redo) {
	Service* newService = malloc(sizeof(Service));
	if (newService == NULL)
		return NULL;
	newService->repo = repo;
	newService->undo = undo;
	newService->redo = redo;
	return newService;
}

void destroy_service(Service* service) {
	free(service->repo);
	free(service->undo);
	free(service->redo);
	free(service);
}

void add_product_service(Service* service, char name[], char category[], int quantity, int year, int month, int day, int make_undo) {
	Product* new_product = create_product(name, category, quantity, year, month, day);
	add_product_repo(service->repo, new_product);
	if (make_undo)
		undo_for_add_product(service->undo, copy_product(new_product));
}

Product* get_a_product_service(Service* service, int index) {
	return get_a_product(service->repo, index);
}

void get_array_of_products_service(Service* service, Product* array_of_products[], int length) {
	get_array_of_products_repo(service->repo, array_of_products, length);
}


int get_size_of_the_array_of_products_service(Service* service) {
	return get_size_of_array_of_products(service->repo);
}

int is_product_already_added_service(Service *service, char category[], char name[]) {
	int size_of_products_array = get_size_of_the_array_of_products_service(service);
	for (int index = 0; index < size_of_products_array; index++) {
		Product* current_product = get_a_product_service(service, index);
		if (strcmp(current_product->category,category)==0 && strcmp(current_product->name,name)==0)
			return index;
	}
	return -1;
}

void update_quantity_of_the_product_service(Service* service, int index, int updated_quantity,int make_undo) {
	if (make_undo) {
		undo_for_update_quantity(service->undo, copy_product(get_a_product(service->repo, index)));
	}
	update_the_quantity_of_the_product(service->repo, index, updated_quantity);
}

void remove_product_from_the_array_service(Service* service, int index, int make_undo) {
	Product* product = get_a_product_service(service, index);
	remove_product_from_the_array(service->repo, index);
	if (make_undo)
		undo_for_delete_product(service->undo, copy_product(product));
}

void update_product_service(Service* service, int index_of_the_product, int quantity, int year_of_expiration, int month_of_expiration, int day_of_expiration, int make_undo) {
	if (make_undo) {
		undo_for_update_product(service->undo, copy_product(get_a_product(service->repo, index_of_the_product)));
	}
	update_product(service->repo, index_of_the_product, quantity, year_of_expiration, month_of_expiration, day_of_expiration);
}

int search_products_that_contain_the_given_string(Service* service, char string_to_search_for[], Product* products_that_contain_the_given_string[]) {
	int length_of_products_that_contain_the_given_string = 0;
	int length_of_array_of_products = get_size_of_the_array_of_products_service(service);
	for (int index = 0; index < length_of_array_of_products; index++) {
		Product* current_product = get_a_product_service(service, index);
		if (strstr(current_product->name, string_to_search_for) != NULL) {
			products_that_contain_the_given_string[length_of_products_that_contain_the_given_string] = current_product;
			length_of_products_that_contain_the_given_string++;
		}
	}
	return length_of_products_that_contain_the_given_string;
}

void sort_products_that_contain_the_given_string(int length_of_products_that_contain_the_given_string, Product* products_that_contain_the_given_string[]) {
	for (int first_index = 0; first_index < length_of_products_that_contain_the_given_string; first_index++)
		for (int second_index = first_index + 1; second_index < length_of_products_that_contain_the_given_string; second_index++)
			if (products_that_contain_the_given_string[first_index]->quantity > products_that_contain_the_given_string[second_index]->quantity) {
				struct Product* intermediate_product;
				intermediate_product = products_that_contain_the_given_string[first_index];
				products_that_contain_the_given_string[first_index] = products_that_contain_the_given_string[second_index];
				products_that_contain_the_given_string[second_index] = intermediate_product;
			}
}

void get_array_of_products(Service *service, Product* array_of_products[]) {
	int size_of_the_array_of_products = get_size_of_the_array_of_products_service(service);
	for (int index = 0; index < size_of_the_array_of_products; index++) 
		array_of_products[index] = get_a_product_service(service, index);
}



int get_days_of_a_date(Service* service, int year, int month, int day) {
	return year * 365 + (month - 1) * 30 + day;
}

void sort_descending_by_expiration(Service* service, Product* array_of_products[], int length_of_array) {
	int current_year = 2023, current_month = 3, current_day = 23;
	int days_for_current_date = get_days_of_a_date(service, current_year, current_month, current_day);
	for (int index1= 0;index1<length_of_array;index1++)
		for (int index2 = index1 + 1; index2 < length_of_array; index2++) {
			Product* current_product1 = array_of_products[index1];
			Product* current_product2 = array_of_products[index2];
			int days_for_current_product1 = get_days_of_a_date(service, current_product1->date_of_expiration.year, current_product1->date_of_expiration.month, current_product1->date_of_expiration.day);
			int days_for_current_product2 = get_days_of_a_date(service, current_product2->date_of_expiration.year, current_product2->date_of_expiration.month, current_product2->date_of_expiration.day);
			if (days_for_current_product1 < days_for_current_product2) {
				Product* aux_product = array_of_products[index1];
				array_of_products[index1] = array_of_products[index2];
				array_of_products[index2] = aux_product;
			}
		}
}


int search_products_from_given_category_that_expire_in_next_days(Service* service, Product* array_of_products[], char category[], int days_until_expiration) {
	int length_of_array_of_products_that_respect_requirements = 0;
	int number_of_all_products = get_size_of_the_array_of_products_service(service);
	int current_year = 2023, current_month = 3, current_day = 23;
	int days_for_current_date = get_days_of_a_date(service, current_year, current_month, current_day);
	for (int index = 0; index < number_of_all_products; index++) {
		Product* current_product = get_a_product(service->repo, index);
		int days_for_current_product = get_days_of_a_date(service, current_product->date_of_expiration.year, current_product->date_of_expiration.month, current_product->date_of_expiration.day);
		if (days_for_current_product - days_for_current_date <= days_until_expiration) {
			if (strcmp(category, "") != 0 && strcmp(category, current_product->category) == 0) {
				array_of_products[length_of_array_of_products_that_respect_requirements] = current_product;
				length_of_array_of_products_that_respect_requirements++;
			}
			else if (strcmp(category, "") == 0) {
				array_of_products[length_of_array_of_products_that_respect_requirements] = current_product;
				length_of_array_of_products_that_respect_requirements++;
			}
		}
	}
	return length_of_array_of_products_that_respect_requirements;
}

int search_products_above_given_quantity(Service* service, Product* array_of_products[], int quantity) {
	int number_of_all_products = get_size_of_the_array_of_products_service(service);
	int length_of_array_of_products_that_respect_requirements = 0;
	for (int index = 0; index < number_of_all_products; index++) {
		Product* current_product = get_a_product(service->repo, index);
		int quantity_for_current_product = current_product->quantity;
		if (quantity_for_current_product >= quantity) {
			array_of_products[length_of_array_of_products_that_respect_requirements] = current_product;
			length_of_array_of_products_that_respect_requirements++;
		}
	}
	return length_of_array_of_products_that_respect_requirements;
}

int undo(Service* service) {
	if (get_length_undo(service->undo) == 0)
		return 0;
	if (get_id_undo(service->undo) == 1) {
		Product* product_to_delete = get_product_undo(service->undo);
		undo_for_delete_product(service->redo, copy_product(product_to_delete));
		int index = is_product_already_added_service(service, product_to_delete->category, product_to_delete->name);
		remove_product_from_the_array_service(service, index, 0);
		destroy_product(product_to_delete);
		decrease_length(service->undo);
	}
	else if (get_id_undo(service->undo) == 2) {
		Product* product_to_add = get_product_undo(service->undo);;
		undo_for_add_product(service->redo, copy_product(product_to_add));
		add_product_service(service, product_to_add->name, product_to_add->category, product_to_add->quantity, product_to_add->date_of_expiration.year, product_to_add->date_of_expiration.month, product_to_add->date_of_expiration.day, 0);
		destroy_product(product_to_add);
		decrease_length(service->undo);
	}
	else if (get_id_undo(service->undo) == 3) {
		Product* product_to_modify_quantity = get_product_undo(service->undo);
		int index = is_product_already_added_service(service, product_to_modify_quantity->category, product_to_modify_quantity->name);
		Product* current_product = get_a_product_service(service, index);
		undo_for_update_quantity(service->redo, copy_product(current_product));
		int quantity = current_product->quantity - product_to_modify_quantity->quantity;
		update_quantity_of_the_product_service(service, index, -quantity, 0);
		destroy_product(product_to_modify_quantity);
		decrease_length(service->undo);
	}
	else if (get_id_undo(service->undo) == 4) {
		Product* product = get_product_undo(service->undo);
		int index = is_product_already_added_service(service, product->category, product->name);
		Product* current_product = get_a_product_service(service, index);
		undo_for_update_product(service->redo, copy_product(current_product));
		update_product_service(service, index, product->quantity, product->date_of_expiration.year, product->date_of_expiration.month, product->date_of_expiration.day, 0);
		destroy_product(product);
		decrease_length(service->undo);
	}
	return 1;
}


int redo(Service* service) {
	if (service->redo->length == 0)
		return 0;
	else if (get_id_undo(service->redo) == 1) {
		Product* product_to_delete = get_product_undo(service->redo);
		int index = is_product_already_added_service(service, product_to_delete->category, product_to_delete->name);
		remove_product_from_the_array_service(service, index, 1);
		destroy_product(product_to_delete);
		decrease_length(service->redo);
	}
	else if (get_id_undo(service->redo) == 2) {
		Product* product_to_add = get_product_undo(service->redo);
		printf("%s", product_to_add->name);
		add_product_service(service, product_to_add->name, product_to_add->category, product_to_add->quantity, product_to_add->date_of_expiration.year, product_to_add->date_of_expiration.month, product_to_add->date_of_expiration.day, 1);
		destroy_product(product_to_add);
		decrease_length(service->redo);
	}
	else if (get_id_undo(service->redo) == 3) {
		Product* product_to_modify_quantity = get_product_undo(service->redo);
		int index = is_product_already_added_service(service, product_to_modify_quantity->category, product_to_modify_quantity->name);
		Product* current_product = get_a_product_service(service, index);
		int quantity = product_to_modify_quantity->quantity - current_product->quantity;
		update_quantity_of_the_product_service(service, index, quantity, 1);
		destroy_product(product_to_modify_quantity);
		decrease_length(service->redo);
	}
	else if (get_id_undo(service->redo) == 4) {
		Product* product = get_product_undo(service->redo);
		int index = is_product_already_added_service(service, product->category, product->name);
		Product* current_product = get_a_product_service(service, index);
		update_product_service(service, index, product->quantity, product->date_of_expiration.year, product->date_of_expiration.month, product->date_of_expiration.day, 0);
		destroy_product(product);
		decrease_length(service->redo);
	}
	return 1;
}

int get_quantity(Service* service, int index) {
	return get_quantity_repo(service->repo, index);
}
