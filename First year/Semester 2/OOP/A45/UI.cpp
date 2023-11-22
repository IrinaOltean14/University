#include "UI.h"
#include <iostream>

using namespace std;

UI::UI() {
}

UI::~UI() = default;

void UI::PrintAdminMenu() {
	cout << "\nSelect an operation\n";
	cout << "1. Add an event\n";
	cout << "2. Delete an event\n";
	cout << "3. Update an event\n";
	cout << "4. Print the events\n";
	cout << "5. Exit admin mode\n";
	cout << "Enter your option: ";
}

bool UI::IsInputNumber(string input) {
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
	if (this->service.GetIndexOfEvent(title) != -1)
		throw "Event is already added";
	cout << "Enter the description: ";
	getline(cin, description);
	cout << "Enter the link: ";
	getline(cin, link);
	cout << "Enter the year of the event: ";
	getline(cin, yearS);
	if (!IsInputNumber(yearS) || yearS.size() != 4)
		throw "Invalid year";
	year = stoi(yearS);
	cout << "Enter the month of the event: ";
	getline(cin, monthS);
	if (!IsInputNumber(monthS) || monthS.size() == 0)
		throw "Invalid month";
	month = stoi(monthS);
	if (month <= 0 || month > 12)
		throw "Invalid month";
	cout << "Enter the day of the event: ";
	getline(cin, dayS);
	if (!IsInputNumber(dayS) || dayS.size() == 0)
		throw "Invalid day";
	day = stoi(dayS);
	if (day < 1 || day>31)
		throw "Invalid day";
	cout << "Enter the hour of the event: ";
	getline(cin, hourS);
	if (!IsInputNumber(hourS) || hourS.size() == 0)
		throw "Invalid hour";
	hour = stoi(hourS);
	if (hour < 0 || hour>23)
		throw "Invalid hour";
	cout << "Enter the minute of the event: ";
	getline(cin, minutesS);
	if (!IsInputNumber(minutesS) || minutesS.size() == 0)
		throw "Invalid minute";
	minute = stoi(minutesS);
	if (minute < 0 || minute>59)
		throw "Invalid minute";
	cout << "Enter the number of people participating: ";
	getline(cin, peopleS);
	if (!IsInputNumber(peopleS) || peopleS.size() == 0)
		throw "Invalid number of people";
	people = stoi(peopleS);
	Event event;
	event = Event(title, description, year, month, day, hour, minute, people, link);
	this->service.AddRepository(event);
	cout << "Event added successfully\n";
}

void UI::DeleteEvent() {
	string title;
	cout << "Enter the title of the string you want to delete: ";
	getline(cin, title);
	getline(cin, title);
	int index = this->service.GetIndexOfEvent(title);
	if (index == -1)
		throw "This event is not added";
	this->service.DeleteEvent(index);
	cout << "Event deleted successfully\n";
}

void UI::UpdateEvent() {
	string title, description, link;
	string yearS, monthS, dayS, hourS, minutesS, peopleS;
	int year, month, day, hour, minute, people;
	cout << "Enter the title of the string you want to update: ";
	getline(cin, title);
	getline(cin, title);
	int index = this->service.GetIndexOfEvent(title);
	if (index == -1)
		throw "This event is not added";
	cout << "Enter the updated description: ";
	getline(cin, description);
	cout << "Enter the updated link: ";
	getline(cin, link);
	cout << "Enter the updated year of the event: ";
	getline(cin, yearS);
	if (!IsInputNumber(yearS) || yearS.size() != 4)
		throw "Invalid year";
	year = stoi(yearS);
	cout << "Enter the updated month of the event: ";
	getline(cin, monthS);
	if (!IsInputNumber(monthS) || monthS.size() == 0)
		throw "Invalid month";
	month = stoi(monthS);
	if (month <= 0 || month > 12)
		throw "Invalid month";
	cout << "Enter the updated day of the event: ";
	getline(cin, dayS);
	if (!IsInputNumber(dayS) || dayS.size() == 0)
		throw "Invalid day";
	day = stoi(dayS);
	if (day < 1 || day>31)
		throw "Invalid day";
	cout << "Enter the updated hour of the event: ";
	getline(cin, hourS);
	if (!IsInputNumber(hourS) || hourS.size() == 0)
		throw "Invalid hour";
	hour = stoi(hourS);
	if (hour < 0 || hour>23)
		throw "Invalid hour";
	cout << "Enter the updated minute of the event: ";
	getline(cin, minutesS);
	if (!IsInputNumber(minutesS) || minutesS.size() == 0)
		throw "Invalid minute";
	minute = stoi(minutesS);
	if (minute < 0 || minute>59)
		throw "Invalid minute";
	cout << "Enter the updated number of people participating: ";
	getline(cin, peopleS);
	if (!IsInputNumber(peopleS) || peopleS.size() == 0)
		throw "Invalid number of people";
	people = stoi(peopleS);
	Event event = Event(title, description, year, month, day, hour, minute, people, link);
	this->service.UpdateEvent(index, event);
	cout << "Event updated successfully\n";
}

