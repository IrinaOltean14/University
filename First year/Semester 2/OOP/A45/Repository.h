#pragma once
#include "DynamicArray.h"

class Repository {
private:
	DynamicArray<Event> dynamicArray;
public:
	Repository();
	~Repository();
	void AddRepo(const Event& event);
	Event* GetElementsRepo();
	void GetAllEvents(Event allEvents[]);
	void DeleteEventRepo(int index);
	void UpdateEventRepo(int index, Event newEvent);
	void SortEventsChronologically();
	int GetSizeRepo();
	DynamicArray<Event> GetAll();
};
void TestRepo();
void TestDynamicArray();
