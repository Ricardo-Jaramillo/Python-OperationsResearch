import cplex
from cplex import SparsePair

'''
Find 
    max z = cx 
s.t
    x <= b
'''

# Initializing parameters
n = 3
a = [5, 10, 15]
var_names = [f'x_{i}' for i in range(n)]

# Declare right hand side
rhs = [20, 30, 40]

# Init the model
c = cplex.Cplex()

# add decision variables. Note indexes and vars are both lists
c.variables.add(
    obj=a,
    names=var_names
)

# Define the Type of decision variables: C -> continuous, I -> integer, B -> binary
# CPLEX defines the model as an a LP (all introduced variables are assumed to be continuous) unless you declare otherwise

# Initialize contraints. Note lists are used for each argument type
c.linear_constraints.add(   lin_expr=[SparsePair(ind=[f'x_{i}'], val=[1]) for i in range(n)],
                            senses=['L']*n,
                            rhs=rhs,
                            names=[f'Constraint_{i}' for i in range(n)])

# Set as a maximizations or minimization as the problem requests. CPLEX set the model to be a minimization one by default
c.objective.set_sense(c.objective.sense.maximize)

c.solve()

x_solution = c.solution.get_values()
print(x_solution)

obj = c.solution.get_objective_value()
print(obj)

print(c.write('problem2_out.lp'))