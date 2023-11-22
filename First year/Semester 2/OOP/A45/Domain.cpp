#include "Domain.h"
#include <utility>
#include <assert.h>
using namespace std;

Event::Event() {
	this->number_of_people = 0;
	this->addedToWatchList = 0;
}

Event::Event(string title, string description, int year, int month, int day, int hour, int minute, int number_of_people, string link) {
	this->number_of_people = number_of_people;
	this->title = title;
	this->description = description;
	this->link = link;
	Date date;
	date.year = year;
	date.month = month;
	date.day = day;
	date.minute = minute;
	date.hour = hour;
	this->date = date;
	this->addedToWatchList = 0;
}

string Event::toString() {
	string day = to_string(this->date.day);
	string month = to_string(this->date.month);
	string year = to_string(this->date.year);
	string minute = to_string(this->date.minute);
	string hour = to_string(this->date.hour);
	string people = to_string(this->number_of_people);
	string date = day + "/" + month + "/" + year + " " + hour + ":" + minute;
	return "Title: " + this->title + " | Description: " + this->description + " | Date: " + date + " | Number of people: " + people + " | Link: " + this->link;
}

string Event::GetLink() {
	return this->link;
}

string Event::GetTitle() {
	return this->title;
}

string Event::GetDescription() {
	return this->description;
}


int Event::GetNumberOfPeople() {
	return this->number_of_people;
}

int Event::GetMonth() {
	return this->date.month;
}

Date Event::GetDate() {
	return this->date;
}

int Event::GetAddedToWatchList() {
	return this->addedToWatchList;
}

void Event::SetAddedToWatchList(int value) {
	this->addedToWatchList = value;
}

void Event::ModiyNumberOfPeople(int value) {
	this->number_of_people += value;
}

void TestDomain() {
	Event event;
	Date date;
	date.day = 31;
	date.month = 3;
	date.year = 2023;
	event = Event("Concert Bosquito", "Muzica de petrecere", 2023, 3, 31, 20, 0, 100, "https://www.facebook.com/events/244327624594653");
	assert(event.GetTitle() == "Concert Bosquito");
	assert(event.GetMonth() == 3);
	assert(event.GetDescription() == "Muzica de petrecere");
	assert(event.GetLink() == "https://www.facebook.com/events/244327624594653");
	assert(event.GetNumberOfPeople() == 100);
	assert(event.GetDate().day == date.day);
	string ToString = "Title: Concert Bosquito | Description: Muzica de petrecere | Date: 31/3/2023 20:0 | Number of people: 100 | Link: https://www.facebook.com/events/244327624594653";
	assert(event.toString() == ToString);
}
