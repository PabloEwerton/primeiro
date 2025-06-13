# ## Tipagem Dinamica

# ## Variaveis
# nome = 'Pablo'
# idade = 28
# altura = 1.80
# peso: float = 80.0
# hoby = ["musica", "canto", "videogame"]
# dicionario = {}

# ### Operadores de condição e Operadores logicos
# if altura >= 1.80 or peso > 80:
#     print("Está acima do peso!")
# elif altura >= 1.80 and peso <= 80:
#     print("Está dentro do peso!")
# else:
#     print("Não consegui validar")
# # O and só verdade se todas as condiçoes forem verdades
# # O or só é falso se todas as condiçoes forem falsas

# ## Operadores de loop
# condicao =  1 == 1
# while condicao:
#     print("Estou no loop")

#     if condicao == False:
#         break
    
#     condicao = False

# i = 0
# for i in range(10):
#     print(i)



# ### Funções
# def validar_imc(altura, peso):
#     imc = peso / (altura ** 2)
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif imc >= 18.5 and imc < 24.9:
#         return "Peso normal"
#     elif imc >= 25 and imc < 29.9:
#         return "Sobre peso"
#     else:
#         return "Obsidade"
    

# imc_danillo = validar_imc(altura=1.80, peso=85)

# print("O Danillo está com o IMC: " + imc_danillo)

# imc_ton = validar_imc(altura=1.75, peso=76)

# print("O Ton está com o IMC: " + imc_ton)



###### Criar uma função que que calcule 2 valores (n1 e n2) ( somar, subtrair, multiplicar e divdir)

def calculadora(n1, n2, operador):
    if operador == "+":
        return n1 + n2
    elif operador == "-":
        return n1 - n2
    elif operador == "*":
        return n1 * n2
    elif operador == "%":
        return n1 % n2
    else:
        return "Essa operção não é permitida"
    
# def calculadora(n1, n2, operador):
#     if operador == "-":
#         return n1 - n2
#     else:
#         return "Essa operção não é permitida"
    
# def calculadora(n1, n2, operador):
#     if operador == "*":
#         return n1 * n2
#     else:
#         return "Essa operção não é permitida"
    
# def calculadora(n1, n2, operador):
#     if operador == "%":
#         return n1 % n2
#     else:
#         return "Essa operção não é permitida"

        
    

print(calculadora(600, 600, "*"))