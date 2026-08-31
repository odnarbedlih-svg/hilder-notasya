package com.umanizales.notasya.controllers;

import com.umanizales.notasya.dtos.EstudianteDTO;
import com.umanizales.notasya.services.EstudianteService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/estudiantes")
@Tag(name = "Estudiantes", description = "Endpoints para la gestión de estudiantes")
@CrossOrigin(origins = "*")
public class EstudianteController {

    private final EstudianteService service;

    public EstudianteController(EstudianteService service) {
        this.service = service;
    }

    @GetMapping
    @Operation(summary = "Obtener todos los estudiantes")
    public ResponseEntity<List<EstudianteDTO.Response>> obtenerTodos() {
        return ResponseEntity.ok(service.obtenerTodosLosEstudiantes());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Obtener estudiante por ID")
    public ResponseEntity<EstudianteDTO.Response> obtenerPorId(@PathVariable Long id) {
        return ResponseEntity.ok(service.obtenerEstudiantePorId(id));
    }

    @GetMapping("/correo/{correo}")
    @Operation(summary = "Obtener estudiante por Correo")
    public ResponseEntity<EstudianteDTO.Response> obtenerPorCorreo(@PathVariable String correo) {
        return ResponseEntity.ok(service.obtenerEstudiantePorCorreo(correo));
    }

    @PostMapping
    @Operation(summary = "Crear nuevo estudiante")
    public ResponseEntity<EstudianteDTO.Response> crear(@Valid @RequestBody EstudianteDTO.Create dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(service.crearEstudiante(dto));
    }

    @PutMapping("/{id}")
    @Operation(summary = "Actualizar estudiante existente")
    public ResponseEntity<EstudianteDTO.Response> actualizar(@PathVariable Long id, @Valid @RequestBody EstudianteDTO.Update dto) {
        return ResponseEntity.ok(service.actualizarEstudiante(id, dto));
    }
}
