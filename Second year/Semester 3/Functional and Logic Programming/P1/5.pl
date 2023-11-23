% a)  Write a predicate to compute the union of two sets.

% member(L - list, E - element)
% member(l1...ln, e) = true, if l1 = e
%					   member(l2..ln,e), otherwise
% flow model: (i,i), (i,o)
member([E|_],E):-!.
member([_|T], E):-
    member(T,E).

% union(L1 - list, L2 - list, L3 - list)
% union(l1...ln, k1..km) = k1..km, n = 0
%						   l1 + union(l2..ln, k1..km), if l1 not in k1..km
%						   union(l2..ln, k1..km), otherwise
% flow model:(i,i,o), (i,i,i)
union([],L2,L2).
union([H|T], L2, [H|R]):-
    not(member(L2,H)),
    !,
    union(T,L2,R).
union([_|T], L2, R):-
    union(T,L2,R).

% Write a predicate to determine the set of all the pairs of elements in a list. 
% Eg.: L = [a b c d] => [[a b] [a c] [a d] [b c] [b d] [c d]]

% generateSets(L - list, K - number, R - result list)
% flow model (i i o)
% generateSets(l1..ln, k) = [], if k  = 0
%							l1 + generateStates(l2..ln, k-1)
%							generatesStates(l1..ln,k)
generateSets(_, 0, []):-
    !.
generateSets([H|T], K, [H|R]):-
    K1 is K - 1,
    generateSets(T, K1, R).
generateSets([_|T], K, R):-
    generateSets(T, K, R).

generateAllSets(L, R):-
    findall(R1, generateSets(L, 2, R1), R).






