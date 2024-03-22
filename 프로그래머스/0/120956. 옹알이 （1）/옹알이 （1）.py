def solution(babbling):
    ans = 0
    for i in babbling:
        talk = list(i)
        spell = [1,1,1,1]
        tr = True
        while len(talk) > 0:
            print(talk)
            
            if talk[:3] == ['a' , 'y' , 'a'] and spell[0] == 1:
                spell[0] =0
                
                talk = talk[3:]
                
            elif talk[:2] == ['y' , 'e'] and spell[1] == 1:

                spell[1] =0
                
                talk = talk[2:]
            elif talk[:3] == ['w','o','o'] and spell[2] == 1:

                spell[2] =0
                
                talk = talk[3:]
            elif talk[:2] == ['m','a'] and spell[3] == 1:

                spell[3] =0
                
                talk = talk[2:]

                
            else :
                tr = False
                break
        if tr:
            ans +=1
    return ans