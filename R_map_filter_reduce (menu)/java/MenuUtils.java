import java.util.Scanner;
public class MenuUtils {
    public static void main(String[] args) {
        
    }
    public static int obterOpcao(String menu,int lastOption){
        Scanner input = new Scanner(System.in);
        System.out.println(menu+"\n>>> ");
        int escolha = input.nextInt(), auxiliar = 0;
        input.close();
        while(auxiliar <= lastOption){
            if(auxiliar==escolha)
                return escolha;
        }return obterOpcao(menu, lastOption);
    }
    public static void limparTela(){
        try{
            String os = System.getProperty("os.name");
            if(os.contains("win")){
                ProcessBuilder builder = new ProcessBuilder("cmd", "/c", "cls");
                builder.inheritIO().start().waitFor();
            }else{
                ProcessBuilder builder = new ProcessBuilder("cmd", "/c", "cls");
                builder.inheritIO().start().waitFor();
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    public static void limparTelaEnter(String string){
        try{
            System.out.print(string);
            Scanner input = new Scanner(System.in);
            input.nextLine();
            input.close();

            String os = System.getProperty("os.name");
            if(os.contains("win")){
                ProcessBuilder builder = new ProcessBuilder("cmd", "/c", "cls");
                builder.inheritIO().start().waitFor();
            }else{
                ProcessBuilder builder = new ProcessBuilder("cmd", "/c", "cls");
                builder.inheritIO().start().waitFor();
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
