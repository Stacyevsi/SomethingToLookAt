class ArgumentError(Exception):
    pass

def validation_input(n):
    try:
        assert n % 2 == 0
        return n
    except ValueError:
        raise ArgumentError('Tne number must have integer type.')
    except AssertionError:
        raise ArgumentError('You should input even number!')

def flag(n):
    final_str = ''
    mediator_list = []
    for row in range(2*n + 2):
        if row == 0 or row == ((2 * n)+1):
            mediator_list.append(('#' * ((3 * n)+2)))
        elif (row > 0 and row <= n/2) or (row > (n/2 + n) and n < (2 * n)+2):
            mediator_list.append(('#' + ' ' * (3 * n) + '#'))
        elif (row == n/2+1 or row == (n/2 + n)) and n != 2:
            mediator_list.append(('#' + ' ' * (n + 1) + '*' * (n - 2) +
                                  ' ' * (n + 1) + '#'))
        elif row >= n/2+1 and row <= (n/2 + n+1):
            mediator_list.append(('#' + ' ' * n + '*' + 'o' * (n - 2) +
                                  '*' + ' ' * n + '#'))

    return '\n'.join(mediator_list)

N = int(input('Input some even number: '))
print(flag(validation_input(N)))
