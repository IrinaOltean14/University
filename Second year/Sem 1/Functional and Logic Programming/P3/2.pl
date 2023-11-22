% A set of n points in a plan (represented using its coordinates) are given. Write a predicate to determine 
% all subsets of collinear points.

% slope(X1 - nb, Y1 - nb, X2- nb, Y2 - nb, Slope - nb) - predicate to calculate the slope between 2 points
% slope(x1,y1,x2,y2) = (y2-y1)/(x2-x1)
% flow model: (i,i,i,i,o)
slope(X1,Y1,X2,Y2, Slope):-
    Slope is (Y2 - Y1) / (X2 - X1).

% Predicate to check if three points are collinear
% collinear(X1 - nb, Y1 - nb, X2 - nb, Y2 - nb, X3 - nb, Y3 - nb)
% collinear([x1,y1],[x2,y2],[x3,y3]) = true, if slope(x1,y1,x2,y2) = slope(x2,y2,x3,y3)
%									   false, otherwise
% flow model: (i,i,i,i,i,i)
collinear([[X1, Y1], [X2, Y2], [X3, Y3]]) :-
    slope(X1, Y1, X2, Y2, Slope1),
    slope(X2, Y2, X3, Y3, Slope2),
    Slope1 =:= Slope2.

% predicate that  generates subsets of a list of coordinate pairs. The second argument 
% specifies the size of the subset, and the third argument accumulates the elements of the
% current subset. The predicate also checks whether the elements in the subset are 
% collinear when the subset is complete (K is 0). The code uses recursion to explore 
% different combinations of elements in the list to generate subsets.
% subset(L - list, K - nb, Col - list, R - list)
% subset((l11,l12)...(ln1,ln2),k,(c11,c12)...(cm1,cm2)) = [], if k = 0 and collinear((c11,c12)...(c31,c32))
%														  (l11,l12) + subset((l21,l22)..., k-1, (l11,l22)(c11,c12)...), if k > 0
%														  subset((l21,l22)...,k,(c11,c12)...), if k > 0
% flow model: (i,i,i,o)
subset(_,0,Col,[]):-
    collinear(Col).
subset([[A,B]|T], K, Col,[[A,B]|R]):-
    K>0,
    K1 is K -1,
    subset(T,K1,[[A,B]|Col],R).
subset([[_,_]|T],K, Col, R):-
    K>0,
    subset(T,K,Col,R).

all_solutions(L,R):-
    findall(X, subset(L,3,[],X),R).