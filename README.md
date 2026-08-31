# NOTASYA - Sistema de Gestión Académica

**Taller de Diseño de Sistemas de Información**  
**Facultad de Ciencias e Ingeniería — Universidad de Manizales**

### Integrantes del Proyecto:
- **Hilder Tangarife**
- **Johntatan Sierra**

---

## 📌 Descripción del Proyecto

**NOTASYA** es una API RESTful empresarial desarrollada con **FastAPI**, **Python 3**, **SQLAlchemy** y **PostgreSQL**, diseñada bajo una **arquitectura por capas estricta** y aplicando principios **SOLID** y **Patrones de Diseño de Software** (GoF).

El sistema permite gestionar de manera integral el ciclo académico gestionando:
* **Estudiantes:** Registro, actualización y consulta por correo/ID.
* **Profesores:** Registro, actualización y consulta por tipo y número de documento.
* **Cursos:** Matriculación, asignación docente y registro de calificaciones con validación estricta de reglas de negocio.

---

## 🏛️ Arquitectura por Capas

El flujo de una solicitud sigue estrictamente la separación de responsabilidades:
```text
Cliente (HTTP) ──> Controlador (FastAPI) ──> Servicio (Reglas de Negocio) ──> Repositorio (SQLAlchemy) ──> PostgreSQL
```
* **`app/controllers/`**: Enruta las solicitudes HTTP, gestiona los códigos de estado y serializa las respuestas con DTOs.
* **`app/services/`**: Implementa la lógica de negocio (validación de existencias, no duplicidad y coherencia de datos).
* **`app/repositories/`**: Encapsula exclusivamente las consultas y persistencia hacia la base de datos PostgreSQL.
* **`app/dtos/`**: Esquemas Pydantic para validación estricta de tipos en entradas y salidas.
* **`app/models/`**: Entidades mapeadas mediante SQLAlchemy ORM.

---

## 🧩 Patrones de Diseño Implementados

1. **Creacional - Singleton (`app/patterns/singleton.py`):**
   * *Problema:* Evita la sobrecarga y fuga de conexiones en el pool de PostgreSQL.
   * *Solución:* Mantiene una única instancia del motor `engine` y `SessionLocal`.
2. **Creacional - Factory Method (`app/patterns/factory.py`):**
   * *Problema:* Centraliza la creación y validación de DTOs según el tipo de entidad dinámica.
3. **Estructural - Adapter (`app/patterns/adapter.py`):**
   * *Problema:* Aísla la aplicación de proveedores externos de correo/mensajería.
   * *Solución:* Adapta interfaces incompatibles de SDKs externos a la interfaz estándar `INotificationService`.
4. **Comportamiento - Strategy (`app/patterns/strategy.py`):**
   * *Problema:* Permite variar los algoritmos de evaluación y cálculo de calificaciones (Estándar, Honores) en tiempo de ejecución.

---

## 💎 Evidencia de Principios SOLID

* **S (Single Responsibility):** Los controladores solo enrutan, los servicios solo validan reglas y los repositorios solo interactúan con la BD.
* **O (Open/Closed):** Nuevas estrategias de calificación o adaptadores de notificación se extienden sin modificar el código base.
* **L (Liskov Substitution):** Los repositorios implementan `IBaseRepository[T]` y pueden ser sustituidos de forma transparente.
* **I (Interface Segregation):** Interfaces pequeñas y enfocadas por entidad (`EstudianteRepository`, `ProfesorRepository`, `CursoRepository`).
* **D (Dependency Inversion):** Los controladores y servicios reciben sus dependencias inyectadas mediante `Depends()` de FastAPI.

---

## 📊 Diagramas UML (PlantUML)

Los diagramas se encuentran en la carpeta `app/docs/`:
* `diagrama_clases.puml`: Modelo conceptual con clases, atributos, métodos y asociaciones.
* `diagrama_secuencia_consulta.puml`: Flujo de consulta GET por correo con todas las capas.
* `diagrama_secuencia_creacion.puml`: Flujo de creación POST de Curso con validación de Estudiante y Profesor.
* `diagrama_despliegue.puml`: Arquitectura de despliegue en contenedores y conexión a PostgreSQL.

---

## 🚀 Instalación y Ejecución Local

### 1. Clonar el repositorio y preparar entorno:
```bash
git clone https://github.com/hilder-tangarife/hilder-notasya.git
cd hilder-notasya

# Crear entorno virtual
python -m venv venv
# Activar en Windows:
.\venv\Scripts\activate
# Activar en Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar variables de entorno:
Copiar `.env.example` a `.env` y configurar la URL de PostgreSQL:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/notasya_db
```

### 3. Ejecutar la API:
```bash
uvicorn app.main:app --reload --port 8000
```

* **Documentación Interactiva Swagger:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Documentación ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
* **Endpoint de Salud:** [http://localhost:8000/health](http://localhost:8000/health)

---

## 🧪 Ejecución de Pruebas Unitarias y de Integración

Para ejecutar la suite completa de pruebas:
```bash
pytest -v
```
