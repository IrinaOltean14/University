#include "GUI.h"
#include <QVBoxLayout>
#include <qlabel.h>
#include <QLineEdit>
#include <QFormLayout>
#include <QDebug>
#include <fstream>
GUI::GUI(Service& service) : service{ service } {
	initGUI();
	connectSignalAndSlots();
}

GUI::~GUI() {
	
}

void GUI::connectSignalAndSlots() {
	QObject::connect(adminButton, &QPushButton::clicked, this, &GUI::showAdmin);
	QObject::connect(userButton, &QPushButton::clicked, this, &GUI::showUser);
}

void GUI::showUser() {
	auto user = new UserGUI{ this->service };
	user->show();
}

void GUI::showAdmin() {
	auto admin = new AdminGUI{ this->service };
	admin->show();
}


void GUI::initGUI() {
	auto verticalLayout = new QVBoxLayout();
	setLayout(verticalLayout);
	verticalLayout->setAlignment(Qt::AlignHCenter);
	auto title = new QLabel{ "Welcome to events app" };
	auto mode = new QLabel{ "Please select your mode:" };
	verticalLayout->addWidget(title);
	verticalLayout->addWidget(mode);
	auto horizontalLayout = new QHBoxLayout{};
	verticalLayout->addLayout(horizontalLayout);
	adminButton = new QPushButton{ "ADMIN" };
	userButton = new QPushButton{ "USER" };
	horizontalLayout->addWidget(adminButton);
	horizontalLayout->addWidget(userButton);
}

AdminGUI::AdminGUI(Service& service) : service{ service } {
	initAdminGUI();
	connectSignalAndSlotsAdmin();
	populate();
}

void AdminGUI::initAdminGUI() {
	auto mainLayout = new QVBoxLayout();
	setLayout(mainLayout);
	mainLayout->setAlignment(Qt::AlignHCenter);
	auto title = new QLabel{ "Administrator mode" };
	mainLayout->addWidget(title);
	
	// put list
	auto horizontalLayout = new QHBoxLayout();
	mainLayout->addLayout(horizontalLayout);
	eventsList = new QListWidget{};
	horizontalLayout->addWidget(eventsList);

	//
	auto dataLayout = new QVBoxLayout();
	horizontalLayout->addLayout(dataLayout);
	auto infoLayout = new QFormLayout();
	//horizontalLayout->addLayout(dataLayout);
	dataLayout->addLayout(infoLayout);

	auto titleLabel = new QLabel{ "Title:" };
	titleEdit = new QLineEdit{};
	titleLabel->setBuddy(titleEdit);
	infoLayout->addRow(titleLabel, titleEdit);

	auto descriptionLabel = new QLabel{ "Description: " };
	descriptionEdit = new QLineEdit{};
	descriptionLabel->setBuddy(descriptionEdit);
	infoLayout->addRow(descriptionLabel, descriptionEdit);

	auto peopleLabel = new QLabel{ "People: " };
	peopleEdit = new QLineEdit{};
	peopleLabel->setBuddy(peopleEdit);
	infoLayout->addRow(peopleLabel, peopleEdit);

	auto linkLabel = new QLabel{ "Link: " };
	linkEdit = new QLineEdit{};
	linkLabel->setBuddy(linkEdit);
	infoLayout->addRow(linkLabel, linkEdit);

	auto yearLabel = new QLabel{ "Year:" };
	yearEdit = new QLineEdit{};
	yearLabel->setBuddy(yearEdit);
	infoLayout->addRow(yearLabel, yearEdit);

	auto monthLabel = new QLabel{ "Month:" };
	monthEdit = new QLineEdit{};
	monthLabel->setBuddy(monthEdit);
	infoLayout->addRow(monthLabel, monthEdit);

	auto hourLabel = new QLabel{ "Hour:" };
	hourEdit = new QLineEdit{};
	hourLabel->setBuddy(hourEdit);
	infoLayout->addRow(hourLabel, hourEdit);

	auto minuteLabel = new QLabel{ "Minute:" };
	minuteEdit = new QLineEdit{};
	minuteLabel->setBuddy(minuteEdit);
	infoLayout->addRow(minuteLabel, minuteEdit);

	auto dayLabel = new QLabel{ "Day:" };
	dayEdit = new QLineEdit{};
	dayLabel->setBuddy(dayEdit);
	infoLayout->addRow(dayLabel, dayEdit);

	auto buttonsLayout = new QHBoxLayout();
	dataLayout->addLayout(buttonsLayout);
	addButton = new QPushButton{ "ADD" };
	buttonsLayout->addWidget(addButton);

	removeButton = new QPushButton{ "REMOVE" };
	buttonsLayout->addWidget(removeButton);

	updateButton = new QPushButton{ "UPDATE" };
	buttonsLayout->addWidget(updateButton);
	
}

AdminGUI::~AdminGUI() {

}

