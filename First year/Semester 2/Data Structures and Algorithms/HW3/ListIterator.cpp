#include "ListIterator.h"
#include "IndexedList.h"
#include <exception>
#include <iostream>
using namespace std;

ListIterator::ListIterator(const IndexedList& list) : list(list){
   //TODO - Implementation
    this->current = list.head;

}

void ListIterator::previous() {
    if (!valid())
        throw exception();
    if (this->current == list.head) {
        
        this->current = -1;
    }
    else {
        int position = list.head;
        while (list.next[position] != this->current)
            position = list.next[position];
        this->current = position;
    }
}
// BC: Theta(1)
// WC: Theta(length) 
// AC: Theta(length)


void ListIterator::first(){
    //TODO - Implementation
    this->current = list.head;
}
// Theta(1)

void ListIterator::next(){
    //TODO - Implementation
    if (valid())
        this->current = list.next[this->current];
    else
        throw exception();
}
// Theta(1)

bool ListIterator::valid() const{
    //TODO - Implementation
    return (this->current != -1);

}
// Theta(1)

TElem ListIterator::getCurrent() const{
   //TODO - Implementation
    if (valid())
        return list.elements[this->current];
    else
        throw exception();
}
// Theta(1)