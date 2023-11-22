#pragma once
#include "DynamicArray.h"
#include "Domain.h"
#include <vector>

class InterestedList {
private:
	vector<Event> events;
	int current;
public:
	InterestedList();
	~InterestedList();

	void AddEvent(const Event& event);
	int GetSize();
	void IncrementIndexOfCurrentEvent();
	Event GetCurrentEvent();
	vector<Event> GetAllEvents();
	void DeleteEvent(int position);
	void DeleteCurrentEvent();
};