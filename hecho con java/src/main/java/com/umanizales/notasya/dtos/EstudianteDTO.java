package com.umanizales.notasya.dtos;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.*;

public class EstudianteDTO {

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Create {
        @NotBlank(message = "El nombre es obligatorio")
        @Size(min = 2, max = 100, message = "El nombre debe tener entre 2 y 100 caracteres")
        private String nombre;

        @NotBlank(message = "El teléfono es obligatorio")
        @Size(min = 7, max = 20, message = "El teléfono debe tener entre 7 y 20 caracteres")
        private String telefono;

        @NotBlank(message = "El correo es obligatorio")
        @Email(message = "Formato de correo electrónico inválido")
        private String correo;
    }

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Update {
        @Size(min = 2, max = 100)
        private String nombre;

        @Size(min = 7, max = 20)
        private String telefono;

        @Email(message = "Formato de correo electrónico inválido")
        private String correo;
    }

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    public static class Response {
        private Long id;
        private String nombre;
        private String telefono;
        private String correo;
    }
}
