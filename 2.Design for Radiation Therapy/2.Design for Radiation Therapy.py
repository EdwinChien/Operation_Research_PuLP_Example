'''
This code is written by Edwin, Chien on 2020/03/12.
2.Design for Radiation Therapy[Python]
'''
# import all of the API from PuLP.
from pulp import *

# Initial Problem
prob = LpProblem(" Design for Radiation Therapy", LpMinimize)

# Initial Variables
x = LpVariable.dicts("x", [i for i in range(2)], 
	lowBound=0, upBound=None, cat="Continous")

# Initial Parameters
coff = [0.4, 0.5]

# Objective Function
prob += lpSum( [x[i] * coff[i] for i in range(2)] )

# Constraint
prob += (0.3*x[0] + 0.1*x[1]) <= 2.7
prob += (0.5*x[0] + 0.5*x[1]) == 6.0
prob += (0.6*x[0] + 0.4*x[1]) >= 6.0

# Problem Solve & Check
prob.solve()
status = prob.solve()

# Show Result
print("Operation status = {}\n".format(LpStatus[status]))
print("Optimal_value = {}\n".format(value(prob.objective)))
for i in range(2):
    print('The batches of product_{} is {}.'.format(i+1, x[i].varValue))