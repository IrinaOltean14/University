% a) Determine the successor of a number represented as digits in a list. 
% Eg.: [1 9 3 5 9 9] --> [1 9 3 6 0 0]

% addLast(L - list, E - element, R - list)
% addLast(l1...ln, e) = [e], if n = 0
%						l1 + addLast(l2...ln), otherwise
% flow model: (i, i, o), (i, i, i)

addLast([],E,[E]).
addLast([H|T],E,[H|R]):-
    addLast(T,E,R).

% reverse(L - list, R - list)
% reverse(l1...ln) = [], if n = 0
%					 addLast(reverse(l2...ln), l1), otherwise
% flow model: (i, i), (i, o)

reverse([],[]).
reverse([H|T], R):-
    reverse(T,R1),
    addLast(R1,H,R).

% successor(L - list, C - number, R - list)
% successor(l1...ln, c) = [], if n = 0 and c = 0
%						  [c], if n = 0 and c != 0
%						  [(l1+c)%10] + successor(l2...ln, (l1+c)/10), otherwise
% flow model: (i, i, o), (i, i, i)

successor([],0,[]):-!.
successor([],C,[C]).
successor([H|T], C, [P|R]):-
    A is H + C,
    NewC is A div 10,
    P is A mod 10,
    successor(T,NewC,R).


main(L, R):-
    reverse(L, R1),
    successor(R1, 1, R2),
    reverse(R2,R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers, determine the successor of a 
% sublist considered as a number.
% [1, [2, 3], 4, 5, [6, 7, 9], 10, 11, [1, 2, 0], 6] => 
% [1, [2, 4], 4, 5, [6, 8, 0], 10, 11, [1, 2, 1], 6]

% successor_sublist(L - list, R - list)
% successor_sublist(l1...ln) = [], if n = 0
%							   successor(l1) + successor_sublist(l2...ln), if is_list(l1)
%							   l1 + successor_sublist(l2...ln), otherwise

successor_sublist([], []).
successor_sublist([H|T], [P|R]):-
    is_list(H),
    !,
    main(H,P),
    successor_sublist(T,R).
successor_sublist([H|T], [H|R]):-
    successor_sublist(T,R).
