class Tipos{

    public static void main(String args[]){

        // TIPOS BASICOS:
        
        // entero: 32bits
        int i;  // crear una variable i que es de tipo entero
        i = 5;  // se asigna el valor 5 a la variable i

        System.out.println(i);

        // reales:
        float f = 5.6f;
        System.out.println(f);
        double d = 5.6;
        System.out.println(d);

        // caracter: 1 byte
        char c = 'a';
        System.out.println(c);

        boolean b = true;
        System.out.println(b);

        // OBJETOS:

        String s = "Hola";
        System.out.println(s); 

        // CONDICIONALES:

        if (i == 5)
            System.out.println(i);

        // En Java se define un BLOQUE de codigo a cada instruccion que
        // hay entre dos llaves: { }
        if (c == 'a'){
            char c2 = c;
            System.out.println(c2);
        }

        if (5<6){
            System.out.println("5 es menor que 6");
        }
        else{
            System.out.println("5 NO es menor que 6");
        }

        if (5<6){
            System.out.println("5 es menor que 6");
        }
        else if(5==6){
            System.out.println("5 es igual que 6");
        }
        else{
            System.out.println("5 NO es menor que 6");
        }

        String s2 = "Hola";

        if (s.equals(s2)){
            System.out.println("Son iguales");
        }
        else{
            System.out.println("Son distintos");
        }


        // ARREGLOS:
        int arr[] = new int[3];

        arr[0]=5;
        arr[1]=4;
        arr[2]=-1;

        System.out.println(arr[2]);

        String arrS[]= new String[9];

        i = 0;
        while (i<9){
            arrS[i]="Hola "+i;
            i+=1;
        }

        for( int j=0; j<9; j=j+1){
            System.out.println(arrS[j]);
        }
        

    }
}
