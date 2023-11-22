#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;


MultiMap::MultiMap(): head(NULL) {
	//TODO - Implementation
	this->length = 0;
}

vector<TValue> MultiMap::removeKey(TKey key) {
	std::vector<TValue> values;
	KeyNode* current_node = this->head;
	ValueNode* value_to_delete;// new ValueNode();
	//search for key and construct vector with its values
	while (current_node != NULL) {
		if (current_node->key == key) {
			ValueNode* current_value = current_node->first_value;
			while (current_value != NULL) {
				values.push_back(current_value->value);
				value_to_delete = current_value;
				current_value = current_value->next;
				delete value_to_delete;
				this->length--;
			}
			break;
		}
		current_node = current_node->next;
	}

	KeyNode* prev_node = this->head;
	if (prev_node == current_node) {
		this->head = current_node->next;
	}
	else {
		while (prev_node->next != current_node)
			prev_node = prev_node->next;
		prev_node->next = current_node->next;
	}
	delete current_node;
	return values;
}
// BC: O(number_of_values for the first key) - the key we look for is the first key in the map
// WC: O(len(Keys)+len(Values)) - the key is the las one, so all the values from the map are parsed
// AG: O(len(Keys)+len(Values))


void MultiMap::add(TKey c, TValue v) {
	//TODO - Implementation
	// if the map is empty, we add the first element without searching
	if (isEmpty()) {
		KeyNode* new_node = new KeyNode();
		new_node->next = NULL;
		new_node->key = c;
		ValueNode* value_node = new ValueNode();
		value_node->value = v;
		value_node->next = NULL;
		new_node->first_value = value_node;

		this->head = new_node;
	}
	else {
		// we want to know if the key already exists in the map
		KeyNode* current_node = this->head;
		bool does_the_key_exist = false;
		while (current_node != NULL && does_the_key_exist == false) {
			if (current_node->key == c) {
				does_the_key_exist = true;
				break;
			}
			current_node = current_node->next;
		}
		// if the key does not exist than we just add the new element to the end of the map
		if (!does_the_key_exist) {
			current_node = this->head;
			while (current_node->next != NULL)
				current_node = current_node->next;
			KeyNode* new_node = new KeyNode();
			new_node->next = NULL;
			new_node->key = c;
			ValueNode* value_node = new ValueNode();
			value_node->value = v;
			value_node->next = NULL;
			new_node->first_value = value_node;
			current_node->next = new_node;
		}
		else {
			// if the key does exist, we add the element in its corresponding place 
			current_node = this->head;
			while (current_node->key != c)
				current_node = current_node->next;
			ValueNode* value_node = new ValueNode();
			value_node->value = v;
			value_node->next = NULL;
			ValueNode* current_value = current_node->first_value;
			while (current_value->next != NULL)
				current_value = current_value->next;
			current_value->next = value_node;
		}
	}
	this->length++;
}
// BC: O(1) - the map is empty and we add the new element to the beginning
// WC: O(len(Keys)+len(Values)) - the map is not empty and we search for its place in the multi map (and its place is at the end of the map so all the elements are parsed)
// AG: Theta(len(Keys)+len(Values))


bool MultiMap::remove(TKey c, TValue v) {
	//TODO - Implementation
	// first we search for the key
	KeyNode* current_node = this->head;
	bool does_the_key_exist = false;
	while (current_node != NULL && !does_the_key_exist) {
		if (current_node->key == c) {
			does_the_key_exist = true;
			break;
		}
		current_node = current_node->next;
	}
	if (does_the_key_exist) {
		// if the key exist we look for the value
		ValueNode* current_value = current_node->first_value;
		bool does_the_value_exist = false;
		while (current_value != NULL && !does_the_value_exist) {
			if (current_value->value == v) {
				does_the_value_exist = true;
				break;
			}
			current_value = current_value->next;
		}
		if (does_the_value_exist) {
			if (current_value == current_node->first_value) {
				if (current_value->next == NULL) {
					// this means that this value is unique for the key so we have to delete both the key and the value
					delete current_value;
					KeyNode* prev_node = this->head;
					if (prev_node == current_node) {
						this->head = current_node->next;
					}
					else {
						while (prev_node->next != current_node)
							prev_node = prev_node->next;
						prev_node->next = current_node->next;
					}
					delete current_node;	
				}
				else {
					// if the value is the first value for a key we have to make the corresponding modifications
					current_node->first_value = current_value->next;
					delete current_value;
				}
			}
			else {
				// if the value is not the first one for the key we just jump over it
				ValueNode* prev_value = current_node->first_value;
				while (prev_value->next != current_value)
					prev_value = prev_value->next;
				prev_value->next = current_value->next;
				delete current_value;
			}
			this->length--;
			return true;
		}
		else
			return false;
		
	}
	else
		return false;
}
// BC: O(1) - the pair we look for is the first one
// WC: O(len(Keys)+len(Values)) - the pair is the last one in the map
// AC: Theta(len(Keys)+len(Values))


vector<TValue> MultiMap::search(TKey c) const {
	//TODO - Implementation
	std::vector<TValue> values;
	KeyNode* current_node = this->head;
	while (current_node != NULL) {
		if (current_node->key == c) {
			ValueNode* current_value = current_node->first_value;
			while (current_value != NULL) {
				values.push_back(current_value->value);
				current_value = current_value->next;
			}
			break;
		}
		current_node = current_node->next;
	}
	return values;
}
// BC: O(number_of_values for the first key) - the key is the first one in the list
// WC: O(len(Keys)+len(Values)) - the key is the last one on the list
// AC: Theta(len(Keys)+len(Values))

int MultiMap::size() const {
	//TODO - Implementation
	return this->length;
}
// Theta(1)


bool MultiMap::isEmpty() const {
	//TODO - Implementation
	if (this->head == NULL)
		return true;
	return false;
}
// Theta(1)

MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}
// Theta(1)


MultiMap::~MultiMap() {
	//TODO - Implementation
	if (!isEmpty()) {
		KeyNode* current_node = this->head;
		ValueNode* current_value = current_node->first_value;
		while (current_node != NULL) {
			current_value = current_node->first_value;
			while (current_value != NULL) {
				current_node->first_value = current_value->next;
				delete current_value;
				current_value = current_node->first_value;
			}
			current_node = current_node->next;
		}
		current_node = this->head;
		while (current_node != NULL) {
			this->head = current_node->next;
			delete current_node;
			current_node = this->head;
		}
	}
}
// BC: O(1) - the map is empty
// WC: O(len(Keys)+len(Values)) - we have to delete every element of the map
// AC: Theta(len(Keys)+len(Values))

