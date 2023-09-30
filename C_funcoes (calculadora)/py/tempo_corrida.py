#Dada a distância da prova (em metros) e a velocidade média do atleta (em km/h), calcule o tempo da prova em minutos. 

def main() :
    metros = int(input('É uma corrida de quantos metros? '))
    vkmh = float(input('Quantos kms por hora? '))
    total = calculo(metros,vkmh)
    saida(total)
    
def calculo(metros,vkmh) :   
    vmm = vkmh / 3.6 * 60 #transformando em metros por minuto
    total = metros / vmm
    return total

def saida(total) :
    print(total)
 
main()