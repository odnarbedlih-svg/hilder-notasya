package com.umanizales.notasya.controllers;

import com.umanizales.notasya.dtos.CursoDTO;
import com.umanizales.notasya.services.CursoService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/cursos")
@Tag(name = "Cursos", description = "Endpoints para la gestión y calificación de cursos")
@CrossOrigin(origins = "*")
public class CursoController {

    private final CursoService service;

    public CursoController(CursoService service) {
        this.service = service;
    }

    @GetMapping
    @Operation(summary = "Obtener todos los cursos")
    public ResponseEntity<List<CursoDTO.Response>> obtenerTodos() {
        return ResponseEntity.ok(service.obtenerTodosLosCursos());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Obtener curso por ID")
    public ResponseEntity<CursoDTO.Response> obtenerPorId(@PathVariable Long id) {
        return ResponseEntity.ok(service.obtenerCursoPorId(id));
    }

    @PostMapping
    @Operation(summary = "Crear nuevo curso")
    public ResponseEntity<CursoDTO.Response> crear(@Valid @RequestBody CursoDTO.Create dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(service.crearCurso(dto));
    }

    @PutMapping("/{id}")
    @Operation(summary = "Actualizar curso existente")
    public ResponseEntity<CursoDTO.Response> actualizar(@PathVariable Long id, @Valid @RequestBody CursoDTO.Update dto) {
        return ResponseEntity.ok(service.actualizarCurso(id, dto));
    }
}
