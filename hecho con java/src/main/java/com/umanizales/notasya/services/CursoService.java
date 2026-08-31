package com.umanizales.notasya.services;

import com.umanizales.notasya.dtos.CursoDTO;
import com.umanizales.notasya.exceptions.ResourceNotFoundException;
import com.umanizales.notasya.models.Curso;
import com.umanizales.notasya.models.Estudiante;
import com.umanizales.notasya.models.Profesor;
import com.umanizales.notasya.repositories.CursoRepository;
import com.umanizales.notasya.repositories.EstudianteRepository;
import com.umanizales.notasya.repositories.ProfesorRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class CursoService {

    private final CursoRepository cursoRepository;
    private final EstudianteRepository estudianteRepository;
    private final ProfesorRepository profesorRepository;

    public CursoService(CursoRepository cursoRepository, EstudianteRepository estudianteRepository, ProfesorRepository profesorRepository) {
        this.cursoRepository = cursoRepository;
        this.estudianteRepository = estudianteRepository;
        this.profesorRepository = profesorRepository;
    }

    @Transactional(readOnly = true)
    public List<CursoDTO.Response> obtenerTodosLosCursos() {
        return cursoRepository.findAll().stream()
                .map(this::mapToResponse)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public CursoDTO.Response obtenerCursoPorId(Long id) {
        Curso c = cursoRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Curso con ID " + id + " no encontrado"));
        return mapToResponse(c);
    }

    @Transactional
    public CursoDTO.Response crearCurso(CursoDTO.Create dto) {
        Estudiante est = estudianteRepository.findById(dto.getEstudianteId())
                .orElseThrow(() -> new ResourceNotFoundException("Estudiante con ID " + dto.getEstudianteId() + " no existe"));

        Profesor prof = profesorRepository.findById(dto.getProfesorId())
                .orElseThrow(() -> new ResourceNotFoundException("Profesor con ID " + dto.getProfesorId() + " no existe"));

        Curso curso = Curso.builder()
                .nombre(dto.getNombre())
                .estudiante(est)
                .profesor(prof)
                .calificacion(dto.getCalificacion())
                .build();

        Curso guardado = cursoRepository.save(curso);
        return mapToResponse(guardado);
    }

    @Transactional
    public CursoDTO.Response actualizarCurso(Long id, CursoDTO.Update dto) {
        Curso c = cursoRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Curso con ID " + id + " no encontrado"));

        if (dto.getNombre() != null) c.setNombre(dto.getNombre());
        if (dto.getCalificacion() != null) c.setCalificacion(dto.getCalificacion());

        if (dto.getEstudianteId() != null) {
            Estudiante est = estudianteRepository.findById(dto.getEstudianteId())
                    .orElseThrow(() -> new ResourceNotFoundException("Estudiante con ID " + dto.getEstudianteId() + " no existe"));
            c.setEstudiante(est);
        }

        if (dto.getProfesorId() != null) {
            Profesor prof = profesorRepository.findById(dto.getProfesorId())
                    .orElseThrow(() -> new ResourceNotFoundException("Profesor con ID " + dto.getProfesorId() + " no existe"));
            c.setProfesor(prof);
        }

        Curso actualizado = cursoRepository.save(c);
        return mapToResponse(actualizado);
    }

    private CursoDTO.Response mapToResponse(Curso c) {
        return CursoDTO.Response.builder()
                .id(c.getId())
                .nombre(c.getNombre())
                .estudianteId(c.getEstudiante().getId())
                .estudianteNombre(c.getEstudiante().getNombre())
                .profesorId(c.getProfesor().getId())
                .profesorNombre(c.getProfesor().getNombre())
                .calificacion(c.getCalificacion())
                .build();
    }
}
