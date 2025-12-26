n = int(input())

meetings = []

for _ in range(n):
    a,b=map(int,input().split())
    meetings.append((a,b))

meetings.sort(key = lambda x: (x[1],x[0]))

count=0
last_end=0

for start, end in meetings:
    if start>= last_end:
        count+=1
        last_end=end
print(count)
