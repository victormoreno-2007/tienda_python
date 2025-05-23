def contar(num):
    contador =0
    while num > 0:
        contador +=1
        num = num // 10
    return contador


numeros = (input('digite el numero deseado '))
print(f'el numero  esta conformado por {contar(int(numeros))} numeros')
pares = 0
impares = 0
suma = 0
digitos = []

for digito in numeros:
    if digito.isdigit():
        valor = int(digito)

        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1

        suma += valor

        digitos.append(str(valor))

operacion = ' + '.join(digitos)

print(f'{operacion} = {suma}')
print(f'cantidad de numeros pares es: {pares}')
print(f'cantidad de numeros impares es: {impares}')
