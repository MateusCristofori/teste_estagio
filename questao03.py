# a) Essa alternativa é uma sequência de números ímpares. Mantendo a sequência, próximo valor seria 9.
num = int(input("a) Digite um valor: "))
values = [1, 3, 5, 7]
if num % 2 == 0:
    print(f"Preicsa ser um número ímpar.")
else:
    values.append(num)
    print(values)

# b) Nessa questão o próximo valor sempre será o dobro do valor anterior. Mantendo a sequência, o próximo valor seria 128.
num = int(input("b) Digite um valor: "))
values = [2, 4, 8, 16, 32, 64]
if num % 2 != 0:
    print("O valor passado precisa ser par.")
else:
    values.append(num*2)
    print(values)

# c) Cada valor é o quadrado do valor do seu índice. Como elevássemos o elemento do array pelo valor do seu índice. Mantendo a sequência, o próximo valor seria 49.
values = [0, 1, 4, 9, 16, 25, 36]
next_value = len(values)**2
values.append(next_value)
print(values)

# d) A lógica é elevar 2 ao índice em que o número aparece para obter o número correspondente.
values = [4, 16, 36, 64]
next_value = 2**(len(values))
values.append(next_value)
print(values)
print(next_value)

# e) A lógica é somar os dois números anteriores para obter o próximo número. Mantendo a sequência, próximo valor é 13.
values = [1, 1, 2, 3, 5, 8]
next_value = values[-1] + values[-2]
values.append(next_value)
print(values)

# f) A lógica é somar um número à soma dos dois números anteriores em cada iteração.
values = [2, 10, 12, 16, 17, 18, 19]
next_value = values[-1] + values[-2] - values[-3]
values.append(next_value)
print(values)