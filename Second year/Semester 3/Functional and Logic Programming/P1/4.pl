% a) Write a predicate to determine the difference of two sets

% member(L - list, E - element)
% member(l1...ln, e) = true, if l1 = e
%					   member(l2..ln,e), otherwise
% flow model: (i,i), (i,o)
member([E|_],E):-!.
member([_|T], E):-
    member(T,E).

% difference(L1 - list, L2 - list, L3 - list)
% difference(l1..ln, k1..km) = [], if n = 0
%							   l1 + difference(l2..ln, k1..km), if l1 not in k1..km
%							   difference(l2..ln, k1..km), otherwise
% flow model: (i,i,o), (i,i,i)

difference([], _, []).
difference([H|T], L2, [H|R]):-
    not(member(L2, H)),
    !,
    difference(T,L2,R).
difference([_|T], L2, R):-
    difference(T, L2, R).

% b)  Write a predicate to add value 1 after every even element from a list.

% add1(L - list, R - list)
% add1(l1..ln) = [], if n = 0
%				 [l1, 1] + add1(l2..ln), if l1 % 2 == 0
%				 add1(l2..ln), otherwise

add1([], []).
add1([H|T], [H,1|R]):-
    H mod 2 =:= 0,
    !,
    add1(T, R).
add1([H|T], [H|R]):-
    add1(T, R).