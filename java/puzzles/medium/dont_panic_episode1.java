import java.util.*;
import java.io.*;
import java.math.*;


class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int nbFloors = in.nextInt(); // number of floors
        int width = in.nextInt(); // width of the area
        int nbRounds = in.nextInt(); // maximum number of rounds
        int exitFloor = in.nextInt(); // floor on which the exit is found
        int exitPos = in.nextInt(); // position of the exit on its floor
        int nbTotalClones = in.nextInt(); // number of generated clones
        int nbAdditionalElevators = in.nextInt(); // ignore (always zero)
        int nbElevators = in.nextInt(); // number of elevators
        
        int[] ele = new int[nbElevators];
        
        for (int i = 0; i < nbElevators; i++) {
            int elevatorFloor = in.nextInt(); // floor on which this elevator is found
            int elevatorPos = in.nextInt(); // position of the elevator on its floor
            System.err.println(elevatorFloor);
            ele[elevatorFloor] = elevatorPos;
        }

        // game loop
        while (true) {
            int cloneFloor = in.nextInt(); // floor of the leading clone
            int clonePos = in.nextInt(); // position of the leading clone on its floor
            String direction = in.next(); // direction of the leading clone: LEFT or RIGHT

            if( cloneFloor != exitFloor && cloneFloor != -1){
                int delta = clonePos - ele[cloneFloor];
                if( (delta > 0 && direction.equals("RIGHT")) ||
                    (delta < 0 && direction.equals("LEFT"))){
                    System.out.println("BLOCK");
                } else {
                    System.out.println("WAIT");   
                }
            } else {
                int delta = clonePos - exitPos;
                if( (delta > 0 && direction.equals("RIGHT")) ||
                    (delta < 0 && direction.equals("LEFT"))){
                    System.out.println("BLOCK");
                } else {
                    System.out.println("WAIT");   
                }
            }
        }
    }
}