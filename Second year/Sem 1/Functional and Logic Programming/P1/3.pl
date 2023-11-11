% a) Define a predicate to remove from a list all repetitive elements. 
% Eg.: l=[1,2,1,4,1,3,4] => l=[2,3])

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

% removeRep(L - list, R - list)
% removeRep(l1..ln) = [], n = 0
%					  removeRep(remove(l1...ln,l1)), if nb_occ(l1, l1..ln) > 1
%					  removeRep(l2..ln), otherwise
% flow model: (i, i), (i, o)
removeRep([],[]).
removeRep([H|T], R):-
    nb_occ([H|T], H, N),
    N > 1,
    !,
    remove([H|T], H, R1),
    removeRep(R1, R).
removeRep([H|T], [H|R]):-
    removeRep(T,R).

% b) Remove all occurrence of a maximum value from a list on integer numbers


% maxim(A - nb, B - nb, R - result)
maxim(A,B,A):-
    A > B,
    !.
maxim(_,B,B).

% maxim_list(L - list, R - number)
% maxim_list(l1..ln) = l1, if n = 1
%					   max(maxim_list(l2..ln), l1), otherwise
% flow model: (i, i), (i, o)
maxim_list([H],H):-!.
maxim_list([H|T], R):-
    maxim_list(T,R1),
    maxim(R1,H,R).

% remove_max(L - list, R - result)
% flow model: (i,i), (i,o)

remove_max(L,Res):-
    maxim_list(L,R),
    remove(L,R,Res).