% a) Define a predicate to determine the longest sequences of consecutive even numbers (if exist more maximal 
% sequences one of them)

% len(L - list, R - number)
% len(l1...ln) = 0, if n = 0
%				 1 + len(l2...ln), otherwise

len([],0).
len([_|T], R):-
    len(T,R1),
    R is R1 + 1.


% append(L:list, E:number, R:list)
% (i,i,o)

append([],E,[E]).
append([H|T],E,[H|R]):-
    append(T,E,R).

% subsq(L - list, Aux - list, C - list, R - list)
% subsq(l1...ln, a1...am, r1...rp) = a1...am, if n = 0 and len(a1...am) > len(r1...rp)
%									 r1...rp, if n = 0 and len(r1...rp) > len(a1...am)
%									 subsq(l2...ln, append(a1...am, l1), r1..rp) if even(l1)
%									 subsq(l2...ln, [], a1...am), if len(a1...am) > len(r1..rp) and not even(l1)
%									 subsq(l2...ln, [], r1...rp), otherwise
subsq([], A, C, A):-
    len(A,La),
    len(C, Lc),
    La > Lc,
    !.
subsq([],_,C,C).
subsq([H|T], A, C, R):-
    H mod 2 =:= 0,
    !,
    append(A,H,NewA),
    subsq(T,NewA,C,R).
subsq([_|T],A,C,R):-
    len(A,La),
    len(C, Lc),
    La > Lc,
    !,
    subsq(T,[],A,R).
subsq([_|T],_,C,R):-
    subsq(T,[],C,R).

main(L,R):-
    subsq(L,[],[],R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers, define a predicate to replace 
% every sublist with the longest sequences of even numbers from that sublist.
% Eg.: [1, [2, 1, 4, 6, 7], 5, [1, 2, 3, 4], 2, [1, 4, 6, 8, 3], 2, [1, 5], 3] =>
% [1, [4, 6], 5, [2], 2, [4, 6, 8], 2, [], 3]

% sub_even(L - list, R - list)
% sub_even(l1...ln) = [], if n = 0
%					  main(l1) + sub_even(l2...ln), if is_list(l1)
%					  l1 + sub_even(l2...ln), otherwise
% flow model: (i,i), (i,o)

sub_even([],[]).
sub_even([H|T], [P|R]):-
    is_list(H),
    !,
    main(H,P),
    sub_even(T,R).
sub_even([H|T], [H|R]):-
    sub_even(T,R).
    