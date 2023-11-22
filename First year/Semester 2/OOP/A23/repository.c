#include "Repository.h"
#include <stdlib.h>

Repository* createRepo(){   
    Repository* newRepo = malloc(sizeof(Repository));
    if (newRepo == NULL)
        return NULL;
    newRepo->capacity = 5;
    newRepo->array_of_products = malloc(newRepo->capacity * sizeof(TElem));
    newRepo->size = 0;
    return newRepo;
}

void destroy_repo(Repository* repo) {
    if (repo == NULL)
        return;
    for (int index = 0; index < repo->size; index++)
        destroy_product(repo->array_of_products[index]);
    free(repo);
}

void resize_the_array_of_products(Repository* repo) {
    repo->capacity *= 2;
    TElem* aux = realloc(repo->array_of_products, sizeof(TElem) * repo->capacity);
    repo->array_of_products = aux;
}

void add_product_repo(Repository *repo, Product* product_to_add) {
    if (repo->size == repo->capacity)
        resize_the_array_of_products(repo);
    repo->array_of_products[repo->size] = product_to_add;
    repo->size++;
}

Product* get_a_product(Repository* repo, int index) {
    return repo->array_of_products[index];
}


int get_size_of_array_of_products(Repository *repo) {
    return repo->size;
}

void update_the_quantity_of_the_product(Repository* repo, int index, int updated_quantity) {
    set_quantity(repo->array_of_products[index], updated_quantity);
}

void remove_product_from_the_array(Repository* repo, int index) {
    Product* intermediate_product = malloc(sizeof(Product));
    if (intermediate_product == NULL)
        return NULL;
    intermediate_product = repo->array_of_products[index];
    repo->array_of_products[index] = repo->array_of_products[repo->size - 1];
    repo->array_of_products[repo->size] = intermediate_product;
    
    repo->size--;
}

void update_product(Repository* repo, int index_of_product, int quantity, int year_of_expiration, int month_of_expiration, int day_of_expiration) {
    update_product_d(repo->array_of_products[index_of_product], quantity, year_of_expiration, month_of_expiration, day_of_expiration); 
}

int get_quantity_repo(Repository* repo, int index) {
    return get_quantity_d(repo->array_of_products[index]);
}

void get_array_of_products_repo(Repository* repo, Product* array_of_products[], int length) {
    for (int index = 0; index < length; index++) {
        array_of_products[index] = get_a_product(repo, index);
    }
}