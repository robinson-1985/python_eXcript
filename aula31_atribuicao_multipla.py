''' Atribuição múltipla é a capacidade de atribuir valores diferentes a variáveis
distintas numa mesma instrução.

Exemplos:

a, b , c = 5, 7, 9

s1, s2 = 'curso', 'python' 

Vamos ver como funciona isto: 

a = 10
b = 5

a, b = b, a

Outro exemplo:

x, y = 2, 4 => x está para 2 e y está para 4 

Exemplo de atribuição múltipla

x, y, z = 2, 4, 8
x, y, z = x*2, x+y+z, x*y*z

x = 2*2 = 04
y = 2+4+8 = 14
z = 2*4*8 = 64'''

a, b, c = 2, 4, 8
a, b, c = a*2, a+b+c, a*b*c
print(a,b,c)

nome, sobrenome = "José", " da Silva"
print(nome + sobrenome)



