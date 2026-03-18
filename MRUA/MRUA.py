while True:
    print("=== MOVIMIENTO RECTILÍNEO UNIFORMEMENTE ACELERADO (MRUA) ===")
    print("0. Salir")
    print("1. Calcular Velocidad Final (v)")
    print("2. Calcular Distancia (d)")
    print("3. Calcular Tiempo (t)")
    print("4. Calcular Aceleración (a)")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 0:
        print("Programa finalizado.")
        break

    elif opcion == 1:
        v0 = float(input("Velocidad inicial v0 (m/s): "))
        a = float(input("Aceleración a (m/s²): "))                  
        t = float(input("Tiempo t (s): "))
        v = v0 + a * t
        print("Velocidad final v =", v, "m/s")

    elif opcion == 2:
        v0 = float(input("Velocidad inicial v0 (m/s): "))
        a = float(input("Aceleración a (m/s²): "))
        t = float(input("Tiempo t (s): "))
        d = v0 * t + 0.5 * a * t**2
        print("Distancia d =", d, "metros")

    elif opcion == 3:
        v = float(input("Velocidad final v (m/s): "))
        v0 = float(input("Velocidad inicial v0 (m/s): "))
        a = float(input("Aceleración a (m/s²): "))
        if a != 0:
            t = (v - v0) / a
            print("Tiempo t =", t, "segundos")
        else:
            print("La aceleración no puede ser 0 para calcular el tiempo.")

    elif opcion == 4:
        v = float(input("Velocidad final v (m/s): "))
        v0 = float(input("Velocidad inicial v0 (m/s): "))
        t = float(input("Tiempo t (s): "))
        if t != 0:
            a = (v - v0) / t
            print("Aceleración a =", a, "m/s²")
        else:
            print("El tiempo no puede ser 0 para calcular la aceleración.")

    else:
        print("Opción no válida")