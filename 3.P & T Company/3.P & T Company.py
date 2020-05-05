'''
This code is written by Edwin, Chien on 2020/03/12.
3.P & T Company[Python]
'''
# import all of the API from PuLP.
from pulp import *

# Initial Problem
prob = LpProblem("P & T Company(Transportation problem)", LpMinimize)

# Initial Parameters
demand = [80, 65, 70, 85]
cost = [464,513,654,867,
        352,416,690,791,
        995,682,388,685]
Avail = [75,125,100]

# Initial Variables => x_CW, C = 3, W = 4
all_loc = []
for C in range(len(Avail)):
    for W in range(len(demand)):
        all_loc.append(str(C+1)+str(W+1))

x = LpVariable.dicts("x", [loc for loc in all_loc], lowBound=0)

# Objective Function
prob += lpSum( [x[i] * cost[all_loc.index(i)] for i in all_loc] )

# Constraint
#     For demand
for _ in range(len(demand)):
    prob += lpSum( [x[i] for i in all_loc if i[1]==str(_+1)] ) == demand[_]
#     For avail
for _ in range(len(Avail)):
    prob += lpSum( [x[i] for i in all_loc if i[0]==str(_+1)] ) == Avail[_]

# Problem Solve & Check
prob.solve()
status = prob.solve()

# Show Result
print("Operation status = {}\n".format(LpStatus[status]))
print("Optimal_value = {}\n".format(value(prob.objective)))
for i in all_loc:
    print('The value of {} is {}.'.format(x[i], x[i].varValue))