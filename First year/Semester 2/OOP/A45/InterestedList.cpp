#include "InterestedList.h"
#include <iostream>

InterestedList::InterestedList() {
	this->current = 0;
}

InterestedList::~InterestedList() {

}

void InterestedList::AddEvent(const Event& event) {
	this->events.addItem(event);
}

int InterestedList::GetSize() {
	return this->events.GetSize();
}

Event InterestedList::GetCurrentEvent() {
	return this->events[this->current];
}

void InterestedList::IncrementIndexOfCurrentEvent() {
	if (this->current + 1 == this->GetSize())
		this->current = 0;
	else
		this->current++;
}

DynamicArray<Event> InterestedList::GetAllEvents() {
	return this->events;
}

void InterestedList::DeleteEvent(int position) {
	this->events.deleteItem(position);
}

