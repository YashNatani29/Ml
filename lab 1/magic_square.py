import numpy as np


def isMagicSquare(mat):
    r_sum = mat.sum(axis=1)
    print('Row Sum =>', r_sum)

    c_sum = mat.sum(axis=0)
    print('Column Sum =>', c_sum)

    max_r_sum = np.max(r_sum)
    print('Max Row Sum =>', max_r_sum)

    max_c_sum = np.max(c_sum)
    print('Max Column Sum =>', max_c_sum)

    min_r_sum = np.min(r_sum)
    print('Min Row Sum =>', min_r_sum)

    min_c_sum = np.min(c_sum)
    print('Column Sum =>', min_c_sum)

    d_sum1 = np.sum(np.diagonal(mat))
    print('Diagonal 1 Sum =>', d_sum1)

    d_sum2 = np.sum(np.fliplr(mat).diagonal())
    print('Diagonal 2 Sum =>', d_sum2)

    if max_r_sum == max_c_sum == min_r_sum == min_c_sum == d_sum1 == d_sum2:
        return True
    else:
        return False


# Driver Code
A = np.array([[17, 24, 1, 8, 15],
              [23, 5, 7, 14, 16],
              [4, 6, 13, 20, 22],
              [10, 12, 19, 21, 3],
              [11, 18, 25, 2, 9]])
B = np.array([[17, 24, 1, 8, 15],
              [23, 5, 7, 14, 16],
              [4, 6, 10, 20, 22],
              [10, 12, 19, 21, 3],
              [11, 18, 5, 2, 9]])

print("\nIs A a Magic Square ", isMagicSquare(A), '\n')
print("\nIs B a Magic Square ", isMagicSquare(B))
