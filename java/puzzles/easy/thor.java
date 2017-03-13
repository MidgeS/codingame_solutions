import java.util.*;
import java.io.*;
import java.math.*;


class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position
        
        int moveX = lightX - initialTX;
        int moveY = lightY - initialTY;

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.
            
            String dir = "";
            
            if(moveY > 0){
                dir += "S";
                moveY--;
            }
            if(moveY < 0){
                dir += "N";
                moveY++;
            }
            
            if(moveX > 0){ 
                dir += "E";
                moveX--;
            }
            if(moveX < 0){
                dir += "W";
                moveX++;
            }

            // A single line providing the move to be made: N NE E SE S SW W or NW
            System.out.println(dir);
        }
    }
}