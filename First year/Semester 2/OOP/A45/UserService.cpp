#include "UserService.h"
#include <iostream>

UserService::UserService() {

}

UserService::~UserService() {

}

DynamicArray<Event> UserService::GetAllEvent() {
	return this->repository.GetAll();
}

bool UserService::DoesEventExist(int month) {
	this->repository.SortEventsChronologically();
	int numberOfEvents = this->repository.GetSizeRepo();
	bool doesEventExist = false;
	for (int index = 0; index < numberOfEvents; index++) {
		if (this->repository.GetElementsRepo()[index].GetAddedToWatchList() == 0 && (this->repository.GetElementsRepo()[index].GetMonth() == month || month == -1)) {
			doesEventExist = true;
			break;
		}
	}
	return doesEventExist;
}

void UserService::SetIndex() {
	this->indexOfCurrentEvent = 0;
}

void UserService::IncreaseIndex() {
	this->indexOfCurrentEvent += 1;
}

Event UserService::GetCurrentEventOfGivenMonth(int month) {
	int numberOfElements = this->repository.GetSizeRepo();
	while (this->indexOfCurrentEvent < numberOfElements) {
		if (this->indexOfCurrentEvent + 1 == numberOfElements)
			this->indexOfCurrentEvent = 0;
		else
			this->indexOfCurrentEvent += 1;
		if (this->repository.GetElementsRepo()[this->indexOfCurrentEvent].GetAddedToWatchList() == 0 && (this->repository.GetElementsRepo()[this->indexOfCurrentEvent].GetMonth() == month||month==-1)) {
			return this->repository.GetElementsRepo()[this->indexOfCurrentEvent];
		}
	}
		
}

void UserService::AddEventToInterested() {
	this->repository.GetElementsRepo()[this->indexOfCurrentEvent].ModiyNumberOfPeople(1);
	this->InterestedList.AddRepo(this->repository.GetElementsRepo()[this->indexOfCurrentEvent]);
	this->repository.GetElementsRepo()[this->indexOfCurrentEvent].SetAddedToWatchList(1);
}

int UserService::GetInterestedListSize() {
	return this->InterestedList.GetSizeRepo();
}

Event* UserService::GetEventsInInterested() {
	return this->InterestedList.GetElementsRepo();
}

int UserService::IsEventAdded(string title) {
	int numberOfElements = this->InterestedList.GetSizeRepo();
	for (int index = 0; index < numberOfElements; index++)
		if (this->GetEventsInInterested()[index].GetTitle() == title)
			return index;
	return -1;
}

void UserService::DeleteEventFromInterested(int index, int index_in_admin) {
	this->InterestedList.DeleteEventRepo(index);
	this->repository.GetElementsRepo()[index_in_admin].ModiyNumberOfPeople(-1);
	this->repository.GetElementsRepo()[index_in_admin].SetAddedToWatchList(0);
}

void UserService::PopulateList() {
	this->repository.AddRepo(Event("Concert Bosquito", "Muzica de petrecere", 2023, 3, 31, 20, 0, 100, "https://www.facebook.com/events/244327624594653"));
	this->repository.AddRepo(Event("Concert The tiger Lillies", "FORM", 2023, 4, 29, 20, 0, 100, "https://www.facebook.com/events/8722417104497109"));
	this->repository.AddRepo(Event("Eat and meet", "Food trucks", 2023, 7, 31, 12, 0, 150, "https://www.facebook.com/events/904836817236714"));
	this->repository.AddRepo(Event("TUJAMO x Heart Society", "Party", 2023, 4, 8, 21, 30, 200, "https://www.facebook.com/events/1014477312857367"));
	this->repository.AddRepo(Event("Ateleier educatie montana si ecologica", "FSEGA", 2023, 2, 3, 19, 0, 50, "https://www.facebook.com/events/721878482736620/"));
	this->repository.AddRepo(Event("Latino Afro Party", "FORM space", 2023, 4, 7, 23, 0, 250, "https://www.facebook.com/events/1424221011653949"));
	this->repository.AddRepo(Event("Meet and play", "Board game night", 2023, 4, 7, 18, 30, 30, "https://www.facebook.com/events/349933163684957/508375337840738/"));
	this->repository.AddRepo(Event("Plaiesii", "Muzica populara", 2023, 8, 23, 17, 0, 70, "https://www.facebook.com/events/915997253059555/"));
	this->repository.AddRepo(Event("Dance cup", "Concurs de dansuri", 2023, 12, 8, 15, 0, 300, "https://www.facebook.com/events/185365324228929"));
	this->repository.AddRepo(Event("Book swap", "Schimb de carti", 2023, 11, 8, 16, 0, 40, "https://www.facebook.com/events/6372068299511170"));
}

void TestUserService() {
	UserService userService;
	userService.SetIndex();
	userService.PopulateList();
	assert(userService.DoesEventExist(9) == false);
	assert(userService.GetCurrentEventOfGivenMonth(3).GetTitle() == "Concert Bosquito");
	userService.AddEventToInterested();
	assert(userService.GetInterestedListSize() == 1);
	assert(userService.GetEventsInInterested()[0].GetTitle() == "Concert Bosquito");
	assert(userService.IsEventAdded("Concert Bosquito") == 0);
	assert(userService.IsEventAdded("Concert") == -1);
	userService.DeleteEventFromInterested(0, 0);
	assert(userService.GetInterestedListSize() == 0);

}

