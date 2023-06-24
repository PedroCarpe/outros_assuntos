def expressao_numerica(string,cont):
    #inicial = string

    if cont >= 2:
        return 1
    
    if string.find('*') != -1:
        contador = cont+1
        posicao = string.find('*')    
        if contador==1:
            calculo = int(string[posicao-1])
        elif contador==2:
            calculo = int(string[posicao+1])

        return expressao_numerica(string,contador)*calculo     
        
     
print(expressao_numerica('5*2',0))
