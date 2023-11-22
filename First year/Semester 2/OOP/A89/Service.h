#pragma once
#include "Repository.h"
#include "InterestedList.h"
#include "InterestedCSV.h"
#include "InterestedHTML.h"
#include "Validator.h"

class Service {
private:
	Repository* repo;
	InterestedList* interestedList;
public:
	explicit Service(Repository* repo, InterestedList* interestedList);
	~Service();

	void AddRepository(const Event& event);
	vector<Event>& GetEvents();
	int GetIndexOfEvent(string title);
	void DeleteEvent(int position);
	void UpdateEvent(int position, const Event& event);
	void ModifyPeople(string title, int people);
	Event& GetEventByIndex(int poisiton);
	Event& GetEventByTitle(string title);

	InterestedList* FilterEventsByMonth(int month, string type);
	void AddInterestedList(const Event& event);
	vector<Event> GetInterestedList();
	int GetIndexOfEventInInterestedList(string title);
	void DeleteFromInterestedList(int position);

	string getType() { return this->interestedList->getType(); } // get the type of file we work with (html or csv)

	/*void InterestedListSave();
	void InterestedListOpen();*/
};
//void Test();