import java.util.*;
import java.io.*;
import java.math.*;

class Node {
    public int number;
    public boolean exit = false;
    public ArrayList<Integer> connections;

    public Node(int num){
        number = num;
        connections = new ArrayList<Integer>();
    }
}


class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // the total number of nodes in the level, including the gateways
        int L = in.nextInt(); // the number of links
        int E = in.nextInt(); // the number of exit gateways
        
        Node[] nodes = new Node[N];
        for(int i = 0; i < N; i++){
            nodes[i] = new Node(i);   
        }
        for (int i = 0; i < L; i++) {
            int N1 = in.nextInt(); // N1 and N2 defines a link between these nodes
            int N2 = in.nextInt();
            nodes[N1].connections.add(N2);
            nodes[N2].connections.add(N1);
        }
        
        ArrayList<Node> exits = new ArrayList<Node>();
        for (int i = 0; i < E; i++) {
            int EI = in.nextInt(); // the index of a gateway node
            nodes[EI].exit = true;
            exits.add(nodes[EI]);
        }

        // game loop
        while (true) {
            int SI = in.nextInt(); // The index of the node on which the Skynet agent is positioned this turn
            
            String cut = "";
            for(Integer con: nodes[SI].connections){
                if(nodes[con].exit == true){
                    System.err.println("cut connection: "+SI+" "+con);
                    cut = SI+" "+con;
                    nodes[SI].connections.remove(Integer.valueOf(con));
                    nodes[con].connections.remove(Integer.valueOf(SI));
                    if(nodes[con].connections.size() == 0){
                        exits.remove(nodes[con]);   
                    }
                    break;
                }
            }
            
            if(cut.equals("")){
                System.err.println("cutting breath");
                int con = exits.get(0).connections.get(0);
                cut = exits.get(0).number+" "+con;
                nodes[SI].connections.remove(Integer.valueOf(con));
                exits.get(0).connections.remove(Integer.valueOf(exits.get(0).number));
                if(exits.get(0).connections.size() == 0){
                    exits.remove(0);   
                }
            }
            // Example: 0 1 are the indices of the nodes you wish to sever the link between
            System.out.println(cut);
        }
    }
}