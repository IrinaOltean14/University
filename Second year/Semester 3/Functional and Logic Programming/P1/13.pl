% a) Transform a list in a set, in the order of the last occurrences of elements. Eg.: [1,2,3,1,2] is transformed in 
% [3,1,2]

% nb_occurences(L - list, E - element, R - result)
% nb_occurences(l1...ln,e) = 0, if n = 0
%							 1 + nb_occurences(l2...ln,e), if l1 = e
%							 nb_occurences(l2...ln), otherwise
% flow model: (i,i,o), (i,i,i)
nb_occurences([],_,0):-!.
nb_occurences([H|T],H,S):-
    !,
    nb_occurences(T,H,S1),
    S is S1 + 1.
nb_occurences([_|T],E,S):-
    nb_occurences(T,E,S).


% set(L - list, R - result)
% set(l1...ln) = [], if n = 0
%				 l1 + set(l2...ln), if nb_occurences(l1) = 0
%				 set(l2...ln), otherwise
% flow model: (i,o), (i,i)

set([],[]).
set([H|T],[H|R]):-
    nb_occurences(T,H,R1),
    R1 =:= 0,
    !,
    set(T,R).
set([_|T], R):-
    set(T,R).
