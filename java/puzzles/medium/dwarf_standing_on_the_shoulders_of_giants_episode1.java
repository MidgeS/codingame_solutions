import java.util.*;
import java.io.*;
import java.math.*;

class Person{

    int number;
    boolean checked = false;
    int count = 0;
    ArrayList<Person> influenced = new ArrayList<Person>();
    
    public Person(int number){
        this.number = number;   
    }
  
}


class Solution {
    
    public Hashtable<Integer,Person> persons = new Hashtable<Integer,Person>();
    
    public void calculate(){
       Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of relationships of influence
        
        for (int i = 0; i < n; i++) {
            int x = in.nextInt(); // a relationship of influence between two people (x influences y)
            int y = in.nextInt();
            
            if(!persons.containsKey(x))
                persons.put(x,new Person(x));
            if(!persons.containsKey(y))
                persons.put(y,new Person(y));
                
            persons.get(Integer.valueOf(x)).influenced.add(persons.get(Integer.valueOf(y)));
            System.err.println(x+" "+y);
        }

        int maxCount = 0;
        Set<Integer> keys = persons.keySet();
        for(int key: keys){
            System.err.println("start: "+key);
            int count = 1+count(persons.get(Integer.valueOf(key)));
            System.err.println("Count: "+count);
            if(count > maxCount)
                maxCount = count;
        }

        // The number of people involved in the longest succession of influences
        System.out.println(maxCount);        
    }
    
    public int count(Person p){
        p.checked = true;
        int count = 0;
        int tmp = 0;
        for(Person pp: p.influenced){
            if(pp != null){
                if(pp.checked == true){
                    tmp = 1+pp.count;
                } else {
                    tmp = 1+count(pp);
                }
                if(tmp > count)
                    count = tmp;
            }
            System.err.println(count);
        }
        p.count = count;
        return p.count;
    }

    public static void main(String args[]) {
        Solution sol = new Solution();
        sol.calculate();
    }
}