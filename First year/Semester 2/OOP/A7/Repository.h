#pragma once
#include "Exceptions.h"
#include "InterestedCSV.h"
#include "Domain.h"
#include <vector>
#include <algorithm>
using namespace std;
class Repository {
private:
	vector<Event> events;
	string filename;

	void ReadFromFile();
	void WriteToFile();
public:
	Repository()=default;
	explicit Repository(string filemame);
	~Repository();

	bool SearchForEventWithTheSameTitle(string title);
	void AddEvent(const Event& event);
	void DeleteEvent(int position);
	void UpdateEvent(int position, const Event& event);
	Event& GetEventByIndex(int position);
	Event& GetEventByTitle(string title);

	//Event& operator[](int position);
	vector<Event>& GetEvents();
	//int GetSize();

};