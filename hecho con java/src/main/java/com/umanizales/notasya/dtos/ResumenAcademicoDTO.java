package com.umanizales.notasya.dtos;

import lombok.*;
import java.util.Map;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ResumenAcademicoDTO {
    private long totalEstudiantes;
    private long totalProfesores;
    private long totalCursos;
    private double promedioGeneral;
    private double tasaAprobacionPorcentaje;
    private int estudiantesConHonor;
    private Map<String, Integer> cursosPorEstado;
}
