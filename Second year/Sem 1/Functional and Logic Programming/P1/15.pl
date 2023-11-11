% a) Write a predicate to transform a list in a set, considering the first occurrence. 
% Eg: [1,2,3,1,2] is transform in [1,2,3]

% member(L - list, E - element)
% member(l1..ln,e) = false, if n = 0
% 					 true, if l1 = e
%					 member(l2...ln), otherwise
% flow model: (i,i)
member([H|_],H):-!.
member([_|T],E):-
    member(T,E).


% addLast(L - list, E - element, R - list)
% addLast(l1...ln, e) = [e], if n = 0
%					    l1 + addLast(l2...ln,e), otherwise
% flow model: (i,i,o), (i,i,i)

addLast([],E,[E]).
addLast([H|T],E,[H|R]):-
    addLast(T,E,R).

% transform(L - list, Col - list, R - list)
% transform(l1...ln, c1...cm) = c1...cm, if n = 0
%								transform(l2...ln, addLast(c1..cm,l1)), if l1 not in c1...cm
%								transform(l2...lm, c1..cm), otherwise
% flow model: (i,i,o), (i,i,i)
transform([], Col, Col).
transform([H|T], Col, R):-
    not(member(Col,H)),
    !,
    addLast(Col,H,NewC),
    transform(T,NewC,R).
transform([_|T], Col, R):-
    transform(T,Col,R).

main_transform(L,R):-
    transform(L,[],R).


% b) Write a predicate to decompose a list in a list respecting the following: [list of even numbers list of odd 
% numbers] and also return the number of even numbers and the numbers of odd numbers

% even(L - list, R - list)
% even(l1...ln) = [], if n = 0
%				  l1 + even(l2...ln), if l1 is even
%				  even(l2...ln), otherwise
% flow model: (i,o), (i,i)

even([],[]).
even([H|T], [H|R]):-
    H mod 2 =:= 0,
    !,
    even(T,R).
even([_|T],R):-
    even(T,R).

% odd(L - list, R - list)
% odd(l1...ln) = [], if n = 0
%				  l1 + odd(l2...ln), if l1 is odd
%				  odd(l2...ln), otherwise
% flow model: (i,o), (i,i)

odd([],[]).
odd([H|T], [H|R]):-
    H mod 2 =:= 1,
    !,
    odd(T,R).
odd([_|T],R):-
    odd(T,R).

% lengthS(L - list, R - nb)
% lengthS(l1...ln) = 0, if n = 0
%					1 + lengthS(l2...ln), otherwise
% flow model: (i,o), (i,i)
lengthS([],0).
lengthS([_|T],R):-
    lengthS(T,R1),
    R is R1 + 1.

% append(L1 - list, L2 - list, R - list)
% append(l1..ln, k1..km) = k1..km, if n = 0
%						   l1 + append(l2..ln, k1..km), otherwise
append([],L2,L2).
append([H|T],L2,[H|R]):-
    append(T,L2,R).


decompose(L,R,L1,L2):-
    even(L,E),
    odd(L,O),
    append(E,O,R),
    lengthS(E,L1),
    lengthS(O,L2).