package com.umanizales.notasya.patterns.strategy;

import java.util.Map;

/**
 * Interfaz común para el patrón Strategy de evaluación académica.
 */
public interface IGradingStrategy {
    Map<String, Object> evaluate(double grade);
}
