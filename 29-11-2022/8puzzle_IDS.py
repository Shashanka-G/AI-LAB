def dfs(src,target,limit,visited_states):

    print(visited_states)

    if src == target:
        return True

    if limit<=0:
        return False

    visited_states.append(src)


    poss_moves = possible_moves(src,visited_states)

    for move in poss_moves:
        if dfs(move,target,limit-1,visited_states):
            return True
    return False



def possible_moves(state,visited_states):

    b = state.index(-1)

    d = []

    if b not in [2,5,8]:
        d.append('r')
    if b-3 in range(9):
        d.append('u')
    if b not in [0,3,6]:
        d.append('l')
    if b+3 in range(9):
        d.append('d')

    pos_moves = []

    for m in d:
        pos_moves.append(gen(state,m,b))

    return [move for move in pos_moves if move not in visited_states]


def gen(state,m,b):
    temp = state.copy()

    if m == 'u':
        temp[b-3],temp[b] = temp[b],temp[b-3]

    if m == 'l':
        temp[b-1],temp[b] = temp[b],temp[b-1]

    if m == 'r':
        temp[b+1],temp[b] = temp[b],temp[b+1]

    if m == 'd':
        temp[b+3],temp[b] = temp[b], temp[b+3]

    return temp


def IDdfs(src,target,depth):
    visited_states = []

    for i in range(1,depth+1):
        if dfs(src,target,i,visited_states):
            return i
    return -1


src = [1,2,3,-1,4,5,6,7,8]
target = [1,2,3,4,5,-1,6,7,8]

depth = 25

val = IDdfs(src=src,target=target,depth=depth)

if val != -1:
    print(val,True)
else:
    print(False)
    
    
    
    
D:\Shashanka G\puzzle8_IDS>python 8puzzle_IDS.py
[1, 2, 3, -1, 4, 5, 6, 7, 8]
[1, 2, 3, 4, -1, 5, 6, 7, 8]
[-1, 2, 3, 1, 4, 5, 6, 7, 8]
[1, 2, 3, 6, 4, 5, -1, 7, 8]
[1, 2, 3, -1, 4, 5, 6, 7, 8]
[1, 2, 3, 4, -1, 5, 6, 7, 8]
[1, 2, 3, 4, 5, -1, 6, 7, 8]
2 True

D:\Shashanka G\puzzle8_IDS> 
