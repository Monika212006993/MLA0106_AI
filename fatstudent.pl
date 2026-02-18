% --- Facts: Student Attributes ---
attribute(john, hardworking).
attribute(john, regular).
attribute(sarah, irregular).
attribute(sarah, average).
attribute(mike, hardworking).
attribute(mike, irregular).
% --- Rules for Performance Prediction ---

% Excellent performance: hardworking + regular attendance
performance(Student, excellent) :-
    attribute(Student, hardworking),
    attribute(Student, regular).
% Good performance: hardworking + irregular attendance
performance(Student, good) :-
    attribute(Student, hardworking),
    attribute(Student, irregular).
% Average performance: has 'average' trait
performance(Student, average) :-
    attribute(Student, average). 
