#pragma once
#include "domain.h"

typedef void* TElem;

typedef struct {
	TElem* array_of_products;
	int size, capacity;

}Repository;

Repository* createRepo();

void destroy_repo(Repository* repo);


void add_product_repo(Repository* repo, Product* product_to_add);

Product* get_a_product(Repository* repo, int index);

int get_size_of_array_of_products(Repository* repo);

void update_the_quantity_of_the_product(Repository* repo, int updated_quantity, int index);

void update_product(Repository* repo, int index_of_product, int quantity, int year_of_expiration, int month_of_expiration, int day_of_expiration);

int get_quantity_repo(Repository* repo, int index);

void get_array_of_products_repo(Repository* repo, Product* array_of_products[], int length);


