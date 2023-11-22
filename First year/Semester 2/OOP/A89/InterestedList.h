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
	void DeleteByTitle(string title);
	int GetSize();
	void IncrementIndexOfCurrentEvent();
	Event& GetCurrentEvent();
	vector<Event> GetAllEvents();
	int GetIndex();
	vector<Event> getEvents();

	void setType(string type);
	string getType();

	//virtual void saveToFile() = 0;
	//virtual void openInApp() = 0;
};