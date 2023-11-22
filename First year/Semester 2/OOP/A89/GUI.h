#pragma once
#include <QWidget>
#include "Service.h"
#include <QPushButton>
#include <qlistwidget.h>
class GUI : public QWidget {
private:
	Service& service;
	QPushButton* adminButton;
	QPushButton* userButton;
public:
	GUI(Service& service);
	~GUI();
	void initGUI();
	void showAdmin();
	void showUser();
	void connectSignalAndSlots();
};

class AdminGUI : public QWidget {
private:
	Service& service;
	QListWidget* eventsList;
	QLineEdit* titleEdit;
	QLineEdit* descriptionEdit;
	QLineEdit* peopleEdit;
	QLineEdit* linkEdit;
	QLineEdit* yearEdit;
	QLineEdit* monthEdit;
	QLineEdit* dayEdit;
	QLineEdit* hourEdit;
	QLineEdit* minuteEdit;
	QPushButton* addButton;
	QPushButton* removeButton;
	QPushButton* updateButton;
public:
	AdminGUI(Service& service);
	~AdminGUI();
	void initAdminGUI();
	void populate();
	void connectSignalAndSlotsAdmin();
	void addEvent();
	void deleteEvent();
	void updateEvent();
	void autofillEvent();
};

class UserGUI : public QWidget {
private:
	Service& service;
	QPushButton* seeFileButton;
	QListWidget* userEventList;
	QListWidget* interestedList;
	QLineEdit* titleEdit;
	QLineEdit* descriptionEdit;
	QLineEdit* peopleEdit;
	QPushButton* interestedButton;
	QPushButton* nextButton;
	QPushButton* filterButton;
	QPushButton* deleteButton;
	QLineEdit* filterEdit;
	InterestedList* eventsByMonth;
	Event currentEvent;
public:
	UserGUI(Service& service);
	~UserGUI();
	void initUserGUI();
	void connectSignalAndSlotsUser();
	void populate();
	void nextEvent();
	void addToInterested();
	void deleteFromInterested();
};