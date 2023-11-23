% a) Write a predicate to test equality of two sets without using the set difference.

% member(L - list, E - element)
% member(l1..ln,e) = false, if n = 0
% 					 true, if l1 = e
%					 member(l2...ln), otherwise
% flow model: (i,i)
member([H|_],H):-!.
member([_|T],E):-
    member(T,E).

% lengthS(L - list, R - nb)
% lengthS(l1...ln) = 0, if n = 0
%					1 + lengthS(l2...ln), otherwise
% flow model: (i,o), (i,i)
lengthS([],0).
lengthS([_|T],R):-
    lengthS(T,R1),
    R is R1 + 1.

% equality(L1 - set, L2 - set)
% equality(l1...ln, k1...km) = true, if n = 0
%							   equality(l2...ln,k1..km), if l1 in k1...km
%							   false, otherwise
% flow model: (i,i)
equality([],_):-!.
equality([H|T],L2):-
    member(L2,H),
    equality(T,L2).


main_equality(L1,L2):-
    lengthS(L1,R1),
    lengthS(L2,R2),
    R1 =:= R2,
    equality(L1,L2).

% b) Write a predicate to select the n-th element of a given list

% select(L - list, P - number, R - number)
% select(l1...ln, p) = l1, if p = 1
%					   select(l2...ln, p-1), otherwise

select([H|_],1,H):-!.
select([_|T],P,R):-
    P1 is P-1,
    select(T,P1,R).