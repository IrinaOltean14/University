#include "Service.h"
#include <iostream>
#include <assert.h>

Service::Service() {
}

Service::~Service() = default;

void Service::AddRepository(const Event& event) {
	this->repo.AddEvent(event);
}

DynamicArray<Event> Service::GetEvents() {
	return this->repo.GetEvents();
}

void Service::PopulateList() {
	this->repo.AddEvent(Event("Concert The tiger Lillies", "FORM", 2023, 4, 29, 20, 0, 100, "https://www.facebook.com/events/8722417104497109"));
	this->repo.AddEvent(Event("Eat and meet", "Food trucks", 2023, 7, 31, 12, 0, 150, "https://www.facebook.com/events/904836817236714"));
	this->repo.AddEvent(Event("TUJAMO x Heart Society", "Party", 2023, 4, 8, 21, 30, 200, "https://www.facebook.com/events/1014477312857367"));
	this->repo.AddEvent(Event("Ateleier educatie montana si ecologica", "FSEGA", 2023, 2, 3, 19, 0, 50, "https://www.facebook.com/events/721878482736620/"));
	this->repo.AddEvent(Event("Meet and play", "Board game night", 2023, 4, 7, 18, 30, 30, "https://www.facebook.com/events/349933163684957/508375337840738/"));
	this->repo.AddEvent(Event("Latino Afro Party", "FORM space", 2023, 4, 7, 23, 0, 250, "https://www.facebook.com/events/1424221011653949"));
	this->repo.AddEvent(Event("Plaiesii", "Muzica populara", 2023, 8, 23, 17, 0, 70, "https://www.facebook.com/events/915997253059555/"));
	this->repo.AddEvent(Event("Dance cup", "Concurs de dansuri", 2023, 12, 8, 15, 0, 300, "https://www.facebook.com/events/185365324228929"));
	this->repo.AddEvent(Event("Book swap", "Schimb de carti", 2023, 11, 8, 16, 0, 40, "https://www.facebook.com/events/6372068299511170"));
}

int Service::GetIndexOfEvent(string title) {
	DynamicArray<Event> events = this->GetEvents();
	for (int index = 0; index < events.GetSize(); index++)
		if (title == events[index].GetTitle())
			return index;
	return -1;
}

void Service::ModifyPeople(string title, int people) {
	DynamicArray<Event> events = this->GetEvents();
	int index = this->GetIndexOfEvent(title);
	Event event = events[index];
	Event new_event = Event(title, event.GetDescription(), event.GetDate().year, event.GetDate().month, event.GetDate().day, event.GetDate().hour, event.GetDate().minute, event.GetPeople() + people, event.GetLink());
	this->UpdateEvent(index, new_event);
}

int Service::GetIndexOfEventInInterestedList(string title) {
	DynamicArray<Event> events = this->GetInterestedList();
	for (int index = 0; index < events.GetSize(); index++)
		if (title == events[index].GetTitle())
			return index;
	return -1;

}

void Service::DeleteEvent(int position) {
	this->repo.DeleteEvent(position);
}

void Service::DeleteFromInterestedList(int position) {
	this->interestedList.DeleteEvent(position);
}

void Service::UpdateEvent(int position, const Event& event) {
	this->repo.UpdateEvent(position, event);
}

InterestedList Service::FilterEventsByMonth(int month) {
	InterestedList eventsByMonth;
	DynamicArray<Event> events = this->GetEvents();
	for (int index1 = 0; index1 < events.GetSize(); index1++)
		for (int index2 = index1 + 1; index2 < events.GetSize(); index2++)
		{
			if (events[index1].GetDate().month > events[index2].GetDate().month || (events[index1].GetDate().month == events[index2].GetDate().month && events[index1].GetDate().day > events[index2].GetDate().day))
							events.switchItems(index1, index2);
		}
			
	for (int index = 0; index < events.GetSize(); index++)
		if (month == -1 || events[index].GetMonth() == month)
			eventsByMonth.AddEvent(events[index]);

	return eventsByMonth;
}

void Service::AddInterestedList(const Event& event) {
	this->interestedList.AddEvent(event);
}

DynamicArray<Event> Service::GetInterestedList() {
	return this->interestedList.GetAllEvents();
}

Event& Service::GetEventByIndex(int position) {
	return this->repo.GetEventByIndex(position);
}

void Test() {
	Event event = Event("Eat and meet", "Food trucks", 2023,11, 31, 12, 0, 150, "https://www.facebook.com/events/904836817236714");
	Service service;
	service.AddRepository(event);
	DynamicArray<Event> events = service.GetEvents();
	assert(events.GetSize() == 1);
	assert(service.GetIndexOfEvent("Eat and meet") == 0);
	assert(service.GetIndexOfEvent("Eat") == -1);
	Event new_event;
	new_event = service.GetEventByIndex(0);
	assert(new_event.GetTitle() == "Eat and meet");
	service.ModifyPeople("Eat and meet", 10);
	new_event = Event("Book swap", "Schimb de carti", 2023, 7, 8, 16, 0, 40, "https://www.facebook.com/events/6372068299511170");
	service.UpdateEvent(0, new_event);
	service.AddInterestedList(event);
	service.AddInterestedList(new_event);
	service.DeleteEvent(0);
	service.AddRepository(event);
	service.AddRepository(new_event);
	DynamicArray<Event> interestedList = service.GetInterestedList();
	assert(interestedList.GetSize() == 2);
	InterestedList eventsByMonth = service.FilterEventsByMonth(-1);	
	Event current_event = eventsByMonth.GetCurrentEvent();
	assert(current_event.GetTitle() == "Book swap");
	eventsByMonth.IncrementIndexOfCurrentEvent();
	//cout << eventsByMonth.GetSize() << endl;
	eventsByMonth.IncrementIndexOfCurrentEvent();
	assert(eventsByMonth.GetSize() == 2);
	assert(service.GetIndexOfEventInInterestedList("Book swap") == 1);
	service.DeleteFromInterestedList(0);
	service.DeleteFromInterestedList(0);
	assert(service.GetInterestedList().GetSize() == 0);
	service.DeleteEvent(0);
	service.DeleteEvent(0);
	assert(service.GetEvents().GetSize() == 0);
	assert(service.GetIndexOfEventInInterestedList("CEva") == -1);
	for (int index=0;index<=11;index++)
		service.AddRepository(event);
	for (int index = 0; index <= 11; index++)
		service.DeleteEvent(0);
}