#include "FakeRepo.h"

FakeRepo::FakeRepo(bool found) : found{ found }{ 

}

bool FakeRepo::SearchForEventWithTheSameTitle(string title){
	return found;
}

vector<Event>& FakeRepo::GetEvents() {
	vector<Event> events;
	if (found == false)
		return events;
	else {
		events.push_back(Event("Title", "Description", 10, 10, 2020, 10, 10, 100, "link"));
		return events;
	}
}


