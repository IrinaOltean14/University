#include "InterestedList.h"
#include <iostream>



InterestedList::~InterestedList() {

}

void InterestedList::AddEvent(const Event& event) {
	this->events.push_back(event);
	saveToFile();
}

int InterestedList::GetSize() {
	return this->events.size();
}

Event& InterestedList::GetCurrentEvent() {
	return this->events[this->current];
}

void InterestedList::IncrementIndexOfCurrentEvent() {
	if (this->current + 1 == this->GetSize())
		this->current = 0;
	else
		this->current++;
}

vector<Event> InterestedList::GetAllEvents() {
	return this->events;
}

void InterestedList::DeleteEvent(int position) {
	this->events.erase(this->events.begin() + position);
	saveToFile();
}

void InterestedList::DeleteCurrentEvent() {
	this->events.erase(this->events.begin() + this->current);
	saveToFile();
}

void InterestedList::setType(string type) {
	this->type = type;
}

string InterestedList::getType() {
	return this->type;
}


