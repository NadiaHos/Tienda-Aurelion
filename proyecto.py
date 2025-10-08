
## Menu principal del proyecto
salir = False
while not salir:
    print("1. Mostrar problema y solucion")
    print("2. Mostrar pseudocodigo")
    print("3. Mostrar datasets utilizados (5 primeras filas)")
    print("4. Mostrar diagrama de flujo")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
   
    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            # Abre el archivo problema_solucion.txt y lo muestra por pantalla
        case "2":
            print("Opcion 2 seleccionada")
            # Abre el archivo pseudocodigo.txt y lo muestra por pantalla
        case "3":
            print("Opcion 3 seleccionada")
            # Abre los archivos datasets y muestra las 5 primeras filas de cada uno
        case "4":
            print("Opcion 4 seleccionada")
            # Abre el archivo diagrama_flujo.png y lo muestra por pantalla
        case "5":
            salir = True
        case _:
            print("Opcion no valida")

