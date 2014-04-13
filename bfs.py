'''
    1           0 - isolated point
    ^
  /   \
 5-----2
 |     |
 |     |
 4-----3
 |
 |
 6
 
'''
k=[[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]]
print k

k[1][5]=k[5][1]=1
k[1][2]=k[2][1]=1
k[5][2]=k[2][5]=1
k[5][4]=k[4][5]=1
k[2][3]=k[3][2]=1
k[4][3]=k[3][4]=1
k[4][6]=k[6][4]=1
print k


s=set([])
def bfs(v): # v -current vertex
    global s
    s=s.union(v) # 1 -->1,2,5 --->1,2,5,3,4 --->1,2,5,3,4,6
    wave=set([])
    for j in v:#1>2;5>3;4>6
        for i in range(len(k)):
            if (k[j][i]==1) and (not i in s):
                wave.add(i)#[2;5]>[3;4]>[6]>[]
    print 'Going from', v, 'to', wave
    if len(wave)!=0:
        bfs(wave)
    print 'Leaving',v

bfs(set([1]))
print s
