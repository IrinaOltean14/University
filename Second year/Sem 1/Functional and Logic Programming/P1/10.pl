% a) Define a predicate to test if a list of an integer elements has a "valley" aspect (a set has a "valley" aspect if 
% elements decreases up to a certain point, and then increases. 
% eg: 10 8 6 9 11 13 – has a “valley” aspect

% valley(L - list, K - number)
% valley(l1..ln, k) = true, if n = 1 and k = 0
%					  valley(l2...ln, 1), if l1 > l2 and k = 1
%					  valley(l2...ln, 0), if l1 < l2 and k = 1,
%					  valley(l2...ln, 0), if l1 < l2 and k = 0,
% 					  false, otherwise

valley([_], 0):-!.
valley([A,B|T], -1):-
    A > B,
    !,
    valley([B|T], 1).
valley([A,B|T], 1):-
    A > B,
    !,
    valley([B|T], 1).
valley([A,B|T], 1):-
    A < B,
    !,
    valley([B|T],0).
valley([A,B|T], 0):-
    A < B, 
    valley([B|T], 0).

calc_valley(L):-
    valley(L,-1).

% b) Calculate the alternate sum of list’s elements (l1 - l2 + l3 ...).

% sum(L - list, K - nb, R - result)
% sum(l1..ln, k) = 0, n = 0
%				   l1 + sum(l2...ln, 0), if k = 1
%				   -l1 + sum(l2..ln, 1), if k = 0
% flow model(i, i, o), (i, i, i)

sum([],_,0):-!.
sum([H|T],1,R):-
    !,
    sum(T,0,R1),
    R is H + R1.
sum([H|T], 0, R):-
    sum(T,1,R1),
    H1 is H * (-1),
    R is H1 + R1.

alternate_sum(L,R):-
    sum(L,1,R).
