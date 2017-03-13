import java.util.*;
import java.io.*;
import java.math.*;


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int C = in.nextInt();
        
        int[] budgets = new int[N];
        int sum = 0;
        
        for (int i = 0; i < N; i++) {
            int B = in.nextInt();
            budgets[i] = B;
            sum += B;
        }
        
        if(C > sum){
            System.out.println("IMPOSSIBLE");
        } else {
            Arrays.sort(budgets);
            solve(budgets,C);
        }
    }
    
    public static void solve(int[] budgets,int sum){
        int each = sum / budgets.length;
        int rest = budgets.length-1;
        if(budgets[0] >= each){
            sum -= each;
            System.out.println(each);
        } else {
            sum -= budgets[0];
            System.out.println(budgets[0]);
        }
        if(budgets.length > 1){
            solve(Arrays.copyOfRange(budgets,1,budgets.length),sum);   
        }
    }
}