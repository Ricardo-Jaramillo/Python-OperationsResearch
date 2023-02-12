import numpy as np
from scipy.optimize import linear_sum_assignment

# Example 1. Minimization
# There are 5 Machines to 5 Jobs. Obtain the minimum cost for each machine to each job

cost_matrix = np.array( [[6, 12, 3, 11, 15],
                        [4, 2, 7, 1, 10],
                        [8, 11, 10, 7, 11],
                        [16, 19, 12, 23, 21],
                        [9, 5, 7, 6, 10]])

row_i, col_i = linear_sum_assignment(cost_matrix)

opt_ass = col_i

total_cost = cost_matrix[row_i, col_i].sum()

print(opt_ass)
print('Total assignement cost: %d' %total_cost)


#Example 2. Maximization

matrix = np.array(
                        [[5, 7, 11, 6, 7],
                        [8, 5, 5, 6, 5],
                        [6, 7, 10, 7, 3],
                        [10, 4, 8, 2, 4]])

cost_matrix = []

for row in matrix:
    cost_row = []
    for col in row:
        cost_row += [np.amax(matrix) - col]
    cost_matrix += [cost_row]

# print(cost_matrix)

drow = np.zeros((5, ), dtype=int)
ncost_matrix = np.vstack((cost_matrix, drow))
# print(ncost_matrix)

row_i, col_i = linear_sum_assignment(ncost_matrix)

opt_ass = col_i

total_profit = np.vstack((matrix, drow))[row_i, col_i].sum()

print(opt_ass)
print('The total profit is %d' %total_profit)