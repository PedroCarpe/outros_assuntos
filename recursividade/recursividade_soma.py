#APF: resolver o problema, quando o valor passado para a função é negativo, pois, a função 'isnumeric()' retorna False.
#Já que, eu quero somar, valores positivos e negativos

def soma_recursiva(valor):
    #soma = valor
    
    if valor == '=':
        return 0
    
    #soma = soma+valor
    
    valor_ = input('Informe um valor para a soma: ')
    
    if valor_.isnumeric() == True:
        valor_ = int(valor_)
    return soma_recursiva(valor_) + valor

print(soma_recursiva(0))