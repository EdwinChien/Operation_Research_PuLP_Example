'''
This code is written by Edwin, Chien on 2020/03/12.
1.Wyndor Glass Co. Problem[Python]
X1 = batches of product 1 per week
X2 = batches of product 2 per week
Profit, in 1000 of dollars
'''
# import all of the API from PuLP.
from pulp import * 

# Initial Problem
prob = LpProblem("Wyndor Glass Co. Problem", LpMaximize)

# Initial Variables
#    x1 = LpVariable("x1")
#    x2 = LpVariable("x2")
x = LpVariable.dicts("x", [i for i in range(2)], 
	lowBound=0, upBound=None, cat="'Continous")

# Initial Parameters
coff = [3000, 5000]

# Objective Function
#    prob += 3000*x1 + 5000*x2
prob += lpSum( [x[i] * coff[i] for i in range(2)] )

# Constraint
prob += x[0] <= 4
prob += 2*x[1] <= 12
prob += 3*x[0] + 2*x[1] <= 18

# Problem Solve & Check
prob.solve()
status = prob.solve()

# Show Result
print("Operation status = {}\n".format(LpStatus[status]))
print("Optimal_value = {}\n".format(value(prob.objective)))
for i in range(2):
    print('The batches of product_{} is {}.'.format(i+1, x[i].varValue))