#pragma once
#include "Repository.h"
#include "InterestedList.h"

class Service {
private:
	Repository repo;
	InterestedList interestedList;
public:
	Service();
	~Service();

	void AddRepository(const Event& event);
	DynamicArray<Event> GetEvents();
	int GetIndexOfEvent(string title);
	void DeleteEvent(int position);
	void UpdateEvent(int position, const Event& event);
	void ModifyPeople(string title, int people);
	Event& GetEventByIndex(int poisiton);

	InterestedList FilterEventsByMonth(int month);
	void AddInterestedList(const Event& event);
	DynamicArray<Event> GetInterestedList();
	int GetIndexOfEventInInterestedList(string title);
	void DeleteFromInterestedList(int position);

	void PopulateList();
};
void Test();