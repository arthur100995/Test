def round_two(a):
    '''Округляет до 2-го числа после точки '''
    return round(a, 2)

def round_negative_ndigits(a):
    """Округляет до 1го числа перед точкой, если a < 10 то возвращает текущее значение"""
    if 0 < a < 10:
        return a
    return round(a, -1)
def candies_to_smash_new(total_candies, total_friends = 3):
    """
    Принимает два аргумента, возвращая остачу от деления 1го на 2й,
    Если второй не указан, он равняеться 3-м
    """
    return total_candies % total_friends

def smallest_absolute(a, b):
    """Возвращает минимальное значение по модулю"""
    return min(abs(a), abs(b))