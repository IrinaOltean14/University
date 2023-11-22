#pragma once
#include "domain.h"

typedef struct {
	int length;
	Product* array_of_products[100];
}Undo;

Undo* create_undo();

void destroy_undo(Undo* undo);

int get_length_undo(Undo* undo);

void undo_for_add_product(Undo* undo, Product* product);

void undo_for_delete_product(Undo* undo, Product* product);

void undo_for_update_quantity(Undo* undo, Product* product);

void undo_for_update_product(Undo* undo, Product* product);

int get_id_undo(Undo* undo);

Product* get_product_undo(Undo* undo);

void decrease_length(Undo* undo);

