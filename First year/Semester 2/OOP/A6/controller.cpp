#include "UI.h"
#include <crtdbg.h>

void startProgram() {
	UI ui;
	ui.start();
}

int main() {
	TestAll();
	startProgram();
	_CrtDumpMemoryLeaks();
	system("pause");
	return 0;
}