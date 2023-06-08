'https://www.mathsisfun.com/numbers/fibonacci-sequence.html'#APF:Usar uma estrutura de pilha, para inserir os numeros.

def fibonacci(num,l):
    lista = l
    lista.append(num)
    
    if len(lista) == 1:
        lista.append(num)

    if len(lista) == 11:
        return lista
    else:
        return fibonacci(lista[-1] + lista[-2],lista)           

print(fibonacci(1,[]))
        
