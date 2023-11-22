#pragma once
#include "Repository.h"
#include "Service.h"
class FakeRepo : public Repository {
private:
	bool found;
public:
	FakeRepo(bool found);
	bool SearchForEventWithTheSameTitle(string title) override;
	vector<Event>& GetEvents() override;
};

