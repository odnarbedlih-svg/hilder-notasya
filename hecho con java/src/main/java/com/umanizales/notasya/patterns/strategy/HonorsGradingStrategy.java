package com.umanizales.notasya.patterns.strategy;

import java.util.HashMap;
import java.util.Map;

public class HonorsGradingStrategy implements IGradingStrategy {
    @Override
    public Map<String, Object> evaluate(double grade) {
        Map<String, Object> result = new HashMap<>();
        boolean passed = grade >= 3.0;
        boolean honors = grade >= 4.5;
        result.put("grade", grade);
        result.put("status", honors ? "Excelente con Mención de Honor" : (passed ? "Aprobado" : "Reprobado"));
        result.put("honors", honors);
        return result;
    }
}
