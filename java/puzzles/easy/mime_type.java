import java.util.*;
import java.io.*;
import java.math.*;


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // Number of elements which make up the association table.
        int Q = in.nextInt(); // Number Q of file names to be analyzed.
        
        Hashtable<String, String> mimes = new Hashtable<String, String>();
        
        
        for (int i = 0; i < N; i++) {
            String EXT = in.next(); // file extension
            String MT = in.next(); // MIME type.
            mimes.put(EXT.toLowerCase(),MT);
        }
        
        in.nextLine();
        for (int i = 0; i < Q; i++) {
            String FNAME = in.nextLine(); // One file name per line.
            
            int extpos = FNAME.lastIndexOf(".");
            if(extpos >= 0){
                String ext = FNAME.substring(extpos+1,FNAME.length()).toLowerCase();
                System.err.println("mime: "+ext);
                if(mimes.containsKey(ext)){
                    System.out.println(mimes.get(ext));
                } else {
                    System.err.println("not in hashtable");
                    System.out.println("UNKNOWN");
                }
            } else {
                System.err.println("no index");
                System.out.println("UNKNOWN");
            }
        }

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
        // For each of the Q filenames, display on a line the corresponding MIME type.
        // If there is no corresponding type, then display UNKNOWN.
    }
}