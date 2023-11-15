% a)  Merge two sorted lists with removing the double values.

% remove_doubles(L - list, R - list)
% remove_doubles(l1...ln) = [l1], if n = 1
%							remove_doubles(l2...ln), if l1 = l2
%							l1 + remove_doubles(l2...ln), otherwise
remove_doubles([X],[X]):-!.
remove_doubles([A,B|T],R):-
    A =:= B,
    !,
    remove_doubles([B|T],R).
remove_doubles([A,B|T],[A|R]):-
    remove_doubles([B|T],R).

% merge(L1 - list, L2 - list, R - list)
% merge(l1...ln, k1...km) = k1...km, if n = 0
%							l1...ln, if m = 0
%							l1 + merge(l2...ln, k1...km), if l1 < k1
%							k1 + merge(l1...lm, k2...km), if l1 > k1
%							merge(l1...lm, k2...km), if l1 = k1
% flow model: (i,i,o)

merge([],L,L):-!.
merge(L,[],L):-!.
merge([H1|T1],[H2|T2],[H1|R]):-
    H1 < H2,
    !,
    merge(T1,[H2|T2],R).
merge([H1|T1],[H2|T2],[H2|R]):-
    H1 > H2,
    !,
    merge([H1|T1], T2, R).
merge([H1|T1],[H2|T2],R):-
    H1 =:= H2,
    merge([H1|T1], T2, R).

% b) . For a heterogeneous list, formed from integer numbers and list of numbers, merge all sublists with removing 
% the double values.
% [1, [2, 3], 4, 5, [1, 4, 6], 3, [1, 3, 7, 9, 10], 5, [1, 1, 11], 8] =>
% [1, 2, 3, 4, 6, 7, 9, 10, 11].

% sub(L - list, Col - list, R - list)
% sub(l1...ln, c1..cm) = c1...cm, if n = 0
%						 sub(l2...ln, merge(l1,c1..cm)), if is_list(l1)
%						 sub(l2...ln, c1...cm), otherwise
sub([],Col,Col):-!.
sub([H|T], Col, R):-
    is_list(H),
    !,
    remove_doubles(H,H1),
    merge(H1,Col,NewC),
    sub(T,NewC,R).
sub([_|T],Col,R):-
    sub(T,Col,R).

main(L,R):-
    sub(L,[],R).
