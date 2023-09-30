import java.util.ArrayList;
public class StrUtils {
    public static void main(String[] args) {
        
    }
    public static String gerarMenu(String titulo, String opcoes){
        StringBuilder menu = new StringBuilder(String.format("***** %s *******\n",titulo));
        String arr_opcoes[] = split(opcoes, ',');
        for(int i = 0; i < arr_opcoes.length; i++){
            menu.append(String.format("%c%d - %s\n",(i<10?'0':'\0'),i+1,trim(arr_opcoes[i])));
        menu.append("0 - Sair\n");
        }return menu.toString();
    }

    public static String[] split(String label, char separador){
        ArrayList<String> saida = new ArrayList<>();
        StringBuilder substring = new StringBuilder();
        for(int i = 0; i < label.length(); i++){
            if(label.charAt(i) != separador )
                substring.append(label.charAt(i));
            else if(substring.length()>0){
                saida.add(substring.toString());
                substring.setLength(0);
            }
        }if(substring.length()>0)
            saida.add(substring.toString());
        return saida.toArray(new String[saida.size()]);
    }

    public static String trim(String label){
        //StringBuilder saida = new StringBuilder(label);
        if(label == null || label.isEmpty())
            return null;
        StringBuilder saida = new StringBuilder(label);
        while (saida.charAt(0) == ' ') {
            saida.deleteCharAt(0);
        }for(int len = saida.length(); len>0; len--){
            if(saida.charAt(len-1) != ' ' || len == 0)
                return saida.toString();
            saida.deleteCharAt(len-1);
        }return saida.toString();//nunca chega aqui
    }
}













/*/*if(saida.charAt(0) == ' '){
            int i;
            boolean empty = true;
            for(i = 1; i < saida.length(); i++){
                if(saida.charAt(i) != ' '){
                    empty = false;
                    break;
                }
            }
            if(empty)
                return null;
        }  
        int len = saida.length();
        if(saida.charAt(len-1) != ' ')
            return saida.toString();
        //'PIX  '
        for(; saida.charAt(len-2) == ' '; len--)//[3]; 4 
            ;
        return saida.substring(0, len-1).toString();//[3] retorna PIX
*/ 
