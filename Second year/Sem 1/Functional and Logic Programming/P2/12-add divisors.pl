% a) Define a predicate to add after every element from a list, the divisors of that number.

% get_divisors(N - number, D - number, R - list)
% get_divisors(n, d) = [], if n >= d  
%					   [d] + get_divisors(n, d+1), if n % d == 0
%					   get_divisors(n, d+1), otherwise
% flow model: (i,i,o), (i,i,i)

get_divisors(N,D,[]):-
    N =< D,
    !.
get_divisors(N,D,[D|R]):-
    N mod D =:= 0,
    !,
    D1 is D + 1,
    get_divisors(N,D1,R).
get_divisors(N,D,R):-
    D1 is D + 1,
    get_divisors(N,D1,R).


% append(L1 - list, L2 - list, R - list)
% append(l1..ln, k1...km) = k1..km, if n = 0
%							l1 + append(l2...ln, k1...km), otherwise
% flow model: (i,i,o), (i,i,i)

append([],L2,L2).
append([H|T], L2, [H|R]):-
    append(T,L2,R).

% add_div(L - list, R - list)
% add_div(l1...ln) = [], if n = 0
%					 l1 + append(get_divisors(l1), add_div(l2...ln)), otherwise
% flow model: (i,o), (i,i)

add_div([],[]).
add_div([H|T], [H|R]):-
    get_divisors(H,2,P),
    add_div(T,R1),
    append(P,R1,R).

% b) For a heterogeneous list, formed from integer numbers and list of numbers, define a predicate to add in 
% every sublist the divisors of every element.
% Eg.: [1, [2, 5, 7], 4, 5, [1, 4], 3, 2, [6, 2, 1], 4, [7, 2, 8, 1], 2] =>
% [1, [2, 5, 7], 4, 5, [1, 4, 2], 3, 2, [6, 2, 3, 2, 1], 4, [7, 2, 8, 2, 4, 1], 2]

% sub_div(L - list, R - list)
% sub_div(l1...ln) = [], if n = 0
% 					 add_div(l1) + sub_div(l2...ln), if is_list(H)
%					 l1 + sub_div(l2...ln), otherwise
% flow model: (i,o), (i,i)

sub_div([],[]).
sub_div([H|T],[P|R]):-
    is_list(H),
    !,
    add_div(H,P),
    sub_div(T,R).
sub_div([H|T],[H|R]):-
    sub_div(T,R).


