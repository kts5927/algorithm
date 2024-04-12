class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        int cal = 0;
        String[] arr = s.split(""); 
        for (int i = 0; i < arr.length;i++){
            
            if(arr[i].equals("(")){
                cal++;
            }
            else{
                if(cal > 0){
                cal--;
                }
                else{
                return false;
                }
            }
        }
        if(cal == 0){
        return answer;
        }else{
            return false;
        }
    }
}