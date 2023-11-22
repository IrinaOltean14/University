#pragma once
#include "Domain.h"
#include <assert.h>
#include <iostream>
template <typename TElem>
class DynamicArray {
private:
	TElem* elements;
	int capacity;
	int size;
public:
	DynamicArray();
	void AddElem(TElem element);
	void resize();
	TElem* GetElements();
	int GetSize();
	void DeleteElem(int index);
	void UpdateElem(int index, TElem element);
	int GetCapacity();
	void Switch(int index1, int index2);
	//destructor
	~DynamicArray();
};

template <typename TElem>
DynamicArray<TElem>::DynamicArray() {
	this->capacity = 1;
	this->size = 0;
	this->elements = new TElem[this->capacity];
}

template <typename TElem>
void DynamicArray<TElem>::UpdateElem(int index, TElem element) {
	this->elements[index] = element;
}

template <typename TElem>
void DynamicArray<TElem>::Switch(int index1, int index2) {
	TElem auxilary = this->elements[index1];;
	this->elements[index1] = this->elements[index2];
	this->elements[index2] = auxilary;
}

template <typename TElem>
void DynamicArray<TElem>::DeleteElem(int index) {
	TElem aux;
	aux = this->elements[this->size - 1];
	this->elements[this->size - 1] = this->elements[index];
	this->elements[index] = aux;
	this->size--;
}

template <typename TElem>
int DynamicArray<TElem>::GetSize() {
	return this->size;
}

template <typename TElem>
int DynamicArray<TElem>::GetCapacity() {
	return this->capacity;
}

template <typename TElem>
TElem* DynamicArray<TElem>::GetElements() {
	return this->elements;
}

template <typename TElem>
void DynamicArray<TElem>::AddElem(TElem element) {
	if (this->size == this->capacity)
		resize();
	this->elements[this->size] = element;
	this->size++;
}

template <typename TElem>
void DynamicArray<TElem>::resize() {
	auto* newElems = new TElem[this->capacity * 2];
	for (int index = 0; index < this->size; index++)
		newElems[index] = this->elements[index];
	delete[] this->elements;
	this->elements = newElems;
	this->capacity *= 2;
}

template <typename TElem>
DynamicArray<TElem>::~DynamicArray() {
	delete[] this->elements;
}
