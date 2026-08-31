package com.umanizales.notasya.services;

import com.umanizales.notasya.dtos.ResumenAcademicoDTO;
import com.umanizales.notasya.models.Curso;
import com.umanizales.notasya.patterns.strategy.AcademicEvaluatorContext;
import com.umanizales.notasya.patterns.strategy.HonorsGradingStrategy;
import com.umanizales.notasya.repositories.CursoRepository;
import com.umanizales.notasya.repositories.EstudianteRepository;
import com.umanizales.notasya.repositories.ProfesorRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class AnaliticaService {

    private final EstudianteRepository estudianteRepository;
    private final ProfesorRepository profesorRepository;
    private final CursoRepository cursoRepository;
    private final AcademicEvaluatorContext evaluator;

    public AnaliticaService(EstudianteRepository estRepo, ProfesorRepository profRepo, CursoRepository cursoRepo) {
        this.estudianteRepository = estRepo;
        this.profesorRepository = profRepo;
        this.cursoRepository = cursoRepo;
        this.evaluator = new AcademicEvaluatorContext(new HonorsGradingStrategy());
    }

    @Transactional(readOnly = true)
    public ResumenAcademicoDTO obtenerResumen() {
        long totalEst = estudianteRepository.count();
        long totalProf = profesorRepository.count();
        List<Curso> cursos = cursoRepository.findAll();
        long totalCursos = cursos.size();

        if (totalCursos == 0) {
            Map<String, Integer> emptyMap = new HashMap<>();
            emptyMap.put("Aprobados", 0);
            emptyMap.put("Reprobados", 0);
            return ResumenAcademicoDTO.builder()
                    .totalEstudiantes(totalEst)
                    .totalProfesores(totalProf)
                    .totalCursos(0)
                    .promedioGeneral(0.0)
                    .tasaAprobacionPorcentaje(0.0)
                    .estudiantesConHonor(0)
                    .cursosPorEstado(emptyMap)
                    .build();
        }

        double suma = cursos.stream().mapToDouble(Curso::getCalificacion).sum();
        double promedio = Math.round((suma / totalCursos) * 100.0) / 100.0;

        int aprobados = 0;
        int conHonor = 0;
        int reprobados = 0;

        for (Curso c : cursos) {
            Map<String, Object> eval = evaluator.executeEvaluation(c.getCalificacion());
            boolean isHonor = (boolean) eval.get("honors");
            if (isHonor) {
                conHonor++;
                aprobados++;
            } else if (c.getCalificacion() >= 3.0) {
                aprobados++;
            } else {
                reprobados++;
            }
        }

        double tasa = Math.round(((double) aprobados / totalCursos) * 1000.0) / 10.0;

        Map<String, Integer> estados = new HashMap<>();
        estados.put("Aprobados", aprobados);
        estados.put("Reprobados", reprobados);
        estados.put("Con Mención de Honor", conHonor);

        return ResumenAcademicoDTO.builder()
                .totalEstudiantes(totalEst)
                .totalProfesores(totalProf)
                .totalCursos(totalCursos)
                .promedioGeneral(promedio)
                .tasaAprobacionPorcentaje(tasa)
                .estudiantesConHonor(conHonor)
                .cursosPorEstado(estados)
                .build();
    }
}
