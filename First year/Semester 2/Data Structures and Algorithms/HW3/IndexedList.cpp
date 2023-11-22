#include <exception>
#include <iostream>

#include "IndexedList.h"
#include "ListIterator.h"
using namespace std;

IndexedList::IndexedList() {
	//TODO - Implementation
    this->capacity = 10;
    this->length = 0;
    this->elements = new TElem[this->capacity];
    this->next = new int[this->capacity];
    for (int index = 0; index < this->capacity; index++)
        this->next[index] = index + 1;
    this->firstFree = 0;
    this->head = -1;
    this->lastIndex = -1;
}
// Theta(capacity)

int IndexedList::size() const {
    //TODO - Implementation
    return this->length;
}
// Theta(1)


bool IndexedList::isEmpty() const {
    //TODO - Implementation
    return (this->length == 0);
}
// Theta(1)

TElem IndexedList::getElement(int pos) const {
    //TODO - Implementation
    if (pos >= this->length || pos<0)
        throw exception();
    int current_position=this->head;
    while (pos > 0) {
        pos--;
        current_position = this->next[current_position];
    }
    return this->elements[current_position];
}
// BC: Theta(1) - we want the element on the first position
// WC: Theta(length) - we want the element on the last position
// AC: O(length)
// O(pos)

TElem IndexedList::setElement(int pos, TElem e) {
    //TODO - Implementation
    if (pos >= this->length || pos < 0)
        throw exception();
    int current_position = this->head;
    TElem current_element=this->elements[current_position];
    while (pos > 0) {
        pos--;
        current_position = this->next[current_position];
        current_element = this->elements[current_position];
    }
    this->elements[current_position] = e;
    return current_element;
}
// BC: Theta(1) - we change the element on the first position
// WC: Theta(length) - we change the element on the last position
// AC: O(length)
// O(pos)

void IndexedList::resize() {
    TElem* array = new TElem[this->capacity*2];
    TElem* array_next = new TElem[this->capacity*2];
    for (int index = 0; index < this->length; index++) {
        array[index] = this->elements[index];
        array_next[index] = this->next[index];
    }
    for (int index = this->length; index < this->capacity*2; index++)
        array_next[index] = index + 1;
    this->capacity *= 2;
    delete[] this->elements;
    delete[] this->next;
    this->elements = array;
    this->next = array_next;
}
// O(2*capacity)

void IndexedList::addToEnd(TElem e) {
    //TODO - Implementation
    if (this->length + 1 == this->capacity)
        resize();
    if (this->head == -1) {
        this->head = 0;
        this->next[0] = 1;
        this->elements[0] = e;
        this->lastIndex = 0;
        this->firstFree = 1;
        this->next[this->lastIndex] = -1;
    }
    else {
        this->elements[this->firstFree] = e;
        int aux = this->firstFree;
        this->firstFree = this->next[this->firstFree];
        //this->next[aux] = this->next[this->lastIndex];
        this->next[this->lastIndex] = aux;
        this->lastIndex = aux;
        this->next[this->lastIndex] = -1;
    }
    this->length++;
}
// O(1)

void IndexedList::addToPosition(int pos, TElem e) {
    //TODO - Implementation
    if (pos >= this->length || pos < 0)
        throw exception();
    if (this->length + 1 == this->capacity)
        resize();
    int current_position = this->head;
    int prev_position = -1;
    for (int index = 0; index < pos; index++) {
        prev_position = current_position;
        current_position = this->next[current_position];
    }

    if (pos == 0) {
        // if we add at the beginning
        if (this->head == -1) {
            // if the list is empty
            this->head = 0;
            this->elements[0] = e;
            this->next[0] = -1;
            this->firstFree = 1;
            this->lastIndex = 0;
            this->length++;
        }
        else {
            this->elements[this->firstFree] = e;
            this->head = this->firstFree;
            int aux = this->next[firstFree];
            this->next[firstFree] = current_position;
            this->firstFree = aux;
            this->length++;
        }
    }
    else if (pos == this->length-1) {
        addToEnd(e);
    }
    else {
        this->elements[this->firstFree] = e;
        int aux = this->firstFree;
        this->firstFree = this->next[aux];
        this->next[prev_position] = aux;
        this->next[aux] = current_position;
        this->length++;

    }
}
//BC: Theta(1) - we add to the first position
//WC: Theta(length) - we add to the last position
//AC: O(length)
// O(pos)

TElem IndexedList::remove(int pos) {
    //TODO - Implementation
    if (pos >= this->length || pos < 0)
        throw exception();
    int current_position = this->head, prev;
    TElem current_element = this->elements[current_position];
    while (pos > 0) {
        pos--;
        prev = current_position;
        current_position = this->next[current_position];
        current_element = this->elements[current_position];
    }
    // we have to check if we delete the first element
    if (current_position == this->head) {
        this->head = this->next[this->head];
    }
    else{
        // check if we delete the last element
        if (current_position==this->lastIndex) {
            this->lastIndex = prev;
        }
        this->next[prev] = this->next[current_position];
    }
    this->next[current_position] = this->firstFree;
    this->firstFree = current_position;
    this->length--;
    return current_element;
}
//BC: Theta(1) - we remove the first element
//WC: Theta(length) - we remove the last element
//AC: O(length)
// O(pos)

int IndexedList::search(TElem e) const{
    //TODO - Implementation
    int pos = 0;
    int current_position = this->head;
    TElem current_element = this->elements[current_position];
    while (pos < this->length) {
        if (current_element == e) {
            return pos;
        }
        pos++;
        current_position = this->next[current_position];
        current_element = this->elements[current_position];
    }
    return -1;
}
// BC: Theta(1) - the element is on the first position
// WC: Theta(length) - the element is on the last position
// AC: Theta(length)

ListIterator IndexedList::iterator() const {
    return ListIterator(*this);        
}
// Theta(1)

IndexedList::~IndexedList() {
	//TODO - Implementation
    delete[] this->elements;
    delete[] this->next;
}
// Theta(1) 

