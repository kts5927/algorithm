import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        List<Integer> ans = new ArrayList<>();
        int pointer = 0;
        int time = 0;
            
        while (pointer < progresses.length){
            
            if ((progresses[pointer] + time*speeds[pointer]) < 100){
                
                time++;
                
            }
            else{
                int count = 0;
                while ((pointer < progresses.length) && (progresses[pointer] + time*speeds[pointer]) >= 100){
                    
                    pointer++;
                    count++;
                    
                }
                ans.add(count);
                
                
            }
            
            
        }
        
        
        return ans.stream().mapToInt(i -> i).toArray();
    }
}