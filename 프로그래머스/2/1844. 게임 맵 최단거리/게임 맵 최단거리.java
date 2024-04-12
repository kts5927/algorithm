import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        int M = maps.length;
        int N = maps[0].length;
        
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{0, 0, 1}); // Start from (0,0) with distance 1
        
        while (!que.isEmpty()) {
            int[] location = que.poll();
            int x = location[0];
            int y = location[1];
            int dist = location[2];
            
            if (x == N - 1 && y == M - 1) {
                answer = dist;
                break; // Found the shortest path, exit the loop
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // Check if the neighbor is within bounds and not visited
                if (nx >= 0 && nx < N && ny >= 0 && ny < M && maps[ny][nx] == 1) {
                    maps[ny][nx] = 0; // Mark the cell as visited
                    que.add(new int[]{nx, ny, dist + 1});
                }
            }
        }
        
        return answer;
    }
}
