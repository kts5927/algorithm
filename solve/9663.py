number = int(input())
pos = [0]*number
flag_a = [False]*number
flag_b = [False]*(2*number-1)
flag_c = [False]*(2*number-1)
cnt = 0
def set(i: int)->None:
    for j in range(number):
        if( not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+number-1]):
            pos[i] =j
            if i==number-1:
                global cnt
                cnt+=1
            else:
                flag_a[j]=flag_b[i+j] = flag_c[i-j+number-1] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+number-1] = False
set(0)

print(cnt)