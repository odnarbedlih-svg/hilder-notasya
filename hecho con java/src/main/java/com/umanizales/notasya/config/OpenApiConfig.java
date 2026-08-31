package com.umanizales.notasya.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class OpenApiConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("NOTASYA - API RESTful de Gestión Académica (Java Edition)")
                        .version("1.0.0")
                        .description("Backend empresarial en Java Spring Boot 3 con Arquitectura por Capas, Patrones GoF y Principios SOLID.\n\n" +
                                "**Integrantes:** Hilder Tangarife y Johntatan Sierra\n" +
                                "**Institución:** Universidad de Manizales - Facultad de Ciencias e Ingeniería")
                        .contact(new Contact()
                                .name("Soporte Académico NOTASYA")
                                .email("jlaguirre@umanizales.edu.co")));
    }
}
