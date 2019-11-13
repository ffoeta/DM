import numpy as np

# A = np.zeros((8,8))
A =   np.full((8,8), 9999)

A[0][2] = 32
A[2][0] = 32

A[1][3] = 28
A[3][1] = 28

A[3][6] = 16
A[6][3] = 16

A[0][5] = 29
A[5][0] = 29

A[1][7] = 17
A[7][1] = 17

A[3][7] = 20
A[7][3] = 20

A[0][5] = 33
A[5][0] = 33

A[2][4] = 23
A[4][2] = 23

A[4][5] = 26
A[5][4] = 26

A[0][7] = 5
A[7][0] = 5

A[2][7] = 13
A[7][2] = 13

A[4][6] = 18
A[6][4] = 18

A[1][2] = 3
A[2][1] = 3

A[3][4] = 8
A[4][3] = 8

A[5][7] = 15
A[7][5] = 15


costs = A[5]
processed = []
parents = [-1 if costs[x] == 9999 else 0 for x in range(len(costs))]


def lowest(costs_arr):
    lowest_cost = 9999
    lowest_cost_node = None
    for i in range(len(costs_arr)):
        cost = costs[i]
        if cost < lowest_cost and i not in processed:
            lowest_cost = cost
            lowest_cost_node = i
    return lowest_cost_node

curr_node = lowest(costs)

while curr_node != None:
    cost = costs[curr_node]
    neighbors = A[curr_node]
    for i in range(len(neighbors)):
        if neighbors[i] == 9999:
            continue
        new_cost = neighbors[i] + cost
        if costs[i] > new_cost:
            costs[i] = new_cost
            parents[i] = curr_node
    processed.append(curr_node)
    curr_node = lowest(costs)


def printWay(curr):
    if (curr - 1 == 0):
        return "6"
    return printWay(parents[curr - 1] + 1) + " -> " + str(curr)

print(printWay(7))
print(costs[3])