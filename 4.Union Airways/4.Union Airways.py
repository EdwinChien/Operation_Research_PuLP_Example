'''
This code is written by Edwin, Chien on 2020/03/13s.
4.Union Airways[Python]
'''
# import all of the API from PuLP.
from pulp import *

# Initial Problem
prob = LpProblem("Union Airways", LpMinimize)

# Initial Parameters
cost = [170, 160, 175, 180, 195]
MinAgents = [48, 79, 65, 87, 64, 73, 82, 43, 52, 15]
Coverage = [[1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1]]

#Initial Variable
x = LpVariable.dicts("x", [s for s in range(len(cost))], lowBound=0)

# Objective Function
prob += lpSum( [x[i] * cost[i] for i in range(len(cost))] )

# Constraint
for _, num in enumerate(MinAgents):
    prob += lpSum( [x[i] * Coverage[_][i] for i in range(len(cost))] ) >= num

# Problem Solve & Check
prob.solve()
status = prob.solve()

# Show Result
print("Operation status = {}\n".format(LpStatus[status]))
print("Optimal_value = {}\n".format(value(prob.objective)))
for i in range(len(cost)):
    print('The value of {} is {}.'.format(x[i], x[i].varValue))