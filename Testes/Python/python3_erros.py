import logging
from typing import Type
import requests

logging.basicConfig(level=logging.ERROS, filename="logs_example.log")
# logging.info("Meu primeiro log")
# logging.erro("Meu primeiro log de ERRO")

try:
    numerator = int(input("Numerador: "))
    denominator = int(input("Denominador: "))
    result = numerator / denominator
    logging.info(result)
    print(f"O resultado é {result}")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
    logging.error("Não é possível dividir um número por zero")
except (ValueError, TypeError):
    print("Erro nos tipos de dados que você digitou")
except KeyboardInterrupt:
    print("Dados não informados")
finally:
    print("Obrigada!")
    
    ###################################################################
    
# logging.basicConfig(level='INFO', filename="logs_example.log")
logging.basicConfig(level=logging.ERROR, filename="logging_users.log")

users = []

def users_validate(name):
    for user in users:
        if user["name"] == name:
            raise TypeError("Já existe um usuário cadastrado com esse nome")

def name_validate(name):
    if len(name) < 10:
        raise TypeError("Nome do usuário deve conter mais de 10 caracteres")

def age_validate(age):
    if age < 18 or age > 100:
        raise TypeError("Usuário deve ser maior de 18 anos e menor de 100 anos.")

def user_add():
    try: 
        name = input("Digite o nome do usuário: ")
        name_validate(name)
        users_validate(name)
        age = int(input("Digite a idade do usuário: "))
        age_validate(age)
    except ValueError:
        print("Erro nos tipos de dados digitados")
        logging.error("Erro nos dados digitados")
        return
    except TypeError as error:
        print(error)
        logging.error(error)
        return
        
    users.append({"name": name, "age": age})
    
    print("\nUsuário cadastrado com sucesso!")
    
def users_list():
    print("\n")
    for user in users:
        print("{} - {} anos".format(user["name"], user["age"]))

def menu():
    while True:
        option = int(input("\nDigite a opção desejada:\n 1 - Cadastrar pessoas\n 2 - Listar pessoas\n 3 - Sair\n"))
        
        if option == 1:
            logging.info("Usuário digitou opção 1")
            user_add()
        elif option == 2:
            logging.info("Usuário digitou opção 2")
            users_list()
        elif option == 3:
            logging.info("Usuário digitou opção 3")
            exit()
        else:
            print("Opção inválida!")
            
menu()

###############################################################

try:
    result = requests.get("https://www.google.com.br/")
    result.raise_for_status()
    print("Google acessado")
except requests.exceptions.HTTPError as error:
    print(f"Não foi possível acessar o Google. Erro {error}")


