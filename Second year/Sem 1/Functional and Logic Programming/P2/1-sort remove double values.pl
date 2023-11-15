% a) Sort a list with removing the double values. E.g.: [4 2 6 2 3 4] --> [2 3 4 6]

% nb_occurences(L - list, E - element,R)
% nb_occurences(l1..ln, e) = 0, if n = 0
%							 1 + nb_occurences(l2..ln,e)
%							 nb_occurences(l2...ln,e)
% flow model: (i,i,o), (i,i,i)

nb_occurences([],_,0).
nb_occurences([E|T],E,R):-
    !,
    nb_occurences(T,E,R1),
    R is R1 + 1.
nb_occurences([_|T],E,R):-
    nb_occurences(T,E,R).

% insert(L - list, E - element, R - list)
% insert(l1...ln, e) = e + l1...ln, if e < l1,
%					   insert(l2...ln,e), otherwise

insert([],E,[E]).
insert([H|T],E,[E,H|T]):-
    E < H,
    !.
insert([H|T],E,[H|R]):-
    insert(T,E,R).

% sort(L - list, Col - list, R - result)
% sort(l1...ln,c1..cm) = c1...cm, n = 0
%				  		 sort(l2...ln, insert(l1,c1..cm)), if nb_occ(l1,l2...ln) = 0
%						 sort(l2..ln, c1..cm), otherwise
% flow model: (i,o), (i,i)

sort([], Col, Col).
sort([H|T], Col, R):-
    nb_occurences(T, H,R1),
    R1 =:= 0,
    !,
    insert(Col, H, NewC),
    sort(T,NewC,R).
sort([_|T], Col,R):-
    sort(T, Col, R).

main_sort(L,R):-
    sort(L,[],R).
    
% b) For a heterogeneous list, formed from integer numbers and list of numbers, write a predicate to sort every 
% sublist with removing the doubles.
% Eg.: [1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
% [1, 2, [1, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1], 7].

% sort_sublist(l1...ln) = [], if n = 0
%						  l1 + sort_sublist(l2...ln), if number(l1)
%						  sort(l1) + sort_sublist(l2...ln), if is_list(l1)

sort_sublist([],[]).
sort_sublist([H|T], [R1|R]):-
    is_list(H),
    !,
    main_sort(H,R1),
    sort_sublist(T,R).
sort_sublist([H|T],[H|R]):-
    sort_sublist(T,R).