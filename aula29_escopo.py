'''Lembrando que o programa abaixo é só um exemplo de função!
não conseguimos acessar as var do bloco 2, 3 e 4 pelo nível 1. Somente o 
contrário.
Cada bloco de instruções só consegue acessar o que for parte do seu escopo, ou o 
escopo universal que é o 1.
O bloco 1 ou escopo 1 é a parte universal do programa, ele interage com todos 
os outros blocos. '''

# bloco 1 - escopo 1.
a = 1
b = 2

# bloco 2 - escopo 2: aqui pode acessar todas as funções que estão no bloco 1
def soma_num(var1, var2):
    s = var1 + var2
    return s 
# bloco 3 - escopo 3: aqui tb o escopo pode ser chamado
def imprime(x_vezes):
    for i in range(x_vezes):
        print(i) # bloco 4 - escopo 4: aqui será printada as inf. q foram chamadas.

print(soma_num(a, b))
imprime(5)