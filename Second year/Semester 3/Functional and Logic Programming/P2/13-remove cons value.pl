% a) Given a linear numerical list write a predicate to remove all sequences of consecutive values. 
% Eg.: remove([1, 2, 4, 6, 7, 8, 10], L) will produce L=[4, 10].

% remove_cons(L - list, R - list)
% remove_cons(l1l2...ln) = [l1..ln], if n <= 1
% 						   [], if n = 2 and l1 + 1 = l2
%						   remove_cons(l2...ln), if l1 + 1 = l2 and l3 = l2 + 1
%						   remove_cons(l3...ln), if l1 + 1 = l2 and l3 != l2 + l1
%						   l1 + remove_cons(l2...ln), otherwise
% flow model(i,o), (i,i)

remove_cons([A],[A]):-!.
remove_cons([],[]).
remove_cons([A,B],[]):-
    A + 1 =:= B,
    !.
remove_cons([A,B,C|T], R):-
    A + 1 =:= B,
    B + 1 =:= C,
    !,
    remove_cons([B,C|T], R).
remove_cons([A,B|T], R):-
    A + 1 =:= B,
    !,
    remove_cons(T,R).
remove_cons([H|T], [H|R]):-
    remove_cons(T,R).

% b)  For a heterogeneous list, formed from integer numbers and list of numbers; write a predicate to delete from 
% every sublist all sequences of consecutive values.
% Eg.: [1, [2, 3, 5], 9, [1, 2, 4, 3, 4, 5, 7, 9], 11, [5, 8, 2], 7] =>
% [1, [5], 9, [4, 7, 9], 11, [5, 8, 2], 7] 

% sub_remove(L - list, R - list)
% sub_remove(l1...ln) = [], if n = 0
%						remove_cons(l1) + sub_remove(l2..ln), if is_list(l1)
%						l1 + remove_cons(l2...ln)
% flow model: (i,o), (i,i)

sub_remove([],[]).
sub_remove([H|T], [P|R]):-
    is_list(H),
    !,
    remove_cons(H,P),
    sub_remove(T,R).
sub_remove([H|T], [H|R]):-
    sub_remove(T, R).




