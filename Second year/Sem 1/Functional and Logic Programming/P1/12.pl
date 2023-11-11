% a) Write a predicate to substitute in a list a value with all the elements of another list

% substitute(L1 - list, E - nb, L2 - list, R - list)
% substitute(l1...ln, e, k1..km) = [], if n = 0
%								   l1 + substitute(l2...ln,e,k1...km), if l1 != e
%								   (k1...km) + substitute(l2...ln,e,k1...km), otherwise
% flow model: (i,i,i,o), (i,i,i,i)

substitute([],_,_,[]).
substitute([H|T], E, L, [H|R]):-
    E =\= H,
    !,
    substitute(T,E,L,R).
substitute([H|T], H, L, [L|R]):-
    !,
    substitute(T,H,L,R).

% b)  Remove the n-th element of a list.

% remove(L - list, P - nb, R - list)
% remove(l1...ln, p) = l2...ln, if p = 0
%					   l1 + remove(l2..ln, p-1), otherwise
% flow model: (i,i,i), (i,i,o)

remove([_|T], 0, T):-!.
remove([H|T], P, [H|R]):-
    P1 is P-1,
    remove(T,P1,R).