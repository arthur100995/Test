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