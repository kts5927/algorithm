import java.util.*;
import java.io.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        Queue<Integer> que = new LinkedList<>();
        boolean[] visited = new boolean[n]; 
        
        
        for(int i = 0 ; i < n ; i++){
            
            if (!visited[i]){
                answer++;
                que.add(i);
                while(!que.isEmpty()){
                    int a = que.poll();
                    visited[a] = true;
                    for (int j = 0 ; j < computers[a].length ; j++){
                        if (!visited[j] && computers[a][j] == 1){
                            System.out.println(j);
                            que.add(j);
                        }
                    }
                }
            }
            
            
        }
        
        return answer;
    }
}