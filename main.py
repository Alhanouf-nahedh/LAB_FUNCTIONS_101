def name(n: int):
    '''
    the function takes the parameters in integer then print the given integer down to 1.
    '''
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
               print(j, end=' ') # 'end' to print the numbers at the same line
        print()  # for new line after each row


name(5)