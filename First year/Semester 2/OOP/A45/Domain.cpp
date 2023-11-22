#include "Domain.h"
#include <assert.h>

Event::Event() {
	this->people = 0;
}

Event::~Event() = default;

Event::Event(string title, string description, int year, int month, int day, int hour, int minute, int people, string link) {
	Date date;
	date.day = day;
	date.year = year;
	date.month = month;
	date.hour = hour;
	date.minute = minute;
	this->title = title;
	this->description = description;
	this->link = link;
	this->date = date;
	this->people = people;
}

string Event::toString() {
	string day = to_string(this->date.day);
	string month = to_string(this->date.month);
	string year = to_string(this->date.year);
	string minute = to_string(this->date.minute);
	string hour = to_string(this->date.hour);
	string people = to_string(this->people);
	string date = day + "/" + month + "/" + year + " " + hour + ":" + minute;
	return "Title: " + this->title + " | Description: " + this->description + " | Date: " + date + " | Number of people: " + people + " | Link: " + this->link;
}

string Event::GetTitle() {
	return this->title;
}

int Event::GetMonth() {
	return this->date.month;
}

string Event::GetDescription() {
	return this->description;
}

string Event::GetLink() {
	return this->link;
}

Date Event::GetDate() {
	return this->date;
}

int Event::GetPeople() {
	return this->people;
}

void Event::ModifyNumberOfPeople(int number) {
	this->people += number;
}

void TestDomain() {
	Event event = Event("Eat and meet", "Food trucks", 2023, 7, 31, 12, 0, 150, "https://www.facebook.com/events/904836817236714");
	Event new_event;
	assert(event.GetTitle() == "Eat and meet");
	assert(event.GetDescription() == "Food trucks");
	assert(event.GetLink() == "https://www.facebook.com/events/904836817236714");
	assert(event.GetMonth() == 7);
	assert(event.GetPeople() == 150);
	Date date;
	date = event.GetDate();
	assert(date.year == 2023 && date.day == 31 && date.month == 7);
	assert(event.toString() == "Title: Eat and meet | Description: Food trucks | Date: 31/7/2023 12:0 | Number of people: 150 | Link: https://www.facebook.com/events/904836817236714");
	event.ModifyNumberOfPeople(1);
	assert(event.GetPeople() == 151);

}