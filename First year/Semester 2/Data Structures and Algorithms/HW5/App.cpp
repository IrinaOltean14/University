#include <iostream>

#include "ShortTest.h"
#include "ExtendedTest.h"

int main(){
	testNew();
    testAll();
	testAllExtended();

    std::cout<<"Finished SMM Tests!"<<std::endl;
	system("pause");
}
