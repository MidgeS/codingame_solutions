import java.util.*;
import java.io.*;
import java.math.*;


class Defibrillator{
 
    public int number;
    public String address;
    public String phone;

    private String name;
    private float longitude;
    private float latitude;

    public Defibrillator(String name, Float longitude, Float latitude){
        this.name = name;
        this.longitude = longitude;
        this.latitude = latitude;
    }

    public float getLongitude(){
        return longitude;
    }

    public float getLatitude(){
        return latitude;
    }

    public String getName(){
        return name;
    }
    
}


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String LON = in.next();
        String LAT = in.next();
        int N = in.nextInt();
        in.nextLine();
        
        Defibrillator[] defis = new Defibrillator[N];

        float userLongitude = Float.parseFloat( LON.replace(",","."));
        float userLatitude = Float.parseFloat( LAT.replace(",",".")); 
        
        for (int i = 0; i < N; i++) {
            String DEFIB = in.nextLine();
            
            String[] parts = DEFIB.split(";");

            float longitude = Float.parseFloat(parts[4].replace(",","."));
            float latitude = Float.parseFloat(parts[5].replace(",","."));

            Defibrillator def = new Defibrillator(parts[1],longitude,latitude );
            def.number = Integer.parseInt(parts[0]);
            def.address = parts[2];
            def.phone = parts[3];
            
            defis[i] = def;
        }
        
        int closest = 0;
        float dist = Float.MAX_VALUE;
        
        for(int i = 0; i < N; i++){
            float x = (defis[i].getLongitude() - userLongitude) * (float)Math.cos( (userLongitude + defis[i].getLongitude()) / 2);
            float y = defis[i].getLatitude() - userLatitude;
            float d = (float)Math.sqrt( x*x + y*y ) * 6371;
            
            if(d < dist){
                closest = i;
                dist = d;
            }
        }

        System.out.println(defis[closest].getName());
    }
}