# NOTASYA - Sistema de Gestión Académica

**Taller de Diseño de Sistemas de Información**  
**Facultad de Ciencias e Ingeniería — Universidad de Manizales**

### Integrantes del Proyecto:
* **Hilder Tangarife**
* **Johntatan Sierra**

---

## 📌 Presentación del Repositorio

Este repositorio contiene la solución completa al **Taller de Diseño de Sistemas de Información**, implementada y documentada en **dos arquitecturas tecnológicas empresariales**:

```text
hilder-notasya/
│── hecho con python/        # Implementación en Python 3 + FastAPI + SQLAlchemy + PostgreSQL
│── hecho con java/          # Implementación en Java 17 + Spring Boot 3 + Spring Data JPA + Hibernate
│── .gitignore
└── README.md                # Este documento de arquitectura
```

Ambas versiones cumplen con:
1. **Arquitectura por Capas Estricta:** `DTOs -> Controladores -> Servicios -> Repositorios -> Base de Datos`.
2. **Patrones de Diseño GoF:** *Singleton*, *Factory Method*, *Adapter* y *Strategy*.
3. **Principios SOLID:** Demostrados y justificados en el código y pruebas.
4. **Diagramas UML en PlantUML:** Clases, Secuencia de Consulta, Secuencia de Creación y Despliegue.
5. **Dashboard Web Reactivo:** Interfaz visual con métricas, gráficos en vivo y registro.
6. **Módulo de Analítica Académica:** Cálculo de promedios, tasas de aprobación y menciones de honor.
7. **Observabilidad:** Middleware con encabezados `X-Process-Time` y `X-Request-ID`.

---

## 🐍 1. Versión en Python (`hecho con python/`)

### Tecnologías:
* **FastAPI**, **Uvicorn**, **SQLAlchemy ORM**, **Pydantic V2**, **PostgreSQL / SQLite**, **Pytest**.

### Cómo Ejecutar:
```bash
cd "hecho con python"

# Instalar dependencias
pip install -r requirements.txt

# Poblar datos iniciales
python seed_data.py

# Iniciar servidor
python -m uvicorn app.main:app --reload --port 8000
```
* 🎨 **Dashboard Web:** [http://localhost:8000/dashboard](http://localhost:8000/dashboard)
* 📄 **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* 🧪 **Ejecutar Pruebas:** `pytest -v`

---

## ☕ 2. Versión en Java (`hecho con java/`)

### Tecnologías:
* **Java 17**, **Spring Boot 3.2**, **Spring Data JPA**, **Hibernate**, **PostgreSQL / H2**, **Jakarta Validation**, **Springdoc OpenAPI**.

### Cómo Ejecutar:
```bash
cd "hecho con java"

# Ejecutar con Maven
mvn spring-boot:run
```
* 🎨 **Dashboard Web:** [http://localhost:8080/](http://localhost:8080/)
* 📄 **Swagger UI:** [http://localhost:8080/docs](http://localhost:8080/docs)
* 🗄️ **Consola H2:** [http://localhost:8080/h2-console](http://localhost:8080/h2-console)

---

## 🧩 Patrones de Diseño Implementados en Ambos Proyectos

1. **Creacional - Singleton:** Garantiza una única instancia del motor/conexión a la base de datos para optimizar recursos y evitar fugas en el pool de conexiones.
2. **Creacional - Factory Method:** Centraliza la creación parametrizada de esquemas de transferencia (DTOs).
3. **Estructural - Adapter:** Desacopla la lógica del sistema adaptando SDKs externos a una interfaz `INotificationService`.
4. **Comportamiento - Strategy:** Permite intercambiar en tiempo de ejecución las políticas de calificación y evaluación académica (Estándar vs. Mención de Honor).

---

## 💎 Justificación de Principios SOLID

* **S (Single Responsibility):** Los controladores únicamente gestionan el protocolo HTTP; los servicios contienen exclusivamente las reglas de negocio; los repositorios encapsulan el acceso a la base de datos.
* **O (Open/Closed):** Nuevas estrategias de calificación o canales de notificación se añaden implementando contratos sin modificar el núcleo del software.
* **L (Liskov Substitution):** Los repositorios y estrategias implementan interfaces genéricas abstractas y pueden sustituirse sin romper el comportamiento esperado.
* **I (Interface Segregation):** Interfaces pequeñas y cohesivas segregadas por responsabilidad y entidad.
* **D (Dependency Inversion):** Los módulos de alto nivel dependen de abstracciones inyectadas mediante inyección de dependencias (`Depends` en FastAPI / `@Autowired` en Spring Boot).
