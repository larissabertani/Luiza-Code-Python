# 4. Crie um professor de classe com atributos nome, idade e salário, onde o salário deve ter um método privado que não pode ser acessado fora da classe.
# a. Crie um método para acessar o método privado, onde é passada a identificação do usuário se ele pode ou não acessar.

class Professor:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __salario(self):
        return f'O salário é R$7.000'
        
    def acesso_salario(self, usuario):
        if usuario == 'Gerente':
            return self.__salario()
        
professor = Professor('Astolfo', '45').acesso_salario('Gerente')
print(professor)

professor2 = Professor('Joaozinho', '70').__salario()
print(professor2)