**Ex_001 Crie um programa que escreva 'Olá, Mundo!' na tela.**

print ('Olá Mundo')





""**Ex_002 Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.**""

nome = input('Digite seu nome: ')
print ('Prazer em te conhecer,',nome ,'!')





""**Ex_003 Crie um programa que leia dois numeros e mostre as somas deles**""

n1 = int(input("Digite um número: "))
n2 = int ( input ('Digite outro número:'))
s = n1 + n2
print ( 'A soma de' , n1 , 'mais' , n2 , 'é' , s)





""**Ex_004 Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informações possiveis sobre ela**""

a = input ('Digite algo: ')
print ('O tipo primitivo desse valor é', type(a))
print ('Apenas tem espaços?', a.isspace())
print ('Apenas é números?' , a.isnumeric())
print ('Apenas tem letras?' , a.isalpha())
print ('Tem números e letras?' , a.isalnum())
print ('Ta apenas em maiúsculas?' , a.isupper())
print ('Ta apenas em minusculas?' , a.islower())





""**Ex_005 Crie um programa que mostre o seu número, o Antecessor do seu número, e o sucessor do seu número.**""

nu = int(input ('Digite um número: '))
an = nu - 1
su = nu + 1
print ('O seu número é {}.\nO antecessor do seu número é {}.\nE o seu sucessor do seu número é {}.'.format (nu , an , su))





""**Ex_006 Crie um algoritimo que leia o número e mostre o seu dobro, o seu tripo ,e a sua raiz quadrada.**""

import math
nu = float(input('Digite um número: '))
do = nu * 2
tri = nu * 3
raiz = math.sqrt(nu)
print ('Seu número é {}.\nO dobro do seu número é {}. \nO triplo do seu número é {}.\nE a raiz quadrada do seu número é {:.2f}.'.format (nu , do , tri , raiz))





""**Ex_007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a media**""

no1 = float(input('Digite a nota do primeiro aluno: '))
no2 = float(input('Digite a nota do segundo aluno: '))
s = (no1 + no2) / 2
print ('A media entre {} e {} é igual a {}.'.format (no1 , no2 , s ))





""**Ex_008 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.**""

m = float(input('Digite o metro: '))
c = m * 100
mm = m * 1000
print ('O metro é {}.\nO centimetro é {}.\nE o milimetro é {}.'.format (m , c , mm))





""**Ex_008b Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros, e agora tbm em km, hm, dam e dm**""

m = float(input('Digite os metros: '))
dm = m * 10
cm = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
print ('{} metros equivale a {}km.\n{} metros equivale a {}hm.\n{} metros equivale a {}dam.\n{} metros equivale a {}dm.\n{} metros equivale a {}cm.\n{} metros equivele a {}mm.\n'.format(m , km , m , hm , m , dam , m , dm , m , cm , m , mm ))





""**Ex_009 Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada**""

n = int(input('Digite seu número: '))
print('\n')
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10

print('A tabuada do {} é: \n{}'.format(n, '-='*6))
print('{} x 1 = {}'.format(n, n1))
print('{} x 2 = {}'.format(n, n2))
print('{} x 3 = {}'.format(n, n3))
print('{} x 4 = {}'.format(n, n4))
print('{} x 5 = {}'.format(n, n5))
print('{} x 6 = {}'.format(n, n6))
print('{} x 7 = {}'.format(n, n7))
print('{} x 8 = {}'.format(n, n8))
print('{} x 9 = {}'.format(n, n9))
print('{} x 10 = {}'.format(n, n10))
print('-='*6)





