#include "UI.h"
#include <crtdbg.h>
#include "InterestedCSV.h"
#include "InterestedHTML.h"
void startProgram() {
	Repository repo{ "Events.txt" };
	while (true) {
		cout << "Choose type of file: \n";
		cout << "1. CSV\n";
		cout << "2. HTML\n";
		string csv = "1", html = "2", command;
		cout << "Enter: ";
		cin >> command;
		InterestedList* interestedList;
		if (command == csv) {
			interestedList = new CSVInterested();
			interestedList->setType("csv");
			Service service{ repo, interestedList };
			UI ui{ service };
			ui.start();
			break;
		}
		else if (command == html) {
			interestedList = new HTMLInterested();
			interestedList->setType("html");
			Service service{ repo, interestedList };
			UI ui{ service };
			ui.start();
			break;
		}

	}
}

int main() {
	TestAll();
	startProgram();
	_CrtDumpMemoryLeaks();
	system("pause");
	return 0;
}