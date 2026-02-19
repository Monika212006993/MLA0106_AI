# Simple Reflex Agent for Vacuum Cleaner Problem

def vacuum_world(loc_A, loc_B, location):
    if location == "A":
        if loc_A == "dirty":
            print("Location A is dirty → CLEAN")
            loc_A = "clean"
        else:
            print("Location A is clean → MOVE RIGHT to B")
            location = "B"

    if location == "B":
        if loc_B == "dirty":
            print("Location B is dirty → CLEAN")
            loc_B = "clean"
        else:
            print("Location B is clean → MOVE LEFT to A")
            location = "A"

    return loc_A, loc_B, location


# Initial conditions
loc_A = "dirty"
loc_B = "clean"
location = "A"

print("Initial State: A =", loc_A, ", B =", loc_B)
loc_A, loc_B, location = vacuum_world(loc_A, loc_B, location)
loc_A, loc_B, location = vacuum_world(loc_A, loc_B, location)

print("\nFinal State: A =", loc_A, ", B =", loc_B)
