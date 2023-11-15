% a) Write a predicate to determine the sum of two numbers written in list representation.

% addLast(L - list, E - element)
% addLast(l1..ln, e) = [e], if n = 0
% 					   addLast(l2..ln,e), otherwise
addLast([],E,[E]).
addLast([H|T],E,[H|R]):-
    addLast(T,E,R).


% reverse(L - list, R - list)
% reverse(l1...ln) = [], if n = 0
%					 addLast(reverse(l2...ln),l1), otherwise
reverse([],[]).
reverse([H|T],R):-
    reverse(T,R1),
    addLast(R1,H,R).


% suma(L1 - list, L2 - list, C - number, R - list)
% suma(l1...ln, k1...km, c) = [], if n = 0 and m = 0 and c = 0
%							  [1], if n = 0 and m = 0 and c = 1
%							  (l1+c)%10 + suma(l2...ln, [], (l1+c)/10), if m = 0
%							  (k1+c)%10 + suma(k2..km, [], (l1+c)/10), if n = 0
%							  (l1+k1+c)%10 + suma(l2..ln,k2..lm,(l1+k1+c)/10), otherwise
suma([],[],0,[]):-!.
suma([],[],1,[1]):-!.
suma([H|T],[],C,[D|R]):-
    !,
    S is H+C,
    D is S mod 10,
    C1 is S div 10,
    suma(T,[],C1,R).
suma([],[H|T],C,[D|R]):-
    !,
    S is H+C,
    D is S mod 10,
    C1 is S div 10,
    suma(T,[],C1,R).
suma([H1|T1],[H2|T2],C,[D|R]):-
    S is H1+C,
    S1 is S+H2,
    D is S1 mod 10,
    C1 is S1 div 10,
    suma(T1,T2,C1,R).

main(L1, L2, R):-
    reverse(L1,A),
    reverse(L2,B),
    suma(A,B,0,R1),
    reverse(R1,R).
   
% b)  For a heterogeneous list, formed from integer numbers and list of digits, write a predicate to compute the 
% sum of all numbers represented as sublists.
% Eg.: [1, [2, 3], 4, 5, [6, 7, 9], 10, 11, [1, 2, 0], 6] => [8, 2, 2]

% sum_list(L - list, R - result)
% sum_list(l1...ln) = [], if n = 0
%					  l1 + sum(l2...ln), if is_list(l1)
%					  sum(l2..ln), otherwise

sum_list([],[]):-!.
sum_list([H|T], R):-
    is_list(H),
    !,
    sum_list(T,R1),
    main(H,R1,R).
sum_list([_|T],R):-
    sum_list(T,R).