void AdminGUI::populate() {
	eventsList->clear();
	for (auto event : this->service.GetEvents())
		eventsList->addItem(QString::fromStdString(event.toString()));
}

void AdminGUI::connectSignalAndSlotsAdmin() {
	QObject::connect(addButton, &QPushButton::clicked, this, &AdminGUI::addEvent);
	QObject::connect(removeButton, &QPushButton::clicked, this, &AdminGUI::deleteEvent);
	QObject::connect(updateButton, &QPushButton::clicked, this, &AdminGUI::updateEvent);
	QObject::connect(eventsList, &QListWidget::itemSelectionChanged, this, &AdminGUI::autofillEvent);
}

void AdminGUI::autofillEvent() {
	int index = eventsList->currentRow();
	titleEdit->setText(QString::fromStdString(this->service.GetEventByIndex(index).GetTitle()));
	descriptionEdit->setText(QString::fromStdString(this->service.GetEventByIndex(index).GetDescription()));
	linkEdit->setText(QString::fromStdString(this->service.GetEventByIndex(index).GetLink()));
	peopleEdit->setText(QString::fromStdString(to_string(this->service.GetEventByIndex(index).GetPeople())));
	yearEdit->setText(QString::fromStdString(to_string(this->service.GetEventByIndex(index).GetDate().year)));
	monthEdit->setText(QString::fromStdString(to_string(this->service.GetEventByIndex(index).GetMonth())));
	dayEdit->setText(QString::fromStdString(to_string(this->service.GetEventByIndex(index).GetDate().day)));
	hourEdit->setText(QString::fromStdString(to_string(this->service.GetEventByIndex(index).GetDate().hour)));
	minuteEdit->setText(QString::fromStdString(to_string(this->service.GetEventByIndex(index).GetDate().minute)));
}

void AdminGUI::addEvent() {
	string title = titleEdit->text().toStdString();
	string description = descriptionEdit->text().toStdString();
	string link = linkEdit->text().toStdString();
	int people = peopleEdit->text().toInt();
	int year = yearEdit->text().toInt();
	int month = monthEdit->text().toInt();
	int day = dayEdit->text().toInt();
	int hour = hourEdit->text().toInt();
	int minute = minuteEdit->text().toInt();
	/*ofstream file("Events1.txt");
	if (file.is_open()) {
		file << year << " ";
		file.close();
	}*/
	Event event = Event(title, description, year, month, day, hour, minute, people, link);
	//this->service.AddRepository(event);
	try {
		this->service.AddRepository(event);
	}
	catch (DuplicateEventException& exception) {
		
	}
	catch (FileException& exception) {
		
	}
	catch (EventException& exception) {
		
	}
	populate();
}

void AdminGUI::deleteEvent() {
	string title;
	title = titleEdit->text().toStdString();
	try {
		int index = this->service.GetIndexOfEvent(title);
		this->service.DeleteEvent(index);
	}
	catch (NonexistentEvent& exception) {
		cout << exception.what() << endl;
	}
	populate();
}

void AdminGUI::updateEvent() {
	string title = titleEdit->text().toStdString();
	string description = descriptionEdit->text().toStdString();
	string link = linkEdit->text().toStdString();
	int people = peopleEdit->text().toInt();
	int year = yearEdit->text().toInt();
	int month = monthEdit->text().toInt();
	int day = dayEdit->text().toInt();
	int hour = hourEdit->text().toInt();
	int minute = minuteEdit->text().toInt();
	Event event = Event(title, description, year, month, day, hour, minute, people, link);
	try {
		int index = this->service.GetIndexOfEvent(title);
		this->service.UpdateEvent(index, event);
	}
	catch (NonexistentEvent& exception) {
	}
	populate();
}

UserGUI::UserGUI(Service& service) : service{ service } {
	initUserGUI();
	connectSignalAndSlotsUser();
}

UserGUI::~UserGUI() {
	initUserGUI();
}

