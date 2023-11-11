% a) . Write a predicate to remove all occurrences of a certain atom from a list.

% remove(L - list, E - element, LRes- list)
% remove(l1..ln, e) = [], n = 0
%					  remove(l2..ln,e), if l1 = e
%					  l1 + remove(l2..ln,e), otherwise
% flow model: (i,i,o), (i,i,i)
remove([], _, []).
remove([E|T], E, R):-
    !,
    remove(T,E,R).
remove([H|T], E, [H|R]):-
    remove(T,E,R).

% b) Define a predicate to produce a list of pairs (atom n) from an initial list of atoms. In this initial list atom has 
% n occurrences.

% member(L - list, E - element)
% member(l1..ln, e) = true, l1 = e
%					  member(l2..ln,e), otherwise
% flow model: (i, i)
member([E|_], E):-!.
member([_|T],E):-
    member(T,E).

% nb_occ(L - list, E - element, N - number)
% nb_occ(l1..ln, e) = 0, n = 0
%					  1 + nb_occ(l2..ln,e), l1 = e
%					  nb_occ(l2..ln,e), otherwise
% flow model: (i,i,o), (i,i,i)
nb_occ([],_,0).
nb_occ([E|T],E,S):-
    !,
    nb_occ(T,E,S1),
    S is S1 + 1.
nb_occ([_|T],E,S):-
    nb_occ(T,E,S).

% pairs(L - list, D - list, R - list)
% pairs(l1..ln, d1..dm) = [], n = 0
%						  [l1, nb_occ(l1,l1..ln)] + pairs(l2..ln, l1d1..dm), if l1 not in d1..dm
%						  pairs(l2..ln,d1..dm), otherwise
% flow model: (i,i,o), (i,i,i)
pairs([], _,[]).
pairs([H|T], D,[[H,N]|R]):-
    not(member(D,H)),
    !,
    nb_occ([H|T], H, N),
    pairs(T,[H|D],R).
pairs([_|T], D,R):-
    pairs(T,D,R).

mainPair(L,R):-
    pairs(L,[],R).

% same but with findall

pairs2([], _, []).
pairs2([H|T], D,[H,N]):-
    not(member(D,H)),
    nb_occ([H|T], H, N).
pairs2([_|T], D,R):-
    pairs(T,D,R).
    
mainPair2(L,R):-
    findall(X, pairs2(L, [], X), R).




