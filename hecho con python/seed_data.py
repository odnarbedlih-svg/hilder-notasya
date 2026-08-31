import sys, os
sys.path.append(os.path.abspath("."))
from app.config.database import SessionLocal, Base, engine
from app.models.estudiante import Estudiante
from app.models.profesor import Profesor
from app.models.curso import Curso

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    if db.query(Estudiante).count() > 0:
        print("La base de datos ya contiene datos. Saltando seed...")
        db.close()
        return

    print("Insertando datos iniciales de prueba para NOTASYA...")

    # Estudiantes
    e1 = Estudiante(nombre="Hilder Tangarife", telefono="3101234567", correo="hilder@umanizales.edu.co")
    e2 = Estudiante(nombre="Johntatan Sierra", telefono="3209876543", correo="johntatan@umanizales.edu.co")
    e3 = Estudiante(nombre="Laura Valentina Gómez", telefono="3158889900", correo="lgomez@umanizales.edu.co")
    e4 = Estudiante(nombre="Mateo Arango Osorio", telefono="3184443322", correo="marango@umanizales.edu.co")
    db.add_all([e1, e2, e3, e4])
    db.commit()

    # Profesores
    p1 = Profesor(nombre="Dr. Jorge Luis Aguirre", tipo_identificacion="CC", numero_identificacion="1053800900", especialidad="Diseño y Arquitectura de Software")
    p2 = Profesor(nombre="Dra. Claudia Patricia Ortiz", tipo_identificacion="CC", numero_identificacion="1024500600", especialidad="Bases de Datos y Computación en la Nube")
    db.add_all([p1, p2])
    db.commit()

    # Cursos
    c1 = Curso(nombre="Diseño de Sistemas de Información", estudiante_id=e1.id, profesor_id=p1.id, calificacion=4.8)
    c2 = Curso(nombre="Diseño de Sistemas de Información", estudiante_id=e2.id, profesor_id=p1.id, calificacion=5.0)
    c3 = Curso(nombre="Bases de Datos Distribuidas", estudiante_id=e3.id, profesor_id=p2.id, calificacion=4.2)
    c4 = Curso(nombre="Arquitectura Empresarial", estudiante_id=e4.id, profesor_id=p1.id, calificacion=2.8)
    db.add_all([c1, c2, c3, c4])
    db.commit()

    print("¡Datos de prueba insertados con éxito!")
    db.close()

if __name__ == "__main__":
    seed()
