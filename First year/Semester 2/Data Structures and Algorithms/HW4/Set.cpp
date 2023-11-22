#include "Set.h"
#include "SetITerator.h"

Set::Set() {
	//TODO - Implementation
	this->length = 0;
	this->all = 0;
	this->capacity = 17;
	this->hashTable = new TElem[17];
	for (int i = 0; i < 17; i++)
		this->hashTable[i] = NULL_TELEM;
	this->MAXloadFactor = 0.75;
}
// Theta(capacity)

bool isPrime(int x) {
	if (x < 2 || x>2 && x % 2 == 0)
		return false;
	for (int d = 3; d * d <= x; d += 2)
		if (x % d == 0)
			return false;
	return true;
}
// BC: Theta(1) when x < 2 or x % 2 = 0
// WC: O(sqrt(x))
// Total: O(sqrt(x))

int Set::getLargestPrime(int x) {
	x++;
	while (!isPrime(x))
		x++;
	return x;
}
// O(n*sqrt(x)) - n average number of iterartions needed to find next prime

int Set::h1(TElem e) const {
	return abs(e) % this->capacity;
}
// Theta(1)

int Set::h2(TElem e) const {
	return 1 + (abs(e) % (this->capacity - 1));
}
// Theta(1)

void Set::resize() {
	int prime = getLargestPrime(this->capacity*2);
	int old_capacity = this->capacity;
	this->capacity = prime;
	TElem* newTable = new TElem[prime];
	for (int index = 0; index < prime; index++)
		newTable[index] = NULL_TELEM;
	for (int index = 0; index < old_capacity; index++) {
		if (this->hashTable[index] != NULL_TELEM) {
			int hash1 = h1(this->hashTable[index]);
			int hash2 = h2(this->hashTable[index]);
			int count = 0;
			int position = (hash1 + count * hash2) % this->capacity;
			while (newTable[position] != NULL_TELEM) {
				count++;
				position = (hash1 + count * hash2) % this->capacity;
			}
			newTable[position] = this->hashTable[index];
		}
	}
	delete[] this->hashTable;
	this->hashTable = newTable;
}
// Theta(capacity)

bool Set::add(TElem elem) {
	//TODO - Implementation
	// if the hash is full we resize
	double loadFacor = (double)this->all / this->capacity;
	if (loadFacor >= this->MAXloadFactor)
		resize();
	int hash1 = h1(elem);
	int hash2 = h2(elem);
	int count = 0;
	int position = (hash1+count*hash2)%this->capacity;
	// if the element is already in the hash we return false
	if (search(elem))
		return false;
	// otherwise we add the element
	while (this->hashTable[position] != NULL_TELEM) {
		count++;
		position = (hash1 + count * hash2) % this->capacity;
	}
	this->hashTable[position] = elem;	
	this->length++;
	this->all++;
	return true;
}
// BC: Theta(1) - the element already exists in the set (is the first one)
// WC: O(n) - when resize is neccessary,  resize operation and rehashing require iterating through all existing elements
// Theta(1) - assumig good hash function and adeqately sized hash table


bool Set::remove(TElem elem) {
	//TODO - Implementation
	int hash1 = h1(elem);
	int hash2 = h2(elem);
	int count = 0;
	int position = (hash1 + count * hash2) % this->capacity;
	int initialPosition = -1111111;
	while (this->hashTable[position] != NULL_TELEM && count<this->capacity) {
		if (this->hashTable[position] == elem) {
			this->hashTable[position] = DELETED_TELEM;
			this->length--;
			return true;
		}
		if (initialPosition == -1111111)
			initialPosition = position;
		count++;
		position = (hash1 + count * hash2) % this->capacity;
	}
	return false;
}
// BC: Theta(1) - the element to be removed is found at the initial position determined by the hash function
// WC: O(n) - element is not in the set, when all elements are clustered together and cause collisions
// Total: O(1) - assumig good hash function and adeqately sized hash table


bool Set::search(TElem elem) const {
	//TODO - Implementation
	int hash1 = h1(elem);
	int hash2 = h2(elem);
	int count = 0;
	int position = (hash1 + count * hash2) % this->capacity;
	int initialPosition = -1111111;
	while (this->hashTable[position] != NULL_TELEM && count<this->capacity) {
		if (this->hashTable[position] == elem) {
			return true;
		}
		if (initialPosition == -1111111)
			initialPosition = position;
		count++;
		position = (hash1 + count * hash2) % this->capacity;
	}
	return false;
}
// BC: Theta(1) - the element is found at the initial position determined by the hash function
// WC: O(capacity) - when all elements are clustered together and cause collisions
// Total: O(1)


int Set::size() const {
	//TODO - Implementation
	return this->length;
}
// Theta(1)


bool Set::isEmpty() const {
	//TODO - Implementation
	return (this->length == 0);
}
// Theta(1)


Set::~Set() {
	//TODO - Implementation
	delete[] this->hashTable;
}


SetIterator Set::iterator() const {
	return SetIterator(*this);
}
// Theta(1)


int Set::difference(const Set& s) {
	int removed = 0;
	SetIterator it = s.iterator();
	while (it.valid()) {
		bool found = remove(it.getCurrent());
		if (found)
			removed++;
		it.next();
	}	
	return removed;
}
// O(length of s) because we have to parse all the elements in s



