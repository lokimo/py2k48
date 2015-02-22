from random import randint

def merge(list):
    '''
    Merges a list
    :param list:
    :return: merged list
    '''
    res = []
    length = len(list)
    prev = None
    for i in list:
        if i == 0: continue
        if not prev: prev = i
        elif i == prev:
            res.append(i+prev)
            prev = None
        else:
            res.append(prev)
            prev = i
    if prev: res.append(prev)
    return res + [0 for _ in range(length - len(res))]

def create_matrix(n):
    '''
    Returns a nXn matrice
    :param n: int
    :return: list containing n times a list of length n
    '''
    list = [[0 for _ in range(n)] for _ in range(n)]
    list[0][0] = 2
    list[0][1] = 2
    return list

def print_matrix(matrix):
    n = len(matrix)
    print('#'*n*2)
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

def turn_right(matrix):
    '''
    Turns the Matrice clockwise
    :param matrix:
    :return:
    '''
    n = len(matrix)
    res = [0 for _ in range(n)]
    for i in range(n):
        res[i] = [0 for _ in range(n)]
        for j in range(n):
            res[i][j] = matrix[j][i]
    return res

def move_left(matrix):
    '''
    Move and merge Numbers to the left
    :param matrix: list
    :return: list
    '''
    res = []
    for row in matrix:
        res.append(merge(row))
    # Next, ad a 2 in a random place
    # TODO check if and where we can add another number
    # TODO check if we can do one move
    place = randint(0, len(matrix)-1)
    res[place][len(matrix)-1] = 2
    return res

def move_right(matrix):
    '''
    Move and merge Numbers to the right
    :param matrix: list
    :return: list
    '''
    res = []
    # TODO deuglify
    for row in matrix:
        res.append(list(reversed(row)))
    matrix = move_left(res)
    res = []
    for row in matrix:
        res.append(list(reversed(row)))
    return res

def move_up(matrix):
    '''
    Move and merge Numbers up
    :param matrix: list
    :return: list
    '''
    res = turn_right(matrix)
    res = move_left(res)
    res = turn_right(res)
    return res

def move_down(matrix):
    '''
    Move and merge Numbers down
    :param matrix: list
    :return: list
    '''
    res = turn_right(matrix)
    res = move_right(res)
    res = turn_right(res)
    return res


m = create_matrix(5)
if __name__ == '__main__':
    print('Lets go!')
    print_matrix(m)
    while True:
        n = input()
        if n == 'w':
            m = move_up(m)
            print_matrix(m)
        elif n == 'a':
            m = move_left(m)
            print_matrix(m)
        elif n == 's':
            m = move_down(m)
            print_matrix(m)
        elif n == 'd':
            m = move_right(m)
            print_matrix(m)
