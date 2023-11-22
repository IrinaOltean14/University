#pragma once
#include "Exceptions.h"
#include "InterestedCSV.h"
#include "Domain.h"
#include <vector>
#include <algorithm>
using namespace std;
class Repository {
public :
	vector<Event> events;
	string filename;

	void ReadFromFile();
	void WriteToFile();
public:
	Repository() = default;
	explicit Repository(string filemame);
	~Repository();

	virtual bool SearchForEventWithTheSameTitle(string title);
	int AddEvent(const Event& event);
	void DeleteEvent(int position);
	void UpdateEvent(int position, const Event& event);
	Event& GetEventByIndex(int position);
	Event& GetEventByTitle(string title);

	//Event& operator[](int position);
	virtual vector<Event>& GetEvents();
	//int GetSize();

};
