% a) Replace all occurrences of an element from a list with another element e

% replace(L - list, A - number, B - number, R - list)
% replace(l1...ln, a, b) = [], if n = 0
%						   b + replace(l2...ln,a,b), if l1 = a
%						   l1 + replace(l2...ln, a, b), otherwise
% flow model: (i,i,i,o), (i,i,i,i)

replace([],_,_,[]).
replace([A|T],A,B,[B|R]):-
    !,
    replace(T,A,B,R).
replace([H|T],A,B,[H|R]):-
    replace(T,A,B,R).

% For a heterogeneous list, formed from integer numbers and list of numbers, define a predicate to determine 
% the maximum number of the list, and then to replace this value in sublists with the maximum value of sublist.
% Eg.: [1, [2, 5, 7], 4, 5, [1, 4], 3, [1, 3, 5, 8, 5, 4], 5, [5, 9, 1], 2] =>
% [1, [2, 7, 7], 4, 5, [1, 4], 3, [1, 3, 8, 8, 8, 4], 5, [9, 9, 1], 2

% get_max(L - list, M - number)
% get_max(l1...ln) = l1, if n = 1 and number(l1)
%					 0, if n = 1 and not number(l1)
%					 max(l1, get_max(l2...ln)), if number(l1)
%					 get_max(l2...ln), otherwise

get_max([E],E):-
    number(E),
    !.
get_max([_],0).
get_max([H|T],H):-
    number(H),
    get_max(T,R),
    H > R,
    !.
get_max([_|T],R):-
    get_max(T,R).
    

% sub(L - list, M - number, R - list)
% sub(l1...ln, m) = [], if n = 0
%					replace(l1,m,get_max(l1)) + sub(l2...ln), if is_list(l1)
%					l1 + sub(l2...ln), otherwise
% flow model: (i,i, o), (i,i,i)
sub([],_,[]).
sub([H|T],M,[P|R]):-
    is_list(H),
    !,
    get_max(H,Max),
    replace(H,M,Max,P),
    sub(T,M,R).
sub([H|T],M,[H|R]):-
    sub(T,M,R).

main(L,R):-
    get_max(L,Max),
    sub(L,Max,R).

    