import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso):
        self.vertices[vertice1][vertice2] = peso
        self.vertices[vertice2][vertice1] = peso

    def dijkstra(self, inicio, destino):
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, inicio))
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[inicio] = 0
        visitados = set()

        while cola_prioridad:
            distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

            if vertice_actual == destino:
                break

            if vertice_actual in visitados:
                continue

            visitados.add(vertice_actual)

            for vecino, peso in self.vertices[vertice_actual].items():
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return distancias[destino]

# Crear el grafo
red_ferrocarriles = Grafo()

# Agregar ciudades y desvíos
red_ferrocarriles.agregar_vertice("Rivendell")
red_ferrocarriles.agregar_vertice("Minas Tirith")
red_ferrocarriles.agregar_vertice("Bree")
red_ferrocarriles.agregar_vertice("Moria")
red_ferrocarriles.agregar_vertice("Gondor")

# Agregar rutas (aristas) entre ciudades y desvíos
red_ferrocarriles.agregar_arista("Rivendell", "Minas Tirith", 10)
red_ferrocarriles.agregar_arista("Rivendell", "Bree", 5)
red_ferrocarriles.agregar_arista("Minas Tirith", "Bree", 15)
red_ferrocarriles.agregar_arista("Minas Tirith", "Gondor", 20)
red_ferrocarriles.agregar_arista("Bree", "Moria", 12)
red_ferrocarriles.agregar_arista("Moria", "Gondor", 8)

# Encontrar la ruta más corta entre Rivendell y Minas Tirith
inicio = "Rivendell"
destino = "Minas Tirith"
distancia_minima = red_ferrocarriles.dijkstra(inicio, destino)
print(f"La distancia mínima entre {inicio} y {destino} es de {distancia_minima} millas.")
