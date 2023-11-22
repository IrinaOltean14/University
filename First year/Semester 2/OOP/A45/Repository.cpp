#include "Repository.h"

Repository::Repository() = default;

Repository::~Repository() = default;

void Repository::AddEvent(const Event& event) {
	this->events.addItem(event);
}

void Repository::DeleteEvent(int position) {
	this->events.deleteItem(position);
}

void Repository::UpdateEvent(int position, const Event& event) {
	this->events.updateItem(position, event);
}

Event& Repository::GetEventByIndex(int position) {
	return this->events.getElement(position);
}