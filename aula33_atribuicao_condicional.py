''' Atribuição condicional é uma estrutura utilizada para simplificar o código,
onde o valor a ser atrbuído será aquele que satisfazer a condição.

<variável> = <valor1> if (True) else <valor2>
    
       var = 10 if (True) else 20

x = 10
texto = 'sim' if x == 10 else 'não'
print(texto)

x = 9
texto = 'sim' if x == 10 else 'não'
print(texto)'''

###################### PROGRAMA 1 ###############

num1 = int(input("Digite um número:"))
s = 'par' if num1 %2 == 0 else 'ímpar'
print('O número digitado é: ', s)


