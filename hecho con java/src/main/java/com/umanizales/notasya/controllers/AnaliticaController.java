package com.umanizales.notasya.controllers;

import com.umanizales.notasya.dtos.ResumenAcademicoDTO;
import com.umanizales.notasya.services.AnaliticaService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/analitica")
@Tag(name = "Analítica Académica", description = "Métricas y KPIs globales de rendimiento académico")
@CrossOrigin(origins = "*")
public class AnaliticaController {

    private final AnaliticaService service;

    public AnaliticaController(AnaliticaService service) {
        this.service = service;
    }

    @GetMapping("/resumen")
    @Operation(summary = "Obtener métricas y KPIs académicos globales")
    public ResponseEntity<ResumenAcademicoDTO> obtenerResumen() {
        return ResponseEntity.ok(service.obtenerResumen());
    }
}
