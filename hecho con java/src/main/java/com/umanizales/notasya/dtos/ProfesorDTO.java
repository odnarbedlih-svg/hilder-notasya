package com.umanizales.notasya.dtos;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.*;

public class ProfesorDTO {

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Create {
        @NotBlank(message = "El nombre es obligatorio")
        @Size(min = 2, max = 100)
        private String nombre;

        @NotBlank(message = "El tipo de identificación es obligatorio")
        @Size(min = 2, max = 10)
        private String tipoIdentificacion;

        @NotBlank(message = "El número de identificación es obligatorio")
        @Size(min = 4, max = 30)
        private String numeroIdentificacion;

        @NotBlank(message = "La especialidad es obligatoria")
        @Size(min = 2, max = 100)
        private String especialidad;
    }

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Update {
        @Size(min = 2, max = 100)
        private String nombre;

        @Size(min = 2, max = 10)
        private String tipoIdentificacion;

        @Size(min = 4, max = 30)
        private String numeroIdentificacion;

        @Size(min = 2, max = 100)
        private String especialidad;
    }

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Response {
        private Long id;
        private String nombre;
        private String tipoIdentificacion;
        private String numeroIdentificacion;
        private String especialidad;
    }
}
