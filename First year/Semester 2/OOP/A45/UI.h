#pragma once
#include "AdministratorService.h"
#include "UserService.h"

class UI {
private:
	AdminService adminService;
	UserService userService;
public:
	UI();
	~UI();
	void start();
	int askForMode();
	void AdminMode();
	void UserMode();
	void PrintUserMenu();
	void CreateListWithEventsUser();
	void PrintInterestedListUser();
	void DeleteEventFromInterested();
	void PrintAdminMenu();
	void PrintEventsUI();
	void DeleteUI();
	void AddUI();
	void UpdateUI();
	bool IsOkInput(string input);
};

void TestAll();
