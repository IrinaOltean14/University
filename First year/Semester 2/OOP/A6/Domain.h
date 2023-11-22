#pragma once
#include <string>\
#include <assert.h>
using namespace std;

struct Date {
	int year, month, day, hour, minute;
};

class Event {
private:
	string title;
	string description;
	string link;
	Date date;
	int people;
public:
	Event();
	Event(string title, string description, int year, int month, int day, int hour, int minute, int people, string link);
	~Event();

	string GetTitle();
	string toString();
	int GetMonth();
	string GetDescription();
	string GetLink();
	Date GetDate();
	int GetPeople();
	void ModifyNumberOfPeople(int number);


};

void TestDomain();