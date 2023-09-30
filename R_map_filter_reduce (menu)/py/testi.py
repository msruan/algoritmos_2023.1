def buscar(lista,item): #in
    for elemento in lista:
        if item == elemento:
            return True
    return False
print(buscar([3,None,None],None))