% a) Determine the position of the maximal element of a linear list. 
% Eg.: maxpos([10,14,12,13,14], L) produces L = [2,5].

% find_max(L - list, M - number)
% find_max(l1...ln) = [l1], if n = 1
%					  max(l1, find_max(l2...ln)), otherwise
% flow model: (i,o), (i, i)
find_max([E],E):-!.
find_max([H|T],H):-
    find_max(T,R1),
    R1 < H,
    !.
find_max([_|T],R):-
    find_max(T,R).

% max_positions(L - list, E - number, P - number, R - list)
% max_positions(l1...ln, e, p) = [], if n = 0
%							     p + max_positions(l2...ln, e, p+1), if l1 = e
%								 max_positions(l2...ln, e, p+1), otherwise
% flow model: (i, i, i, o), (i, i, i, i)

max_positions([],_,_,[]):-!.
max_positions([H|T], H, P, [P|R]):-
    !,
    P1 is P + 1,
    max_positions(T, H, P1, R).
max_positions([_|T], E, P, R):-
    P1 is P + 1,
    max_positions(T, E, P1, R).

determine_pos(L, R):-
    find_max(L,M),
    max_positions(L,M,1,R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers, replace every sublist with the 
% position of the maximum element from that sublist.
% [1, [2, 3], [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
% [1, [2], [1, 3], 3, 6, [2], 5, [1, 2, 3], 7

% max_sublist(L - list, R - list)
% max_sublist(l1...ln) = [], if n = 0
%						 determine_pos(l1) + max_sublist(l2...ln), if is_list(l1)
%						 l1 + max_sublist(l2...ln), otherwise
% flow model: (i, o)

max_sublist([],[]).
max_sublist([H|T], [P|R]):-
    is_list(H),
    !,
    determine_pos(H, P),
    max_sublist(T,R).
max_sublist([H|T], [H|R]):-
    max_sublist(T,R).