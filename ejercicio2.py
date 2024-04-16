class Mision:
    def __init__(self, tipo, reino, solicitante):
        self.tipo = tipo
        self.reino = reino
        self.solicitante = solicitante

class Recurso:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class AsignadorRecursos:
    def __init__(self):
        self.recursos_disponibles = {
            "Valkirias": 100,
            "Unidades": 500
        }

    def asignar_recursos(self, mision):
        if mision.solicitante in ["Odín", "Loki"]:
            prioridad = "Alta"
        else:
            prioridad = "Normal"

        print(f"\nAsignando recursos para la misión de {mision.tipo} en el reino {mision.reino}, solicitada por {mision.solicitante} (Prioridad: {prioridad})")

        if mision.tipo == "defensa":
            valkirias_necesarias = 20
            unidades_necesarias = 100
        elif mision.tipo == "exploración":
            valkirias_necesarias = 10
            unidades_necesarias = 50
        elif mision.tipo == "conquista":
            valkirias_necesarias = 30
            unidades_necesarias = 150
        else:
            print("Tipo de misión no válido.")
            return

        if self.recursos_disponibles["Valkirias"] >= valkirias_necesarias and self.recursos_disponibles["Unidades"] >= unidades_necesarias:
            self.recursos_disponibles["Valkirias"] -= valkirias_necesarias
            self.recursos_disponibles["Unidades"] -= unidades_necesarias
            print(f"Recursos asignados: {valkirias_necesarias} Valkirias, {unidades_necesarias} Unidades")
        else:
            print("No hay suficientes recursos disponibles para esta misión.")

    def mostrar_recursos_disponibles(self):
        print("\nRecursos disponibles:")
        for recurso, cantidad in self.recursos_disponibles.items():
            print(f"{recurso}: {cantidad}")

# Función principal
def main():
    asignador = AsignadorRecursos()

    while True:
        print("\n--- Gestión de Misiones en la Fortaleza de Asgard ---")
        tipo = input("Ingrese el tipo de misión (defensa, exploración, conquista): ").lower()
        reino = input("Ingrese el reino destino: ")
        solicitante = input("Ingrese el dios que solicita la misión (Odín o Loki): ")

        mision = Mision(tipo, reino, solicitante)
        asignador.asignar_recursos(mision)
        asignador.mostrar_recursos_disponibles()

        continuar = input("\n¿Desea ingresar otra solicitud de misión? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()
