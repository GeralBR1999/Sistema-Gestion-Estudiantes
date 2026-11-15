def sistema_gestion_estudiantes():
  estudiantes = []
  capacidad = 1000
  banderaSalir = 0

  while banderaSalir == 0:
    print("------------------------") 
    print("FUNDACIÓN UNIVERSITARIA COMPENSAR")
    print("REGISTRO DE ESTUDIANTES")
    print("(1) Agregar nuevo estudiante")
    print("(2) Mostrar lista de estudiantes")
    print("(3) Búsqueda de ID del estudiante")
    print("(4) Salir")
    print("------------------------")
    
    try:
      opc = int(input("Ingrese una opción: "))
    except ValueError:
        print("Debe ingresar un número")
        continue

    match opc:
      case 1:
        if len(estudiantes) < capacidad:
          nombre = input("Ingrese el nombre del estudiante: ")
          estudiantes.append(nombre)
          print("Estudiante agregado correctamente")
        else:
          print("La capacidad del sistema ha sido alcanzada")

      case 2:
        if len(estudiantes) == 0:
          print("No hay estudiantes registrados")
        else:
            print("\nLista de estudiantes:")
            for id_estudiante, estudiante in enumerate(estudiantes, start=1):
              print(f"ID: {id_estudiante} - Nombre: {estudiante}")
      
      case 3:
        try:
          id_buscado = int(input("Ingrese el ID del estudiante a buscar: "))
          if id_buscado >= 1 and id_buscado <= len(estudiantes):
            print(f"ID: {id_buscado} - Nombre: {estudiantes[id_buscado - 1]}")
          else:
            print("ID no encontrado")
        except ValueError:
          print("Ingrese un número válido")

      case 4:
        print("Saliendo del sistema")
        banderaSalir = 1

      case _:
        print("Opción no válida")

sistema_gestion_estudiantes()