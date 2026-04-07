

#Ejercicio 1 
nombre = input("ingrese su nombre: ")

while not nombre.isalpha():
    print("Error. Ingrese solo letras.")
    nombre = input("Ingrese su nombre: ")

cantidad = input("Ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error. Ingrese cantidad mayor a 0.")
    cantidad = input("Ingrese la cantidad de productos: ")


cantidad = int(cantidad)

total_sin_descuento = 0 
total_con_descuento = 0

for i in range(cantidad):
    print(f"\nProducto {i+1}")

    precio = input("Ingrese el precio: ")
    while not precio.isdigit():
        print("Error. Ingrese un numero valido: ")
        precio = input("Ingrese el precio:")

    precio = int(precio)

    descuento = input("¿Tiene descuento? (S/N): ").lower()
    
    while descuento != "s" and descuento != "n":
        print("Error. Ingrese S o N: ")
        descuento = input("¿Tiene descuento? (S/N): ").lower()

    total_sin_descuento += precio

    if descuento == "s":
        precio_desc = precio *0.9
    else:
        precio_desc = precio
    total_con_descuento += precio_desc

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n --- Resumen ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuento: {total_sin_descuento}")
print(f"Total con descuento: {total_con_descuento:2f}")
print(f"Ahorro total: {ahorro:2f}")
print(f"Promedio por producto: {promedio:2f}")


#Ejercicio 2

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 3
access = False

