#pragma once

template <typename TElem>

class DynamicArray {
private:
	TElem* elements;
	int size;
	int capacity;
public:
	// default constructor
	explicit DynamicArray(int capacity = 10);

	//copy constructor
	DynamicArray(const DynamicArray<TElem>& vector);

	// destructor
	~DynamicArray();

	void resize();
	void addItem(const TElem& element);
	void deleteItem(int position);
	void updateItem(int position, const TElem& element);
	void switchItems(int position1, int position2);

	TElem& operator[](int index);
	int GetSize() const { return this->size; };
	int getCapacity() const { return this->capacity; }
	TElem& getElement(const int position) const {
		return this->elements[position];
	}
};


template <typename TElem>
DynamicArray<TElem>::DynamicArray(int capacity) {
	this->size = 0;
	this->capacity = capacity;
	this->elements = new TElem[capacity];
}

template <typename TElem>
DynamicArray<TElem>::DynamicArray(const DynamicArray<TElem>& array) {
	this->size = array.GetSize();
	this->capacity = array.getCapacity();
	this->elements = new TElem[this->capacity];
	for (int index = 0; index < this->size; index++)
		this->elements[index] = array.getElement(index);
}

template <typename TElem>
DynamicArray<TElem>::~DynamicArray() {
	delete[] this->elements;
}

template <typename TElem>
void DynamicArray<TElem>::resize() {
	this->capacity *= 2;
	TElem* array = new TElem[this->capacity];
	for (int index = 0; index < this->size; index++)
		array[index] = this->elements[index];
	delete[] this->elements;
	this->elements = array;
}

template <typename TElem>
void DynamicArray<TElem>::addItem(const TElem& element) {
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size++] = element;
}

template <typename TElem>
void DynamicArray<TElem>::deleteItem(int position) {
	for (int index = position; index < this->size - 1; ++index)
		this->elements[index] = this->elements[index + 1];
	--this->size;
}

template <typename TElem>
void DynamicArray<TElem>::updateItem(int position, const TElem& element) {
	this->elements[position] = element;
}

template <typename TElem>
TElem& DynamicArray<TElem>::operator[](int index) {
	return this->elements[index];
}

template <typename TElem>
void DynamicArray<TElem>::switchItems(int position1, int position2) {
	TElem auxiliary_element;
	auxiliary_element = this->elements[position1];
	this->elements[position1] = this->elements[position2];
	this->elements[position2] = auxiliary_element;
}