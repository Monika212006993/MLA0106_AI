color(red).
color(green).
color(blue).

map(A,B,C,D) :-
    color(A), color(B), color(C), color(D),
    A \= B,
    A \= C,
    B \= C,
    B \= D,
    C \= D.
