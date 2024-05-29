import java.io.IOException;

class Ejemplo{

    public static void main(String args[]) throws IOException{

        double lado;
        lado = U.readDouble("lado cuadrado? ");
        
        double area_cuad = lado * lado;
        double r = (lado/2);
        double area_circ = 3.14159256 * r * r ;

        U.print("area = "+(area_cuad-area_circ));
        U.print("perimetro = "+ (4*lado+2*r*3.141592) ); 
    }

}
