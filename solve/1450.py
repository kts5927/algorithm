from itertools import combinations
from math import floor,ceil
import sys
N,S = map(int,input().split())
arr = list(map(int,sys.stdin.readline().split()))


arr1 = arr[:ceil(N/2)]
arr2 = arr[ceil(N/2):]

len1 = len(arr1)
len2 = len(arr2)

sub1 = []
sub2 = []

for number in range(len1 + 1):
   for sub in combinations(arr1 , number):
       sub1.append(sum(sub))
       
for number in range(len2 + 1):
    for sub in combinations(arr2,number):
        sub2.append(sum(sub))
        
     
        
        
sub1.sort(key = lambda x : x) 

ans = 0

for i in sub2:
    if i > S:
        continue
    left = 0
    right = len(sub1)
    
    while left < right:
        mid = floor((left + right)/2)
        if i + sub1[mid] > S:
            right = mid
        else : 
            left = mid+1
            
    ans += right

print(ans)