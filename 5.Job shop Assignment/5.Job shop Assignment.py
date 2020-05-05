'''
This code is written by Edwin, Chien on 2020/03/13.
5.Job shop Assignment[Python]
'''
# import all of the API from PuLP.
from pulp import *

# Initial Problem
prob = LpProblem("Job shop Assignment", LpMinimize)

# Initial Parameters
cost = [13, 16, 12, 11,
        15, 999,13, 30,
         5,  7, 10,  6,
         0,  0,  0,  0]
A_T_range = 4

# Initial Variable
A_T = []
for C in range(A_T_range):
    for W in range(A_T_range):
        A_T.append(str(C+1)+str(W+1))

x = LpVariable.dicts("x", [i for i in A_T], lowBound=0, upBound=1, cat='Binary')

# Objective Function
prob += lpSum( [x[i] * cost[A_T.index(i)] for i in A_T] )

# Constraint
#     For Assignee
for _ in range(A_T_range):
    prob += lpSum( [x[i] for i in A_T if i[0]==str(_+1)] ) == 1 
#     For Task
for _ in range(A_T_range):
    prob += lpSum( [x[i] for i in A_T if i[1]==str(_+1)] ) == 1

# Problem Solve & Check
prob.solve()
status = prob.solve()

# Show Result
print("Operation status = {}\n".format(LpStatus[status]))
print("Optimal_value = {}\n".format(value(prob.objective)))
for i in A_T:
    print('The value of {} is {}.'.format(x[i], x[i].varValue))