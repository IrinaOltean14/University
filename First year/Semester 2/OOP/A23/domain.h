#pragma once

typedef struct{
	int month, year, day;
}Date;

typedef struct{
	char *name, *category;
	int quantity, id;
	Date date_of_expiration;
}Product;

Product* create_product(char *name, char *category, int quantity, int year, int month, int day);

void destroy_product(Product* product);


void set_quantity(Product* product, int new_quantity);

void update_product_d(Product* product, int quantity, int year_of_expiration, int month_of_expiration, int day_of_expiration);

Product* copy_product(Product* product);

int get_id(Product* product);

int get_quantity_d(Product* product);

