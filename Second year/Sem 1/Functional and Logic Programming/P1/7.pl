% a) Write a predicate to compute the intersection of two sets

% member(L - list, E - element)
% member(l1...ln, e) = true, if l1 = e
%					   member(l2..ln,e), otherwise
% flow model: (i,i), (i,o)
member([E|_],E):-!.
member([_|T], E):-
    member(T,E).

% intersection(L1 - list, L2 - list, R - list)
% intersection(l1..ln, k1..km) = [], n = 0
%								 l1 + intersection(l2..ln,k1..km), if l1 in k1..km
%								 intersection(l2..ln, k1..km), otherwise
intersection([],_,[]).
intersection([H|T], L2, [H|R]):-
    member(L2,H),
    !,
    intersection(T,L2,R).
intersection([_|T],L2,R):-
    intersection(T,L2,R).

% b) Write a predicate to create a list (m, ..., n) of all integer numbers from the interval [m, n]

% interval(A - number, B - number, R - result list)
% interval(a, b) = [b], if a = b
%				   a + interval(a+1, b), otherwise

interval(A,A,[A]):-!.
interval(A,B,[A|R]):-
    A1 is A + 1,
    interval(A1,B,R).