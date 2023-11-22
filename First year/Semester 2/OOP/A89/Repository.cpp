#include "Repository.h"
#include <fstream>
#include <utility>
#include <algorithm>

Repository::Repository(string filename) {
	this->filename = filename;
	this->ReadFromFile();
}

Repository::~Repository() = default;

bool Repository::SearchForEventWithTheSameTitle(string title) {
	auto find = find_if(this->events.begin(), this->events.end(), [title](Event event) {return event.GetTitle() == title; });
	if (find != this->events.end())
		return true;
	return false;
}

int Repository::AddEvent(const Event& event) {
	//if (SearchForEventWithTheSameTitle(event.GetTitle()))
		//throw DuplicateEventException();
	this->events.push_back(event);
	this->WriteToFile();
	return 1;
}

void Repository::DeleteEvent(int position) {
	this->events.erase(this->events.begin() + position);
	this->WriteToFile();
}

void Repository::UpdateEvent(int position, const Event& event) {
	this->events[position] = event;
	this->WriteToFile();
}

//Event& Repository::operator[](int position) {
//	return this->events[position];
//}

//int Repository::GetSize() {
//	return this->events.size();
//}


vector<Event>& Repository::GetEvents() {
	return this->events;
}

Event& Repository::GetEventByIndex(int position) {
	return this->events[position];
}

Event& Repository::GetEventByTitle(string title) {
	for (auto& event : this->events)
		if (title == event.GetTitle())
			return event;
}

void Repository::ReadFromFile() {
	ifstream file(this->filename);
	if (file.is_open()) {
		Event event;
		while (file >> event) {
			this->events.push_back(event);
		}
		file.close();
	}
	else
		throw FileException("This file is not open!");
}

void Repository::WriteToFile() {
	ofstream file(this->filename);
	if (file.is_open()) {
		for (const auto& event : this->events)
			file << event;
		file.close();
	}
	else
		throw FileException("This file is not open!");
}
