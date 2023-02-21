from pulp import LpProblem, LpVariable, LpStatus, LpMinimize, GLPK, value

M = 3
N = 3
a = range(1, M + 1)
a1 = range(M)
b = range(1, N + 1)
b1 = range(N)

xindx = [(a[i], b[j]) for j in b1 for i in a1]

model = LpProblem("Transportation LP Problem", LpMinimize)

x = LpVariable.dicts('X', xindx, 0, None)

model +=    4*x[1, 1] + 3*x[1, 2] + 8*x[1, 3] + \
            7*x[2, 1] + 5*x[2, 2] + 9*x[2, 3] + \
            4*x[3, 1] + 5*x[3, 2] + 5*x[3, 3], 'Transportation cost'

model += x[1, 1] + x[1, 2] + x[1, 3] <= 300, 'Supply Pt 1'
model += x[2, 1] + x[2, 2] + x[2, 3] <= 300, 'Supply Pt 2'
model += x[3, 1] + x[3, 2] + x[3, 3] <= 100, 'Supply Pt 3'

model += x[1, 1] + x[1, 2] + x[1, 3] >= 200, 'Demand Pt 1'
model += x[2, 1] + x[2, 2] + x[2, 3] >= 200, 'Demand Pt 2'
model += x[3, 1] + x[3, 2] + x[3, 3] >= 300, 'Demand Pt 3'

model.solve(GLPK())

print('Status: ', LpStatus[model.status])

for v in model.variables():
    print(v.name, '=', v.varValue)

print("Objective Function", value(model.objective))