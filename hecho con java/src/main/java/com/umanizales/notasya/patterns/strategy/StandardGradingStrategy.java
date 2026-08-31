package com.umanizales.notasya.patterns.strategy;

import java.util.HashMap;
import java.util.Map;

public class StandardGradingStrategy implements IGradingStrategy {
    @Override
    public Map<String, Object> evaluate(double grade) {
        Map<String, Object> result = new HashMap<>();
        result.put("grade", grade);
        result.put("status", grade >= 3.0 ? "Aprobado" : "Reprobado");
        result.put("honors", false);
        return result;
    }
}
