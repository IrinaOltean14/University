#include "AdministratorService.h"


AdminService::AdminService() {

}

AdminService::~AdminService() {

}

void AdminService::PopulateList() {
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

int AdminService::GetSizeService() {
	return this->repository.GetSizeRepo();
}

Event* AdminService::GetElementsService() {
	return this->repository.GetElementsRepo();
}

int AdminService::IsEventAdded(string title) {
	Event* events = this->GetElementsService();
	int numberOfEvents = this->GetSizeService();
	for (int index = 0; index < numberOfEvents; index++)
		if (title == events[index].GetTitle())
			return index;
	return -1;
}

void AdminService::AddEventService(string title, string description, int year, int month, int day, int hour, int minute, int people, string link) {
	Event event;
	event = Event(title, description, year, month, day, hour, minute, people, link);
	this->repository.AddRepo(event);
}

void AdminService::DeleteEventService(int index) {
	this->repository.DeleteEventRepo(index);
}

void AdminService::UpdateEventService(int index, string title, string description, int year, int month, int day, int hour, int minute, int people, string link) {
	Event event;
	event = Event(title, description, year, month, day, hour, minute, people, link);
	this->repository.UpdateEventRepo(index, event);
}

void AdminService::GetAllEvents(Event allEvents[]) {
	this->repository.GetAllEvents(allEvents);
}

DynamicArray<Event> AdminService::GetAll(){
	return this->repository.GetAll();
}

void TestAdmin() {
	AdminService service;
	service.PopulateList();
	assert(service.GetSizeService() == 10);
	service.AddEventService("Concert", "FORM", 2023, 2, 29, 20, 0, 100, "https://www.facebook.com/events/8722417104497109");
	assert(service.GetSizeService() == 11);
	assert(service.GetElementsService()[0].GetTitle() == "Concert Bosquito");
	service.DeleteEventService(0);
	assert(service.GetSizeService() == 10);
	service.UpdateEventService(0, "Concert Bosquito", "Muzica de petrecere", 2023, 3, 31, 20, 0, 100, "https://www.facebook.com/events/244327624594653");
	assert(service.GetElementsService()[0].GetTitle() == "Concert Bosquito");
	
}
