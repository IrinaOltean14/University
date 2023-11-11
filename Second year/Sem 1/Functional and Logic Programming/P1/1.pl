% a) Write a predicate to determine the lowest common multiple of a list formed from integer numbers.

% gcd(a - number, b - number)
% gcd(a, b) = a, b = 0
%			  gcd(b, a %b), otherwise
% flow model: (i, i, o), (i, i, i)
gcd(A,0,A):-!.
gcd(A,B,R):-
    B1 is A mod B,
    gcd(B,B1,R).

% lcm(a - number, b - number)
% lcm(a, b) = a*b/gcd(a,b)
% flow model: (i,i,o), (i,i,i)
lcm(A,B,R):-
    P is A*B,
    gcd(A,B,R1),
    R is P/R1.

% lcmL(L - list, R - number)
% lcmL(l1..ln) = l1, if n = 1
%				 lcm(l1, lmcL(l2...ln)), otherwise
% flow model: (i, o), (i, i)
lcmL([A], A):-!.
lcmL([H|T], R):-
    lcmL(T, R1),
    lcm(H,R1,R).

% b) Write a predicate to add a value v after 1-st, 2-nd, 4-th, 8-th, … element in a list.

% add2(L - list, V - number, LRes - list)
% flow model: (i, i, o), (i, i, i)
add2(L, V, LRes):-
    addV2(L,1,1,LRes,V).

% addV2(L - list, P - nb, N - nb, LRes - list, V - nb)
% addV2(l1..ln, P, N,V) = [], n = 0
%						l1,V + addV2(l2..ln,P+1,N*2,V) if P=N
%						l1 + addV2(l2..ln,P+1,N,V) otherwise
% flow model: (i, i, i, o, i), (i, i, i, i)
addV2([],_,_,[],_):-!.
addV2([H|T],P,N,[H,V|R],V):-
    P =:= N,
    !,
    N1 is N * 2,
    P1 is P+1,
    addV2(T,P1,N1,R,V).
addV2([H|T],P,N,[H|R], V):-
    P =\= N,
    P1 is P+1,
    addV2(T,P1,N,R,V).