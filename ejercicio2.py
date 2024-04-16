class Mision:
    def __init__(self, tipo, reino, dios):
        self.tipo = tipo
        self.reino = reino
        self.dios = dios

# Función para asignar recursos a una misión
def asignar_recursos(misiones_pendientes, valkirias_disponibles, unidades_disponibles):
    if not misiones_pendientes:
        print("No hay misiones pendientes.")
        return

    # Ordenar las misiones por prioridad
    misiones_pendientes.sort(key=lambda x: x.dios in ["Odín", "Loki"], reverse=True)

    # Procesar cada misión pendiente
    for mision in misiones_pendientes:
        print(f"Atendiendo misión: Tipo - {mision.tipo}, Reino - {mision.reino}, Dios - {mision.dios}")

        # Asignar recursos según el tipo de misión
        if mision.tipo == "defensa":
            valkirias_asignadas = min(valkirias_disponibles, 3)
            unidades_asignadas = min(unidades_disponibles, 100)
        elif mision.tipo == "exploración":
            valkirias_asignadas = min(valkirias_disponibles, 5)
            unidades_asignadas = min(unidades_disponibles, 50)
        elif mision.tipo == "conquista":
            valkirias_asignadas = min(valkirias_disponibles, 10)
            unidades_asignadas = min(unidades_disponibles, 200)
        else:
            print("Tipo de misión no válido.")
            continue

        # Mostrar los recursos asignados
        print(f"Recursos asignados: Valkirias - {valkirias_asignadas}, Unidades - {unidades_asignadas}")

        # Actualizar recursos disponibles
        valkirias_disponibles -= valkirias_asignadas
        unidades_disponibles -= unidades_asignadas

        # Preguntar si hay más misiones pendientes
        continuar = input("¿Hay más misiones pendientes? (s/n): ").lower()
        if continuar != 's':
            break

# Función principal
def main():
    # Recursos iniciales disponibles
    valkirias_disponibles = 20
    unidades_disponibles = 500

    # Lista de misiones pendientes
    misiones_pendientes = [
        Mision("defensa", "Midgard", "Odín"),
        Mision("conquista", "Jotunheim", "Loki"),
        Mision("exploración", "Vanaheim", "Freyr"),
        Mision("defensa", "Asgard", "Thor")
    ]

    # Asignar recursos a las misiones pendientes
    asignar_recursos(misiones_pendientes, valkirias_disponibles, unidades_disponibles)

if __name__ == "__main__":
    main()