import java.io.IOException;

class ES{

    public static void main(String args[]) throws IOException{
        U.print("no de hombres?");
        int h = U.readInt();
        U.print("no de mujeres?");
        int m = U.readInt();
        double p = 100.0*h/(h+m);
        U.print("% de hombres = "); 
        U.println(p);
        U.print("% de mujeres = "); 
        U.println(100-p);

    }
}