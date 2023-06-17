import os
import time

#Limpiar pantalla
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')

#Mostrar mensaje con efecto piola
def mostrar_mensaje(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.03)
    print()

#Opciones de que hacer este noche
def mostrar_opciones():
    mostrar_mensaje("¿Qué prefieres hacer?")
    mostrar_mensaje("1. Quedarse en casa.")
    mostrar_mensaje("2. Salir al boliche.")

#Bucle para que elija entre 2 opciones si o si
def obtener_eleccion_con_2_opciones():
    eleccion_accion = input("-")
    while eleccion_accion not in ["1", "2"]:
        limpiar_pantalla()
        mostrar_mensaje("           ADVERTENCIA     ")
        mostrar_mensaje("...................................")
        
        mostrar_mensaje("¡Tienes que elegir la opción 1 o 2!")
        eleccion_accion = input("-")
    return eleccion_accion

#Bucle para que elija entre 3 opciones
def obtener_eleccion_con_3_opciones():
    eleccion_accion = input()
    while eleccion_accion not in ["1", "2","3"]:
        limpiar_pantalla()
        mostrar_mensaje("           ADVERTENCIA     ")
        mostrar_mensaje("...................................")
        mostrar_mensaje("¡Tienes que elegir la opción 1, 2 o 3")
        eleccion_accion = input("-")
    return eleccion_accion

#Bucle para que elija entre 4 opciones
def obtener_eleccion_con_4_opciones():
    eleccion_accion = input()
    while eleccion_accion not in ["1", "2","3","4"]:
        limpiar_pantalla()
        mostrar_mensaje("           ADVERTENCIA     ")
        mostrar_mensaje("...................................")
        mostrar_mensaje("¡Tienes que elegir la opción 1, 2, 3 o 4!")
        eleccion_accion = input("-")
    return eleccion_accion


