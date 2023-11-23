% a) Sort a list with keeping double values in resulted list. E.g.: [4 2 6 2 3 4] --> [2 2 3 4 4 6]

% insert(L - list, E - element, R - list)
% insert(l1...ln, e) = [e], if n = 0
% 					   e + l1...ln, if e <= l1
%					   insert(l2...ln,e), otherwise
% flow model(i,i,o), (i,i,i)

insert([],E,[E]).
insert([H|T], E, [E,H|T]):-
    E =< H,
    !.
insert([H|T], E, [H|R]):-
    insert(T,E,R).

% sort(L - list, Col - list, R - result)
% sort(l1..ln, c1..cm) = c1...cm, if n = 0
%						 sort(l2...ln, insert(c1...cm, l1)), otherwise
% flow model: (i,i,o), (i,i,i)
sort([],Col,Col).
sort([H|T], Col, R):-
    insert(Col,H,NewC),
    sort(T,NewC,R).

main_sort(L,R):-
    sort(L,[],R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers, write a predicate to sort every 
% sublist, keeping the doubles.
% Eg.: [1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
% [1, 2, [1, 4, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1, 1, 1], 7].

% sort_sublist(L - list, R - list)
% sort_sublist(l1...ln) = [], if n = 0
%						  main_sort(l1) + sort_sublist(l2...ln), if is_list(l1)
%						  l1 + sort_sublist(l2...ln), otherwise
% flow model: (i,o), (i,i)

sort_sublist([], []).
sort_sublist([H|T], [R1|R]):-
    is_list(H),
    !,
    main_sort(H,R1),
    sort_sublist(T,R).
sort_sublist([H|T], [H|R]):-
    sort_sublist(T,R).