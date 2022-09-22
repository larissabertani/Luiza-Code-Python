import math
import logging
from typing import Type

logging.basicConfig(level=logging.ERROR, filename="logging_erros.log")

# Ex1:  Faça um programa que calcule a raiz quadrada de um número n e trate os casos em que n < 0. OBS: Utilize o módulo math para calcular a raiz quadrada.

def number_validate(numero):
    if numero < 0:
        raise ValueError("O número deve ser maior que zero")
    
def calcular_raiz():
    try:
        numero = float(input("Entre com um número"))
        number_validate(numero)
        raiz = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {raiz}")
    except ValueError:
        print("Erro nos tipos de dados digitados")
        logging.error("Erro nos dados digitados")
        return
calcular_raiz()
    
# Ex2: Faça um programa que calcule a divisão de dois números m e n e trate os casos em que n = 0.

def n_validate(numero):
    if numero == 0:
        raise ValueError("Não é possível fazer divisão por 0")

def calculo_divisao():
    try:
        m = float(input("Insira o primeiro número:"))
        n = float(input("Insira o segundo número:"))
        n_validate(n)
        divisao = m / n
        print(f"O resultado da divisão é {divisao}")
    except ValueError:
        print(("Não é possível fazer divisão por 0"))
        logging.error("O denominador não pode ser 0")
        return
calculo_divisao()

# Ex.3: Observe o programa abaixo: Reescreva esse código de uma forma com que ele seja capaz de tratar a inserção de um caractere por parte do usuário.
number = int(input("Digite um número: "))
print("O número digitado foi:", number)

def tratar_insercao():    
    try:
        number = int(input("Digite um número: "))
        print(f"O número digitado{number} é válido.")
    except ValueError:
        print("Erro no tipo de dado digitado")
        logging.error("Erro no tipo de dado digitado")
        return
tratar_insercao()

# Ex.4: Observe o seguinte programa: Tendo em mente que ao executá-lo a exceção NameError é gerada, reescreve o código de forma com que tal exceção seja tratada.

try:
    number = int(input("Digite um número: "))
    print("O número digitado foi:", n)
except NameError:
    print("Variável incorreta")


# Ex.5: Observe o seguinte programa: Qual exceção será gerada durante a execução?
import mathmatics
print(math.sqrt(25))

"A exceção gerada durante a execução é: ModuleNotFoundError: No module named 'mathmatics"

# Ex.6: Observe o seguinte programa: Escreva o que será impresso na tela caso o mesmo seja executado com as seguintes entradas (5, 3):
try:
    number_1 = float(input("Insira um número: "))
    number_2 = float(input("Insira outro número: "))
    result = number_1 / number_2
    
    print("Resultado: {:.2f}".format(resultado))
except ValueError:
    print("Isso não é um número.")
except ZeroDivisionError:
    print("Divisao por 0 indeterminada.")
except:
    print("Algo deu errado.")
    
"Será impresso na tela a mensagem de except: Algo deu errado."

# Ex.7: Uma colega tentou executar o seguinte programa: E obteve a seguinte mensagem de erro: Reescreva o código para que esse erro seja exibido de forma mais clara e amigável.
file = open("file.txt", "r")
file_lines = file.readline()
file.close()

try:
    file = open("file.txt", "r")
    file_lines = file.readline()
    file.close()
except FileNotFoundError:
    print("O arquivo indicado não foi encontrado, verifique e tente novamente.") 

# Ex.8: Observe o seguinte programa: Um dos problemas do código acima é que o mesmo além de possuir um erro lógico (execução de um comando de escrita em um arquivo em modo de leitura), abre um
# arquivo e tem a sua execução encerrada sem realizar o close

try:
    file = open("file.txt", "r")
    file.write("Exemplo de texto.")
except FileNotFoundError:
    print("O arquivo indicado não foi encontrado.")
except IOError:
    print("Não foi possível escrever no arquivo.")
finally:
    file.close()



    

