#include "Validator.h"
#include <fstream>
Validator::Validator() = default;

Validator::~Validator() = default;

void Validator::validate_event(const Event& event) {
	vector<string> errors;
	Date date = event.GetDate();
	ofstream file("Events1.txt");
	if (date.year < 1900 || date.year>2100)
		errors.emplace_back("Invalid year\n");
	if (date.month < 0 || date.month>12)
		errors.emplace_back("Invalid month\n");
	if (date.day < 0 || date.day>31)
		errors.emplace_back("Invalid day\n");
	if (event.GetPeople() < 0)
		errors.emplace_back("There can not be a negative number of people\n");

	if (!errors.empty())
		throw EventException(errors);
}

EventException::EventException(vector<string> errors) {
	this->errors = errors;
}

vector<string> EventException::getErrors() const {
	return this->errors;
}