% a) Write a predicate to determine if a list has even numbers of elements without counting the elements from 
% the list.

% evenList(L - list)
% evenList(l1l2..ln) = true, if n = 0
%					   evenList(l3..ln), n >= 2
%					   false, otherwise
evenList([]).
evenList([_,_|T]):-
    evenList(T).

% b) Write a predicate to delete first occurrence of the minimum number from a list.

% find_min(L - list, R - number)
% find_min(l1..ln) = l1, if n = 1
%					 min(l1, find_min(l2..ln)), otherwise
% flow model: (i,i), (i,o)
find_min([E], E):-!.
find_min([H|T], H):-
    find_min(T, E),
    E > H,
    !.
find_min([_|T], E):-
    find_min(T,E).

% delete_elem(L - list, E - element, R - result)
% delete_elem(l1..ln, e) = l2..ln, if l1 = e
%						   l1 + delete_elem(l2..ln,e), otherwise
% flow model: (i,i,i), (i,i,o)
delete_elem([E|T],E,T):-!.
delete_elem([H|T],E,[H|R]):-
    delete_elem(T,E,R).

delete_first_min(L,R):-
    find_min(L,M),
    delete_elem(L,M,R).