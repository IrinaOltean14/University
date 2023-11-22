#pragma once

#include <utility>

//DO NOT CHANGE THIS PART
typedef int TElem;
typedef std::pair<int, int>  ValuePair;
#define NULL_TELEM 0

class Matrix {

private:
	//TODO - Representation
	int lines, columns, capacity;
	TElem* nonZeroElements, * columnIndices, * lineCounter;

	//resize
	void resize(int newCapacity);

public:
	//constructor
	Matrix(int nrLines, int nrCols);

	//destructor
	~Matrix();

	//returns the number of lines
	int nrLines() const;

	//returns the number of columns
	int nrColumns() const;

	//returns the element from line i and column j (indexing starts from 0)
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem element(int i, int j) const;

	//modifies the value from line i and column j
	//returns the previous value from the position
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem modify(int i, int j, TElem e);

	int position_line(TElem element);

	int position_column(TElem element);

	ValuePair position(TElem element);

};
