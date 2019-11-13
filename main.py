import numpy as np
import sys # Library for INT_MAX 

N = 8
	
# A =	np.full((8,8), 9999)
A = np.zeros((8,8))

def primPrint(graph, parent): 
        print("Edge \tWeight")
        for i in range(1,N): 
            print (parent[i],"-",i,"\t",graph[i][ parent[i] ])

def lowest(key, mstSet): 
  
        min = 9999
        for n in range(N): 
            if key[n] < min and mstSet[n] == False: 
                min = key[n] 
                min_index = n 
        return min_index 



def prim(graph): 
  
        key = [9999] * N 
        parent = [None] * N 
        key[0] = 0 
        mstSet = [False] * N 
  
        parent[0] = -1
        for cout in range(N): 
            m = lowest(key, mstSet) 
            mstSet[m] = True
            for n in range(N): 
                if graph[m][n] > 0 and mstSet[n] == False and key[n] > graph[m][n]: 
                        key[n] = graph[m][n] 
                        parent[n] = m 
        primPrint(graph, parent) 

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

# for k in range(N):
#     for i in range(N):
#     	if i == k:
#     		A[i][k] = 0


# P = np.array([ 	[1, 0, 3, 0, 0, 6, 0, 8],
#                 [0, 2, 3, 4, 0, 0, 0, 8],
#                 [1, 2, 3, 0, 5, 0, 0, 8],
# 				[0, 2, 0, 4, 5, 0, 7, 8],
# 				[0, 0, 3, 4, 5, 6, 7, 0],
# 				[1, 0, 0, 0, 5, 6, 0, 8],
# 				[0, 0, 0, 4, 5, 0, 7, 0],
#                 [1, 2, 3, 4, 0, 6, 0, 8] ])


# for k in range(N):
#     for i in range(N):
#         if (i != k and A[i][k] != -1):
#             for j in range(N):
#                 if (j != k and j != i and A[k][j] != -1):
#                     temp = A[i][k] + A[k][j];
#                     if (A[i][j] == -1 or temp < A[i][j]):
#                         A[i][j] = temp;
#                         P[i][j] = P[i][k];

# print('P')
# print(P)



# print('From 6 to 7');

# i = 6
# k = 5
# res = ""

# while (True):
#     if (P[k][i] == 7):
#         res += "v" + str(k+1) + " -> ";
#         break;

#     res += "v" + str(k+1) + " -> ";
#     k = P[k][i] - 1;

# print(res+"v7") 

# g.graph = [ [0, 2, 0, 6, 0], 
#             [2, 0, 3, 8, 5], 
#             [0, 3, 0, 0, 7], 
#             [6, 8, 0, 0, 9], 
#             [0, 5, 7, 9, 0]] 
  
prim(A); 