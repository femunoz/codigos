import java.io.IOException;

class Ejemplo{

    public static void main(String args[]) throws IOException{

        double lado;
        lado = U.readDouble("lado cuadrado? ");
        
        double area_cuad = lado * lado;
        double r = (lado/2);
        double area_circ = Math.PI * Math.pow(r,2); //3.14159256 * r * r ;
        


        U.println("area = "+(area_cuad-area_circ));
        U.println("perimetro = "+ (4*lado+2*r*3.141592) ); 
    }

}
