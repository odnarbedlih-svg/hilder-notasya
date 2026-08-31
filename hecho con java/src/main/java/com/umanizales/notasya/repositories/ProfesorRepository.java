package com.umanizales.notasya.repositories;

import com.umanizales.notasya.models.Profesor;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface ProfesorRepository extends JpaRepository<Profesor, Long> {
    Optional<Profesor> findByTipoIdentificacionAndNumeroIdentificacion(String tipoIdentificacion, String numeroIdentificacion);
    boolean existsByTipoIdentificacionAndNumeroIdentificacion(String tipoIdentificacion, String numeroIdentificacion);
}
