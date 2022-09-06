# 5. Escreva uma classe "Quadrado", crie dois métodos que retornem a área do quadrado e o perímetro, não crie a instância nesse exercício.

class Quadrado:
    def __init__ (self, lado):
        self.lado = lado
    
    def area_quadrado (self):
        print (self.lado * self.lado)
        
    def perimetro_quadrado(self):
        return (self.lado * 4)
    
lado = Quadrado(2)
lado.area_quadrado()
lado.perimetro_quadrado()

# 6. Crie um arquivo main.py, importe a classe "Quadrado", crie uma nova instância e acesse seus métodos.