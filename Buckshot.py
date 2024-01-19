#--- <Importaciones> ---
import sys #para detener el codigo mientras
import random #uso esta libreria para generar numeros random
import time #uso esta libreria para poder hacer pausas de tiempo
#--- </Importaciones>---

#--- <Classes> ---
#una clase para crear un jugador se puede usar cuantas veces se quiera
# ejemplo de uso: jugador1 = Jugador() y ya luego se le asignan los atributos
# con jugador1.nombre = "Jhonn Doe" por ejemplo
class Jugador:
    nombre = ""
    desfibriladores = 0
    esposas= 0
    lupa = 0
    cigarrillo = 0
    cerveza = 0
    cuhillo = 0
    
#una clase sencilla para crear la escopeta 
class Escopeta:
    MaxBalas = 0
    balas_vacias = 0
    balas_cargadas = 0
    orden_de_cartuchos = []
    

#--- </Classes> ---

#--- <Funciones> ---

# una funcion sencilla para el cambio de ronda
def eleccion_de_ronda():
    if ronda == 1:
        ronda1()
    elif ronda == 2: # ronda es una variable
        ronda2()
    else:
        ronda3()
        
# funcion sencilla para elegir la camtidad de balas vacias o cargadas
def elegir_balas():
    la_escopeta.balas_cargadas = random.randint(1,2)
    la_escopeta.balas_vacias = la_escopeta.MaxBalas - la_escopeta.balas_cargadas
    
#para la creacion del orde  de los cartuchos para poder tener la lupa
def crear_orden_cartuchos():
    #hago una copia de las variables de balas para modificar sin preocupaciones
    balasvacias = la_escopeta.balas_vacias
    balascargadas = la_escopeta.balas_cargadas
    #contador para manejar el while
    cont2 = 0
    while cont2 < la_escopeta.MaxBalas:
        if random.randint(1, balasvacias + balascargadas) <= balasvacias:
            la_escopeta.orden_de_cartuchos.append(False)
            balasvacias -= 1
        else:
            la_escopeta.orden_de_cartuchos.append(True)
            balascargadas -= 1
        cont2 += 1
    print("Se recaró la escopeta en un orden aleatorio")
    print(f"el orden de los cartuchos es: {la_escopeta.orden_de_cartuchos}")
#logica de la primera ronda segun el juego original
def ronda1():
    la_escopeta.MaxBalas = 3
    el_jugador.desfibriladores = 2
    oponente.desfibriladores = 2
    elegir_balas()
    crear_orden_cartuchos()
    elegir_disparar()
    print("Fin de la primera ronda")
    
#logica de la segunda ronda segun el juego original
def ronda2():
    a=1
    
#logica de la tercera ronda segun el juego original
def ronda3():
    a=1
#para que el jugador pueda elegir a quien disparar
def elegir_disparar():
    global eleccion
    global jugada
    jugada = "jugador"
    print("(1): Dispararte a ti mismo")
    print("(2): Dispararle al oponente")
    eleccion = int(input("Elige pibe (1) ó (2): "))
    disparar()
    
#se realiza la accion de disparar
def disparar():
    if eleccion == 1:
        dispararse()
    else:
        dispararle_al_oponente()
        
#funcion para dispararle al jugador
def dispararse():
    global disparo_a
    global escopeta_disparo
    termina_ronda()
    disparo_a = "jugador"
    if jugada == "jugador":
        print("Elegiste dispararte")
    else:
        print("El oponente eligio dispararte")
    time.sleep(1.8)
    if la_escopeta.orden_de_cartuchos[0] == True:
        print("¡Bang! pierdes una vida")
        bajar_desfibri()
        balas_camara()
        escopeta_disparo = True
        aquien_letoca()
    else:
        print("La escopeta no disparó")
        balas_camara()
        escopeta_disparo = False
        aquien_letoca()
        
#literalmente el nombre de la funcion lo dice
def dispararle_al_oponente():
    global disparo_a
    global escopeta_disparo
    termina_ronda()
    disparo_a = "ia"
    if jugada == "jugador":
        print("Elegiste dispararle al oponente")
    else:
        print("El oponente se disparo a si mismo")
    time.sleep(1.8)
    if la_escopeta.orden_de_cartuchos[0] == True:
        print("¡Bang! el oponente perdio una vida")
        bajar_desfibri()
        balas_camara()
        escopeta_disparo = True
        aquien_letoca()
    else:
        print("La escopeta no disparó")
        balas_camara()
        escopeta_disparo = False
        aquien_letoca()