while intentos > 0:
    usuario = input("Ingrese el Usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print(f"Ingreso Exitoso")
        access = True
        break
    else:
        intentos -= 1
        print(f"Ingreso invalido, Intentos Restantes: ", intentos)

if intentos == 0:
    print(f"Se agoto los intentos. Acceso Bloqueado.")

while access:
    print("\n1) Estado 2) Cambiar Clave 3) Mensaje 4) Salir")

    opcion = input("opcion: ")

    if not opcion.isdigit():
        print("Error: ingrese un numero valido.")
        continue
    opcion = int(opcion)

    if opcion < 1 or opcion > 4:
        print("Error: opcion fuera de rango.")
        continue
    if opcion == 1:
        print("Inscripto")
    
    elif opcion  == 2:
        while True:
            nueva = input("Nueva Clave: ")
            
            if len(nueva) < 6:
                print("Error: Minimo 6 Caracteres.\n")
                continue
            
            confirmar = input("Confirma Clave: ")    
            
            if nueva != confirmar:
                print("Error: las claves no coinciden.\n")
            else:
                clave_correcta = nueva
                print("Clave cambiada correctamente.")
                break 
    elif opcion == 3:
        print("Sigue adelante aprendiendo vos podes!!!.")
    
    elif opcion == 4:
        print("Cerrar Sesion")
        break



#Ejercicio 3
while True:
    operador = input("Ingrese su nombre: ")
    
    if operador.isalpha():
        break
    else:
        print("Error. Ingrese solo letras ")

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

while True:
        print("1) Reservar 2) Cancelar 3) Ver dia 4) Resumen 5) Salir")
        opcion = input("Opcion: ")

        if not opcion.isdigit():
            print("Error")
            continue
        
        opcion = int(opcion)

        if opcion == 1:
            dia = input(" Dia (1=Lunes, 2=Martes): ")
            while dia  != "1" and dia != "2":
                dia = input ("Error. Dia (1=Lunes, 2=Martes): ")
            
            nombre = input("Nombre: ")
            while not nombre.isalpha():
                nombre = input("Error. Solo Letras: ")
            
            if dia == "1":
                if nombre in (lunes1, lunes2, lunes3, lunes4):
                    print("Nombre repetido.")
                elif lunes1 == "":
                    lunes1 = nombre
                    print(f"Turno reservado correctamente {operador}")
                elif lunes2 == "":
                    lunes2 = nombre
                    print(f"Turno reservado correctamente {operador}")
                elif lunes3 == "":
                    lunes3 = nombre
                    print(f"Turno reservado correctamente {operador}")
                elif lunes4 == "":
                    lunes4 = nombre
                    print(f"Turno reservado correctamente {operador}")
                else:
                    print("No hay mas turnos disponibles.")
            else:
                if nombre in (martes1, martes2, martes3):
                    print("Nombre repetido.")
                elif martes1 == "":
                    martes1 = nombre
                    print(f"Turno reservado correctamente {operador}")
                elif martes2 == "":
                    martes2 = nombre
                    print(f"Turno reservado correctamente {operador}")
                elif martes3 == "":
                    martes3 = nombre
                    print(f"Turno reservado correctamente {operador}")
                else:
                    print("No hay mas trunos disponibles")
        elif opcion == 2:
            dia = input("Dia (1=Lunes, 2=Martes): ")
            nombre = input("Nombre a cancelar: ").lower()

            if dia == "1":
                if lunes1 == nombre: 
                    lunes1 = ""
                    print(f"Turno cancelado correctamente {operador}")
                elif lunes2== nombre: 
                    lunes2 = ""
                    print(f"Turno cancelado correctamente {operador}")
                elif lunes3== nombre: 
                    lunes3 = ""
                    print(f"Turno cancelado correctamente {operador}")
                elif lunes4== nombre: 
                    lunes4 = ""
                    print(f"Turno cancelado correctamente {operador}")
                else: print("No encontrado")
            else: 
                if martes1 == nombre: 
                    martes1 = ""
                    print(f"Turno cancelado correctamente {operador}")
                elif martes2 == nombre: 
                    martes2 = ""
                    print(f"Turno cancelado correctamente {operador}")
                elif martes3 == nombre: 
                    martes3 = "" 
                    print(f"Turno cancelado correctamente {operador}")
                else: print("No encontrado")
        elif opcion == 3:
            dia = input("Dia (1=Lunes, 2=Martes):")
            
            if dia == "1":
                print("Lunes: ")
                print("1:", lunes1 if lunes1 else "Libre")
                print("2:", lunes2 if lunes2 else "Libre")
                print("3:", lunes3 if lunes3 else "Libre")
                print("4:", lunes4 if lunes4 else "Libre")
            elif dia == "2":
                print("Martes: ")
                print("1:", martes1 if martes1 else "Libre")
                print("2:", martes2 if martes2 else "Libre")
                print("3:", martes3 if martes3 else "Libre")
            else:
                print("Error: dia Invalido.")
        elif opcion == 4:
            ocupado_lunes = sum([lunes1!="", lunes2!="", lunes3!="", lunes4!=""])
            ocupado_martes = sum([martes1!="", martes2!="", martes3!=""])

            print("Lunes Ocupados:", ocupado_lunes, "/ 4")
            print("Martes Ocupados:", ocupado_martes, "/4")

            if ocupado_lunes > ocupado_martes:
                print("Mas Turnos: Lunes")
            elif ocupado_martes > ocupado_lunes:
                print("Mas turnos: Martes")
            else:
                print("Disponibilidad Ambos dias")
        
        elif opcion == 5:
            print("Cerrar Sistema...")
            break

#Ejercicio 4
    
energia = 100
llaves = 0 
tiempo = 10

while energia > 0 and tiempo > 0:
    print("1)Forzar 2)Buscar 3)Descansar")
    opcion = input("Opcion: ")
    
    if not opcion.isdigit():
        print("Error, Ingrese un numero valido")
        continue
    opcion = int(opcion)

    if opcion == 1:
        print("Intentas Forzar la cerradura...")
        energia -= 30
        tiempo -= 1

        if llaves >= 3:
            print("Escapaste!!!...")
            break
        else:
            print("No lograste abrir...")
    elif opcion == 2:
        print("Buscasndo Pistas...")
        llaves += 1
        energia -= 10
        tiempo -= 1
    
    elif opcion == 3:
        print("Descanasando...")
        energia += 20
        tiempo -= 1 
    
        if energia > 100:
            energia = 100
    else:
        print("Opcion Invalida")
    
    print(f"Energia: {energia}| Llaves: {llaves} | Tiempo: {tiempo}")

if energia <= 0:
    print("Perdiste: Sin energia")
elif tiempo <= 0: 
    print("Perdiste: Te quedaste sin Tiempo")

#Ejercicio 5
import random

energia = 100
llaves = 0 
fuerza = 10

while energia > 0:
    print("1)Entrenar 2)Buscar llaves 3)Pelear 4)Escapar")
    opcion = input("Opcion: ")
    
    if not opcion.isdigit():
        print("Error, Ingrese un numero valido")
        continue
    
    opcion = int(opcion)

    if opcion == 1:
        print("Entrenando...")
        fuerza += 5
        energia -= 10
        print("Aumentaste la Fuerza..")
    elif opcion == 2:
        print("Buscando llaves...")
        energia -= 10   

        if random.randint(1, 2) == 1: 
            llaves += 1
            print("Encontraste una Llave!!")
        else:
            print("No encontraste nada.. Continua")
    elif opcion == 3:
        print("Peliando contra una enemigo...")
        energia -= 20
        
        if random.randint(1, 2) == 1:
            print("Ganaste la Pelea!!!!")
            fuerza += 2
        else:
            print("Perdiste la Batalla...")
            energia -= 20
    elif opcion == 4:
        print("Intentando Escapar...")
        if llaves >= 3 and fuerza >= 20:
            print("Escapaste de la Arena!!!!")
            break
        else:
            print("No tenes Sufiecientes Recursos para Escapar.")
    else:
        print("Opcion Invalida")

    print(f"Energia: {energia}| Llaves: {llaves} | Fuerza: {fuerza}")

if energia <= 0:
    print("Perdiste: te quedaste sin energia...")
else:
    print("Fin del Juego")