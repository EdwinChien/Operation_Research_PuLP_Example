'''
This code is written by Edwin, Chien on 2020/03/14.
7.Distribution Unlimited(Min_cost_flow)[Python]
Minimum Cost Network Flow model.
'''
# import all of the API from PuLP.
from pulp import *

# Initial Problem
prob = LpProblem("Distribution_Unlimited(Min_cost_flow)", LpMinimize)

# Initial Parameters
Node = ["A","B","C","D","E"]
SUPPLY = [50, 40, 0, -30, -60]
COST = [2, 4, 9, 3, 1, 3, 2]

# Initial Variable
x_AB = LpVariable("x_AB", lowBound=0, upBound=10)
x_CE = LpVariable("x_CE", lowBound=0, upBound=80)
x_AC = LpVariable("x_AC", lowBound=0)
x_AD = LpVariable("x_AD", lowBound=0)
x_BC = LpVariable("x_BC", lowBound=0)
x_DE = LpVariable("x_DE", lowBound=0)
x_ED = LpVariable("x_ED", lowBound=0)
#    Collect all of the variables
V_list = [x_AB, x_AC, x_AD, x_BC, x_CE, x_DE, x_ED]

# Objective Function
total_cost = 0
for i in range (len(V_list)):
    total_cost += V_list[i]*COST[i]
prob+=total_cost

# Constraint
for i in range (len(SUPPLY)):
    init_1 = 0
    init_2 = 0
    for j in V_list:
        if str(j)[2] == Node[i]:
            init_1+=j
    for k in V_list:
        if str(k)[3] == Node[i]:
            init_2+=k
    prob += SUPPLY[i] + init_2 >= init_1

# Problem Solve & Check
prob.solve()
status = prob.solve()

# Show Result
print("Operation status = {}\n".format(LpStatus[status]))
print("Optimal_value = {}\n".format(value(prob.objective)))
for i in V_list:
    result = "{} = {:0.0f}".format(i, i.varValue)
    print(result)