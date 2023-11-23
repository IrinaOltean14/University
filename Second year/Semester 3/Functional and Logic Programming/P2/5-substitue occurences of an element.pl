% a) Substitute all occurrences of an element of a list with all the elements of another list. 
% Eg. subst([1,2,1,3,1,4],1,[10,11],X) produces X=[10,11,2,10,11,3,10,11,4].


% append(L1 - list, L2 - list)
% append(l1...ln, k1...km) = k1...km, if n = 0
%							 l1 + append(l2...ln,k1..km), otherwise
append([],L2,L2).
append([H|T],L,[H|R]):-
    append(T,L,R).

% subst(L - list, E, L2 - list, R - list)
% subst(l1..ln,e,k1..km) = [], if n = 0
%						   append(k1...km, subst(l2...ln,e,k1...km)), if l1 = e
%						   subst(l2..ln,e,k1...km), otherwise
subst([],_,_,[]).
subst([H|T],H,L,R):-
    !,
    subst(T,H,L,R1),
    append(L,R1,R).
subst([H|T],E,L,[H|R]):-
    subst(T,E,L,R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers, replace in every sublist all 
% occurrences of the first element from sublist it a new given list.
% Eg.: [1, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] si [11, 11] =>
% [1, [11, 11, 1, 11, 11], 3, 6, [11, 11, 10, 1, 3, 9], 5, [11 11 11 11 11 11], 7

getFirst([],0):-!.
getFirst([H|_],H).

% substitute_all(L - list, Re - list, R - list)
% substitute_all(l1...ln, k1...km) = [], if n = 0
%										subst(l1, l1', k1...km) + substitute_all(l2..ln,e,k1...km), if is_list(l1)
%										l1 + substitute_all(l2...ln,k1...km), otherwise

substitute_all([],_,[]).
substitute_all([H|T],L,[R1|R]):-
    is_list(H),
    !,
    getFirst(H,F),
    subst(H,F,L,R1),
    substitute_all(T,L,R).
substitute_all([H|T],L,[H|R]):-
    substitute_all(T,L,R).


