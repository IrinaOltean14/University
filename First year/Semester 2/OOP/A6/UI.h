#pragma once

#include "Service.h"

class UI {
private:
	Service service;
public:
	UI();
	~UI();

	void AdminMode();
	void PrintAdminMenu();
	void AddUI();
	bool IsInputNumber(string input);
	void PrintEvents();
	void DeleteEvent();
	void UpdateEvent();

	void UserMode();
	void PrintUserMenu();
	void CreateListWithEventsUser();
	void PrintInterestedList();
	void DeleteFromInterestedList();

	void start();
}; 
void TestAll();
