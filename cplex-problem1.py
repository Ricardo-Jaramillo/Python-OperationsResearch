import cplex
from cplex import SparsePair

'''
Find 
    max z = x 
s.t
    x <= 10
'''

# Declare right hand side
rhs = [10]

# Init the model
c = cplex.Cplex()

# add decision variables. Note indexes and vars are both lists
c.variables.add(
    obj=[1],
    names=['x']
)

# Define the Type of decision variables: C -> continuous, I -> integer, B -> binary
# CPLEX defines the model as an a LP (all introduced variables are assumed to be continuous) unless you declare otherwise

# Initialize contraints. Note lists are used for each argument type
c.linear_constraints.add( lin_expr=[SparsePair(ind=['x'], val=[1])],
                            senses=['L'],
                            rhs=rhs,
                            names=['Constraint_1'])

# Set as a maximizations or minimization as the problem requests. CPLEX set the model to be a minimization one by default
c.objective.set_sense(c.objective.sense.maximize)

c.solve()

x_solution = c.solution.get_values('x')
print(x_solution)

obj = c.solution.get_objective_value()
print(obj)