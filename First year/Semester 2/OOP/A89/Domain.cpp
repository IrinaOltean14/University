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

string Event::GetTitle() const {
	return this->title;
}

int Event::GetMonth() {
	return this->date.month;
}

string Event::GetDescription() const {
	return this->description;
}

string Event::GetLink() const {
	return this->link;
}

Date Event::GetDate() const {
	return this->date;
}

int Event::GetPeople() const {
	return this->people;
}

void Event::ModifyNumberOfPeople(int number) {
	this->people += number;
}


istream& operator>>(istream& is, Event& event) {
	if (is.eof())
		is.setstate(ios_base::failbit);
	else {
		string line;
		vector<string> input;
		getline(is, line);
		if (!line.empty()) {
			size_t start;
			size_t end = 0;

			while ((start = line.find_first_not_of(',', end)) != string::npos) {
				end = line.find(',', start);
				input.push_back(line.substr(start, end - start));
			}
			event.title = input[0];
			event.description = input[1];
			event.date.year = stoi(input[2]);
			event.date.month = stoi(input[3]);
			event.date.day = stoi(input[4]);
			event.date.hour = stoi(input[5]);
			event.date.minute = stoi(input[6]);
			event.people = stoi(input[7]);
			event.link = input[8];
		}
	}
	return is;
}

ostream& operator<<(ostream& os, const Event& event) {
	os << event.title << "," << event.description << "," << event.date.year << "," << event.date.month << "," << event.date.day<<"," << event.date.hour << "," << event.date.minute << "," << event.people << "," << event.link << "\n";
	return os;
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