[Uploading sistema_gestion_estudiante_final.py…]()
def sistema_gestion_estudiantes():
  
  # Lista donde se almacenarán los nombres de los estudiantes
  estudiantes = []

  # Capacidad máxima del sistema
  capacidad = 1000

  # Variable de control para salir del bucle
  banderaSalir = 0

# Bucle principal del sistema, mientras banderaSalir sea 0, el sistema seguirá ejecutándose
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
      # Opción 1: Agregar nuevo estudiante
      case 1:
        if len(estudiantes) < capacidad:
          nombre = input("Ingrese el nombre del estudiante: ")
          estudiantes.append(nombre)
          print("Estudiante agregado correctamente")
        else:
          print("La capacidad del sistema ha sido alcanzada")

      # Opción 2: Mostrar lista de estudiantes
      case 2:
        if len(estudiantes) == 0:
          print("No hay estudiantes registrados")
        else:
            print("\nLista de estudiantes:")
            for id_estudiante, estudiante in enumerate(estudiantes, start=1):
              print(f"ID: {id_estudiante} - Nombre: {estudiante}")

      # Opción 3: Búsqueda de ID del estudiante
      case 3:
        try:
          id_buscado = int(input("Ingrese el ID del estudiante a buscar: "))
          if id_buscado >= 1 and id_buscado <= len(estudiantes):
            print(f"ID: {id_buscado} - Nombre: {estudiantes[id_buscado - 1]}")
          else:
            print("ID no encontrado")
        except ValueError:
          print("Ingrese un número válido")

      # Opción 4: Salir del sistema
      case 4:
        print("Saliendo del sistema")
        banderaSalir = 1

      # Opción no válida
      case _:
        print("Opción no válida")

sistema_gestion_estudiantes()
