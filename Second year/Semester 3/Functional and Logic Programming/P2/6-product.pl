% a) Determine the product of a number represented as digits in a list to a given digit. 
% Eg.: [1 9 3 5 9 9] * 2 => [3 8 7 1 9 8]

% addLast(L - list, E - element)
% addLast(l1...ln, e) = [e], if n = 0
%						l1 + addLast(l2...ln,e), otherwise
addLast([],E,[E]).
addLast([H|T],E,[H|R]):-
    addLast(T,E,R).

% reverse(L - list, R - list)
% reverse(l1...ln) = [], if n = 0
%					 addLast(reverse(l2...ln),l1), otherwise
reverse([],[]).
reverse([H|T], R):-
    reverse(T,R1),
    addLast(R1,H,R).

% product(L1 - list, N - number, C - number,R - list)
% product(l1..ln, m, c) = [], if n = 0 and c = 0
%						  [c], if n = 0 and c > 0
%						  [l1*n+c] + product(l2...ln,m,c), otherwise

product([],_,0,[]):-!.
product([],_,C,[C]).
product([H|T], N, C, [P|R]):-
    Pr is H*N,
    Prr is Pr+C,
    P is Prr mod 10,
    NewC is Prr div 10,
    product(T,N,NewC,R).


main(L1,N,R):-
    reverse(L1,A),
    product(A,N,0,R1),
    reverse(R1,R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers, write a predicate to replace 
% every sublist with the position of the maximum element from that sublist.
% [1, [2, 3], [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
% [1, [2], [1, 3], 3, 6, [2], 5, [1, 2, 3], 7


% find_max(L - list, M - number)
% find_max(l1...ln) = l1, if n = 1
%					 max(l1, find_max(l2...ln)), otherwise
find_max([X],X):-!.
find_max([H|T],R1):-
    find_max(T,R1),
    R1 > H,
    !.
find_max([H|_],H).

% max_pos(L - list, M - number, P - number, R - list)
% max_pos(l1...ln, m, p) = [], if n = 0
% 						   p + max_pos(l2...ln,m,p+1) if l1 = m
%						   max_pos(l2..ln, m , p+1), otherwise
max_pos([],_,_,[]).
max_pos([H|T],H,P,[P|R]):-
    !,
    P1 is P + 1,
    max_pos(T,H,P1,R).
max_pos([_|T],E,P,R):-
    P1 is P + 1,
    max_pos(T,E,P1,R).


% replace_sublist(L - list, R - list)
% replace_sublist(l1...ln) = [], if n = 0
% 							 max_pos(l1, find_max(l1), 0) + replace_sublist(l2..ln), if is_list(l1)
%							 replace_sublist(l2...ln), otherwise

replace_sublist([],[]).
replace_sublist([H|T],[S|R]):-
    is_list(H),
    !,
    find_max(H,M),
    max_pos(H,M,1,S),
    replace_sublist(T,R).
replace_sublist([H|T],[H|R]):-
    replace_sublist(T,R).

