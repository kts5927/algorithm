import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        
        int len = commands.length;
        int[] answer = new int[len];
        
        for(int i = 0; i < len; i++){
            
            int[] lst = new int[commands[i][1]-commands[i][0]+1];
            int k = 0;
            
            for(int j = commands[i][0] - 1; j < commands[i][1] ; j++){
                lst[k] = array[j];
                k++;
            }
            Arrays.sort(lst);
            answer[i] = lst[commands[i][2] - 1];
        }
        
        return answer;
    }
}