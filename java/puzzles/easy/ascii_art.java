import java.util.*;
import java.io.*;
import java.math.*;

// Representing a character made out of multiple ascii characters
class Character {
    
    public String[] lines;
    
    public Character(int linecount){
        lines = new String[linecount];
    }
        
}


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int L = in.nextInt();
        int H = in.nextInt();
        in.nextLine();
        String T = in.nextLine();
        
        Character[] characters= new Character[27];
        for(int i = 0; i < 27; i++){
            characters[i] = new Character(H);   
        }
        
        for (int i = 0; i < H; i++) {
            String ROW = in.nextLine();
            
            for(int j = 0; j*L < ROW.length(); j++){
                characters[j].lines[i] = ROW.substring(j*L,(j*L)+L);
            }
        }

        String[] lines = new String[H];
        for(int i = 0; i < H; i++){
            lines[i] = "";
        }
        
        T = T.replaceAll("[^a-zA-Z]","[");
        T = T.toUpperCase();
        System.err.println(T);
  
        for(int s = 0; s < T.length(); s++){
            int k = T.charAt(s)-65;  
            System.err.println("character: "+k);
            for(int i = 0; i< H; i++){
                lines[i] += characters[k].lines[i];
            }
        }
        
        for(int i = 0; i < H; i++){
            System.out.println(lines[i]);   
        }
    }
}