""**Ex_010 Crie um programa que leia quanto dinheiros uma pessoa tem e mostre quanto ela teria em Dólar. (Valor do Dólar: 3.27 reais**""

real = float(input('Digite quantos reais vc tem: R$'))
dolar = real / 3.27
print ('Vc tem entorno de {:.2f} dólares'.format(dolar))





""**Ex_011 Faça um programa que leia a largura e a altura da parede em metros , calcule a sua area e a quantidade de tinta necessaria para pinta a parede, sabendo que cada metros pinta 2m**""

lar = float(input('Digite a largura da parede: '))
al = float(input('Digite a altura da parede: '))
a = lar * al
tinta = a / 2
print ('A área da sua parede é {}m.\nPara pintar a parede será necessario gastar {} litros de tinta.'.format (a , tinta))





""**Ex_012 Faça um algoritimo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.**""

preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o valor do desconto: %'))
total = preco * (1 - desconto / 100)
print ('O novo valor do produto é R${:.2f}'.format (total))





""**Ex_013 Faça um algoritimo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento**""

salario = float(input('Digite o seu salario: R$'))
aumento = float(input('Digite o seu aumento porcentual: %'))
nsalario = salario * (1 + aumento / 100)
print ('O seu novo salrio é R${:.2f}.'.format(nsalario))





""**Ex_014 Escreva um programa que converta uma temperatura digitada em °C e converta para °F**""

grauc = float(input('Digite a temperatura em °C: '))
fare = grauc * 1.8 + 32
print ('A temperatura de {}°C\nEquivalente a {}°F.'.format(grauc , fare))





""**Ex_015 Escreva um programa que pergute  a quantidade de dias  e km rodados por um carro alugado, e calcule o preço a ser pago. Sabendo que o custa R$ 60 por dia e reais 0.15 por km rodado.**""

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km andados? '))
pago = (dias * 60) + (km * 0.15)
print ('O valor total a ser pago é: R${:.2f}'.format(pago))





""**Ex_016 Crie um programa que leia um número Real qualquer pela tela e mostre a sua porção inteira.**""

import math
nu = float(input('Digite um número: '))
print ('O número {} tem a parte inteira de {}.'.format(nu , math.trunc (nu)))





""**Ex_017 Faça um programa  que leia  o comprimento  do cateto  oposto e do cateto adjacente  de um triângulo  retângulo , calcule  e mostre  o comprimento da hiportenusa.**""

import math
catetops = float(input('Digite o comprimento do cateto oposto: '))
catetoad = float(input('Digite o comprimento do cateto adjecente: '))
hipor = math.hypot (catetops , catetoad)
print ('O comprimento da hiportenusa é {: .2f}'.format (hipor))





""**Ex_018 Faça um programa  que leia o angulo  qualquer e mostre  o valor do seno, coseno e tangente  desse angulo**""

import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin (math.radians(angulo))
coseno = math.cos (math.radians(angulo))
tangente = math.tan (math.radians(angulo))
print ('O Ângulo de {}.\nTem o SENO de: {: .2f}.\nO COSENO de: {: .2f}.\nE o TANGENTE de: {: .2f}'.format (angulo , seno , coseno , tangente))





""**Ex_019 Faça um programa que sorteie nomes diferentes**""

import random
n1 = input ('Primeiro Aluno: ')
n2 = input ('Segundo Aluno: ')
n3 = input ('Terceiro Aluno: ')
n4 = input ('Quarto Aluno: ')
lista = [n1 , n2 ,n3 ,n4]
escolhido = random.choice(lista)
print ('O aluno escolhido foi {}!'.format (escolhido))





""**Ex_020 Faça um programa que leia os nomes de 4 pessoas e sorteie a ordem de apresentação**""

import random
n1 = input ('Primeiro Aluno: ')
n2 = input ('Segundo Aluno: ')
n3 = input ('Terceiro Aluno: ')
n4 = input ('Quarto Aluno: ')
lista = [n1 , n2 , n3 , n4]
random.shuffle(lista)
print ('A ordem de apresentação será: ')
print(lista)





""**Ex_021 Faça um programa em Python que abra e reproduza o áudio em um arquivo MP3. (Não terminado)**""

import pygame
pygame.init()
pygame.mixer.music.load('only.mp3')
pygame.mixer.music.play ()
pygame.event.wait()





""**Ex_022 Crie um programa que leia o nome complero de uma pessoa e mostre:**""
O nome com todas as letras maisculas.
O nome com todas as letras minusculas.
Quantas letras tem no nome sem contar os espaços
Quantas letras tem o primeiro nome


nome = str(input('Digite seu Nome Completo: ')).strip()
print('Analisando o seu Nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count (' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))





""**Ex_023 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.**""
Ex: Digite um número: 1834
unidade: 4, dezena: 3, centena: 8, milhar: 1,

num = int(input ('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número: {}'.format (num))
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))





""**Ex_024 Crie um programa que leia um nome de uma cidade e diga se ela começa com a ou não com o nome 'Santo'**""

cidade = input('Em que cidade vc nasceu? ').strip()
print (cidade[:6].upper() == 'SANTO')





