#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
	//TODO - Implementation
	int node = map.root;
	if (node != -1) {
		while (!stack.empty())
			stack.pop();
		while (node != -1) {
			stack.push(node);
			node = map.left[node];
			
		}
		if (!stack.empty())
			currentNode = stack.top();
		else
			currentNode = -1;
	}
	else
		currentNode = -1;
}
// WC: Theta(n) - for a higlhly inbalanced tree
// Total: O(log n)

void SMMIterator::first(){
	//TODO - Implementation
	int node = map.root;
	if (node != -1) {
		while (!stack.empty())
			stack.pop();
		while (node != -1) {
			stack.push(node);
			node = map.left[node];
		}
		if (!stack.empty())
			currentNode = stack.top();
		else
			currentNode = -1;
	}
	else
		currentNode = -1;
}
// WC: Theta(n) - for a highly inbalanced tree
// Total: O(log n)

void SMMIterator::next(){
	//TODO - Implementation
	if (!stack.empty()) {
		int node = stack.top();
		stack.pop();
		if (map.right[node] != -1) {
			node = map.right[node];
			while (node != -1) {
				stack.push(node);
				//cout << node << endl;
				node = map.left[node];
			}
		}
		if (!stack.empty())
			currentNode = stack.top();
		else
			currentNode = -1;
	}
	else
		throw exception();
}
// BC: Theta(1) - the stack is empty or the node does not have any right children
// WC: Theta(n) - for a highly inbalanced tree
// Total: O(log n)

bool SMMIterator::valid() const{
	//TODO - Implementation
	return currentNode != -1;
}
// Theta(1)

TElem SMMIterator::getCurrent() const{
	//TODO - Implementation
	if (valid())
		return map.nodes[currentNode];
	else 
		throw exception();
}
// Theta(1)


