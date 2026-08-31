package com.umanizales.notasya.config;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.UUID;

/**
 * Middleware / Filtro de Observabilidad y Auditoría Técnica.
 * Inyecta X-Process-Time y X-Request-ID para trazabilidad en microsegundos.
 */
@Component
public class AuditFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {
        long startTime = System.nanoTime();
        String requestId = UUID.randomUUID().toString();

        try {
            filterChain.doFilter(request, response);
        } finally {
            long durationNs = System.nanoTime() - startTime;
            double durationMs = durationNs / 1_000_000.0;
            response.setHeader("X-Process-Time", String.format("%.3f ms", durationMs));
            response.setHeader("X-Request-ID", requestId);
        }
    }
}
