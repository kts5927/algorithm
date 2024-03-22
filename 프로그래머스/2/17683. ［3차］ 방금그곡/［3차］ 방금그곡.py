import re
def change_minute(s_time, e_time):
    s_h, s_m = s_time.split(":")
    e_h, e_m = e_time.split(":")
    
    s_time = int(s_h) * 60 + int(s_m)
    e_time = int(e_h) * 60 + int(e_m)
    
    return e_time - s_time
    
def match(text1, text2, during_time):
    def process(text, during_time=None):
        result_text = []
        for t in text:
            if t == "#":
                result_text[-1] = result_text[-1] + "#"
            else:
                result_text.append(t)
        
        if during_time:
            for i in range(during_time - len(result_text)):
                result_text.append(result_text[i])
            
            result_text = result_text[:during_time]
        
        return result_text
    text1 = process(text1)
    text2 = process(text2, during_time)
    
    count = 0
    idx = 0
    while idx < len(text2):
        if text2[idx] == text1[count]:
            count += 1
            idx +=1
        else:
            if text2[idx] != text1[0]:
                idx +=1
            count = 0
        if count == len(text1):
            return True
    if count == len(text1):
        return True
        
    return False
    
    
def solution(m, musicinfos):
    answer = "(None)"
    max_during = 0
    for musicinfo in musicinfos:
        start_time, end_time, title, pitch = musicinfo.split(",")
        during_time = change_minute(start_time, end_time)
        
        if match(m, pitch, during_time) and max_during < during_time:
            answer = title
            max_during = during_time
           
        
    return answer