class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
      self.items.insert(0,item)
          
  def __str__(self):
    return f'{self.items}'

#----------------------------
pilha_ = Stack()

def conversao_dec_bin(numero,pilha):
    if numero < 1:
        return pilha.__str__()
    
    resto = numero % 2
    pilha.push(resto)
    numero = numero//2
    
    return conversao_dec_bin(numero,pilha)

print(conversao_dec_bin(515,pilha_))