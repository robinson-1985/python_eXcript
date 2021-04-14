# resto da divisão: % exemplo: 6 / 2 = 0; 3 / 2 = 1.

'''print(3%2)
print(4%2)
print(7%3.1)

print(900%100==0)'''

num1 = float(input("Digite um número: "))
num2 =float(input("Digite outro número: "))

divisao = num1 / num2
resto = num1 % num2
print()
print(num1, "dividido por", num2, "é igual a: ", divisao)
print("o resto da divisão entre", num1, "e", num2, "é igual a:", resto)