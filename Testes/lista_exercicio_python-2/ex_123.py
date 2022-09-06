# 1. Dadas as seguintes informações: pessoa, cpf, nome e idade, crie uma classe onde teremos o retorno do documento, o retorno do nome e verificação de tipo de pessoa, onde um método
# irá receber como parâmetro "F" ou "N" para trazer fumante ou não fumante. Feito isso, crie uma instância e retorne esses valores.

class Pessoa:
    def __init__ (self, cpf, nome, idade, fumante):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.fumante = fumante
        
       
def teste_fumante(fumante):
        if fumante == 'f':
            return f'É fumante'
        return f'Não é fumante'
    
def dados_pessoa (pessoa):
    return f'CPF: {pessoa.cpf}, Nome: {pessoa.nome}, Idade: {pessoa.idade}, Fumante?: {teste_fumante(pessoa.fumante)}'

cpf = '123.456.789-10'
nome = 'Larissa'
idade = 25
fumante = 'N'

pessoa = Pessoa(cpf, nome, idade, fumante)
dados_pessoa(pessoa)


# 2. Escreva uma classe "PessoaFisica" e herde Pessoa, crie um método exclusivo para a classe e acesse-o.

class PessoaFisica(Pessoa):
    def __init__ (self, cpf, nome, idade, fumante, sobrenome):
        self.sobrenome = sobrenome
        super().__init__(cpf, nome, idade, fumante)
        
    def input_sobrenome (self, sobrenome):
        self.sobrenome = sobrenome
        
def dados_pessoa_fisica (pessoaFisica):
    return f'CPF: {pessoaFisica.cpf}, NomeCompleto: {pessoaFisica.nome} {pessoaFisica.sobrenome} Idade: {pessoaFisica.idade}, Fumante?: {teste_fumante(pessoaFisica.fumante)}'

cpf = '123.456.789-10'
nome = 'Larissa'
idade = 25
fumante = 'N'
sobrenome = 'Bertani'

pessoaFisica = PessoaFisica(cpf, nome, idade, fumante, sobrenome)
dados_pessoa_fisica(pessoaFisica)
pessoaFisica.input_sobrenome('teste')
dados_pessoa_fisica(pessoaFisica)

# 3. Escreva uma classe "PessoaJuridica" e herde Pessoa, agora modificando o comportamento, retorne o cnpj. Crie uma instância e acesse os dados.

class PessoaJuridica(Pessoa):
    def __init__ (self, cpf, nome, idade, fumante, cnpj):
        self.cnpj = cnpj
        super().__init__(cpf, nome, idade, fumante)
        
    def input_cnpj (self, cnpj):
        self.cnpj = cnpj
        
def dados_pessoa_juridica (pessoaJuridica):
    return f'CPF: {pessoa.cpf}, CNPJ: {pessoaJuridica.cnpj}, NomeCompleto: {pessoaJuridica.nome} {pessoaJuridica.sobrenome} Idade: {pessoaJuridica.idade}, Fumante?: {teste_fumante(pessoaJuridica.fumante)}'

cpf = '123.456.789-10'
nome = 'Larissa'
idade = 25
fumante = 'N'
sobrenome = 'Bertani'
cnpj = '10.296.544/0001-60'

pessoaJuridica = PessoaJuridica(cpf, cnpj, nome, idade, fumante)
dados_pessoa_juridica(pessoaJuridica)
