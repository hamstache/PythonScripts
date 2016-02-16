def identity_mat(num):

    return [[int(r == c) for c in range(num)] for r in range(num)]


def main():
    '''Provides some tests for identity_mat function.
    '''
    print('identity matrix')
    print(identity_mat(1), [[1]])
    print(identity_mat(2), [[1, 0], [0, 1]])
    print(identity_mat(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])


if __name__ == '__main__':
    main()
