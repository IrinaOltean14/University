#include "Matrix.h"
#include <exception>
#include <iostream>
using namespace std;


Matrix::Matrix(int nrLines, int nrCols) {
	   
	//TODO - Implementation
	// constructor
	this->lines = nrLines;
	this->columns = nrCols;
	this->lineCounter = new TElem[this->lines + 1];
	this->capacity = 2 * this->lines;
	this->columnIndices = new TElem[this->capacity];
	this->nonZeroElements = new TElem[this->capacity];

	for (int i = 0; i <= this->lines; i++)
		this->lineCounter[i] = 0;
}
// Theta(1)

ValuePair Matrix::position(TElem element) {
	ValuePair returnedValue;
	returnedValue.first = -1;
	returnedValue.second = -1;
	for (int line = 0; line < this->lines; line++)
		for (int column = this->lineCounter[line]; column < this->lineCounter[line + 1]; column++)
			if (this->nonZeroElements[column] == element) {
				returnedValue.first = line;
				returnedValue.second = this->columnIndices[column];
			}
	return returnedValue;
}

Matrix::~Matrix() {
	// destructor
	delete[] this->columnIndices;
	delete[] this->nonZeroElements;
	delete[] this->lineCounter;
}
// Theta(1)


int Matrix::nrLines() const {
	//TODO - Implementation
	return this->lines;
}
// Theta(1)


int Matrix::nrColumns() const {
	//TODO - Implementation
	return this->columns;
}
// Theta(1)


TElem Matrix::element(int i, int j) const {
	//TODO - Implementation
	if (i < 0 || j < 0 || i >= this->lines || j >= this->columns)
		throw exception();
	bool found = false;
	TElem value = NULL_TELEM;
	for (int index = this->lineCounter[i]; index < this->lineCounter[i+1];index++)
		if (this->columnIndices[index] == j) {
			found = true;
			value = this->nonZeroElements[index];
			break;
		}

	return value;
}
// Best case: Theta(1) - the element is the first one
// Worst case: Theta(nrLines) - the element is zero 
// Average case: Theta(nrLines)
// Total complexity: O(nrLines)

void Matrix::resize(int newCapacity) {
	TElem* newArrayNonZeroElements = new TElem[newCapacity];
	TElem* newArrayOfColumnIndices = new int[newCapacity];


	for (int i = 0; i < this->capacity; i++) {
		newArrayNonZeroElements[i] = this->nonZeroElements[i];
		newArrayOfColumnIndices[i] = this->columnIndices[i];
	}

	delete[] this->nonZeroElements;
	delete[] this->columnIndices;

	this->nonZeroElements = newArrayNonZeroElements;
	this->columnIndices = newArrayOfColumnIndices;
	this->capacity = newCapacity;
}

int Matrix::position_line(TElem element) {
	for (int line = 0; line < this->lines; line++)
		for (int column = this->lineCounter[line]; column < this->lineCounter[line + 1]; column++)
			if (this->nonZeroElements[column] == element)
				return line;
	return -1;
}
// Best case: O(1)
// Worst case: O(size)
// Theta(size)

int Matrix::position_column(TElem element) {
	for (int line = 0; line < this->lines; line++)
		for (int column = this->lineCounter[line]; column < this->lineCounter[line + 1]; column++)
			if (this->nonZeroElements[column] == element)
				return this->columnIndices[column];
	return -1;
}
// Best case: O(1)
// Worst case: O(size)
//Theta(size)


TElem Matrix::modify(int i, int j, TElem e) {
	//TODO - Implementation
	if (i < 0 || j < 0 || i >= this->lines || j >= this->columns)
		throw exception();
	// Cases:
	// 1. The element is zero (we have to add it and modify all 3 arrays)
	// 2. The element is non zero and we modify it no a non zero value (we have to change its value)
	// 3. The element is zero and we modify it to a zero value (we have to delete it from the 3 arrays)

	TElem value = NULL_TELEM;
	int ind, index;
	bool found = false;
	for (index = this->lineCounter[i]; index < this->lineCounter[i + 1]; index++)
		if (this->columnIndices[index] == j) {
			found = true;
			value = this->nonZeroElements[index];
			break;
		}
	if (value == NULL_TELEM) {

		//Here is case 1
		TElem nbNonZeroElements = this->lineCounter[this->lines];
		if (nbNonZeroElements == this->capacity)
			this->resize(2 * this->capacity);
		for (index = this->lineCounter[i]; index < this->lineCounter[i + 1]; index++)
			if (this->columnIndices[index] > j)
				break;
		for (ind = nbNonZeroElements; ind > index; ind--) {
			this->columnIndices[ind] = this->columnIndices[ind - 1];
			this->nonZeroElements[ind] = this->nonZeroElements[ind - 1];
		}
		for (ind = i + 1; ind <= this->lines; ind++)
			this->lineCounter[ind]++;
		
		this->columnIndices[index] = j;
		this->nonZeroElements[index] = e;
		
	}
	else if (value != 0) {
		if (e != NULL_TELEM) {

			// Here is case 2
			this->nonZeroElements[index] = e;
		}
		else {
			// Here is case 3

			TElem nbNonZeroElements = this->lineCounter[this->lines];
			for (ind = i + 1; ind <= this->lines; ind++)
				this->lineCounter[ind]--;
			for (ind = index; ind < nbNonZeroElements - 1; ind++) {
				this->columnIndices[ind] = this->columnIndices[ind + 1];
				this->nonZeroElements[ind] = this->nonZeroElements[ind + 1];
			}
		}
	}
	return value;
}
// Best case: Theta(1) - we look for an element that is first on its column and we change it into a non zero element (case 2)
// Worst case: on the given position is a 0 which has to be replaced with a non-zero element, after performing a resize
/// Theta(new_capacity)
/// Total: O(current_capacity)


