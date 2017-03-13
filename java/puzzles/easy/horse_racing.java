import java.util.*;
import java.io.*;
import java.math.*;


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        
        int[] list = new int[N];
        
        for (int i = 0; i < N; i++) {
            list[i] = in.nextInt();
        }
        
        Arrays.sort(list);
        
        int diff = Integer.MAX_VALUE;
        int select = 0;
        for(int i = N-1; i > 0; i--){
            if(list[i] - list[i-1] < diff){
                select = i;
                diff = list[i] - list[i-1];
            }
        }

        System.out.println(diff);
    }
}