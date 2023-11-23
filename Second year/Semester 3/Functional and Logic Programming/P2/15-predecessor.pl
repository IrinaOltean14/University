% a) Define a predicate to determine the predecessor of a number represented as digits in a list. 
% eg: [1 9 3 6 0 0] => [1 9 3 5 9 9]

% addLast(L - list, E - element, R - list)
% addLast(l1...ln) = [e], if n = 0
%					 l1 + addLast(l2...ln, e), otherwise
% flow model: (i,i,o), (i,i,i)

addLast([],E,[E]).
addLast([H|T],E,[H|R]):-
    addLast(T,E,R).

% reverse(L - list, R - list)
% reverse(l1...ln) = [], if n = 0
% 					 addLast(reverse(l2...ln), l1), otherwise

reverse([],[]).
reverse([H|T], R):-
    reverse(T,R1),
    addLast(R1,H,R).

% predecessor(L - list, C - number, R - list)
% predecessor(l1...ln, c) = [l1-c], if n = 1
%							[9] + predecessor(l2..ln, 1), if l1 = 0 and c = 1
%							[l1-c] + predecessor(l2...ln, 0), otherwise
predecessor([1],1,[]):-!.
predecessor([A],C,[R]):-
    !,
    R is A - C.
predecessor([0|T],1,[9|R]):-
    !,
    predecessor(T,1,R).
predecessor([H|T],C,[P|R]):-
    P is H - C,
    predecessor(T,0,R).

main(L, R):-
    reverse(L,L1),
    predecessor(L1,1,R1),
    reverse(R1,R).

% b)  For a heterogeneous list, formed from integer numbers and list of numbers, define a predicate to determine 
% the predecessor of the every sublist considered as numbers.
% Eg.: [1, [2, 3], 4, 5, [6, 7, 9], 10, 11, [1, 2, 0], 6] =>
% [1, [2, 2], 4, 5, [6, 7, 8], 10, 11, [1, 1, 9] 6]

% pred_sub(L - list, R - list)
% pred_sub(l1..ln) = [], if n = 0
%					 predecessor(l1) + pred_sub(l2...ln), if is_list(l1)
%					 l1 + pred_sub(l2...ln), otherwise

pred_sub([],[]).
pred_sub([H|T], [P|R]):-
    is_list(H),
    !,
    main(H,P),
    pred_sub(T,R).
pred_sub([H|T], [H|R]):-
    pred_sub(T,R).
