#include "UI.h"
#include <iostream>
using namespace std;

UI::UI() {
}

UI::~UI()
{

}

bool UI::IsOkInput(string input) {
	for (int index = 0; index < input.size(); index++)
		if (isalpha(input[index]))
			return false;
	return true;
}

void UI::AddUI() {
	string title, description, link;
	string yearS, monthS, dayS, hourS, minutesS, peopleS;
	int year, month, day, hour, minute, people;
	cout << "Enter the title: ";
	getline(cin, title);
	getline(cin, title);
	if (this->adminService.IsEventAdded(title) != -1)
		throw "Event is already added";
	cout << "Enter the description: ";
	getline(cin, description);
	cout << "Enter the link: ";
	getline(cin, link);
	cout << "Enter the year of the event: ";
	getline(cin, yearS);
	if (!IsOkInput(yearS) || yearS.size() != 4)
		throw "Invalid year";
	year = stoi(yearS);
	cout << "Enter the month of the event: ";
	getline(cin, monthS);
	if (!IsOkInput(monthS) || monthS.size() == 0)
		throw "Invalid month";
	month = stoi(monthS);
	if (month <= 0 || month > 12)
		throw "Invalid month";
	cout << "Enter the day of the event: ";
	getline(cin, dayS);
	if (!IsOkInput(dayS) || dayS.size() == 0)
		throw "Invalid day";
	day = stoi(dayS);
	if (day < 1 || day>31)
		throw "Invalid day";
	cout << "Enter the hour of the event: ";
	getline(cin, hourS);
	if (!IsOkInput(hourS) || hourS.size() == 0)
		throw "Invalid hour";
	hour = stoi(hourS);
	if (hour < 0 || hour>23)
		throw "Invalid hour";
	cout << "Enter the minute of the event: ";
	getline(cin, minutesS);
	if (!IsOkInput(minutesS) || minutesS.size() == 0)
		throw "Invalid minute";
	minute = stoi(minutesS);
	if (minute < 0 || minute>59)
		throw "Invalid minute";
	cout << "Enter the number of people participating: ";
	getline(cin, peopleS);
	if (!IsOkInput(peopleS) || peopleS.size() == 0)
		throw "Invalid number of people";
	people = stoi(peopleS);
	this->adminService.AddEventService(title, description, year, month, day, hour, minute, people, link);
	cout << "Event added successfully\n";
}


void UI::PrintAdminMenu() {
	cout << "\nSelect an operation\n";
	cout << "1. Add an event\n";
	cout << "2. Delete an event\n";
	cout << "3. Update an event\n";
	cout << "4. Print the events\n";
	cout << "5. Exit admin mode\n";
	cout << "Enter your option: ";
}

void UI::PrintEventsUI() {
	Event all_events[100];
	//all_events = this->adminService.GetAll()
	this->adminService.GetAllEvents(all_events);
	int numberOfEvents;
	numberOfEvents = this->adminService.GetSizeService();
	//cout << numberOfEvents << endl;
	for (int index = 0; index < numberOfEvents; index++)
		cout << all_events[index].toString() << endl;
}

void UI::DeleteUI() {
	string title;
	cout << "Enter the title of the string you want to delete: ";
	getline(cin, title);
	getline(cin, title);
	int index = this->adminService.IsEventAdded(title);
	if (index == -1)
		throw "This event is not added";
	this->adminService.DeleteEventService(index);
	cout << "Event deleted successfully\n";
}

void UI::UpdateUI() {
	string title, description, link;
	string yearS, monthS, dayS, hourS, minutesS, peopleS;
	int year, month, day, hour, minute, people;
	cout << "Enter the title of the string you want to update: ";
	getline(cin, title);
	getline(cin, title);
	int index = this->adminService.IsEventAdded(title);
	if (index == -1)
		throw "This event is not added";
	cout << "Enter the updated description: ";
	getline(cin, description);
	cout << "Enter the updated link: ";
	getline(cin, link);
	cout << "Enter the updated year of the event: ";
	getline(cin, yearS);
	if (!IsOkInput(yearS) || yearS.size() != 4)
		throw "Invalid year";
	year = stoi(yearS);
	cout << "Enter the updated month of the event: ";
	getline(cin, monthS);
	if (!IsOkInput(monthS) || monthS.size() == 0)
		throw "Invalid month";
	month = stoi(monthS);
	if (month <= 0 || month > 12)
		throw "Invalid month";
	cout << "Enter the updated day of the event: ";
	getline(cin, dayS);
	if (!IsOkInput(dayS) || dayS.size() == 0)
		throw "Invalid day";
	day = stoi(dayS);
	if (day < 1 || day>31)
		throw "Invalid day";
	cout << "Enter the updated hour of the event: ";
	getline(cin, hourS);
	if (!IsOkInput(hourS) || hourS.size() == 0)
		throw "Invalid hour";
	hour = stoi(hourS);
	if (hour < 0 || hour>23)
		throw "Invalid hour";
	cout << "Enter the updated minute of the event: ";
	getline(cin, minutesS);
	if (!IsOkInput(minutesS) || minutesS.size() == 0)
		throw "Invalid minute";
	minute = stoi(minutesS);
	if (minute < 0 || minute>59)
		throw "Invalid minute";
	cout << "Enter the updated number of people participating: ";
	getline(cin, peopleS);
	if (!IsOkInput(peopleS) || peopleS.size() == 0)
		throw "Invalid number of people";
	people = stoi(peopleS);
	this->adminService.UpdateEventService(index, title, description, year, month, day, hour, minute, people, link);
	cout << "Event updated successfully\n";

}

