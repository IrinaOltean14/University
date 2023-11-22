#include "Service.h"
#include <iostream>
#include <algorithm>
#include <assert.h>
#include <utility>

Service::Service(Repository* repo, InterestedList* interestedList) {
	this->repo = repo;
	this->interestedList = interestedList;
}

Service::~Service() = default;

void Service::AddRepository(const Event& event) {
	//Validator::validate_event(event);
	this->repo->AddEvent(event);
}

vector<Event>& Service::GetEvents() {
	return this->repo->GetEvents();
}

int Service::GetIndexOfEvent(string title) {
	vector<Event> events = this->GetEvents();
	/*int index = -1;
	for (auto& event : events) {
		index += 1;
		if (title == event.GetTitle())
			return index;
	}
	return -1;*/
	auto found = find_if(events.begin(), events.end(), [title](Event event) {return event.GetTitle() == title; });
	if (found == events.end())
		throw NonexistentEvent();
	else
		return distance(events.begin(), found);
}

Event& Service::GetEventByTitle(string title) {
	return this->repo->GetEventByTitle(title);
}

void Service::ModifyPeople(string title, int people) {
	vector<Event> events = this->GetEvents();
	int index = this->GetIndexOfEvent(title);
	Event event = events[index];
	Event new_event = Event(title, event.GetDescription(), event.GetDate().year, event.GetDate().month, event.GetDate().day, event.GetDate().hour, event.GetDate().minute, event.GetPeople() + people, event.GetLink());
	this->UpdateEvent(index, new_event);
}

int Service::GetIndexOfEventInInterestedList(string title) {
	vector<Event> events = this->GetInterestedList();
	/*int index = -1;
	for (auto& event : events) {
		index += 1;
		if (title == event.GetTitle())
			return index;
	}
	return -1;*/
	auto found = find_if(events.begin(), events.end(), [title](Event event) {return event.GetTitle() == title; });
	if (found == events.end())
		return -1;
	else
		return distance(events.begin(), found);
}

void Service::DeleteEvent(int position) {
	this->repo->DeleteEvent(position);
}

void Service::DeleteFromInterestedList(int position) {
	this->interestedList->DeleteEvent(position);
}

void Service::UpdateEvent(int position, const Event& event) {
	Validator::validate_event(event);
	this->repo->UpdateEvent(position, event);
}

InterestedList* Service::FilterEventsByMonth(int month, string type) {
	InterestedList* eventsByMonth = new InterestedList();
	vector<Event>& events = this->GetEvents();
	sort(events.begin(), events.end(), [](Event a, Event b) {return a.GetDate().day < b.GetDate().day; });
	sort(events.begin(), events.end(), [](Event a, Event b) {return a.GetDate().month < b.GetDate().month; });
	for (auto& event : events)
		if (month == -1 || event.GetMonth() == month)
			eventsByMonth->AddEvent(event);
	return eventsByMonth;
}

void Service::AddInterestedList(const Event& event) {
	this->interestedList->AddEvent(event);
}

vector<Event> Service::GetInterestedList() {
	return this->interestedList->GetAllEvents();
}

Event& Service::GetEventByIndex(int position) {
	return this->repo->GetEventByIndex(position);
}

//void Service::InterestedListSave() {
//	this->interestedList->saveToFile();
//}
//
//void Service::InterestedListOpen() {
//	this->interestedList->openInApp();
//}

//void Test() {
//	Event event = Event("Eat and meet", "Food trucks", 2023, 7, 31, 12, 0, 150, "https://www.facebook.com/events/904836817236714");
//	Repository repo{ "Events.txt" };
//	InterestedList *interestedList;
//	interestedList = new CSVInterested();
//	interestedList->setType("csv");
//	Service service{ repo, interestedList };
//	service.AddRepository(event);
//	vector<Event> events = service.GetEvents();
//	assert(events.size() == 1);
//	assert(service.GetIndexOfEvent("Eat and meet") == 0);
//	assert(service.GetIndexOfEvent("Eat") == -1);
//	Event new_event = service.GetEventByTitle("Eat and meet");
//	assert(new_event.GetDescription() == "Food trucks");
//	new_event = service.GetEventByIndex(0);
//	assert(new_event.GetTitle() == "Eat and meet");
//	service.ModifyPeople("Eat and meet", 10);
//	new_event = Event("Book swap", "Schimb de carti", 2023, 11, 8, 16, 0, 40, "https://www.facebook.com/events/6372068299511170");
//	service.UpdateEvent(0, new_event);
//	service.AddInterestedList(new_event);
//	service.AddInterestedList(event);
//	vector<Event> interested = service.GetInterestedList();
//	assert(interested.size() == 2);
//	service.AddRepository(event);
//	InterestedList* eventsByMonth = service.FilterEventsByMonth(-1, "csv");
//	Event current_event = eventsByMonth->GetCurrentEvent();
//	assert(current_event.GetTitle() == "Eat and meet");
//	eventsByMonth->IncrementIndexOfCurrentEvent();
//	assert(eventsByMonth->GetSize() == 2);
//	eventsByMonth->IncrementIndexOfCurrentEvent();
//	eventsByMonth->DeleteCurrentEvent();
//	assert(eventsByMonth->GetSize() == 1);
//	assert(service.GetIndexOfEventInInterestedList("Book swap") == 0);
//	service.DeleteFromInterestedList(0);
//	service.DeleteEvent(0);
//	assert(service.GetEvents().size() == 0);
//	assert(service.GetIndexOfEventInInterestedList("CEva") == -1);
//}