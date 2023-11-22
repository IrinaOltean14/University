#include "undo.h"
#include <stdlib.h>


// Id for undo:
// 1 - undo an add operation
// 2 - undo a delete operation
// 3 - undo for update quantity
// 4 - undo for update product

Undo* create_undo() {
	Undo* new_undo = malloc(sizeof(Undo));
	if (new_undo == NULL)
		return NULL;
	new_undo->length = 0;
	return new_undo;
}

void destroy_undo(Undo* undo) {
	for (int index = 0; index < undo->length; index++)
		destroy_product(undo->array_of_products[index]);
	free(undo);
}

int get_length_undo(Undo* undo) {
	return undo->length;
}

void undo_for_add_product(Undo* undo, Product* product) {
	undo->array_of_products[undo->length] = product;
	undo->array_of_products[undo->length]->id = 1;
	undo->length++;
}

int get_id_undo(Undo* undo) {
	Product* product = undo->array_of_products[undo->length - 1];
	return get_id(product);
}

Product* get_product_undo(Undo* undo) {
	return undo->array_of_products[undo->length - 1];
}

void decrease_length(Undo* undo) {
	undo->length--;
}

void undo_for_delete_product(Undo* undo, Product* product) {
	undo->array_of_products[undo->length] = product;
	undo->array_of_products[undo->length]->id = 2;
	undo->length++;
}

void undo_for_update_quantity(Undo* undo, Product* product) {
	undo->array_of_products[undo->length] = product;
	undo->array_of_products[undo->length]->id = 3;
	undo->length++;
}

void undo_for_update_product(Undo* undo, Product* product) {
	undo->array_of_products[undo->length] = product;
	undo->array_of_products[undo->length]->id = 4;
	undo->length++;
}