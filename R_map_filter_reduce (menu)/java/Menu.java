import java.util.Scanner;
public class Menu{
    public static final int SAIR = 0;
    public static void main(String[] args) {
        
        String menu = StrUtils.gerarMenu("MENU", "Gerar vetor");
        int numeros[], opcao;
        do{
            opcao = MenuUtils.obterOpcao(menu,1);
            numeros = new int[3];
        }while(opcao != SAIR);
        switch(1){
        case 0:
            break;
        case 1:
            System.out.print("Digite o tamanho do vetor: ");
            Scanner input = new Scanner(System.in);
            int len = input.nextInt();
            numeros = new int[len];
            break;
        }
    }
    
}
/*1. Gerar vetor N posições, pedir valor padrão
Pedi N ao usuário e gera um vetor com todas as posições vazia (None ou undefined) ou com valor padrão se fornecido
python: vetor = [None] * N
javascript: vetor = Arrays(N)
Em seguida, use sua função mapear para preencher com o valor padrão, ou seja, transformar cada item no valor que o usuário pediu

2. Preencher vetor manualmente item a item
Pedi ao usuário sequencialmente cada dos valores (somente números)

3. Preencher vetor automaticamente
Peça ao usuário valores Mínimos e Máximos 

4. Mostrar vetor
Mostra os elementos do vetor

5. Transformar vetor: elevar a potência N
Substitui cada item por seu quadrado se expoente for 2, por exemplo

6. Contar: Positivos, Negativos e Zeros

7. Somatório: De todos, Dos Negativos e dos Positivos
Exibir as 3 informações sobre os valores

8. Exibir Média e Mediana: De Todos, Dos Positivos e Dos Negativos


9. Exibir Maior e Menor número


10. Sortear dois números: um positivo e um negativo


11. Gerar N grupos de T tamanhos. Não repetir valores


12. Pedir um novo vetor e verificar se está 100% presente nos números do sistema (e na mesma ordem)


13. Top N maiores números


14. Top N menores números


15. Listar valor médio, e listar números maiores que a Média e Menores que a Média


17. Somatório da Média dos Números Positivos múltiplos dois COM o Produto acumulado dos números negativos pares reduzidos à metade


18. Ordenar os números em ordem crescente: 
Pergunta se: todos, ou apenas pares, ou impares, ou positivos ou negativos, ou ainda apenas os múltiplos (positivos ou negativos) de N


19. Ordenar em ordem decrescente
Pergunta se: todos, ou apenas pares, ou impares, ou positivos ou negativos, ou ainda apenas os múltiplos (positivos ou negativos) de N



20. Eliminar números múltiplos de N e M (simultaneamente)


0. Sair (mensagem automática de tchau) */