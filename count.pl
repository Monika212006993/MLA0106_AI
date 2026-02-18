% --- Fact ---
sentence("This is my first Degree in abc college of Engineering").
% --- Check vowel ---
vowel(Char) :-
    member(Char, [a, e, i, o, u, A, E, I, O, U]).
% --- Count vowels in a list ---
count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H), !,
    count_vowels(T, Remaining),
    Count is Remaining + 1.
count_vowels([_|T], Count) :-
    count_vowels(T, Count).
% --- Main rule to count vowels in the sentence ---
vowel_count(Count) :-
    sentence(S),
    string_chars(S, CharList),
    count_vowels(CharList, Count).
