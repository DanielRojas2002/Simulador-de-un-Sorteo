import time
import datetime
import random
import math
import sys

class inventario():
    def __init__(self,nombre,boleto,carro,hora,minuto,segundo):
        self.__nombre=nombre
        self.__boleto=boleto
        self.__carro=carro
        self.__hora=hora
        self.__minuto=minuto
        self.__segundo=segundo
        
        
    def sorteo(self):
        print(separador)
        print("*"*20,"Bienvenido","*"*20)
        print(separador)
        print(f"Este es el carro que selecionaste : {self.__carro}")
        tiempo=5
        print(separador)
        print("Checando base de datos...")
        print(separador)
        temporizador=time.sleep(tiempo)
      
        print(f"Bienvenido {self.__nombre}")
        print(separador)
        print("Recopilando datos...")
        
        temporizador2=time.sleep(tiempo)
        print(separador)
        reloj1=datetime.time(self.__hora,self.__minuto,self.__segundo)
        print(separador)
        print(f"Esta es la hora del registro de tu boleto  : {reloj1.hour} hr")
        
        print(f"Esta es la minuto del registro de tu boleto  : {reloj1.minute} min")
        
        print(f"Esta es la segundo del registro de tu boleto  : {reloj1.second} seg")
        print(separador)
        minimenu=1
        if minimenu==1:
            aleatorio=random.randrange(1,6)
            print("Checando en la base de datos si tu boleto es el ganador...")
            temporizador3=time.sleep(tiempo)
            print(separador)
            if aleatorio==self.__boleto:
                print(separador)
                print(f"Felicidades acabas de ganar el auto de tus sueños\nGANASTE:{self.__carro}")
                reloj1=datetime.date.today()
                fecha_a_recojer=reloj1+datetime.timedelta(days=+10)
                print(separador)
                print(f"Puedes recojerlo en la unidad mas cercana\nEl dia {fecha_a_recojer}")
                print(separador)
            
            else:
                print(separador)
                print("Lo sentimos no has sido afortunado de ganar el carro")
                print(separador)
                print("Pero si contestas 5 preguntas bien te ganas el carro")
                print("Quieres intentarlo ")
                print(separador)
                submenu=input("Si\nNo\n:")
                contador=0
                if submenu=="Si"or submenu=="SI"or submenu=="si" or submenu=="sI":
                    print(separador)
                    print("Okey vamos a empezar")
                    print(separador)
                    print(f"Pregunta 1")
                    num1=random.randrange(20)
                    num2=random.randrange(10)
                    p1=float(input(f"Dime el maximo coumun divisor de {num1} y {num2} : "))
                    respuesta1=math.gcd(num1,num2)
                    if p1==respuesta1:
                        print("Respuesta Correcta")
                        contador=contador+1
                        
                    print(separador)
                    print(f"Pregunta 2")
                    num3=random.randrange(100)
                    p2=float(input(f"Dime la raiz cuadrada de {num3} (con 3 decimales) : "))
                    respuesta2=math.sqrt(num3)
                    z=round(respuesta2,3)
                    if p2==z:
                        print("Respuesta Correcta")
                        contador=contador+1
                    print(separador)
                    
                    print(f"Pregunta 3")
                    num4=random.randrange(10)
                    num5=random.randrange(5)
                    p3=float(input(f"Dime la potencia de {num4} a la potencia {num5} (con 3 decimales) : "))
                    respuesta3=math.pow(num4,num5)
                    w=round(respuesta3,3)
                    if p3==w:
                        print("Respuesta Correcta")
                        contador=contador+1
                    print(separador)
                    
                    
                    print(f"Pregunta 4")
                    p4=float(input(f"Dime cuanto vale el Pi: "))
                    respuesta4=3.1416
                    if p4==respuesta4:
                        print("Respuesta Correcta")
                        contador=contador+1
                    print(separador)
                    
                    
                    print(f"Pregunta 5")
                    num6=random.randrange(20)
                    p5=float(input(f"Dime cuanto vale el factorial  {num6}: "))
                    respuesta5=math.factorial(num6)
                    if p5==respuesta5:
                        print("Respuesta Correcta")
                        contador=contador+1
                    print(separador)
                    
                    
                
                    
                    if contador==5:
                        print("Felicidades has contestado las preguntas y todas las has sacado bien")
                        print(separador)
                        reloj2=datetime.date.today()
                        fecha_a_recojer2=reloj2+datetime.timedelta(days=+10)
                        print(separador)
                        print(f"Recoje tu carro este dia: {fecha_a_recojer2} en la unidad mas cercana ")
                        print("GRACIAS POR SU PREFERENCIA ")
                    
                    else:
                        print(separador)
                        print(f"lo siento has obtenido {contador} de 5")
                        print("Suerte para la proxima ")
                        print(separador)


separador=("*"*40)     
opcion="Si"

try:
    while opcion=="Si"or opcion=="si":
        print("*"*20,"BIENVENIDO AL SORTEO DE CARROS","*"*20)
        reloj=datetime.date.today()
        print(f"El dia de hoy es :{reloj}")
        print(separador)
        print("Quieres entrar al menu=1")
        menu=int(input(": "))
    
        if menu==1:
            nombre=input("Ingresa tu nombre : ")
            boleto=int(input("Dime el numero de tu boleto del 1 al 5: "))
            carro=(input("Que carro quieres ganar: "))
            hora=int(input("A que hora compraste el boleto: "))
            minuto=int(input("A que minuto: "))
            segundo=int(input("A que segundo: "))
            objeto=inventario(nombre,boleto,carro,hora,minuto,segundo)
            objeto.sorteo()
            opcion=input("Deseas intentar otra vez\nSi\nNo\n: ")

except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[0]}")
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)

finally:
    print("*"*30,"Fin del Programa","*"*30) 