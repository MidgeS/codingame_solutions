import java.util.*;
import java.io.*;
import java.math.*;


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        in.nextLine();
        String temps = in.nextLine(); // the n temperatures expressed as integers ranging from -273 to 5526
        
        System.err.println(temps);
        
        if(temps.length() > 0){
            String[] parts = temps.split(" ");
            
            int temp = Integer.MAX_VALUE;
            int tmp = 0;
            
            for(int i = 0; i < parts.length; i++){
                 tmp = Integer.parseInt(parts[i]);
                 
                 if(Math.abs(tmp) < Math.abs(temp)){
                     temp = tmp;
                 } else {
                    if(Math.abs(tmp) == Math.abs(temp) && temp < tmp){
                           temp = tmp;
                    }
                 }
            }
            
            System.out.println(temp);
        } else {
            System.out.println(0);
        }
    }
}