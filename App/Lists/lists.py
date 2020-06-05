def select_second(list):
    """Return the second element of the given list.
    If the list has no second element, return None."""
    if len(list) > 1:
        return list[1]
    else:
        return None

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names,
     return the 2nd player (captain) from the last listed team"""
    return teams[-1][1]

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list)
     to last place and vice versa."""
    tmp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = tmp
    return racers

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name,
     return whether the guest with that name was fashionably late."""
    if arrivals.index(name) > len(arrivals) // 2:
        if arrivals.index(name) < len(arrivals) - 1:
            return True
        else:
            return False
    else:
        return False

