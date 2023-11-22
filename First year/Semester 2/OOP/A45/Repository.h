#pragma once

#include "Domain.h"
#include "DynamicArray.h"

class Repository {
private:
	DynamicArray<Event> events;
public:
	Repository();
	~Repository();

	void AddEvent(const Event& event);
	void DeleteEvent(int position);
	void UpdateEvent(int position, const Event& event);
	Event& GetEventByIndex(int position);

	DynamicArray<Event> GetEvents() const { return this->events; }
};
