import java.util.*;
import java.io.*;
import java.math.*;

class ActiveCell{
    
    public int posx;
    public int posy;
       
}


class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int width = in.nextInt(); // the number of cells on the X axis
        int height = in.nextInt(); // the number of cells on the Y axis
        in.nextLine();
        
        System.err.println("height: "+height+" width: "+width);
        
        char[][] field = new char[width][height];
        ArrayList<ActiveCell> active = new ArrayList<ActiveCell>();
        
        for (int i = 0; i < height; i++) {
            String line = in.nextLine(); // width characters, each either 0 or .
            for(int j = 0; j < width; j++){
                System.err.println(i+" "+j);
                field[j][i] = line.charAt(j);
                if(field[j][i] == '0'){
                    ActiveCell tmp = new ActiveCell();
                    tmp.posx = j;
                    tmp.posy = i;
                    active.add(tmp);
                }
            }
        }
        
        for(ActiveCell cell: active){
            System.err.println("pos: "+cell.posx+" "+cell.posy);
            int nextX = -1;
            int nextY = -1;
            for(int i = cell.posx+1; i < width; i++){
                if(field[i][cell.posy] == '0'){
                    nextX = i;
                    break;
                }
            }
            for(int i = cell.posy+1; i < height; i++){
                if(field[cell.posx][i] == '0'){
                    nextY = i;
                    break;
                }
            }
            String result = cell.posx+" "+cell.posy+" ";
            if(nextX > -1){
                result += nextX+" "+cell.posy+" ";   
            } else {
                result += "-1 -1 ";
            }
            if(nextY > -1){
                result += cell.posx+" "+nextY+" ";   
            } else {
                result += "-1 -1 ";
            }
            System.out.println(result);
        }
        // Three coordinates: a node, its right neighbor, its bottom neighbor
    }
}