#Funcion si te quedas en tu casa
def quedarse_en_casa():
    mostrar_mensaje("¡Has elegido quedarte en casa!")
    mostrar_mensaje("¿Qué planeas hacer esta noche?")
    mostrar_mensaje("1. No vas a hacer nada.")
    mostrar_mensaje("2. Hacer algo.")
    eleccion_esta_noche = obtener_eleccion_con_2_opciones()
    limpiar_pantalla()
    if eleccion_esta_noche=="1":
        mostrar_mensaje("Has elegido no hacer nada!")
        mostrar_mensaje("Te vas a dormir.")
        mensaje_finalizacion()
    #Opcion de hacer algo 
    elif eleccion_esta_noche=="2":
        mostrar_mensaje("Has elegido aprovechar la noche y hacer algo.")
        mostrar_mensaje("¿Que te gustaria hacer?.")
        mostrar_mensaje("1. Ver alguna pelicula o serie.") #Preguntar que serie
        mostrar_mensaje("2. Jugar videojuegos.") #Preguntar que videojuego
        mostrar_mensaje("3. Ver curso online")  #Preguntar curso de acerca que
        mostrar_mensaje("4. Practicar") #Preguntar que cosa
        
        eleccion_actividad_noche= obtener_eleccion_con_4_opciones()
        limpiar_pantalla()
        #Eleccion de ver pelicula/serie
        if eleccion_actividad_noche=="1":
            mostrar_mensaje("¡Has elegido ver alguna pelicula/serie.")
            mostrar_mensaje("¿Que tenes pensado ver?")
            mostrar_mensaje("1. Pelicula.")
            mostrar_mensaje("2. Serie.")
        
            eleccion_serie_o_pelicula=obtener_eleccion_con_2_opciones()
            limpiar_pantalla()
        #Eleccion nº 1 (Quedarse viendo una pelicula)
            if eleccion_serie_o_pelicula == "1":
                mostrar_mensaje("¡Vas a ver una pelicula!")
                mostrar_mensaje("¿Que pelicula vas a ver?")
                mostrar_mensaje("Escriba el nombre.")
                pelicula_name=input("-") #digitar nombre de la pelicula
                limpiar_pantalla()
                mostrar_mensaje("Wow! Suena interesante!")
                mostrar_mensaje("¿De que genero es "+ str(pelicula_name) + ("?"))
                pelicula_genero=input("-") #digitar tipo de genero de pelicula. ej; Terror, comedia,etc
                limpiar_pantalla()
                mostrar_mensaje("El genero "+str(pelicula_genero).lower()+ " suena totalmente increible!")
                mostrar_mensaje("Espero que disfrutes tu noche de peliculas!")
                mensaje_finalizacion()
            #Eleccion nº 2 (Quedarse viendo una serie)
            elif eleccion_serie_o_pelicula == "2":
                mostrar_mensaje("¡Vas a ver una una serie!")
                mostrar_mensaje("¿Que serie vas a ver?")
                mostrar_mensaje("Escriba el nombre.")
                serie_name=input("-") #digitar nombre de la serie
                limpiar_pantalla()
                mostrar_mensaje("Wow! Parece estar buena la serie!")
                mostrar_mensaje("¿De que genero es "+ str(serie_name) + ("?"))
                serie_genero=input("-") #digitar el genero de la serie. ej; terror psicologico, etc
                limpiar_pantalla()
                mostrar_mensaje("El genero "+str(serie_genero).lower()+ " suena totalmente increible!") 
                mostrar_mensaje("Espero que disfrutes tu noche de serie!")
                mensaje_finalizacion()
                
        #Eleccion de jugar videojuegos
        elif eleccion_actividad_noche == "2":
            mostrar_mensaje("¡Has elegido jugar videojuego esta noche!")
            mostrar_mensaje("¿Que videojuego vas a jugar?")
            videojuego_name=input("-") #nombre del juego
            limpiar_pantalla()
            mostrar_mensaje("Me suena ese juego!")
            mostrar_mensaje("¿Puedes decirme de que se trata " +str(videojuego_name)+(" o que tipo de juego es?"))
            genero_del_juego=input("-") #Genero del juego. ej; accion, terror, choice game, etc;
            limpiar_pantalla()
            mostrar_mensaje("Aaaah, ahora lo recuerdo!")
            mostrar_mensaje("Sin duda el genero de "+str(genero_del_juego)+(" es totalmente divertido!"))
            mostrar_mensaje("Disfruta viciando toda la noche!")
            mensaje_finalizacion()
        
        #Eleccion de curso
        elif eleccion_actividad_noche == "3":
            mostrar_mensaje("¡Has elegido hacer cursos online!")
            mostrar_mensaje("¿Sobre que vas a hacer curso?")
            curso_sobre_que=input("-") #¿Curso de que? ej; Matematica, ingles, programacion,etc
            limpiar_pantalla()
            mostrar_mensaje("Suena divertido.")
            mostrar_mensaje("¿Porque has decidido hacer curso de "+str(curso_sobre_que).lower()+(" ?"))
            preguntar_porque=input("-") #razon de porque haces el curso. (por gusto, porque lo necesitas)
            limpiar_pantalla()
            mostrar_mensaje("¡Me alegro que hagas los cursos porque "+str(preguntar_porque).lower()+(" !"))
            mensaje_finalizacion()

        #Eleccion de practica
        elif eleccion_actividad_noche == "4":
            mostrar_mensaje("¡Has elegido practicar!")
            mostrar_mensaje("¿Sobre que vas a practicar?")
            practica=input("-") #ejercicios de matematica, lo que sea
            limpiar_pantalla()
            mostrar_mensaje("Mmmmmm......")
            mostrar_mensaje("¿Porque has decidido practicar "+str(practica).lower()+(" ?"))
            preguntar_porque=input("-") #porque tenias examen, porque tenias ganas,etc
            limpiar_pantalla()
            mostrar_mensaje("¡Me alegro que practiques por "+str(preguntar_porque).lower()+(" !"))
            mensaje_finalizacion()

