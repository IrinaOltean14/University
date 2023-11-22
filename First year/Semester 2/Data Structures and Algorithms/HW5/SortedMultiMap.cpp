#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;

SortedMultiMap::SortedMultiMap(Relation r) {
	this->r = r;
	this->capacity = 10;
	this->length = 0;
	this->firstFree = 0;
	this->nextFree = new int[this->capacity];
	this->nodes = new TElem[this->capacity];
	this->left = new int[this->capacity];
	this->right = new int[this->capacity];
	for (int i = 0; i < capacity; i++) {
		this->nextFree[i] = i + 1;
		this->nodes[i] = NULL_TELEM;
		this->left[i] = -1;
		this->right[i] = -1;
	}
	this->nextFree[capacity - 1] = -1;
	this->root = -1;
}
// Theta(capacity)

void SortedMultiMap::resize() {
	int newCapacity = capacity * 2; // Double the capacity
	// Create new arrays with the new capacity
	int* newFreePositions = new int[newCapacity];
	TElem* newNodes = new TElem[newCapacity];
	int* newLeft = new int[newCapacity];
	int* newRight = new int[newCapacity];

	// Copy the existing elements to the new arrays
	for (int i = 0; i < capacity; i++) {
		newFreePositions[i] = nextFree[i];
		newNodes[i] = nodes[i];
		newLeft[i] = left[i];
		newRight[i] = right[i];
	}

	// Initialize the remaining positions
	for (int i = capacity; i < newCapacity; i++) {
		newFreePositions[i] = i + 1;
		newNodes[i] = NULL_TELEM;
		newLeft[i] = -1;
		newRight[i] = -1;
	}

	// Update the firstFree position
	this->firstFree = capacity;

	// Set the last position in the new freePositions array as -1 to indicate the end
	newFreePositions[newCapacity - 1] = -1;
	// Deallocate the memory of the old arrays
	delete[] nextFree;
	delete[] nodes;
	delete[] left;
	delete[] right;

	// Update the member variables with the new arrays and capacity
	nextFree = newFreePositions;
	nodes = newNodes;
	left = newLeft;
	right = newRight;
	capacity = newCapacity;
	this->nextFree[capacity - 1] = -1;
}
// Theta(capacity)

void SortedMultiMap::add(TKey c, TValue v) {
	//TODO - Implementation
	TElem newElem = make_pair(c, v);
	if (this->length == capacity)
		resize();
	// if the adt is empty
	if (isEmpty()) {
		this->root = this->firstFree;
		this->firstFree = this->nextFree[this->firstFree];
		this->nodes[this->root] = newElem;
	}
	else {
		int current_position = root;
		int parent;
		while (current_position != -1) {
			parent = current_position;
			if (r(this->nodes[current_position].first, c)) {
				current_position = this->right[current_position];
			}
				
			else
				current_position = this->left[current_position];
		}
		if (!r(this->nodes[parent].first,c))
			this->left[parent] = this->firstFree;
		else
			this->right[parent] = this->firstFree;
		this->nodes[this->firstFree] = newElem;
		this->firstFree = this->nextFree[this->firstFree];
		
	}
	this->length++;

}
// BC: Theta(1) - if the map is empty, we add the root
// WC: Theta(n) - we add an element to the last level and the tree is highly inbalanced
// Total: O(log n)

vector<TValue> SortedMultiMap::search(TKey c) const {
	//TODO - Implementation
	vector<TValue> result;
	int current_position = this->root;
	while (current_position!=-1) {
		if (this->nodes[current_position].first == c)
			result.push_back(this->nodes[current_position].second);
		if (r(this->nodes[current_position].first, c))
			current_position = this->right[current_position];
		else
			current_position = this->left[current_position];
	}
	return result;
}
// BC: Theta(1) - the element we are looking for is the root
// WC: Theta(n) - if the tree is highly imbalanced, and each node only has one child resulting in a linear search
// Total: O(log n) - at each step of the search, the search space is divided in half

int SortedMultiMap::get_minimum(int node) {
	int current = node;
	while (this->left[current] != -1)
		current = this->left[current];
	return current;
}
// WC: O(n) - the tree is highly inbalanced
// Total: O(log n)

