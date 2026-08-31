package com.umanizales.notasya.patterns.strategy;

import java.util.Map;

/**
 * Contexto del patrón de comportamiento Strategy.
 */
public class AcademicEvaluatorContext {
    private IGradingStrategy strategy;

    public AcademicEvaluatorContext(IGradingStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(IGradingStrategy strategy) {
        this.strategy = strategy;
    }

    public Map<String, Object> executeEvaluation(double grade) {
        return this.strategy.evaluate(grade);
    }
}
