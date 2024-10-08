tareas = [] 

def agregar_tarea():
    """Función para agregar una nueva tarea."""
    
    codigo_tarea = input("Ingrese el código de la tarea: ")
    nombre_tarea = input("Ingrese el nombre de la tarea: ")

    while True:
        try:
            puntaje = float(input("Ingrese la nota (de 0 a 5): "))
            if 0 <= puntaje <= 5:
                break
            else:
                print("La nota debe estar entre 0 y 5.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    while True:
        try:
            tipo_tarea = int(input("Seleccione el tipo de tarea (1: Examen, 2: Proyecto, 3: Tarea práctica): "))
            if tipo_tarea in [1, 2, 3]:
                break
            else:
                print("Ingrese una opción válida (1, 2 o 3).")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    tarea = {
        'Código': codigo_tarea,
        'Nombre': nombre_tarea,
        'Nota': puntaje,
        'Tipo': obtener_tipo_tarea(tipo_tarea)
    }
    
    tareas.append(tarea)
    print(f"Tarea '{nombre_tarea}' registrada correctamente.")


def obtener_tipo_tarea(tipo_tarea):
    "Función para clasificar el tipo de tarea."
    if tipo_tarea == 1:
        return "Examen"
    elif tipo_tarea == 2:
        return "Proyecto"
    elif tipo_tarea == 3:
        return "Tarea práctica"


def listar_tareas():
    """Función para mostrar las tareas registradas."""
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\nTareas registradas:")
        for tarea in tareas:
            print(f"Código: {tarea['Código']}, Nombre: {tarea['Nombre']}, Nota: {tarea['Nota']}, Tipo: {tarea['Tipo']}")


def ciclo_registro():
    """Función para ejecutar el ciclo de registro de tareas."""
    while True:
        opcion = input("\n¿Desea agregar una nueva tarea? (s/n): ").lower()
        if opcion == 's':
            agregar_tarea()
        elif opcion == 'n':
            break
        else:
            print("Opción inválida. Por favor, ingrese 's' para sí o 'n' para no.")
    
    listar_tareas()

ciclo_registro()