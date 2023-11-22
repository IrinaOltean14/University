#pragma once
#include "Repository.h"
#include "Undo.h"


typedef struct {
	Repository* repo;
	Undo* undo;
	Undo* redo;

}Service;

Service* createService(Repository*);

void destroy_service(Service* service);

void add_product_service(Service* service, char name[], char category[], int quantity, int year, int month, int day, int make_undo);

Product* get_a_product_service(Service* service, int index);

int get_size_of_the_array_of_products_service(Service* service);

int is_product_already_added_service(Service* service, char category[], char name[]);

void update_quantity_of_the_product_service(Service* service, int index, int updated_quantity, int make_undo);

void remove_product_from_the_array_service(Service* service, int index, int make_undo);

void update_product_service(Service* service, int index_of_the_product, int quantity, int year_of_expiration, int month_of_expiration, int day_of_expiration, int make_undo);

int search_products_that_contain_the_given_string(Service* service, char string_to_search_for[], Product* products_that_contain_the_given_string[]);

void sort_products_that_contain_the_given_string(int length_of_products_that_contain_the_given_string, Product* products_that_contain_the_given_string[]);

int search_products_from_given_category_that_expire_in_next_days(Service* service, Product* array_of_products[], char category[], int days_until_expiration);

int undo(Service* service);

int redo(Service* service);

void sort_descending_by_expiration(Service* service, Product* array_of_products[], int length_of_array);

int search_products_above_given_quantity(Service* service, Product* array_of_products[], int quantity);

int get_quantity(Service* service, int index);

void get_array_of_products_service(Service* service, Product* array_of_products[], int length);
