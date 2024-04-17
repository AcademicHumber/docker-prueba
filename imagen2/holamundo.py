while True:
    print("""
    Dime, ¿qué quieres hacer?
    1) Imprimir el nombre del autor
    2) Imprimir el apellido del autor
    3) Cerrar
    """)

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("DIEGO")
    elif opcion == 2:
        print("FUENTES")
    elif opcion == 3:
        break
    else:
        print("Opción incorrecta")
