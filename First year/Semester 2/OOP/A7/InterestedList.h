#pragma once

#include "Domain.h"
#include <vector>

class InterestedList {
protected:
	vector<Event> events;
	int current{};
	string type;
public:
	InterestedList() = default;
	~InterestedList();

	void AddEvent(const Event& event);
	void DeleteEvent(int position);
	void DeleteCurrentEvent();
	int GetSize();
	void IncrementIndexOfCurrentEvent();
	Event& GetCurrentEvent();
	vector<Event> GetAllEvents();

	void setType(string type);
	string getType();

	virtual void saveToFile() = 0;
	virtual void openInApp() = 0;
};