package com.umanizales.notasya.services;

import com.umanizales.notasya.dtos.ProfesorDTO;
import com.umanizales.notasya.exceptions.ConflictException;
import com.umanizales.notasya.exceptions.ResourceNotFoundException;
import com.umanizales.notasya.models.Profesor;
import com.umanizales.notasya.repositories.ProfesorRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ProfesorService {

    private final ProfesorRepository repository;

    public ProfesorService(ProfesorRepository repository) {
        this.repository = repository;
    }

    @Transactional(readOnly = true)
    public List<ProfesorDTO.Response> obtenerTodosLosProfesores() {
        return repository.findAll().stream()
                .map(this::mapToResponse)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public ProfesorDTO.Response obtenerProfesorPorId(Long id) {
        Profesor p = repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Profesor con ID " + id + " no encontrado"));
        return mapToResponse(p);
    }

    @Transactional(readOnly = true)
    public ProfesorDTO.Response obtenerProfesorPorTipoYNumero(String tipo, String numero) {
        Profesor p = repository.findByTipoIdentificacionAndNumeroIdentificacion(tipo, numero)
                .orElseThrow(() -> new ResourceNotFoundException("Profesor con documento " + tipo + "-" + numero + " no encontrado"));
        return mapToResponse(p);
    }

    @Transactional
    public ProfesorDTO.Response crearProfesor(ProfesorDTO.Create dto) {
        if (repository.existsByTipoIdentificacionAndNumeroIdentificacion(dto.getTipoIdentificacion(), dto.getNumeroIdentificacion())) {
            throw new ConflictException("Ya existe un profesor con el documento " + dto.getTipoIdentificacion() + "-" + dto.getNumeroIdentificacion());
        }

        Profesor p = Profesor.builder()
                .nombre(dto.getNombre())
                .tipoIdentificacion(dto.getTipoIdentificacion())
                .numeroIdentificacion(dto.getNumeroIdentificacion())
                .especialidad(dto.getEspecialidad())
                .build();

        Profesor guardado = repository.save(p);
        return mapToResponse(guardado);
    }

    @Transactional
    public ProfesorDTO.Response actualizarProfesor(Long id, ProfesorDTO.Update dto) {
        Profesor p = repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Profesor con ID " + id + " no encontrado"));

        if (dto.getNombre() != null) p.setNombre(dto.getNombre());
        if (dto.getTipoIdentificacion() != null) p.setTipoIdentificacion(dto.getTipoIdentificacion());
        if (dto.getNumeroIdentificacion() != null) p.setNumeroIdentificacion(dto.getNumeroIdentificacion());
        if (dto.getEspecialidad() != null) p.setEspecialidad(dto.getEspecialidad());

        Profesor actualizado = repository.save(p);
        return mapToResponse(actualizado);
    }

    private ProfesorDTO.Response mapToResponse(Profesor p) {
        return ProfesorDTO.Response.builder()
                .id(p.getId())
                .nombre(p.getNombre())
                .tipoIdentificacion(p.getTipoIdentificacion())
                .numeroIdentificacion(p.getNumeroIdentificacion())
                .especialidad(p.getEspecialidad())
                .build();
    }
}
