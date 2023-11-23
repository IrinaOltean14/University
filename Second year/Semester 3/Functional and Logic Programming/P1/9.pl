% a) Insert an element on the position n in a list.

% insert(L - list, E - element, P - positon, R - result list)
% insert(l1...ln, p, e) = e + l1..ln, if p = 0
%						  l1 + insert(l2...ln, p-1, e), otherwise
% flow model: (i,i,i,o), (i,i,i,i)
insert(L, E, 0, [E|L]):-
    !.
insert([H|T], E, P, [H|R]):-
    P1 is P-1,
    insert(T,E,P1,R).

% b) Define a predicate to determine the greatest common divisor of all numbers from a list.

% gcd(A - nb, B - nb, R - nb)
% gcd(a, b) = a, if a = b
%		      gcd(b, a%b), otherwise
% flow model: (i,i,o), (i,i,i)
gcd(A,0,A):-!.
gcd(A,B,R):-
    C is A mod B,
    gcd(B,C,R).

% determine_gcd(L - list, R - number)
% determine_gcd(l1..ln) = gcd(l1,l2), if n = 2
%						  l1, if n = 1
%						  gcd(l1, determine_gcd(l2..ln)), otherwise

determine_gcd([X], X):-!.
determine_gcd([X,Y], R):-
    !,
    gcd(X,Y,R).
determine_gcd([H|T], R):-
    determine_gcd(T,R1),
    gcd(H,R1,R).