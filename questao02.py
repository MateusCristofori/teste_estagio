num = int(input("Informe um número: "))

# dois valores iniciais da sequência
a: int = 0
b: int = 1

# o valor e A e B na iteração sempre recebem os valores anteriores de A e B.
while b < num:
    a = b
    b = a+b
if b == num:
    print(f"O número {num} não pertence a sequência de fibonacci")
else:
    print(f"O número {num} percente a sequência de fibonacci")