# NOTASYA - Sistema de Gestión Académica (Versión Java)

**Taller de Diseño de Sistemas de Información**  
**Facultad de Ciencias e Ingeniería — Universidad de Manizales**

### Integrantes del Proyecto:
- **Hildebrando Tangarife Cardona**
- **Hildebrando Tangarife Cardona**

---

## 📌 Descripción del Proyecto

**NOTASYA (Java Edition)** es una API RESTful empresarial de alto rendimiento desarrollada con **Java 17**, **Spring Boot 3**, **Spring Data JPA**, **Hibernate** y **PostgreSQL**, estructurada bajo una **arquitectura por capas estricta** y aplicando principios **SOLID** y **Patrones de Diseño GoF**.

El sistema gestiona integralmente el ciclo académico:
* **Estudiantes:** Registro, validación de correo único, actualización y consulta.
* **Profesores:** Registro, validación de documento de identidad único y especialidad docente.
* **Cursos:** Matriculación, asignación docente y registro de calificaciones en rango de 0.0 a 5.0.

---

## 🏛️ Arquitectura por Capas en Java Spring Boot

```text
Cliente HTTP ──> Controller (@RestController) ──> Service (@Service) ──> Repository (JpaRepository) ──> Base de Datos
```
* **`controllers/`**: Enrutamiento de peticiones HTTP, validación `@Valid` y códigos de respuesta.
* **`services/`**: Lógica de negocio (validaciones de existencia, no duplicidad y coherencia transaccional `@Transactional`).
* **`repositories/`**: Interfaces `JpaRepository` con consultas optimizadas y transaccionales hacia la base de datos.
* **`dtos/`**: Clases estáticas `Create`, `Update` y `Response` con validaciones Jakarta (`@NotBlank`, `@Email`, `@DecimalMin`, `@DecimalMax`).
* **`models/`**: Entidades persistentes `@Entity` mapeadas con Hibernate y JPA.

---

## 🧩 Patrones de Diseño Implementados

1. **Creacional - Singleton (`patterns/singleton/`):**
   * Gestionado nativamente por el contenedor de Spring y encapsulado en `DatabaseManagerSingleton`.
2. **Creacional - Factory Method (`patterns/factory/`):**
   * `EntityDTOFactory` centraliza la creación parametrizada de DTOs.
3. **Estructural - Adapter (`patterns/adapter/`):**
   * `EmailNotificationAdapter` adapta el SDK externo `ExternalEmailSDK` a la interfaz `INotificationService`.
4. **Comportamiento - Strategy (`patterns/strategy/`):**
   * `IGradingStrategy` (`StandardGradingStrategy`, `HonorsGradingStrategy`) para evaluación dinámica de calificaciones.

---

## 💎 Principios SOLID en Java

* **S (Single Responsibility):** Controladores enrutan, Servicios validan y Repositorios persisten.
* **O (Open/Closed):** Nuevas estrategias de calificación se añaden implementando `IGradingStrategy` sin modificar código existente.
* **L (Liskov Substitution):** Repositorios y estrategias cumplen estrictamente con sus interfaces base.
* **I (Interface Segregation):** Repositorios e interfaces segregados por entidad.
* **D (Dependency Inversion):** Inyección de dependencias mediante `@Autowired` / Constructor Injection en Spring Boot.

---

## 🚀 Cómo Ejecutar la Aplicación

### Opción 1: Ejecutar con Maven (Línea de comandos)
```bash
cd "C:\Users\LEIDY\Desktop\hecho en java"
mvn spring-boot:run
```

### Opción 2: Ejecutar con Docker Compose
```bash
docker-compose up --build
```

---

## 🌐 Endpoints y Vistas Disponibles

* 🎨 **Dashboard Web Visual:** [http://localhost:8080/](http://localhost:8080/)
* 📄 **Swagger UI Interactivo:** [http://localhost:8080/docs](http://localhost:8080/docs)
* 📊 **Métricas de Analítica:** [http://localhost:8080/api/v1/analitica/resumen](http://localhost:8080/api/v1/analitica/resumen)
* 🩺 **Health Check:** [http://localhost:8080/health](http://localhost:8080/health)
* 🗄️ **Consola H2 Database:** [http://localhost:8080/h2-console](http://localhost:8080/h2-console)