#funcion para la logica del oponente ia
#no sabra realmente el orden de los cartuchos
#manejo completo de aleatoriedad y probabilidad
def inteligencia_oponente():
    global jugada
    jugada = "ia"
    print("inicio de la inteligencia del oponente")
    print(f"maxbalas: {la_escopeta.MaxBalas}")
    if la_escopeta.MaxBalas <3:
        if random.randint(1,2) == 1:
            dispararse()
        else:
            dispararle_al_oponente()
            
def bajar_desfibri():
    if jugada == "ia":
        el_jugador.desfibriladores -=1
    else:
        oponente.desfibriladores -=1
# mensajes para ecplicar las reglas
#aunque que hueva hacer eso xd
def explicar_reglas():
    print("No te explico ni vrga vamo a juga")

# funcuon que se usa luego de disparar ya que resta una bala (la que se gasto)
# a las variables y lo muestra en pantalla
def balas_camara():
    la_escopeta.MaxBalas -=1
    la_escopeta.orden_de_cartuchos.pop(0)
    print(f"Quedan: {la_escopeta.MaxBalas} balas en la recamara")
    print(f"orden de los cartuchos: {la_escopeta.orden_de_cartuchos} ")
#logica para saber a quien le toca el siguiente turno
def aquien_letoca():
    
    print("a quien le toca si sirve")
    
   
    # Cuando el jugador es el que dispar
    # cuando la escopeta dispara o no dispara, el objetivo es la ia y la jugada la hizo el jugador le toca a la ia el siguiente turno
    if escopeta_disparo == True or escopeta_disparo == False and disparo_a == "ia" and jugada == "jugador":
        print("si despues de este mensaje hay errores separa en ambos lugsres")
        ia_juega()
    #cuando la escopeta no dispara y el jugador mismo se disparo le toca denuevo al jugador
    elif escopeta_disparo == False and disparo_a == "jugador" and jugada == "jugador":
        print("escopeta no disparo y el jugador mismo se disparo")
        jugador_juega()
    # cuando la escopeta dispara y el jugador mismo se disparo le toca a la ia
    elif escopeta_disparo == True and disparo_a == "jugador" and jugada == "jugador":
        ia_juega()
    # Cuando la ia es la que dispara
    #no lo explico porque es literalmente oo mismo de arriba pero con los roles invertidos
    elif escopeta_disparo == True or escopeta_disparo == False and disparo_a == "jugador" and jugada == "ia":
        jugador_juega()
    elif escopeta_disparo == False and disparo_a == "ia" and jugada == "ia":
        ia_juega()
    elif escopeta_disparo == True and disparo_a == "jugador" and jugada == "ia":
        jugador_juega()
    
#cuando le toca al jugador jugar xd
def jugador_juega():
    print("Te toca a ti elige a quien disparar")
    elegir_disparar()

def termina_ronda():
    print("se ejecuto el termina ronda")
    if el_jugador.desfibriladores > 0 and oponente.desfibriladores < 1:
        print("El jugador gana")
        sys.exit()
    elif el_jugador.desfibriladores < 1 and oponente.desfibriladores > 0:
        print("La ia gana")
        sys.exit()
    elif la_escopeta.MaxBalas < 1:
        print("la ronda debe terminar porque no hay mas balas en el cargador")
        sys.exit()
    elif el_jugador.desfibriladores > 0 and oponente.desfibriladores > 0:
        pass
#--- </Funciones> ---

#--- <Oponente IA> ---

def ia_juega():
    print("Ahora le toca al oponente")
    inteligencia_oponente()
#--- </Oponente IA> ---

#--- <Instancias> ---
el_jugador = Jugador()
oponente = Jugador()
la_escopeta = Escopeta()
#--- </Instancias>---

#--- <Variables> ---
ronda = 1
eleccion = None
disparo_a = "jugador"
escopeta_disparo = False
jugada = "jugador"
#--- </Variables> ---

#--- Algoritmo ---
el_jugador.nombre = str(input("¿Cual es su nombre?: "))
reglas = str(input(f"Ok {el_jugador.nombre} vamos a jugar quieres que te explique las reglas? (s/n): "))
if reglas == "s":
    explicar_reglas()
else:
    print("Bueno igual no te iba a explicar ni mrda")
time.sleep(1.5)
ronda1()
#--- </Algoritmo> ---