void UI::PrintEvents() {
	DynamicArray<Event> events = this->service.GetEvents();
	for (int index = 0; index < events.GetSize(); index++)
		cout << events[index].toString() << endl;
}

void UI::AdminMode() {
	cout << "\nYou are in administrator mode\n";
	bool inAdminMode = true;
	while (inAdminMode) {
		try {
			PrintAdminMenu();
			string command;
			string addEvent = "1", printEvents = "4", deleteEvent = "2", updateEvent = "3", exit = "5";
			cin >> command;
			if (command == addEvent)
				AddUI();
			else if (command == printEvents)
				PrintEvents();
			else if (command == deleteEvent)
				DeleteEvent();
			else if (command == updateEvent)
				UpdateEvent();
			else if (command == exit)
				break;
			else
				cout << "Invalid command";
		}
		catch (const char* ErrorMessage) {
			cout << ErrorMessage << endl;
		}
		catch (const exception& exception) {
			cerr << exception.what();
			cout << endl;
		}


	}
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
	InterestedList eventsByMonth = this->service.FilterEventsByMonth(month);
	if (eventsByMonth.GetSize() == 0)
		cout << "No events with the given month" << endl;
	else {
		bool next = true;
		while (next) {
			if (eventsByMonth.GetSize() == 0) {
				cout << "No events with the given month" << endl;
				break;
			}
			Event event = eventsByMonth.GetCurrentEvent();
			cout << event.toString() << endl;
			string link = string("start ").append(event.GetLink());
			system(link.c_str());
			cout << "Do you want to add the event to your interested list? Yes or no: ";
			string command;
			cin >> command;
			if (command == "yes") {
				int index = this->service.GetIndexOfEvent(event.GetTitle());
				eventsByMonth.DeleteEvent(index);
				this->service.GetEventByIndex(index).ModifyNumberOfPeople(1);
				this->service.AddInterestedList(this->service.GetEventByIndex(index));
			}
			cout << "Do you want to see the next event? Yes or no: ";
			cin >> command;

			if (command == "yes")
				eventsByMonth.IncrementIndexOfCurrentEvent();
			else
				next = false;
		}
	}
}

void UI::PrintInterestedList() {

	DynamicArray<Event> events = this->service.GetInterestedList();
	cout << events.GetSize() << endl;
	for (int index = 0; index < events.GetSize(); index++)
		cout << events[index].toString() << endl;
}

void UI::DeleteFromInterestedList() {
	string title;
	cout << "Enter the title of the event you want to delete: ";
	getline(cin, title);
	getline(cin, title);
	int index = this->service.GetIndexOfEventInInterestedList(title);
	if (index == -1)
		cout << "The event is not in the interested list\n";
	else {
		this->service.DeleteFromInterestedList(index);
		index = this->service.GetIndexOfEvent(title);
		this->service.GetEventByIndex(index).ModifyNumberOfPeople(-1);
		cout << "Event deleted successfully\n";
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
		string seeEventsByMonth = "1", deleteEvent = "2", printYourList = "3", exit = "4";
		cin >> command;
		if (command == seeEventsByMonth)
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
		else if (command == deleteEvent)
			DeleteFromInterestedList();
		else if (command == exit)
			break;
		else if (command == printYourList)
			PrintInterestedList();
	}
}

void UI::start() {
	this->service.PopulateList();
	while (true) {
		bool askForMode = true;
		string command;
		string administrator = "1", user = "2", exit = "3";
		while (askForMode) {
			cout << "\nChoose your mode\n";
			cout << "1. Administrator\n";
			cout << "2. User\n";
			cout << "3. Exit\n";
			cout << "Enter your mode: ";
			cin >> command;
			if (command == administrator || command == user || command == exit)
				break;
		}
		if (command == administrator)
			AdminMode();
		else if (command == user)
			UserMode();
		else if (command == exit)
			break;
	}
}

void TestAll() {
	TestDomain();
	Test();
}
