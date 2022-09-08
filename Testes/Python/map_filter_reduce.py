#Importando função reduce 

from functools import reduce

#Entrada:

lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1-0.1)

# 1. Dada uma lista com n valores, aplicar a função de desconto usando map() | Saída: [90.0, 224.01000000000002, 79.2, 112.41000000000001]

print("#MAP: Os valores com desconto aplicado são:")
lista_desconto = map(lambda x: desconto(x), lista)
print(list(lista_desconto))


# 2. Retornar os valores maiores que 100, usando filter() | Saída: [248.9, 124.9]

print("#Filter: Os valores maiores que 100 são:")
valores_maior100 = filter(lambda x: x > 100, lista)
print(list(valores_maior100))


# 3. Somar todos os valores da lista usando reduce() | Saída: 561.8

print("#Reduce: O valor da soma de todos os valores da lista é:")
soma_valores = reduce(lambda x, y: x+y, lista)
print(soma_valores)