package com.umanizales.notasya.controllers;

import com.umanizales.notasya.dtos.ProfesorDTO;
import com.umanizales.notasya.services.ProfesorService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/profesores")
@Tag(name = "Profesores", description = "Endpoints para la gestión de profesores")
@CrossOrigin(origins = "*")
public class ProfesorController {

    private final ProfesorService service;

    public ProfesorController(ProfesorService service) {
        this.service = service;
    }

    @GetMapping
    @Operation(summary = "Obtener todos los profesores")
    public ResponseEntity<List<ProfesorDTO.Response>> obtenerTodos() {
        return ResponseEntity.ok(service.obtenerTodosLosProfesores());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Obtener profesor por ID")
    public ResponseEntity<ProfesorDTO.Response> obtenerPorId(@PathVariable Long id) {
        return ResponseEntity.ok(service.obtenerProfesorPorId(id));
    }

    @GetMapping("/identificacion/{tipo}/{numero}")
    @Operation(summary = "Obtener profesor por tipo y número de identificación")
    public ResponseEntity<ProfesorDTO.Response> obtenerPorIdentificacion(@PathVariable String tipo, @PathVariable String numero) {
        return ResponseEntity.ok(service.obtenerProfesorPorTipoYNumero(tipo, numero));
    }

    @PostMapping
    @Operation(summary = "Crear nuevo profesor")
    public ResponseEntity<ProfesorDTO.Response> crear(@Valid @RequestBody ProfesorDTO.Create dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(service.crearProfesor(dto));
    }

    @PutMapping("/{id}")
    @Operation(summary = "Actualizar profesor existente")
    public ResponseEntity<ProfesorDTO.Response> actualizar(@PathVariable Long id, @Valid @RequestBody ProfesorDTO.Update dto) {
        return ResponseEntity.ok(service.actualizarProfesor(id, dto));
    }
}
