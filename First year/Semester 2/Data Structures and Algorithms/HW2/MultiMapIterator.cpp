#include "MultiMapIterator.h"
#include "MultiMap.h"
#include <iostream>


MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	//TODO - Implementation
	this->current_node = this->col.head;
	if (this->current_node != NULL)
		this->current_value = this->current_node->first_value;
	else
		this->current_value = NULL;
}

TElem MultiMapIterator::getCurrent() const{
	//TODO - Implementation
	TElem current;
	if (!valid())
		throw exception();
	current.first = this->current_node->key;
	current.second = this->current_value->value;
	return current;
}
// Theta(1)

bool MultiMapIterator::valid() const {
	//TODO - Implementation
	if (this->col.isEmpty())
		return false;
	if (this->current_value != NULL)
		return true;
	return false;
}
// Theta(1)

void MultiMapIterator::next() {
	//TODO - Implementation
	if (!valid())
		throw exception();
	if (this->current_value->next != NULL) {
		//cout << 1 << endl;
		this->current_value = this->current_value->next;
	}
	else if (this->current_node->next!=NULL){
		//cout << 2 << endl;
		this->current_node = this->current_node->next;
		this->current_value = this->current_node->first_value;
	}
	else {
		//cout << 3 << endl;
		this->current_node = NULL;
		this->current_value = NULL;
	}
}
// Theta(1)

void MultiMapIterator::first() {
	//TODO - Implementation
	this->current_node = this->col.head;
	this->current_value = this->current_node->first_value;
}
// Theta(1)

