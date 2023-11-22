#pragma once
#include "Service.h"


typedef struct {
	Service* service;
}Ui;

Ui* createUi(Service* service);

void destroy_ui(Ui* ui);

int verify_if_user_input_is_valid(char category_of_the_product[], int month_of_expiration, int day_of_expiration);

void print_the_array_of_products(Ui* ui);

void add_product_ui(Ui* ui);

void printMenu(Ui* ui);