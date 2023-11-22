#pragma once
#include "Domain.h"
#include <exception>
#include <vector>

class Validator {
public:
	Validator();
	~Validator();
	static void validate_event(const Event& event);

};

class EventException : public exception {
private:
	vector<string> errors;
public:
	explicit EventException(vector<string> errors);
	vector<string> getErrors() const;
};