bool SortedMultiMap::remove(TKey c, TValue v) {
	//TODO - Implementation
	int current_position = root;
	int parent;
	while (current_position != -1) {
		if (this->nodes[current_position].first == c && this->nodes[current_position].second == v) {
			// we found the element
			// we have to check if it is the root
			if (current_position == root) {
				if (this->left[current_position] == -1 && this->right[current_position] == -1) {
					this->nextFree[current_position] = this->firstFree;
					this->firstFree = current_position;
					root = -1;
					this->length--;
				}
				else if (this->left[current_position] == -1 && this->right[current_position] != -1) {
					root = this->right[current_position];
					this->nextFree[current_position] = this->firstFree;
					this->firstFree = current_position;
					this->length--;

				}
				else if (this->left[current_position] != -1 && this->right[current_position] == -1) {
					root = this->left[current_position];
					this->nextFree[current_position] = this->firstFree;
					this->firstFree = current_position;
					this->length--;
				}
				else {
					int minimum = get_minimum(this->right[current_position]);
					remove(this->nodes[minimum].first, this->nodes[minimum].second);
					this->nodes[current_position] = this->nodes[minimum];
				}
				return true;
			}
			if (this->left[current_position] == -1 && this->right[current_position] == -1) {
				if (this->r(this->nodes[parent].first, this->nodes[current_position].first)) {
					this->right[parent] = -1;
				}
				else
					this->left[parent] = -1;
				this->nextFree[current_position] = this->firstFree;
				this->firstFree = current_position;
				this->length--;
			}
			else if (this->left[current_position] == -1 && this->right[current_position] != -1) {
				if (this->r(this->nodes[parent].first, this->nodes[current_position].first)) {
					this->right[parent] = this->right[current_position];
				}
				else
					this->left[parent] = this->right[current_position];
				this->nextFree[current_position] = this->firstFree;
				this->firstFree = current_position;
				this->length--;
			}
			else if (this->left[current_position] != -1 && this->right[current_position] == -1) {
				if (this->r(this->nodes[parent].first, this->nodes[current_position].first)) {
					this->right[parent] = this->left[current_position];
				}
				else
					this->left[parent] = this->left[current_position];
				this->nextFree[current_position] = this->firstFree;
				this->firstFree = current_position;
				this->length--;
			}
			else {
				// implement here please
				int minimum = get_minimum(this->right[current_position]);
				remove(this->nodes[minimum].first, this->nodes[minimum].second);
				this->nodes[current_position] = this->nodes[minimum];
			}
			return true;
		}
		parent = current_position;
		if (r(this->nodes[current_position].first, c))
			current_position = this->right[current_position];
		else
			current_position = this->left[current_position];
	}
	return false;
}
// BC: Theta(1) - we delete the root, and the root does not have 2 children
// WC: Theta(n) - if the tree is highly imbalanced
// Total: O(log n) 

int SortedMultiMap::size() const {
	//TODO - Implementation
	return this->length;
}
// Theta(1)

bool SortedMultiMap::isEmpty() const {
	//TODO - Implementation
	return (this->length == 0);
}
// Theta(1)

SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}
// Theta(1)

SortedMultiMap::~SortedMultiMap() {
	//TODO - Implementation
	delete[] nextFree;
	delete[] nodes;
	delete[] left;
	delete[] right;

}
// Theta(1)

bool SortedMultiMap::searchKey(int c) {
	int current_position = this->root;
	while (current_position != -1) {
		if (this->nodes[current_position].first == c)
			return true;
		if (r(this->nodes[current_position].first, c))
			current_position = this->right[current_position];
		else
			current_position = this->left[current_position];
	}
	return false;
}
// BC: Theta(1) - the element we are looking for is the root
// WC: Theta(n) - if the tree is highly imbalanced, and each node only has one child resulting in a linear search
// Total: O(log n) - at each step of the search, the search space is divided in half


int SortedMultiMap::addIfNotPresent(SortedMultiMap& smm) {
	int count = 0;
	SMMIterator it = smm.iterator();
	it.first();
	TElem current;
	while (it.valid()) {
		current = it.getCurrent();
		int key = current.first;
		bool found = searchKey(key);
		if (!found) {
			add(current.first, current.second);
			count++;
		}
		it.next();
	}
	return count;

}
// Total: O(sizeof(smm))