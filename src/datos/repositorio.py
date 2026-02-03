class RepositorioTareas:
    """
    Gestiona el almacenamiento en memoria usando un diccionario.
    """
    def __init__(self):
        self._tareas = {}  # Diccionario {id: tarea}

    def guardar(self, tarea):
        self._tareas[tarea.id] = tarea

    def obtener_todas(self):
        return list(self._tareas.values())

    def generar_id(self):
        """Genera un ID autoincremental."""
        return max(self._tareas.keys(), default=0) + 1