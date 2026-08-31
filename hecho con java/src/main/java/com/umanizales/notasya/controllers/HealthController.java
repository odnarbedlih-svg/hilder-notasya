package com.umanizales.notasya.controllers;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/health")
@Tag(name = "Health", description = "Estado de salud del backend Java")
@CrossOrigin(origins = "*")
public class HealthController {

    @GetMapping
    @Operation(summary = "Verificar estado de salud del sistema")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> res = new HashMap<>();
        res.put("status", "online");
        res.put("app_name", "NOTASYA (Java Spring Boot Edition)");
        res.put("version", "1.0.0");
        res.put("engine", "Java 17 + Spring Boot 3 + Spring Data JPA");
        return ResponseEntity.ok(res);
    }
}
