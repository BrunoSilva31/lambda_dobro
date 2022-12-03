numeros = [num for num in range(1, 21)]

# Calcular o dobro de cada valor em números
# Utilizando map e cast para lista

numeros_dobro = list(map(lambda dobro: dobro * 2, numeros))
print(numeros)
print(numeros_dobro)
