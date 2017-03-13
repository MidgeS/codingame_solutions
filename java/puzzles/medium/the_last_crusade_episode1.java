import java.util.*;
import java.io.*;
import java.math.*;

enum Direction{
    Left,
    Right,
    Up,
    Down,
    None
}

class Room{
 
    int type;

    public Room(int type){
        this.type = type;
    }

    public Direction predict(String entry){
        Direction dir = Direction.None;
        switch(type){
        case 0: 
            break;
        case 1: 
            dir = Direction.Down;
            break;
        case 2: 
            if(entry.equals("LEFT")){
                dir = Direction.Right;
            } else {
                dir = Direction.Left;
            }
            break;
        case 3:
            dir = Direction.Down;
            break;
        case 4:
            if(entry.equals("TOP")){
                dir = Direction.Left;
            } else {
                dir = Direction.Down;
            }
            break;
        case 5:
            if(entry.equals("LEFT")){
                dir = Direction.Down;
            } else {
                dir = Direction.Right;
            }
            break;
        case 6:
            if(entry.equals("TOP")){
                dir = Direction.None;
            }
            if(entry.equals("LEFT")){
                dir = Direction.Right;
            }
            if(entry.equals("RIGHT")){
                dir = Direction.Left;
            }
            break;
        case 7:
        case 8:
        case 9:
            dir = Direction.Down;
            break;
        case 10:
            if(entry.equals("LEFT")){
                dir = Direction.None;
            } else {
                dir = Direction.Left;
            }
            break;
        case 11:
            if(entry.equals("RIGHT")){
                dir = Direction.None;
            } else {
                dir = Direction.Right;
            }
            break;
        case 12:
        case 13:
            dir = Direction.Down;
            break;
        default:
            dir = Direction.None;
        }
        
        return dir;
    }
}



class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int W = in.nextInt(); // number of columns.
        int H = in.nextInt(); // number of rows.
        in.nextLine();
        
        Room[][] rooms = new Room[W][H];
        
        for (int i = 0; i < H; i++) {
            String LINE = in.nextLine(); // represents a line in the grid and contains W integers. Each integer represents one room of a given type.
            
            String[] parts = LINE.split(" ");
            
            for(int j=0; j < parts.length; j++){
                rooms[j][i] = new Room( Integer.parseInt(parts[j]) );    
            }
            
            
        }
        int EX = in.nextInt(); // the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

        // game loop
        while (true) {
            int XI = in.nextInt();
            int YI = in.nextInt();
            String POS = in.next();

            Direction dir = rooms[XI][YI].predict(POS);
            
            int newX = XI;
            int newY = YI;
            
            switch(dir){
            case Left:
                newX--;
                break;
            case Right:
                newX++;
                break;
            case Down:
                newY++;
                break;
            case Up:
                newY--;
                break;
            default:
                break;
            }

            // One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
            System.out.println(newX+" "+newY);
        }
    }
}