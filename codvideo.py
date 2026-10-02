import random

vida = 100
nivel = 1
experiencia = 0

def batalla():
    global vida, experiencia

    enemigo = random.randint(30, 60)

    print("\n¡Encontraste un enemigo!")
    print("Vida del enemigo:", enemigo)

    while enemigo > 0 and vida > 0:

        print("\n1. Atacar")
        print("2. Usar habilidad")

        opcion = input("Elige: ")

        if opcion == "1":
            daño = random.randint(10, 25)
            enemigo -= daño
            print("Hiciste", daño, "de daño")

        elif opcion == "2":
            daño = random.randint(20, 35)
            enemigo -= daño
            print("¡Usaste una habilidad!")
            print("Hiciste", daño, "de daño")

        else:
            print("Opción incorrecta")
            continue

        if enemigo > 0:
            daño_enemigo = random.randint(5, 15)
            vida -= daño_enemigo
            print("El enemigo te hizo", daño_enemigo, "de daño")

        print("Tu vida:", vida)
        print("Vida enemigo:", enemigo)

    if vida <= 0:
        print("\n💀 PERDISTE")
        return False

    print("\n¡Ganaste la batalla!")
    experiencia += 50
    return True

def jugar():
    global nivel, experiencia, vida

    print("\n--- NUEVA PARTIDA ---")

    nombre = input("Escribe tu nombre: ")

    print("\n¡Bienvenido", nombre, "!")
    print("Comienzas en el nivel 1.")

    while nivel <= 3 and vida > 0:

        print("\n====================")
        print("NIVEL", nivel)
        print("====================")

        print("1. Explorar")
        print("2. Ver estado")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            encontrado = random.choice([True, False])

            if encontrado:
                if batalla() == False:
                    break
            else:
                print("\nNo encontraste ningún enemigo.")

        elif opcion == "2":

            print("\nNombre:", nombre)
            print("Nivel:", nivel)
            print("Vida:", vida)
            print("Experiencia:", experiencia)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción incorrecta")

        if experiencia >= 100:
            nivel += 1
            experiencia = 0
            vida = 100

            print("\n⭐ ¡SUBISTE DE NIVEL!")
            print("Ahora eres nivel", nivel)

    if nivel > 3 and vida > 0:
        print("\n👑 ¡LLEGASTE AL JEFE FINAL!")

        jefe = 100

        while jefe > 0 and vida > 0:

            daño = random.randint(15, 30)
            jefe -= daño

            print("\nAtacaste al jefe e hiciste", daño, "de daño.")

            if jefe > 0:
                daño = random.randint(10, 20)
                vida -= daño
                print("El jefe te hizo", daño, "de daño.")

            print("Tu vida:", vida)
            print("Vida del jefe:", jefe)

        if vida > 0:
            print("\n🎉 ¡DERROTASTE AL JEFE FINAL!")
            print("🏆 ¡GANASTE EL JUEGO!")
        else:
            print("\n💀 El jefe te derrotó.")

# MENÚ PRINCIPAL

while True:

    print("\n==============================")
    print("   VIDEO JUEGO - AVENTURA")
    print("==============================")

    print("1. Nueva partida")
    print("2. Opciones")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        jugar()

    elif opcion == "2":
        print("\nJuego de aventura.")
        print("Derrota enemigos y sube de nivel.")

    elif opcion == "3":
        print("\n¡Gracias por jugar!")
        break

    else:
        print("Opción incorrecta")

