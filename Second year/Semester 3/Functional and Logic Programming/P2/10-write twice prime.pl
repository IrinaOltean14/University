% a) For a list of integer numbers, define a predicate to write twice in list every prime number.

% prime(N - number, D - number)
% prime(n, d) = true, if n = d
%				false, if n % d == 0
%				prime(n, d+1), otherwise
% flow model: (i, i)

prime(N,N):-!.
prime(N,D):-
    N > 1,
    R is N mod D,
    R =\= 0,
    !,
    D1 is D + 1,
    prime(N,D1).

% write_prime(L - list, R - list)
% write_prime(l1...ln) = [], if n = 0
%						 l1 + l1 + write_prime(l2..ln), if prime(l1)
%						 l1 + write_prime(l2...ln), otherwise
% flow model: (i, o), (i, i)

write_prime([],[]).
write_prime([H|T], [H,H|R]):-
    prime(H,2),
    !,
    write_prime(T,R).
write_prime([H|T], [H|R]):-
    write_prime(T, R).

% b)  For a heterogeneous list, formed from integer numbers and list of numbers, define a predicate to write in 
% every sublist twice every prime number.
% Eg.: [1, [2, 3], 4, 5, [1, 4, 6], 3, [1, 3, 7, 9, 10], 5] =>
% [1, [2, 2, 3, 3], 4, 5, [1, 4, 6], 3, [1, 3, 3, 7, 7, 9, 10], 5]

% sub(L - list, R - list)
% sub(l1..ln) = [], if n = 0
% 				write_prime(l1) + sub(l2...ln), if is_list(l1)
%				l1 + sub(l2...ln), otherwise

sub([],[]).
sub([H|T], [P|R]):-
    is_list(H),
    !,
    write_prime(H,P),
    sub(T,R).
sub([H|T], [H|R]):-
    sub(T,R).
