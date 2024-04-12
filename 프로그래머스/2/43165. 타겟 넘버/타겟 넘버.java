import java.util.ArrayList;
import java.util.List;

class Solution {
    static int dfs(int i, int numb, int[] numbers, int target) {
        List<Integer> lst = new ArrayList<>();
        lst.add(numb);

        if (i == numbers.length - 1) {
            int sum = 0;
            for (int val : lst) {
                sum += val;
            }
            return (sum == target) ? 1 : 0;
        }

        int cal1 = dfs(i + 1, numb + numbers[i + 1], numbers, target);
        int cal2 = dfs(i + 1, numb - numbers[i + 1], numbers, target);

        return cal1 + cal2;
    }

    public int solution(int[] numbers, int target) {
        int answer = dfs(0, numbers[0], numbers, target) + dfs(0, -numbers[0], numbers, target);
        return answer;
    }
}
