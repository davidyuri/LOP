
import math
#1. Calculadora Simples---------------------------------------------------------------------------------

print ("#1. Calculadora Simples")

valor_1=float(input("Digite o primeiro número: "));
valor_2=float(input("Digite o segundo número: "));

print(f"soma: {valor_1 + valor_2}" )
print(f"subtração:{valor_1 - valor_2}")
print(f"multiplicação: {valor_1 * valor_2}")
print(f"Divisão: {valor_1 / valor_2}")


#2. Conversor de Temperatura ---------------------------------------------------------------------------
# print ("#2. Conversor de Temperatura")

# Ce = float(input("Digite a temperatura em celsius: "));
# Fa = Ce*(9/5)+32 

# print(f"A temperatura é {Fa} graus Fahrenheit")

# 3. Área do Círculo---------------------------------------------------------------------------------------
# print("3. Área do Círculo")

# r = float(input("Digite o valor do raio: "))
# A =  math.pi*r**2

# print(f"A área é: {A}")

# 4. Área do Triângulo---------------------------------------------------------------------------------------
# print("4. Área do Triângulo")

# b = float(input("Digite o valor da base: "))
# h =  float(input("Digite o valor da altura: "))
# A = (b*h)/2

# print(f"A área é: {A}")

# 5. Volume da Esfera---------------------------------------------------------------------------------------
# print("5. Volume da Esfera")

# r = float(input("Digite o valor do raio: "))
# A =  (4/3)*math.pi*r**3

# print(f"O Volume da Esfera é: {A}")

# 6. Calculadora de Média Aritmética---------------------------------------------------------------------------------------
# print("6. Calculadora de Média Aritmética")

# n1 = float(input("digite a primeira nota: "))
# n2 = float(input("digite a segunda nota: "))
# n3 = float(input("digite a terceira nota: "))
# m = (n1+n2+n3)/3

# print(f"a média aritmética entre as notas é : {m}")

# 7. Calculadora de Média Ponderada---------------------------------------------------------------------------------------
# print("7. Calculadora de Média Ponderada")

# n1 = float(input("digite a primeira nota: "))
# p1 = float(input("digite o peso da primeira nota: "))
# n2 = float(input("digite a segunda nota: "))
# p2 = float(input("digite o peso da segunda nota: "))
# n3 = float(input("digite a terceira nota: "))
# p3 = float(input("digite o peso da terceira nota: "))
# n4 = float(input("digite a quarta nota: "))
# p4 = float(input("digite o peso da quarta nota: "))

# m = (n1*p1+n2*p2+n3*p3+n4*p4)/(p1+p2+p3+p4)

# print(f"a média ponderada entre as notas é : {m}")

# 8. Equação de Segundo Grau---------------------------------------------------------------------------------------
# print("8. Equação de Segundo Grau")

# a = float(input("digite a: "))
# b = float(input("digite b: "))
# c = float(input("digite c: "))
# x = float(input("digite x: "))

# y = a*x**2+b*x+c

# print(f"O resultado da equação é :{y}")

# 9. Calculadora de IMC-------------------------------------------------------------------------------------------
# print("9. Calculadora de IMC")

# p = float(input("digite o peso: "))
# a = float(input("digite a altura: "))
# imc = p/(a**2)

# print(f"o IMC é: {imc}")

# 10. Tabuada---------------------------------------------------------------------------------------------------------
# print("10. Tabuada")

# numero = int(input("digite um numero: "))

# print(f"{numero} x 1 = {numero*1}", end="; ")
# print(f"{numero} x 2 = {numero*2}", end="; ")
# print(f"{numero} x 3 = {numero*3}", end="; ")
# print(f"{numero} x 4 = {numero*4}", end="; ")
# print(f"{numero} x 5 = {numero*5}", end="; ")
# print(f"{numero} x 6 = {numero*6}", end="; ")
# print(f"{numero} x 7 = {numero*7}", end="; ")
# print(f"{numero} x 8 = {numero*8}", end="; ")
# print(f"{numero} x 9 = {numero*9}", end="; ")
# print(f"{numero} x 10 = {numero*10};")

# 11. Conversão de Segundos para o Formato HORA:MINUTO:SEGUNDO---------------------------------------------------------------------------------------------------------
# print("11. Conversão de Segundos para o Formato HORA:MINUTO:SEGUNDO")

# seg = int(input("digite um tempo em segundos: "))

# hora = int(seg/3600)
# seg = seg%3600
# min = int(seg/60)
# seg = seg%60

# print(f"{hora:02d}", end=":")
# print(f"{min:02d}", end=":")
# print(f"{seg:02d}")

