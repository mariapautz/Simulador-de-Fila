import random
lista_idoso = []
lista_gestante = []
lista_comum = []
def classificaçao():
    classificação = int(input("Insira 1 para idoso, 2 para gestante e 3 para pessoa comum: "))
    if classificação == 1:
        a = random.randint(1,50)
        print ("Sua senha é " + str(a))
        lista_idoso.append(a)
        
    elif classificação == 2:
        b = random.randint(1,50)
        print ("Sua senha é " + str(b))
        lista_gestante.append(b)
    elif classificação == 3:
        c = random.randint(1,50)
        print ("Sua senha é " + str(c))
        lista_comum.append(c)
    else:
        print ("Este comando não existe")
def prox_senha():
    while len(lista_idoso) != 0:
        print ("A senha da vez é " + str(lista_idoso[0]))
        lista_idoso.pop(0)
    
    while len(lista_gestante) != 0:
        print ("A senha da vez é " + str(lista_gestante[0]))
        lista_gestante.pop(0)
        
    while len(lista_comum) != 0:
        print ("A senha da vez é " + str(lista_comum[0]))
        lista_comum.pop(0)
def mostrar():
    print ("a lista de idosos é " + str(lista_idoso))
    print ("a lista de gestantes é " + str(lista_gestante))
    print (" a lista comum é " + str(lista_comum))

    
rodando = True
while rodando:

    menu = int(input("Digite 1 para inserir; 2 para remover; 3 para mostrar as filas e 4 para sair do programa: "))
    if menu == 1:
        classificaçao()
    elif menu == 2:
        prox_senha()
    
    elif menu == 3:
        mostrar()
    elif menu == 4:
        print ("tenha um bom dia :)")
        rodando = False
    else:
        print ("este comando não existe!")
   
