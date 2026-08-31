package com.umanizales.notasya.dtos;

import jakarta.validation.constraints.*;
import lombok.*;

public class CursoDTO {

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Create {
        @NotBlank(message = "El nombre de la asignatura es obligatorio")
        @Size(min = 2, max = 100)
        private String nombre;

        @NotNull(message = "El ID del estudiante es obligatorio")
        @Positive
        private Long estudianteId;

        @NotNull(message = "El ID del profesor es obligatorio")
        @Positive
        private Long profesorId;

        @NotNull(message = "La calificación es obligatoria")
        @DecimalMin(value = "0.0", message = "La calificación mínima es 0.0")
        @DecimalMax(value = "5.0", message = "La calificación máxima es 5.0")
        private Double calificacion;
    }

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Update {
        @Size(min = 2, max = 100)
        private String nombre;

        @Positive
        private Long estudianteId;

        @Positive
        private Long profesorId;

        @DecimalMin(value = "0.0")
        @DecimalMax(value = "5.0")
        private Double calificacion;
    }

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Response {
        private Long id;
        private String nombre;
        private Long estudianteId;
        private String estudianteNombre;
        private Long profesorId;
        private String profesorNombre;
        private Double calificacion;
    }
}
