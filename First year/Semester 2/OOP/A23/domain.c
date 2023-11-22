#include "domain.h"
#include <stdio.h>
#include <stdlib.h>

Product* create_product(char *name, char *category, int quantity, int year, int month, int day) {
	Date date_of_expiration;
	date_of_expiration.year = year;
	date_of_expiration.month = month;
	date_of_expiration.day = day;
	Product* new_product=malloc(sizeof(Product));
	if (new_product == NULL)
		return NULL;
	new_product->name = malloc((strlen(name) + 1) * sizeof(char));
	if (new_product->name == NULL)
		return NULL;
	strcpy(new_product->name, name);
	new_product->category = malloc((strlen(category) + 1) * sizeof(char));
	if (new_product->category == NULL)
		return NULL;
	strcpy(new_product->category, category);
	new_product->quantity = quantity;
	new_product->date_of_expiration = date_of_expiration;
	return new_product;
}

void destroy_product(Product* product) {
	if (product == NULL)
		return;
	// free memomry which was allocated for the components fields
	free(product->name);
	free(product->category);
	// field memory that was allocated for the structure
	free(product);
}

void set_quantity(Product* product, int new_quantity) {
	product->quantity += new_quantity;
}

void update_product_d(Product* product, int quantity, int year_of_expiration, int month_of_expiration, int day_of_expiration) {
	product->quantity = quantity;
	product->date_of_expiration.day = day_of_expiration;
	product->date_of_expiration.month = month_of_expiration;
	product->date_of_expiration.year = year_of_expiration;
}

Product* copy_product(Product* product) {
	return create_product(product->name, product->category, product->quantity, product->date_of_expiration.year, product->date_of_expiration.month, product->date_of_expiration.day);
}

int get_id(Product* product) {
	return product->id;
}

int get_quantity_d(Product* product) {
	return product->quantity;
}