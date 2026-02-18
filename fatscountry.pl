% --- Facts ---
american(robert).
weapon(missile).
hostile(countryA).
owns(countryA, missile).
sells(robert, missile, countryA).
% --- Rules (Forward Chaining Style) ---
criminal(X) :-
    american(X),
    sells(X, Item, Country),
    weapon(Item),
    hostile(Country).
