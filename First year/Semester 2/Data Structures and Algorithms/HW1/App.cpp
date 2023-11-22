
#include <iostream>
#include <assert.h>
#include "Matrix.h"
#include "ExtendedTest.h"
#include "ShortTest.h"

using namespace std;

void TestNew() {
	cout << "Test new\n";
	Matrix m(4, 4);
	m.modify(1, 1, 5);
	assert(m.position_line(5) == 1);
	assert(m.position_column(5) == 1);
	m.modify(2, 3, 10);
	assert(m.position_line(10) == 2);
	assert(m.position_column(10) == 3);
	m.modify(1, 3, 15);
	assert(m.position_line(15) == 1);
	assert(m.position_column(15) == 3);
	assert(m.position(15).first == 1);
	assert(m.position(15).second == 3);
}


int main() {
	TestNew();
	testAll();
	testAllExtended();
	cout << "Test End" << endl;
	system("pause");
}