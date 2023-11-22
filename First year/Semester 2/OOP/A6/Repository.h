#pragma once

#include "Domain.h"
#include "DynamicArray.h"
#include <vector>
#include <algorithm>
using namespace std;

class Repository {
private:
	vector<Event> events;
public:
	Repository();
	~Repository();

	void AddEvent(const Event& event);
	void DeleteEvent(int position);
	void UpdateEvent(int position, const Event& event);
	Event& GetEventByIndex(int position);
	Event& GetEventByTitle(string title);

	//Event& operator[](int position);
	vector<Event> GetEvents();
	//int GetSize();
	
};