void UI::AdminMode() {
	cout << "\nYou are in administrator mode\n";
	bool inAdminMode = true;
	while (inAdminMode) {
		try {
			PrintAdminMenu();
			string command;
			cin >> command;
			if (command == "1")
				AddUI();
			else if (command == "2")
				DeleteUI();
			else if (command == "3")
				UpdateUI();
			else if (command == "4")
				PrintEventsUI();
			else if (command == "5")
				return;
			else
				cout << "Invalid command\n";
		}
		catch (const char* msg) {
			cout << msg << endl;
		}
		catch (const exception& exc) {
			cerr << exc.what();
			cout << endl;
		}


	}
}

void UI::PrintUserMenu() {
	cout << "\nSelect an operation\n";
	cout << "1. See the events for a given month ordered chronologically\n";
	cout << "2. Delete an event from your list\n";
	cout << "3. See your list\n";
	cout << "4. Exit\n";
	cout << "Enter your option: ";
}

void UI::UserMode() {
	cout << "You are in user mode\n";
	while (true) {
		this->PrintUserMenu();
		string command;
		cin >> command;
		if (command == "1")
			try {
			this->CreateListWithEventsUser();
		}
		catch (const char* message) {
			cout << message << endl;
		}
		catch (const exception& exception) {
			cerr << exception.what();
			cout << endl;
		}
		else if (command == "2")
			DeleteEventFromInterested();
		else if (command == "3")
			PrintInterestedListUser();
		else if (command == "4")
			break;
		else
			cout << "Invalid command\n";
	}
}

void UI::DeleteEventFromInterested() {
	string title;
	cout << "Enter the title of the string you want to delete: ";
	getline(cin, title);
	getline(cin, title);
	int index = this->userService.IsEventAdded(title);
	int index_in_admin_service = this->adminService.IsEventAdded(title);
	if (index == -1)
		cout << "The event you want to delete is not added\n";
	else {
		this->userService.DeleteEventFromInterested(index, index_in_admin_service);
	}
}

void UI::PrintInterestedListUser() {
	int numberOfEventsInInterested = this->userService.GetInterestedListSize();
	Event* events = this->userService.GetEventsInInterested();
	for (int index = 0; index < numberOfEventsInInterested; index++)
		cout << events[index].toString() << endl;
}

void UI::CreateListWithEventsUser() {
	int month;
	string input;
	cout << "Enter a month: ";
	getline(cin, input);
	getline(cin, input);
	if (input == "")
		month = -1;
	else {
		month = stoi(input);
		if (month <= 0 || month > 12)
			throw exception("Invalid month\n");
	}
	bool isMonthCorrect = this->userService.DoesEventExist(month);
	if (!isMonthCorrect)
		cout << "There are no events for this month\n";
	else {
		bool next = true;
		this->userService.SetIndex();
		while (next) {
			Event event = this->userService.GetCurrentEventOfGivenMonth(month);
			cout << event.toString() << endl;
			string link = string("start ").append(event.GetLink());
			system(link.c_str());
			this->userService.IncreaseIndex();
			cout << "Do you want to add the event to your interested list? Yes or no: ";
			cin >> input;
			if (input == "yes")
				this->userService.AddEventToInterested();
			cout << "Do you want to see the next event? Yes or no: ";
			cin >> input;
			if (input == "no")
				next = false;
			else {
				bool doesEventExist = this->userService.DoesEventExist(month);
				if (!doesEventExist) {
					cout << "No more events available\n";
					next = false;
				}
			}
			
		}
	}
}

void UI::start() {
	this->adminService.PopulateList();
	this->userService.PopulateList();
	TestAll();
	while (true) {
		int mode;
		mode = askForMode();
		if (mode == 1)
			AdminMode();
		else if (mode == 2)
			UserMode();
		else
			break;
	}
}

int UI::askForMode() {
	bool askForMode = true;
	while (askForMode) {
		string command;
		cout << "\nChoose your mode\n";
		cout << "1. Administrator\n";
		cout << "2. User\n";
		cout << "3. Exit\n";
		cout << "Enter your mode: ";
		cin >> command;
		if (command == "1")
			return 1;
		else if (command == "2")
			return 2;
		else if (command == "3")
			return 3;
		else
			cout << "Invalid input\n";
	}
}

void TestAll() {
	TestDomain();
	TestAdmin();
	TestUserService();
	TestDynamicArray();
	TestRepo();
	cout << "Tests successfull\n";
}
