def add_func(a, b):
    '''Возвращает сумму a и b'''
    return round((a + b), 2)


def true_division(a, b):
    '''Результат деления a на b'''
    return round((a / b), 2)


def exponantional_to(a, b):
    '''Вознесение a к степени b'''
    return a ** b


def exchange_values(a, b):
    '''Обмен значений a на b и наоборот'''
    return b, a


def candies_to_smash(alice, bob, carol):
    '''Сколько конфет останется(будет уничтожено), после деления поровну между друзьями'''
    return round(
        (alice + bob + carol) % 3, 2
    )
