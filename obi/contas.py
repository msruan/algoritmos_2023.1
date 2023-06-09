def main():
    saldo = int(input())
    conta_1 = int(input())
    conta_2 = int(input())
    conta_3 = int(input())
    print(quantas_contas_posso_pagar(saldo,conta_1,conta_2,conta_3))
def quantas_contas_posso_pagar(saldo,a,b,c):
    contas = (a + b + c)
    if contas <= saldo:
        return(3)
    #ab bc ac
    if saldo >= (a + b) or saldo >= (b + c) or saldo >= (a + c):
        return 2
    if saldo >= a or saldo >= b or saldo >= c:
        return(1)
    return 0
main()