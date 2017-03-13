import java.util.*;
import java.io.*;
import java.math.*;


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String MESSAGE = in.nextLine();

        String bitstring = "";
        String result = "";
        
        System.err.println(MESSAGE);
        
        for(int i = 0; i < MESSAGE.length(); i++){
            String temp =  Integer.toBinaryString(MESSAGE.charAt(i));
            int missing = 7 - temp.length();
            String filler = "";
            if(missing > 0){
                for(int j = 0; j < missing; j++){
                       filler += "0";
                }
            }
            bitstring += filler + temp;
        }
        
        System.err.println(bitstring);
        
        String[] sequences = bitstring.split("(?<=0)(?=1)|(?<=1)(?=0)");
        
        for(int i = 0; i < sequences.length; i++){
            if(i > 0){
                result += " ";
            }
            if(sequences[i].charAt(0) == '1'){
                result += "0 ";
            } else {
                result += "00 ";
            }
            for(int j = 0; j < sequences[i].length(); j++){
                result += "0";   
            }
        }

        System.out.println(result);
    }
}