% a) Write a predicate to test if a list is a set

% member(L - list, E - element)
% member(l1...ln, e) = true, if l1 = e
%					   member(l2..ln,e), otherwise
% flow model: (i,i), (i,o)
member([E|_],E):-!.
member([_|T], E):-
    member(T,E).

% test(L - list)
% test(l1..ln) = true, n = 0
%				 false, if l1 in l2..ln
%				 test(l2..ln), otherwise
test([]).
test([H|T]):-
    not(member(T,H)),
    !,
  	test(T).

% b) Write a predicate to remove the first three occurrences of an element in a list. If the element occurs less 
% than three times, all occurrences will be removed

% remove_occ(L - list, E - element, K - nb of occurences, R - list)
% remove_occ(l1..ln,e,k) = [], if n = 0
%						   l1...ln, if k = 0
%						   l1 + remove_occ(l2..ln,e,k), if l1 != k
%						   remove_occ(l2..ln, e, k-1), if l1 = k
% flow model: (i,i,i,o), (i,i,i,i)
remove_occ(L,_,0,L):-!.
remove_occ([],_,_,[]).
remove_occ([H|T],H,K,R):-
    !,
    K1 is K - 1,
    remove_occ(T,H,K1,R).
remove_occ([H|T],E,K,[H|R]):-
    remove_occ(T,E,K,R).

remove3(L, E, R):-
    remove_occ(L,E,3,R).




