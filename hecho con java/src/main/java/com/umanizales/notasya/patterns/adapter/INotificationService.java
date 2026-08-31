package com.umanizales.notasya.patterns.adapter;

/**
 * Interfaz objetivo para el envío de notificaciones desacopladas.
 */
public interface INotificationService {
    boolean sendNotification(String recipient, String message);
}
