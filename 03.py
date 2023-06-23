lista1 =[]
mult = 1

while True:
    lista = int(input("Digite 0 para parar, informe o número: "))
    lista1.append(lista)
    if lista == 0:
        lista1.remove(0)
        break

soma = sum(lista1)
maior = max(lista1)
menor = min(lista1)

print(f'Soma: ',soma)
print(f'Maior: ', maior)
print(f'Menor: ',menor)