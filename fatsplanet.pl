% --- Facts: Orbiting Bodies ---
orbits(mercury, sun).
orbits(venus, sun).
orbits(earth, sun).
orbits(mars, sun).
orbits(moon, earth).
orbits(phobos, mars).
orbits(deimos, mars).
% --- Optional: A rule to check planets orbiting the Sun ---
planet(X) :-
    orbits(X, sun).
% --- Optional: A rule to check moons of a planet ---
moon_of(Moon, Planet) :-
    orbits(Moon, Planet).
