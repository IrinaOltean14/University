% a)  Write a predicate to substitute an element from a list with another element in the list.

% substitute(L - list, E1 - nb, E2 - nb, R - list)
% substitute(l1...ln, e1, e2) = [], if n = 0
%								e2 + substitute(l2..ln,e1,e2), if l1 = e1
%								l1 + substitute(l2..ln,e1,e2), otherwise
substitute([],_,_,[]).
substitute([E1|T], E1, E2, [E2|R]):-
    !,
    substitute(T,E1,E2,R).
substitute([H|T], E1, E2, [H|R]):-
    substitute(T,E1,E2,R).

% b) Write a predicate to create the sublist (lm, …, ln) from the list (l1,…, lk)

% sublist(L - list, M - number, N - number, R - list)
% sublist(l1...lk, m, n) =  [], if n = 0
%							sublist(l2...lk, m-1, n-1), if m > 0
%							l1 + sublist(l2..lk, m-1, n-1), if n > 0
% flow model: (i,i,i,i), (i,i,i,o)
sublist(_, _, -1, []):-!.
sublist([_|T], M, N, R):-
    M > 0,
    !, 
    M1 is M-1,
    N1 is N-1,
    sublist(T,M1,N1,R).
sublist([H|T], 0, N, [H|R]):-
    N >= 0,
    !,
    N1 is N-1,
    sublist(T,0,N1,R).