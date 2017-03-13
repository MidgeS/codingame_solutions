import java.util.*;
import java.io.*;
import java.math.*;


class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int W = in.nextInt(); // width of the building.
        int H = in.nextInt(); // height of the building.
        int N = in.nextInt(); // maximum number of turns before game over.
        int X0 = in.nextInt();
        int Y0 = in.nextInt();
        
        int Ymin = 0;
        int Xmin = 0;
        int Ymax = H;
        int Xmax = W;

        // game loop
        while (true) {
            String bombDir = in.next(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

            System.err.println("current: "+X0+" "+Y0);

            switch(bombDir){
            case "U":
                Ymax = Y0;
                Y0 = Y0 - (int)Math.ceil((float)(Y0-Ymin) / 2);
                break;
            case "UR":
                Ymax = Y0;
                Xmin = X0;
                Y0 = Y0 - (int)Math.ceil((float)(Y0-Ymin) / 2);
                X0 = X0 + (int)Math.ceil((float)(Xmax-X0)/2);
                break;
            case "R":
                Xmin = X0;
                X0 = X0 + (int)Math.ceil((float)(Xmax-X0)/2);
                break;
            case "DR":
                Ymin = Y0;
                Xmin = X0;
                Y0 = Y0 + (int)Math.ceil((float)(Ymax-Y0)/2);
                X0 = X0 + (int)Math.ceil((float)(Xmax-X0)/2);
                break;
            case "D":
                Ymin = Y0;
                Y0 = Y0 + (int)Math.ceil((float)(Ymax-Y0)/2);
                break;
            case "DL":
                Ymin = Y0;
                Xmax = X0;
                Y0 = Y0 + (int)Math.ceil((float)(Ymax-Y0)/2);
                X0 = X0 - (int)Math.ceil((float)(X0-Xmin) / 2);
                break;
            case "L":
                Xmax = X0;
                X0 = X0 - (int)Math.ceil((float)(X0-Xmin) / 2);
                break;
            case "UL":
                Ymax = Y0;
                Xmax = X0;
                Y0 = Y0 - (int)Math.ceil((float)(Y0-Ymin) / 2);
                X0 = X0 - (int)Math.ceil((float)(X0-Xmin) / 2);
                break;
            }
            
            System.err.println("dir: "+bombDir);
            System.err.println("new pos: "+X0+" "+Y0);

            // the location of the next window Batman should jump to.
            System.out.println(X0+" "+Y0);
        }
    }
}