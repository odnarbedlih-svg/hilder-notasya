package com.umanizales.notasya.patterns.singleton;

/**
 * Patrón Creacional: Singleton
 * Problema: Garantiza una única instancia del gestor de configuración de base de datos.
 */
public class DatabaseManagerSingleton {
    private static volatile DatabaseManagerSingleton instance;
    private String databaseUrl;

    private DatabaseManagerSingleton() {
        this.databaseUrl = "jdbc:postgresql://localhost:5432/notasya_db";
    }

    public static DatabaseManagerSingleton getInstance() {
        if (instance == null) {
            synchronized (DatabaseManagerSingleton.class) {
                if (instance == null) {
                    instance = new DatabaseManagerSingleton();
                }
            }
        }
        return instance;
    }

    public String getDatabaseUrl() {
        return databaseUrl;
    }
}
