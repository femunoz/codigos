import java.io.IOException;

class EntradaSalida{

    public static void main(String args[]) throws IOException{

        //U.print("no de hombres?");
        int h = U.readInt("no de hombres?");
        //U.print("no de mujeres?");
        int m = U.readInt("no de mujeres?");
        double p = 100.0*h/(h+m);
        U.print("% de hombres = "); U.println(p);
        U.print("% de mujeres = "); U.println(100-p);


       
    }

}