void UserGUI::initUserGUI() {
	auto mainLayout = new QVBoxLayout{};
	setLayout(mainLayout);
	auto typeLayout = new QHBoxLayout{};
	mainLayout->addLayout(typeLayout);
	auto typeFormLayout = new QFormLayout{};
	typeLayout->addLayout(typeFormLayout);
	auto typeFileLabel = new QLabel{ "Type of file you want:" };
	auto typeFileEdit = new QLineEdit{};
	typeFileLabel->setBuddy(typeFileEdit);
	typeFormLayout->addRow(typeFileLabel, typeFileEdit);
	seeFileButton = new QPushButton{ "See file" };
	typeLayout->addWidget(seeFileButton);
	auto mainListLayout = new QHBoxLayout{};
	mainLayout->addLayout(mainListLayout);
	auto eventListLayout = new QVBoxLayout{};
	mainListLayout->addLayout(eventListLayout);
	auto interestedListLayout = new QVBoxLayout{};
	userEventList = new QListWidget{};
	interestedList = new QListWidget{};
	auto eventListLabel = new QLabel{ "Events list: " };
	auto interestedListLabel = new QLabel{ "Interested list: " };
	eventListLayout->addWidget(eventListLabel);
	eventListLayout->addWidget(userEventList);
	interestedListLayout->addWidget(interestedListLabel);
	interestedListLayout->addWidget(interestedList);

	auto eventDataInfo = new QFormLayout{};
	mainListLayout->addLayout(eventDataInfo);
	mainListLayout->addLayout(interestedListLayout);

	auto titleLabel = new QLabel{ "Title:" };
	titleEdit = new QLineEdit{};
	titleLabel->setBuddy(titleEdit);
	
	auto descriptionLabel = new QLabel{ "Description: " };
	descriptionEdit = new QLineEdit{};
	descriptionLabel->setBuddy(descriptionEdit);

	auto peopleLabel = new QLabel{ "People: " };
	peopleEdit = new QLineEdit{};
	peopleLabel->setBuddy(peopleEdit);
	
	eventDataInfo->addRow(titleLabel, titleEdit);
	eventDataInfo->addRow(descriptionLabel, descriptionEdit);
	eventDataInfo->addRow(peopleLabel, peopleEdit);

	auto buttonLayout = new QHBoxLayout{};
	mainLayout->addLayout(buttonLayout);
	interestedButton = new QPushButton{ "Add to interested" };
	nextButton = new QPushButton{ "Next" };
	filterButton = new QPushButton{ "Filter" };
	deleteButton = new QPushButton{ "Delete" };
	buttonLayout->addWidget(interestedButton);
	buttonLayout->addWidget(nextButton);
	buttonLayout->addWidget(filterButton);
	buttonLayout->addWidget(deleteButton);

	auto filterLabel = new QLabel{ "Enter a month:" };
	filterEdit = new QLineEdit{};
	filterLabel->setBuddy(filterEdit);

	auto filterLayout = new QFormLayout{};
	filterLayout->addRow(filterLabel, filterEdit);
	mainLayout->addLayout(filterLayout);
}

void UserGUI::connectSignalAndSlotsUser() {
	QObject::connect(filterButton, &QPushButton::clicked, this, &UserGUI::populate);
	QObject::connect(nextButton, &QPushButton::clicked, this, &UserGUI::nextEvent);
	QObject::connect(interestedButton, &QPushButton::clicked, this, &UserGUI::addToInterested);
	QObject::connect(deleteButton, &QPushButton::clicked, this, &UserGUI::deleteFromInterested);
}

void UserGUI::deleteFromInterested() {
	int index = interestedList->currentRow();
	vector<Event> events = this->service.GetInterestedList(); 
	Event eventD = events[index];
	this->service.DeleteFromInterestedList(index);
	events = this->service.GetInterestedList();
	interestedList->clear();
	for (auto event : events)
		interestedList->addItem(QString::fromStdString(event.toString()));
	eventsByMonth->AddEvent(eventD);
	userEventList->clear();
	for (auto event : eventsByMonth->getEvents())
		userEventList->addItem(QString::fromStdString(event.toString()));
}

void UserGUI::addToInterested() {
	//interestedList->addItem(QString::fromStdString(currentEvent.toString()));
	Event& event1 = this->service.GetEventByTitle(currentEvent.GetTitle());
	event1.ModifyNumberOfPeople(1);
	eventsByMonth->DeleteByTitle(currentEvent.GetTitle());
	userEventList->clear();
	for (auto event : eventsByMonth->getEvents())
		userEventList->addItem(QString::fromStdString(event.toString()));
	this->service.AddInterestedList(event1);
	vector<Event> events = this->service.GetInterestedList();
	interestedList->clear();
	for (auto event : events)
		interestedList->addItem(QString::fromStdString(event.toString()));
}

void UserGUI::nextEvent() {
	Event event = eventsByMonth->GetCurrentEvent();
	titleEdit->setText(QString::fromStdString(event.GetTitle()));
	descriptionEdit->setText(QString::fromStdString(event.GetDescription()));
	peopleEdit->setText(QString::fromStdString(to_string(event.GetPeople())));
	currentEvent = event;
	eventsByMonth->IncrementIndexOfCurrentEvent();

}

void UserGUI::populate() {
	userEventList->clear();
	int month = filterEdit->text().toInt();
	eventsByMonth = this->service.FilterEventsByMonth(month, this->service.getType());
	if (eventsByMonth->GetSize() == 0)
		cout << "No events with the given month" << endl;
	else {
		bool next = true;
		while (next) {
			if (eventsByMonth->GetSize() == 0) {
				cout << "No events with the given month" << endl;
				break;
			}
			Event event = eventsByMonth->GetCurrentEvent();
			userEventList->addItem(QString::fromStdString(event.toString()));
			eventsByMonth->IncrementIndexOfCurrentEvent();
			if (eventsByMonth->GetIndex() == 0)
				break;
		}
	}
}