""**Ex_025 Crie um programa que leia o nome de uma pessoa e diga se tem 'Silva' nome**""

nom = input ('Digite seu nome completo: ').strip()
sil = 'silva' in nome.lower()
print ('Seu nome tem Silva: {}'.format(sil))





""**Ex_026 Faça um programa que leia uma frase pelo teclado e mostre:**""
Quantas vezes apareceu a letra A.
Em que posição ela aparaceu pela primeira vez.
Em que posicão ela apareceu pela última vez.


frase = (input('Digite uma frase: ')).strip()
print ('A letra A aparece {} na frase.'.format(frase.lower().count('a')))
print ('A primeira letra A apareceu na posição {}.'.format(frase.lower().find('a')+1))
print ('A última letra A apareceu na posição {}.'.format(frase.lower().rfind('a')+1))





Ex_027 Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza.
Primeiro: Ana.
Último: Souza.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu segundo nome é: {}.'.format(nome[len(nome)-1]))





**Ex_028 Escreva um programa que o computador escolha um número de 0 a 5. E a pessoa deverá acerta caso ela acerte mostre uma mensagem dizendo que ela acertou. Mas caso ela não acerte, faça mostra uma mensagem dizendo que ela errou.

import random
from time import sleep
nu = random.randint(0 , 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep (3)
if num == nu:
  print('PARABÉNS! Você conseguiu me vencer!')
else:
  print('GANHEI! Eu pensei no número {} e não o {}!'.format(nu , num))





**Ex_029 Escreva um programa que leia a velocidade de um carro .**
Se ele ultrapassar os 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar 7 Reais por cada km acima do limite.


velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade >80:
 print('\033[31;40mMULTADO! Você excedeu o limite permitido que é de 80km/h \n Você deve pagar uma multa de R${: .2f}!\033[m'.format(multa))

print('\033[33;40mTenha um Bom dia! Dirija com segurança!')





**Ex_030 Crie um programa que leia um número inteiro e mostra na tela se ele é impar ou par. (Não Terminado)**

nu = int(input('Me diga um número qualquer: '))
resultado = nu % 2
if resultado == 0:
  print('Seu número é \033[34mPAR!')
else:
  print('Seu número é \033[33mÍMPAR!')





**Ex_031 Desenvolva um programa que pergunte a distância de uma Viagem em Km. Calcule o preço da passagem, cobrando 0.50 reais por Km para viagens de até 200km e 0.45 reais para viagens mais longas**

distancia = float(input('Qual a distância da sua viagem? '))
print('Vc está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <=200:
  valor = distancia * 0.50
  print('O preço da sua passagem será de R${: .2f}'.format(valor))
else:
  valor2 = distancia * 0.45
  print('O valor da sua passagem será de R${: 2.f}'.format(valor2))





**Ex_032 Faça um programa que leia um ano qualquer e mostre se ele é um ano bissexto.**

from datetime import date
ano = int(input('Que ano vc quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
  print('O ano {} é BISSEXTO!'.format(ano))
else:
  print('O ano {} NÃO é BISSEXTO!'.format(ano))





**Ex_033 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.**

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a<b and a<c:
  menor = a
if b<c and b<a:
  menor = b
if c<a and c<b:
  menor = c

if a>b and a>c:
  maior = a
if b>c and b>a:
  maior = b
if c>a and c>b:
  maior = c
print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))




**Ex_034 Escreva um programa que pergunte o sálario de um funcionário e calcule  o valor do seu aumento.**
**Para sálarios superiores  a 1250 reais, calcule um aumento de 10%.**
**Para os inferiores ou iguais , o aumento é de 15%.**

salario = float(input('Qual o salário do funcionário? R$'))
if salario >1250:
  newsalario = salario * (1 + 10 / 100)
  print('Quem ganhava R${} passa a ganhar R${} agora.'.format(salario , newsalario))
else:
  new = salario * (1 + 15 / 100)
  print('Quem ganhava R${} passa a ganhar R${} agora.'.format(salario , new))





**Ex_035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo.**

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
se1 = float(input('Primeiro segmento: '))
se2 = float(input('Segundo segmento: '))
se3 = float(input('Terceiro segmento: '))
if se1 < se2 + se3 and se2 < se1 + se3 and se3 < se1 + se2:
  print('Os segmentos acima PODEM FORMAR um Triângulo!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR um Triângulo!')