#Funcion si decides salir a algun boluche
def salir_al_boliche():
    mostrar_mensaje("¡Has elegido salir al boliche!")
#Funcion para obtener si o si un valor numerico
def obtener_valor_numerico(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número válido.")


# Función para obtener el presupuesto del usuario
def obtener_presupuesto():
    presupuesto = obtener_valor_numerico("¿Cuánto dinero tienes para salir? ")
    mostrar_mensaje("Cuentas con un presupuesto de " + str(presupuesto) + " pesos.")
    return presupuesto


# Función para obtener el nombre del boliche
def obtener_nombre_boliche():
    while True:
        boliche = input("¿A qué boliche te gustaría salir? ")
        if not boliche.isnumeric():  # Verifica que sea texto y no un número
            mostrar_mensaje("Has elegido salir a " + str(boliche.capitalize()) + ".")
            return boliche
        else:
            print("Respuesta inválida. Debes ingresar el nombre del boliche, no un número.")

#Preguntar precio de la entrada
def precio_entrada():
    precio = obtener_valor_numerico("¿Cuál es el precio de la entrada? ")
    return precio

# Función para obtener la bebida del usuario
def obtener_bebida():
    while True:
        bebida = input("¿Qué bebidas vas a comprar? ")
        if not bebida.isnumeric():  # Verifica que sea texto y no un número
            return bebida
        else:
            print("Respuesta inválida. Debes ingresar el nombre de la bebida que quieras, no un número.")


# Función para obtener el precio de la bebida
def obtener_precio():
    precio = obtener_valor_numerico("¿Cuál es el precio? ")
    return precio


# Función para preguntar si desea tomar otra bebida
def preguntar_tomar_otra_bebida(dinero_restante, bebidas):
    while True:
        respuesta = input("¿Deseas tomar otra bebida? (Sí/No): ").lower()
        if respuesta == "s":
            return elegir_otra_bebida(dinero_restante, bebidas)
        elif respuesta == "n":
            mostrar_mensaje("Has elegido no comprar más bebida!")
            lista_compra(bebidas)
            exit()
        else:
            print("Respuesta inválida. Por favor, ingresa 'S' o 'N'.")
            
        return bebidas

# Funcion para elegir bebida (Lo más importante)
def elegir_bebida():
    bebidas=[]
    while True:
        presupuesto = precio_total()
        bebida = obtener_bebida()
        precio_bebida = obtener_precio()
        dinero_restante = presupuesto - precio_bebida
        if dinero_restante > 0:  # Se seguirá ejecutando el programa si le queda saldo.
            mostrar_mensaje(
                "Has elegido comprar " + str(bebida).lower() + " que cuesta " + str(precio_bebida) + " pesos.")
            mostrar_mensaje("Te quedan " + str(dinero_restante) + " pesos.")
            bebidas.append(bebida) #se utiliza para agregar un elemento (en este caso, una bebida) a una lista
            presupuesto = dinero_restante
            return preguntar_tomar_otra_bebida(dinero_restante, bebidas)
        else:  # Se finaliza el programa debido a que no tienes suficiente saldo.
            mostrar_mensaje("¡No te queda más dinero para comprar bebidas!")
            lista_compra(bebidas)
            exit()


# Función para calcular el presupuesto restante después de restar el precio de la entrada
def precio_total():
    presupuesto = obtener_presupuesto()
    entrada = precio_entrada()
    precioTotal = presupuesto - entrada
    if precioTotal > 0:  # Si la entrada vale menos que el presupuesto que tienes, se seguirá ejecutando el programa.
        mostrar_mensaje("Tu presupuesto es de " + str(precioTotal) + ".")
        return precioTotal
    else:  # Si la entrada vale más de lo que tienes de presupuesto, el programa va a finalizar.
        mostrar_mensaje("¡No tienes dinero para salir!")
        mostrar_mensaje("Programa finalizado.")
        exit()


# Función para elegir otra bebida
def elegir_otra_bebida(dinero_restante, bebidas):
    presupuesto = dinero_restante
    bebida = obtener_bebida()
    precio_bebida = obtener_precio()
    dinero_restante = presupuesto - precio_bebida
    if dinero_restante > 0:
        mostrar_mensaje(
            "Has elegido comprar " + str(bebida).lower() + " que cuesta " + str(precio_bebida) + " pesos.")
        mostrar_mensaje("Te quedan " + str(dinero_restante) + " pesos.")
        bebidas.append(bebida)
        return preguntar_tomar_otra_bebida(dinero_restante,bebidas)
    else:
        mostrar_mensaje("¡No te queda más dinero para comprar bebidas!")
        exit()


# Lista de compra de bebidas
def lista_compra(bebidas):
    mostrar_mensaje("Tu lista de compra:")
    for bebida in bebidas:
        mostrar_mensaje("- " + str(bebida).capitalize())

#Funcion sobre la acciones que vas a tomar en en el boliche
def acciones_en_boliche():
    mostrar_mensaje("¿Vas a tomar?") #Preguntar si va a toamr
    mostrar_mensaje("1. Si")
    mostrar_mensaje("2. No")
    eleccion_tomar=obtener_eleccion_con_2_opciones()
    limpiar_pantalla()
    #Elegis tomar
    if eleccion_tomar=="1":
        mostrar_mensaje("¡Has elegido tomar!")
        bebidas = []
        elegir_bebida() #Elegis bebida para tomar
        elegir_otra_bebida(bebidas) #Te pregunta nuevamente si queres tomar otra bebida
        lista_compra(bebidas) #Te muestra todo lo que has comprado para tomar a la noche
        pass
    
    elif eleccion_tomar=="2":
        mostrar_mensaje("¡Has elegido no tomar!")
        mostrar_mensaje("¿Que deseas hacer?")
        mostrar_mensaje("1. Bailar.")
        mostrar_mensaje("2. Conversar con personas desconocidas.")
        mostrar_mensaje("3. Intentar encarar.")
        accion_siguiente_noche=obtener_eleccion_con_3_opciones()
        limpiar_pantalla()
        
        #Decides bailar
        if accion_siguiente_noche == "1":
            mostrar_mensaje("Decides bailar toda la noche.")
            mostrar_mensaje("La vas a pasar bomba!")
            mensaje_finalizacion()

        elif accion_siguiente_noche == "2":
            mostrar_mensaje("Decides que prefieres conversar con gente desconocidas.")
            mostrar_mensaje("Haras muchos amigos!")
            mensaje_finalizacion()
            
        elif accion_siguiente_noche == "3":
            mostrar_mensaje("Decides salir de caceria esa noche.")
            mostrar_mensaje("Esperemos que tengas suerte!")
            mensaje_finalizacion()
        
#Funcion para la introduccion
def introduccion():
    mostrar_mensaje("¡Bienvenidos al programa para organizar tu finde!")

#Funcion para terminar el programa
def mensaje_finalizacion():
    mostrar_mensaje("El programa ha finalizado.")
    mostrar_mensaje("¡Gracias por haber utilizado el programa!")

#Funcion para la ejecucion del programa
def ejecucion_del_programa():
    limpiar_pantalla()
    introduccion()
    mostrar_opciones()
    while True:
        eleccion = obtener_eleccion_con_2_opciones()
        limpiar_pantalla()
        if eleccion == "1":
            quedarse_en_casa()
        elif eleccion == "2":
            salir_al_boliche() #Muestra el mensaje de "¡Has salido a un boliche!"
            obtener_nombre_boliche() #Te pregunta el nombre del boliche
            acciones_en_boliche() #Muestra varias acciones para hacer en el boliche (Te invito a leer el codigo para ver bien)

        mostrar_mensaje("¿Deseas intentar nuevamente las acciones?") 
        mostrar_mensaje("1. Sí")
        mostrar_mensaje("2. No")
        eleccion_otra_accion = obtener_eleccion_con_2_opciones()
        if eleccion_otra_accion == "2":
            break

ejecucion_del_programa()
