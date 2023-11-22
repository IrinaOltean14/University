#include <iostream>
#include "UI.h"
#include "Domain.h"
#include <crtdbg.h>

using namespace std;

void RunProgram() {
	UI ui;
	ui.start();
}

int main() {
	RunProgram();
	_CrtDumpMemoryLeaks();
	system("pause");
	return 0;
}