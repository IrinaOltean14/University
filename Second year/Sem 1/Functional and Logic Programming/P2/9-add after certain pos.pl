% a) For a list of integer number, write a predicate to add in list after 1-st, 3-rd, 7-th, 15-th element a given value 

% add_value(L - list, P - number, E - number, R - list)
% add_value(l1...ln, p, e) = [], if n = 0
%							 l1 + e + add_value(l2...ln, p+1, e), if p = 1 or p = 3 or p = 7 or p = 15
%							 l1 + add_value(l2...ln, p+1, e), otherwise
% flow model: (i, i, i, o), (i, i, i, i)'

add_value([],_,_,[]).
add_value([H|T],P,E,[H,E|R]):-
    (P =:= 1 ; P =:= 3 ; P =:= 7 ; P =:= 15),
    !,
    P1 is P + 1,
    add_value(T,P1,E,R).
add_value([H|T],P,E,[H|R]):-
    P1 is P + 1,
    add_value(T,P1,E,R).

main(L,E,R):-
    add_value(L,1,E,R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers; add in every sublist after 1-st, 
% 3-rd, 7-th, 15-th element the value found before the sublist in the heterogenous list. The list has the particularity 
% that starts with a number and there aren’t two consecutive elements lists.
% Eg.: [1, [2, 3], 7, [4, 1, 4], 3, 6, [7, 5, 1, 3, 9, 8, 2, 7], 5] =>
% [1, [2, 1, 3], 7, [4, 7, 1, 4, 7], 3, 6, [7, 6, 5, 1, 6, 3, 9, 8, 2, 6, 7], 5].


% sub(L - list, R - list)
% sub(l1...ln) = [], if n = 0
%				 l1 + main(l2, l1) + sub(l3...ln), if is_list(l2)
%				 l1 + sub(l2..ln), otherwise
sub([],[]).
sub([A,B|T],[A,P|R]):-
    is_list(B),
    !,
    main(B,A,P),
    sub(T,R).
sub([H|T], [H|R]):-
    sub(T,R).

