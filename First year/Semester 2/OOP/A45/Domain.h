#pragma once
#include <string>
using namespace std;

struct Date {
	int year, month, day, hour, minute;
};

class Event {
private:
	string title;
	string description;
	Date date;
	int number_of_people;
	string link;
	int addedToWatchList;
public:
	// constructor
	//Event(string title = "", string description = "", int year = 0, int month = 0, int day = 0, int minutes = 0, int number_of_people = 0, string link = "");
	Event();
	Event(string title, string description, int year, int month, int day, int hour, int minute, int number_of_people, string link);
	string toString();
	string GetTitle();
	string GetDescription();
	string GetLink();
	Date GetDate();
	int GetMonth();
	int GetNumberOfPeople();
	int GetAddedToWatchList();
	void SetAddedToWatchList(int value);
	void ModiyNumberOfPeople(int value);
};
void TestDomain();