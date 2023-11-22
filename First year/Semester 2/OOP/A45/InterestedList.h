#pragma once
#pragma once
#include "DynamicArray.h"
#include "Domain.h"

class InterestedList {
private:
	DynamicArray<Event> events;
	int current;
public:
	InterestedList();
	~InterestedList();

	void AddEvent(const Event& event);
	int GetSize();
	void IncrementIndexOfCurrentEvent();
	Event GetCurrentEvent();
	DynamicArray<Event> GetAllEvents();
	void DeleteEvent(int position);
};