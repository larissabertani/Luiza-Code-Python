
# class Doguinhos:
#     raca = 'shitzu'
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self. idade = idade

# cachorro1 = Doguinhos('Noobinho', '10')
# cachorro2 = Doguinhos('Lulucrey', '2')

# print(cachorro1.nome)
# print(cachorro2.idade)


class Netflix:
    def __init__(self, nome, genero, temporadas):
        self.nome = nome
        self.genero = genero
        self.temporadas = temporadas
    
    def obter_temporadas_serie(self):
        return f"A série {self.nome} possui {self.temporadas} temporadas disponíveis para assistir."
    
serie = Netflix('Peaky Blinders', 'Drama', '5')

qtd_temporadas = serie.obter_temporadas_serie()
print('Temporadas:', qtd_temporadas)

# Temporadas: A série Peaky Blinders possui 5 temporadas disponíveis para assistir.