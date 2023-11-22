#include "Repository.h"


Repository::Repository() {
	
}

Repository::~Repository() {

}

DynamicArray<Event> Repository::GetAll() {
	return this->dynamicArray;
}

void Repository::AddRepo(const Event& event) {
	this->dynamicArray.AddElem(event);
}

Event* Repository::GetElementsRepo() {
	return this->dynamicArray.GetElements();
}

int Repository::GetSizeRepo() {
	return this->dynamicArray.GetSize();
}

void Repository::SortEventsChronologically() {
	int numberOfEvents = this->GetSizeRepo();
	for (int index1=0;index1<numberOfEvents;index1++)
		for (int index2 = index1 + 1; index2 < numberOfEvents; index2++) {
			Date date1 = this->GetElementsRepo()[index1].GetDate();
			Date date2 = this->GetElementsRepo()[index2].GetDate();
			if (date1.year > date2.year || (date1.year == date2.year && date1.month > date2.month) || (date1.year == date2.year && date1.month == date2.month && date1.day > date2.day) || (date1.year == date2.year && date1.month == date2.month && date1.day == date2.day && date1.hour > date2.hour) || (date1.year == date2.year && date1.month == date2.month && date1.day == date2.day && date1.hour == date2.hour && date1.minute > date2.minute)) {
				this->dynamicArray.Switch(index1, index2);
			}
		}

}

void Repository::UpdateEventRepo(int index, Event newEvent) {
	this->dynamicArray.UpdateElem(index, newEvent);
}

void Repository::DeleteEventRepo(int index) {
	this->dynamicArray.DeleteElem(index);
}

void Repository::GetAllEvents(Event allEvents[]) {
	for (int index = 0; index < this->GetSizeRepo(); index++)
		allEvents[index] = this->GetElementsRepo()[index];
}

void TestRepo() {
	Repository repository;
	assert(repository.GetSizeRepo() == 0);
	Event event;
	event = Event("Concert Bosquito", "Muzica de petrecere", 2023, 3, 31, 20, 0, 100, "https://www.facebook.com/events/244327624594653");
	repository.AddRepo(event);
	assert(repository.GetSizeRepo() == 1);
	assert(repository.GetElementsRepo()[0].GetTitle() == "Concert Bosquito");
	Event new_event;
	new_event = Event("Concert Bosquito", "Form Space", 2023, 3, 31, 20, 0, 100, "https://www.facebook.com/events/244327624594653");
	repository.UpdateEventRepo(0, new_event);
	assert(repository.GetElementsRepo()[0].GetDescription() == "Form Space");
	repository.DeleteEventRepo(0);
	assert(repository.GetSizeRepo() == 0);

}

void TestDynamicArray() {
	DynamicArray<int> dynamicArray;
	assert(dynamicArray.GetCapacity() == 1);
	dynamicArray.AddElem(2);
	dynamicArray.AddElem(3);
	dynamicArray.AddElem(4);
	dynamicArray.AddElem(5);
	assert(dynamicArray.GetSize() == 4);
	dynamicArray.DeleteElem(0);
	assert(dynamicArray.GetSize() == 3);
	dynamicArray.UpdateElem(0, 10);
	assert(dynamicArray.GetElements()[0] == 10);
}