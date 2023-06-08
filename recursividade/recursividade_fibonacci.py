'https://www.mathsisfun.com/numbers/fibonacci-sequence.html'

def fibonacci(num,l,comprimento):
    lista = l
    lista.append(num)
    
    if len(lista) == 1:
        lista.append(num)

    if len(lista) == comprimento:
        return lista
    else:
        return fibonacci(lista[-1] + lista[-2],lista,comprimento)           

print(fibonacci(1,[],11))
        
