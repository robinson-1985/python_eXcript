# range ([start], stop[, step])

list(range(10))
list(range(1, 15))
list(range(0, 100, 10))
list(range(0, 100, 3))
list(range(100, 0, -3))
list(range(-100, 0, 3))

print(list(range(10)))
print(list(range(1, 15)))
print(list(range(0, 100, 10)))
print(list(range(0, 100, 3)))
print(list(range(100, 0, -3)))
print(list(range(-100, 0, 3)))


# agor veremos range com for

for i in range(10): #aqui queremos que o programa vai do 1 até o zero.
    print(i)

# a forma abaixo é a melhor para trabalhar a função range com for. 
for i in range(-10, 0, 1): # aqui queremos que o -10 chegue a zero indo de 1 em 1.
    print(i)
