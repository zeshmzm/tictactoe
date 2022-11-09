import sys
import math
import numpy as np
lst = []

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

for i in range(3):
    line = input()
    lst.append(list(line))
lst = np.array(lst)
print("original...",lst , file=sys.stderr, flush=True)
ii_x = (lst=='X')
conidtion = [lst=='O', lst=='X', lst == '.']
choices = [1, -1, 0]
arr = np.select(conidtion, choices)
#arr = np.where(lst=='O', 1, 0)
print("x places",ii_x , file=sys.stderr, flush=True)



#Calculating the sum of rows, columns, and diagonals.
a = np.sum(arr, axis = 1)
b = np.sum(arr, axis = 0)
diag1 = np.sum(np.diag(arr))
diag2 = np.sum(np.diag(np.fliplr(arr)))
print("Debug Initia;l...",arr , file=sys.stderr, flush=True)
print("vallll...",a,b, diag1, diag2 , file=sys.stderr, flush=True)

#Using conditional statement to find whether the solution is complete or incomplete.
if 3  in np.concatenate([a,b,[diag1], [diag2]]):
    print("already won state...")
    
if 2 not in np.concatenate([a,b,[diag1], [diag2]]):
    print("false")
flag = False

if 2 in a:
    flag = True
    idx = np.nonzero(a == 2)[0][0]
    arr[idx, :] = [1,1,1]
    arr = np.where(arr==1, 'O', '.')
    arr[ii_x] = 'X'
    #pos = np.where(pos == 0, 1, 1)
    print("Debug messages...",arr , file=sys.stderr, flush=True)

elif 2 in b:
    flag = True
    idx = np.nonzero(b == 2)[0][0]
    arr[:, idx] = [1,1,1]
    arr = np.where(arr==1, 'O', '.')
    arr[ii_x] = 'X'
    #pos = np.where(pos == 0, 1, 1)
    print("Debug messages.. 2nd ...",arr , file=sys.stderr, flush=True)

elif  diag1 == 2:
    flag = True
    #idx = np.nonzero(a == 2)[0][0]
    np.fill_diagonal(arr, 1)
    #arr[:, idx] = [1,1,1]
    arr = np.where(arr==1, 'O', '.')
    arr[ii_x] = 'X'
    #pos = np.where(pos == 0, 1, 1)
    print("Debug messages.. 2nd ...",arr , file=sys.stderr, flush=True)

elif diag2 == 2:
    flag = True
    #idx = np.nonzero(a == 2)[0][0]
    temp = np.rot90(arr)
    np.fill_diagonal(temp, 1)
    arr = np.rot90(temp, k = 3)
    print("ulta pulta...",arr , file=sys.stderr, flush=True)
    #arr[:, idx] = [1,1,1]
    arr = np.where(arr==1, 'O', '.')
    arr[ii_x] = 'X'
    #pos = np.where(pos == 0, 1, 1)
    print("Debug messages.. 2nd ...",arr , file=sys.stderr, flush=True)




    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True
if flag:
    print("Final..  ...",arr , file=sys.stderr, flush=True)
    print("".join(arr[0,:].tolist()))
    print("".join(arr[1,:].tolist()))
    print("".join(arr[2,:].tolist()))

