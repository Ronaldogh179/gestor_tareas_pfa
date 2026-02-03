from src.logica.tarea import Tarea

class GestorTareas:
    """
    Controlador que maneja las reglas de negocio.
    """
    def __init__(self, repo):
        self.repo = repo

    def agregar_tarea(self, descripcion: str):
        # Validar duplicados (case-insensitive)
        for t in self.repo.obtener_todas():
            if t.descripcion.lower() == descripcion.lower():
                raise ValueError("Ya existe una tarea con esa descripción.")
        
        nuevo_id = self.repo.generar_id()
        nueva_tarea = Tarea(nuevo_id, descripcion)
        self.repo.guardar(nueva_tarea)
        print(f"--> Tarea agregada: {descripcion}")