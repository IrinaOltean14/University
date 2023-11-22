#pragma once
#include <string>
#include <assert.h>
#include <iostream>
//#include <Windows.h>
//#include <shellapi.h>
#include <utility>
#include <vector>
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
	Event(string title, string description, int day, int month, int year, int hour, int minute, int people, string link);
	~Event();

	string GetTitle() const;
	string toString();
	int GetMonth();
	string GetDescription() const;
	string GetLink() const;
	Date GetDate() const;
	int GetPeople() const;
	void ModifyNumberOfPeople(int number);

	friend istream& operator>>(istream& is, Event& event);
	friend ostream& operator<<(ostream& os, const Event& event);
};

void TestDomain();