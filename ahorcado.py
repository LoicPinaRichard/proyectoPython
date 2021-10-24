import time
nombre=input("Cual es tu Nombre?")
print("hola, "+nombre,"vamos a jugar al juego del ahorcado")
print(" ")
time.sleep(1)
print("Comienza a adivinar: \n")
time.sleep(0.5)
palabra="empleo"
tupalabra=""
vidas=5

while vidas > 0:
    pierdes=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            pierdes +=1
    if pierdes==0:
        print(" Felicidades me has contratado por este juego!")
        break
    tuletra=input("  introduce tu letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print(" te has equivocado")
        print(" tienes ", vidas,"vidas mas")
    if vidas==0:
        print(" has perdido pero me haria muy feliz una llamada para trabajar con vosotros")
        