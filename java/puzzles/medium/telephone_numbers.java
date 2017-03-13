import java.util.*;
import java.io.*;
import java.math.*;

class Node{

Hashtable<Integer,Node> childs;

public Node(){
    childs = new Hashtable<Integer,Node>();
}

public int countNodes(){
    int count = 1;
    Set<Integer> keys = childs.keySet();
    for(int key: keys){
        count += childs.get(key).countNodes();
    }
    return count;
}

public Node addNode(int number){
    if(childs.containsKey(number)){
        return childs.get(number);
    } else {
        Node tmp = new Node();
        childs.put(number,tmp);
        return tmp;
    }
}
   
}


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        
        Hashtable<Integer,Node> roots = new Hashtable<Integer,Node>();
        
        for (int i = 0; i < N; i++) {
            String telephone = in.next();
            Node lastNode = new Node();
            for(int j=0; j< telephone.length(); j++){
                int number = Integer.parseInt(telephone.substring(j,j+1));
                if(j==0){
                    if(roots.containsKey(number)){
                        lastNode = roots.get(number);
                    } else {
                        lastNode = new Node();
                        roots.put(number,lastNode);
                    }
                } else {
                    lastNode = lastNode.addNode(number);
                }
            }
        }

        int count = 0;
        Set<Integer> keys = roots.keySet();
        for(int key: keys){
            count += roots.get(key).countNodes();
        }

        // The number of elements (referencing a number) stored in the structure.
        System.out.println(count);
    }
}