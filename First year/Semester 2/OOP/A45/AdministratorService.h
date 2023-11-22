#pragma once
#include "Repository.h"

class AdminService {
private:
	Repository repository;
public:
	AdminService();
	~AdminService();
	DynamicArray<Event> GetAll();
	void PopulateList();
	int GetSizeService();
	void AddEventService(string title, string description, int year, int month, int day, int hour, int minute, int people, string link);
	Event* GetElementsService();
	int IsEventAdded(string);
	void GetAllEvents(Event allEvents[]);

	void DeleteEventService(int index);
	void UpdateEventService(int index, string title, string description, int year, int month, int day, int hour, int minute, int people, string link);
};
void TestAdmin();