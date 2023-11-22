#include "SetIterator.h"
#include "Set.h"


SetIterator::SetIterator(const Set& m) : set(m)
{
	//TODO - Implementation
	if (set.size() == 0)
		this->currentPosition = -1;
	else
		first();
}
// Theta(1)


void SetIterator::first() {
	//TODO - Implementation
	this->currentPosition = 0;
	while (!valid())
		this->currentPosition++;
}
// O(capacity)


void SetIterator::next() {
	//TODO - Implementation
	if (valid()) {
		this->currentPosition++;
		while (!valid() && this->currentPosition < set.capacity)
			this->currentPosition++;
	}
	else
		throw exception();
}
// BC: Theta(1)
// WC: O(n)

TElem SetIterator::getCurrent()
{
	//TODO - Implementation
	if (valid())
		return set.hashTable[currentPosition];
	else
		throw exception();
}
// Theta(1)

bool SetIterator::valid() const {
	//TODO - Implementation
	return (this->currentPosition < set.capacity && set.hashTable[currentPosition] != NULL_TELEM && set.hashTable[currentPosition] != DELETED_TELEM&&this->currentPosition>=0);
}
// Theta(1)



