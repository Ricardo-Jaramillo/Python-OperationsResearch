import numpy as np
from scipy.optimize import linear_sum_assignment

# There are 5 Machines to 5 Jobs. Obtain the minimum cost for each machine to each job

cost_matrix = np.array( [[6, 12, 3, 11, 15],
                        [4, 2, 7, 1, 10],
                        [8, 11, 10, 7, 11],
                        [16, 19, 12, 23, 21],
                        [9, 5, 7, 6, 10]])

row_i, col_i = linear_sum_assignment(cost_matrix)

opt_ass = col_i

tc = cost_matrix[row_i, col_i].sum()

print(opt_ass)
print('Total assignement cost: %d' %tc)