# Clase representando un videojuego, indicando el uso de constructores y destructores.

class Videojuego:
    # Constructor se llama automáticamente al crear un objeto de esta clase
    def __init__(self, nombre, genero, jugadores):
        self.nombre = nombre          # Atributo: nombre del videojuego
        self.genero = genero          # Atributo: género del videojuego
        self.jugadores = jugadores    # Atributo: número de jugadores

        # Mensaje verificando que el juego se ha inicializado correctamente
        print(f" Se ha iniciado el videojuego '{self.nombre}' de género '{self.genero}' con capacidad para {self.jugadores} jugador(es).")

    # mostrando detalles del juego
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Género: {self.genero}")
        print(f"Número de jugadores: {self.jugadores}")

    # Destructor se llama automáticamente cuando el objeto ya no se usa o se destruye manualmente
    def __del__(self):
        # Mensaje indicando que el juego ha sido cerrado y se han liberado recursos
        print(f" El videojuego '{self.nombre}' ha sido cerrado. Recursos liberados.")


# Crear una instancia de la clase Videojuego
juego1 = Videojuego("Leyenda del Dragón", "Aventura", 2)

# Llamar al método para mostrar información del juego
juego1.mostrar_info()

# El objeto se elimina manualmente (también se eliminaría automáticamente al finalizar el programa)
del juego1