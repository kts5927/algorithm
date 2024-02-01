N = int(input())

lecture = [list(map(int,input().split())) for _ in range(N)]
lecture.sort(key = lambda x:(x[2],x[1]))


for i in lecture: