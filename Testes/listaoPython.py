
# 1) O Python trabalha tipos de valores. Com os valores abaixo, dê o nome de seus tipos:

from re import X


a = 1
b = 12.6
c = True
d = False
e = -543
f = -5.78
g = 'copo'
h  = 'Belo dia'

print(type(a)) #int
print(type(b)) #float
print(type(c)) #bool
print(type(d)) #bool
print(type(e)) #int
print(type(f)) #float
print(type(g)) #str
print(type(h)) #str

lista = [1, 12.6, True, False, -543, -5.78, 'copo', 'Belo dia']
tipo = map(lambda x: type(x), lista)
print(list(tipo))
#[<class 'int'>, <class 'float'>, <class 'bool'>, <class 'bool'>, <class 'int'>, <class 'float'>, <class 'str'>, <class 'str'>]

# 2) Digite cada linha abaixo no shell do Python e informe quais estão corretos e quais apresentam erro:

1 #correto
1a #erro
a1 #erro
1. #correto
.2 #correto
-.3 #correto
'agua"limpa' #correto
"agua""      #erro
"""teste 1 2 3""" #correto

# 3) Determine qual é o resultado dos seguintes cálculos no Python:

# a. Operadores matemáticos

print(10 + 3) #13
print (10 - 3) #7
print (10 * 3) #30
print (10 / 3) #3.3333333333333335
print (10 / 3.0) #3.3333333333333335
print (13 / 3) #4.333333333333333
print (13 / 3.0) #4.333333333333333
print (13 // 3.0) #4.0

# b. Ordem dos operadores

print (5 + 30 * 20) #605
print ((5 + 30) * 20) #700
print (((5 + 30) * 20) / 10) #70.0
print (5 + 30 * 20 / 10) #65.0

# c. Operadores comparação

print (2 < 3) #True
print(9 > 8) #True
print(1 == 1) #True
print (1 != 2) #True
print (1 != 1) #False
print (4 <= 4) #True
print (5 >= 6) #False
print( 1 < 2 < 3) #True
print(1 < 2 < 2) #False
print (1 + 2 < 25 / 5) #True

#d. Mais operadores matemáticos:

print(2 ** 4) #16
print(26 % 5) #1

# e. Operadores lógicos:

print (not True) #False
print (not False) #True
print (True and True) #True
print (True and False) #False
print (False and True) #False
print (False and False) #False
print (True or True) #True
print (True or False) #True
print (False or True) #True
print (False or False) #False
print (True or True and False) #True
print (True or True) and False #True
print (not True or False) #False
print (not (True or False)) #False
print (not (True and False) and (True or False)) #True
print (1 > 2 and 3 > 4) #False
print (1 > 2 and 3 < 4) #False
print (1 < 2 and 3 < 4) #True
print (1 + 2 and 3 + 4) #7
print (1 + 2 or 3 + 4) #3
print (True and 3 > 5) #False
print (False and 3 >5) #False


# 4) Qual será o valor final de x?

x = 10

x = x + 10
x = 100 - x

print (x) #80


# 5) Resolva estes problemas em Python, guardando os valores e seus resultados em variáveis diferentes.

# a. Calcule a área de um quadrado cujo lado seja 2 cm.

lado = 2

area_quadrado = lado ** 2
print (area_quadrado) #4

# b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela.

preco_mala = 120.00
desconto = 0.05

print(preco_mala * (1 - desconto)) #114.0

#c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem será 200 Km. Quantas horas irá demorar a viagem.

velocidade_media = 100
trecho_viagem = 200

print (trecho_viagem / velocidade_media) #2.0

# d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e sua média.

joao = 2
maria = 3
sofia = 1

print (joao + maria + sofia) #6
print ((joao + maria + sofia) / 3) #2.0

# criancas = {'joao': 2, 'maria': 3, 'sofia': 1}
# criancas['joao' + 'maria' + 'sofia']

# e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a verificação se a idade de Davi é maior que a idade de sua irmã.

davi = 13
irma_davi = 7

eh_mais_velho = davi > irma_davi
print (eh_mais_velho) #True

# 6) Qual será o valor de z? Qual seria outra forma de escrever este trecho de código?

z = 3
z += 2
z *= 6
z /= 5
print (z) #6.0

z = z + 2
z = z * 6
z = z / 5

# 7) Considere as seguintes variáveis:

ovo = 3.4
caju = 12.4

# Qual será o valor de resposta em cada linha:

#resposta1
if 1 > 2:
    print (ovo)
else: 
    print (caju) 
#12.4

#resposta2
if ovo > caju:
    print (ovo)
else:
    print (caju) 
#12.4

#resposta3
if ovo < caju:
    print (ovo) 
else:
    print (caju)
#3.4

#resposta4
if ovo + caju >15:
    print (100)
else:
    print (200)
#100
    
#resposta5
if ovo == 3:
    print (100)
else:
    print (0)
#0
    
    
# 8) Qual é o resultado deste problema? Qual é o valor final da variável fim?

ab = 10
Ab = 20
aB = 30
AB = ab + Ab + aB
print (AB) #60
fim = AB + 1
print (fim) #61


# 9) Qual é o resultado de cada linha de comando do Python? Siga a ordem dos comandos.

valor = input ("Informe um valor") #Informe um valor
print ("Valor informado: ", valor) 
tipo = type(valor)
x_str = "123"
x = int(x_str) #123
xf = float (x) #123
sao_iguais = x == xf
print ("Um float é igual a um int?", sao_iguais) #True


# 10) Colete o nome da pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar os dados coletados em linhas diferentes. E também, deverá informar quantos anos a pessoa terá no ano 2030.

nome_pessoa = input ('Nome pessoa')
cidade_nascimento = input ('Cidade de nascimento')
ano_nascimento = input ('Ano de nascimento')

print(nome_pessoa)
print (cidade_nascimento)
print (ano_nascimento)
idade_2030 = (2022 - int (ano_nascimento))
print (idade_2030 + (2030 - 2022))


# 11) Este programa irá calcular a área de um quadrado. Peça para a pessoa informar a medida numérica de um lado do quadrado. E depois informe-lhe o valor da área do quadrado.

lado_quadrado = input ('Informe a medida numérica de um lado do quadrado')
area_quadrado = int (lado_quadrado) ** 2
print (area_quadrado)


# 12) Este programa irá calcular a área de um triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois colete o valor da altura. Apresente o valor da área do triângulo.

base_triangulo = input ('Informe a medida numérica da base do triâgulo')
altura_triangulo = input ('Informe a altura do triangulo')
area_triangulo = (int (base_triangulo) * int (altura_triangulo)) / 2
print (area_triangulo)


# 13)  Colete a idade de 3 pessoas e mostre a média de suas idades.

idade_1 = input('Informe sua idade')
idade_2 = input('Informe sua idade')
idade_3 = input('Informe sua idade')

media_idades = (int (idade_1) + int (idade_2) + int (idade_3) ) / 3
print (media_idades)


# 14) Colete a idade de duas pessoas. E informe se a primeira idade é maior do que a da primeira. Neste aqui, basta responder True para informar que a primeira idade é maior que a primeira

idade_pessoa1 = input('Informe sua idade')
idade_pessoa2 = input('Informe sua idade')
print (idade_pessoa1 > idade_pessoa2)


# 15)  Em uma casa, uma família decidiu dividir o valor da conta de energia entre os moradores da casa. No programa eles informam o valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará quanto cada um deverá contribuir com a conta de energia.

conta_energia = input ('Informe o valor da conta ')
pagantes_mes = input ('Informe quantas pessoas irão pagar a conta no mês ')
print ( float (conta_energia) / float (pagantes_mes))

# 16) Estou tentando entender os juros do meu banco. Para isto, ele me informou esta fórmula: Crie um programa que colete cada um destes valores para calcular o valor final que estarei pagando ao banco.


valor_emprestimo = input ('Qual o valor do empréstimo?') 
taxa = input ('Qual a taxa por mês?') 
tempo = input ('Em quantos meses o empréstimo será pago?')
valor_final = float (valor_emprestimo) + (float (valor_emprestimo) * float (taxa) * int (tempo))
print (valor_final)


# 17)  Dada uma equação de segundo grau, calcule suas raízes utilizando a fórmula de Bhaskara.

a = input ('Informe o coeficiente a')
b = input ('Informe o coeficiente b')
c = input ('Informe o coeficiente c')

delta = float (b)**2 - 4 * float (a) * float (c)
print (delta)
x1 = (-float (b) + delta**0.5) / 2
print (x1)
x2 = (-float (b) - delta**0.5) / 2
print (x2)


# 18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um valor inteiro entre zero e 100. Se o valor não estiver neste intervalo, informe que a nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso contrário, informa que ele foi reprovado.

nota_aluno = input('Qual a nota do aluno')
if  (int (nota_aluno) < 0 or int (nota_aluno) > 100):
    print ('A nota é inválida')
elif int (nota_aluno) > 60:
    print ('Aluno aprovado')
else: 
    print ('Aluno reprovado!')
    
    
# 19)Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a venda for … Faça um programa que informe o valor da comissão do vendedor para uma venda.

valor_venda = input ('Qual valor vendido?')
valorvenda_float = float(valor_venda)
if valorvenda_float < 1000:
    print ('Não ganha comissão')
elif valorvenda_float >= 1000 and valorvenda_float <= 5000:
    print  ("O valor da comissão será: " + str (valorvenda_float*0.1))
elif valorvenda_float > 5000 and valorvenda_float <= 10000:
    print ("O valor da comissão será: " + str (valorvenda_float*0.2))
elif valorvenda_float > 10000 and valorvenda_float <= 50000:
    print ("O valor da comissão será: " + str (valorvenda_float*0.25))
else:
    print ("O valor da comissão será: " + str (valorvenda_float*0.3))
    
    
# 20) Crie um programa para calcular o valor a ser pago para um determinado produto para a empresa NaoQueroMuitoSeuDinheiro. O pessoal desta empresa pediu o seguinte:

str_valor_inicialparcela = input ('Qual valor da parcela?')
str_valor_percentualparcela = input ('Qual valor percentual de cada parcela?')
str_quantidade_parcelas = input ('Qual a quantidade de parcelas?')

valor_inicialparcela = float (str_valor_inicialparcela)
valor_percentualparcela = float (str_valor_percentualparcela)
quantidade_parcelas = int (str_quantidade_parcelas)

parcela_atual = 1

while parcela_atual <= quantidade_parcelas :
    if parcela_atual == 1:
        valor_parcela = valor_inicialparcela + (valor_inicialparcela * valor_percentualparcela)
    else:
        valor_parcela = valor_parcela + (valor_parcela * valor_percentualparcela)
    print ("Parcela " + str (parcela_atual) + ": $ "+ str (valor_parcela))
    parcela_atual +=1
    
    
# 21) Crie um script que liste todos os números dos telefones, ao serem informados, o prefixo e os sufixos. Por exemplo, suponha que o prefixo seja “3232” e que o primeiro prefixo seja “0001” e o último sufixo seja “0005”; logo o programa irá imprimir:

# prefixo = input ('Prefixo')
# sufixo1 = input ('Primeiro sufixo')
# sufixo2 = input ('Segundo sufixo')

# sufixo_atual = 

# while sufixo_atual <= sufixo2:


# 22) Crie um script que leia 10 números inteiros positivos e que irá apresentar:


# 23)  Neste script você irá ler o nome de 4 alunos e suas notas e determinar qual aluno possui a maior nota
    