#pragma once
#include "Repository.h"
#include "AdministratorService.h"

class UserService {
private:
	Repository repository;
	int indexOfCurrentEvent;
	Repository InterestedList;
public:
	UserService();
	~UserService();
	bool DoesEventExist(int month);
	Event GetCurrentEventOfGivenMonth(int month);
	void AddEventToInterested();
	int GetInterestedListSize();
	void DeleteEventFromInterested(int index, int index_in_admin);
	Event* GetEventsInInterested();
	void UserService::PopulateList();
	void SetIndex();
	void IncreaseIndex();
	int IsEventAdded(string title);
	DynamicArray<Event> GetAllEvent();
};
void TestUserService();