% --- Gender Facts ---
female(sarah).
female(rebekah).
female(hagar_concubine).
female(milcah).
female(bashemath).
female(mahalath).
female(first_daughter).
female(rachel).
female(labans_wife).
male(terah).
male(abraham).
male(nahor).
male(haran).
male(isaac).
male(ismael).
male(uz).
male(kemuel).
% --- Example Parent Facts (Added to show relationships) ---
% You can modify these if needed.
parent(terah, abraham).
parent(terah, nahor).
parent(terah, haran).
parent(abraham, isaac).
parent(hagar_concubine, ismael).
parent(abraham, ismael).
parent(haran, uz).
parent(nahor, kemuel).
% --- Family Relationship Rules ---
% father(X,Y): X is father of Y
father(X, Y) :-
    male(X),
    parent(X, Y).
% mother(X,Y): X is mother of Y
mother(X, Y) :-
    female(X),
    parent(X, Y).
% brother(X,Y): same parent, male
brother(X, Y) :-
    male(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.
% sister(X,Y): same parent, female
sister(X, Y) :-
    female(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.
% grandfather(X,Y)
grandfather(X, Y) :-
    male(X),
    parent(X, Z),
    parent(Z, Y).

% grandmother(X,Y)
grandmother(X, Y) :-
    female(X),
    parent(X, Z),
    parent(Z, Y).
