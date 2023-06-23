vl = []

while True:
    num = (int(input('Digite um número: ')))
    for i in vl:
        if num in vl:
            vl.remove(i)
    vl.append(num)
    sr = str(input("Quer sair?"))
    if sr == "s":
        break
vl.sort()
print(vl)