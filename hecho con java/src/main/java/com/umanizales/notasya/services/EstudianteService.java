package com.umanizales.notasya.services;

import com.umanizales.notasya.dtos.EstudianteDTO;
import com.umanizales.notasya.exceptions.ConflictException;
import com.umanizales.notasya.exceptions.ResourceNotFoundException;
import com.umanizales.notasya.models.Estudiante;
import com.umanizales.notasya.repositories.EstudianteRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class EstudianteService {

    private final EstudianteRepository repository;

    public EstudianteService(EstudianteRepository repository) {
        this.repository = repository;
    }

    @Transactional(readOnly = true)
    public List<EstudianteDTO.Response> obtenerTodosLosEstudiantes() {
        return repository.findAll().stream()
                .map(this::mapToResponse)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public EstudianteDTO.Response obtenerEstudiantePorId(Long id) {
        Estudiante e = repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Estudiante con ID " + id + " no encontrado"));
        return mapToResponse(e);
    }

    @Transactional(readOnly = true)
    public EstudianteDTO.Response obtenerEstudiantePorCorreo(String correo) {
        Estudiante e = repository.findByCorreo(correo)
                .orElseThrow(() -> new ResourceNotFoundException("Estudiante con correo '" + correo + "' no encontrado"));
        return mapToResponse(e);
    }

    @Transactional
    public EstudianteDTO.Response crearEstudiante(EstudianteDTO.Create dto) {
        if (repository.existsByCorreo(dto.getCorreo())) {
            throw new ConflictException("Ya existe un estudiante registrado con el correo: " + dto.getCorreo());
        }

        Estudiante e = Estudiante.builder()
                .nombre(dto.getNombre())
                .telefono(dto.getTelefono())
                .correo(dto.getCorreo())
                .build();

        Estudiante guardado = repository.save(e);
        return mapToResponse(guardado);
    }

    @Transactional
    public EstudianteDTO.Response actualizarEstudiante(Long id, EstudianteDTO.Update dto) {
        Estudiante e = repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Estudiante con ID " + id + " no encontrado"));

        if (dto.getCorreo() != null && !dto.getCorreo().equals(e.getCorreo())) {
            if (repository.existsByCorreo(dto.getCorreo())) {
                throw new ConflictException("El correo '" + dto.getCorreo() + "' ya está en uso");
            }
            e.setCorreo(dto.getCorreo());
        }

        if (dto.getNombre() != null) e.setNombre(dto.getNombre());
        if (dto.getTelefono() != null) e.setTelefono(dto.getTelefono());

        Estudiante actualizado = repository.save(e);
        return mapToResponse(actualizado);
    }

    private EstudianteDTO.Response mapToResponse(Estudiante e) {
        return EstudianteDTO.Response.builder()
                .id(e.getId())
                .nombre(e.getNombre())
                .telefono(e.getTelefono())
                .correo(e.getCorreo())
                .build();
    }
}
