import numpy as np
import itertools
from numpy.linalg import det





def main():
    permuts = list(itertools.product([1, -1, 0], repeat=16))
    numpy_list = []
    count = 0
    for permut in permuts:
        count += 1
        numpy_list.append(np.array(list(permut)).reshape((4, 4)))
    print('Count: ' + str(count))
    det_list = []
    for mat in numpy_list:
        det_list.append(det(mat))
    max_det = np.max(np.array(det_list))
    count_of_max = 0
    for ind in range(len(det_list)):
        if det_list[ind] == max_det:
            count_of_max += 1
            print('Det: ' + str(det_list[ind]))
            print(numpy_list[ind])
    print('A total of ' + str(count_of_max) + ' unique matrices')

if __name__ == "__main__":
    main()