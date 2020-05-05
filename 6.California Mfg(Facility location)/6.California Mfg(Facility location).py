'''
This code is written by Edwin, Chien on 2020/03/14.
6.California Mfg(Facility location)[Python]
'''
# import all of the API from PuLP.
from pulp import *

# Initial Problem
prob = LpProblem("California Mfg(Facility location)", LpMaximize)

# Initial Parameters
NPV  = [9, 5, 6, 4]
cost = [6, 3, 5, 2]
CapitalAvail = 10

# Initial Variable
x_1 = LpVariable("x_1", lowBound=0, upBound=1, cat='Binary')
x_2 = LpVariable("x_2", lowBound=0, upBound=1, cat='Binary')
#    Hint : x_1 >= x_3, x_2 >= x_4
x_3 = LpVariable("x_3", lowBound=0, upBound=x_1)
x_4 = LpVariable("x_4", lowBound=0, upBound=x_2)
#    Collect all of the variables
V_list = [x_1, x_2, x_3, x_4]

# Objective Function
MAX = 0
for i in range(len(V_list)):
    MAX += V_list[i]*NPV[i]
prob += MAX

# Constraint
constraint = 0
for i in range(len(V_list)):
    constraint += V_list[i]*cost[i]
prob += constraint <= CapitalAvail
prob += x_3 + x_4 <= 1

# Problem Solve & Check
prob.solve()
status = prob.solve()

# Show Result
print("Operation status = {}\n".format(LpStatus[status]))
print("Optimal_value = {}\n".format(value(prob.objective)))
for i in V_list:
    result = "{} = {:0.0f}".format(i, i.varValue)
    print(result)