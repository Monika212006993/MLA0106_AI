% --- Facts ---
bird(eagle).
bird(sparrow).
bird(penguin).
% --- Rules ---
fly(penguin) :- !, fail.   
fly(X) :- bird(X).         
