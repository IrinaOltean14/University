#include "Exceptions.h"
#include <utility>

FileException::FileException(string message) :message(move(message)) {

}

const char* FileException::what() {
	return message.c_str();
}

RepositoryException::RepositoryException() :exception{} {

}

RepositoryException::RepositoryException(string message) :message(move(message)) {

}

const char* RepositoryException::what() {
	return this->message.c_str();
}

const char* DuplicateEventException::what() {
	return "There is another event with the same title!";
}

const char* NonexistentEvent::what() {
	return "Event does not exist";
}