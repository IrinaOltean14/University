#pragma once
//DO NOT INCLUDE SETITERATOR
#include <iostream>
using namespace std;
//DO NOT CHANGE THIS PART
#define NULL_TELEM -111111
#define DELETED_TELEM -222222
typedef int TElem;
class SetIterator;

class Set {
	//DO NOT CHANGE THIS PART
	friend class SetIterator;

    private:
		//TODO - Representation
        TElem* hashTable; // the hash table implemented as an array of TElem elements
        int length;
        int capacity;
        double MAXloadFactor;
        int all;

        int h1(TElem e) const; // the primary hash function
        int h2(TElem e) const; // the secondary hash function
        int getLargestPrime(int capacity);
    public:
        //implicit constructor
        Set();

        void resize();

        //adds an element to the set
		//returns true if the element was added, false otherwise (if the element was already in the set and it was not added)
        bool add(TElem e);

        //removes an element from the set
		//returns true if e was removed, false otherwise
        bool remove(TElem e);

        //checks whether an element belongs to the set or not
        bool search(TElem elem) const;

        //returns the number of elements;
        int size() const;

        //check whether the set is empty or not;
        bool isEmpty() const;

        //return an iterator for the set
        SetIterator iterator() const;

        int difference(const Set& s);

        // destructor
        ~Set();

};





