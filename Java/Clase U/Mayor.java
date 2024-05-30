import java.io.IOException;

class Mayor{

    public static void main(String args[]) throws IOException{
        
        int n1 = enteroAlAzar();
        int n2 = enteroAlAzar();
        int n3 = enteroAlAzar();
        
        U.println(n1+" "+n2 + " " + n3+ " mayor:"+mayor(n1,n2,n3));
    }

    //
    // FUNCIONES AUXILIARES: nos ayudan a resolver un problema colaborando entre sí
    // BUENA PRÁCTICA: REUTILIZACIÓN
    //

    // enteroAlAzar: null -> int
    public static int enteroAlAzar(){
        double r = Math.random();

        double entre1y100= (100-1)*r+1;
        //U.println((int)entre1y100);

        return (int)entre1y100;
    }

    // mayor: int int int -> int
    // entrega el mayor entre los enteros n1,
    // n2 y n3
    // ej: mayor(2,4,8) entrega 8.
    public static int mayor(int n1, int n2, int n3){
        int mayor = n1;
        if (n2>=n1)
            mayor = n2;
        if (n3 >= mayor)
            mayor = n3;
        return mayor;
    }
}
