M = int(input())  
N = int(input())  
D = [input().split() for i in range(N)]
y = []
for i in range(M):  
    y.append([])
    for j in range(N):
        y[i].append(D[j][i])
D = [i[::-1] for i in y]
k = int(input())
D.sort(key=lambda x: x[N - k])
y = []
for i in range(N):  
    y.append([])
    for j in range(M):
        y[i].append(D[j][i])
D = y[::-1]
for i in D:  
    print(*i)
