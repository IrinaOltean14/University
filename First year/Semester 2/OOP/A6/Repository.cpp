#include "Repository.h"

Repository::Repository() = default;

Repository::~Repository() = default;

void Repository::AddEvent(const Event& event) {
	this->events.push_back(event);
}

void Repository::DeleteEvent(int position) {
	this->events.erase(this->events.begin() + position);
}

void Repository::UpdateEvent(int position, const Event& event) {
	this->events[position] = event;
}

//Event& Repository::operator[](int position) {
//	return this->events[position];
//}

//int Repository::GetSize() {
//	return this->events.size();
//}


vector<Event> Repository::GetEvents() {
	return this->events;
}

Event& Repository::GetEventByIndex(int position) {
	return this->events[position];
}

Event& Repository::GetEventByTitle(string title) {
	for (auto& event: this->events)
		if (title == event.GetTitle())
			return event;}
