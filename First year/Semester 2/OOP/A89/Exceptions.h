#pragma once
#include <exception>
#include <string>
using namespace std;

class RepositoryException : public exception {
protected:
	string message;
public:
	RepositoryException();
	explicit RepositoryException(string message);
	~RepositoryException() override = default;
	virtual const char* what();
};

class DuplicateEventException : public RepositoryException {
public:
	const char* what() override;
};

class FileException : public std::exception {
protected:
	string message;
public:
	explicit FileException(string message);
	virtual const char* what();
};

class NonexistentEvent : public RepositoryException {
public:
	const char* what() override;
};