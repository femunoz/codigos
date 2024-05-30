import java.io.IOException;

class Cadena{

    public static void main(String args[]) throws IOException{
        
        String s = U.readLine("Palabra o \"fin\": ");

        int largo = -1;
        int masLarga = -1;
        int orden = -1;
        int iMayor = -1;
        String sMasLargo="";
        String mayor = "";
        while (true){

            if ( s.equals("fin") ){
            //if ( s=="fin" ){
                break;
            }
            else{
                largo=s.length();
                
                if ( s.compareTo(mayor)>0 ) {
                    mayor = s;
                }
                
                if (largo>=masLarga){
                    masLarga = largo;
                    sMasLargo=s;
                }
            }

            
            s = U.readLine("Palabra o \"fin\": ");
            
        } 
        U.println("Más larga = "+sMasLargo);
        U.println("Mayor = "+mayor);
        
    }

}
