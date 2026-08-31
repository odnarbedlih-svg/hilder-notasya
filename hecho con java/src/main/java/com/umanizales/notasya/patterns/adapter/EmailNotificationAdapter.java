package com.umanizales.notasya.patterns.adapter;

/**
 * Patrón Estructural: Adapter
 * Problema: Adapta la API del SDK externo a nuestra interfaz INotificationService.
 */
public class EmailNotificationAdapter implements INotificationService {

    private final ExternalEmailSDK externalSDK;

    public EmailNotificationAdapter(ExternalEmailSDK externalSDK) {
        this.externalSDK = externalSDK;
    }

    @Override
    public boolean sendNotification(String recipient, String message) {
        String res = externalSDK.deliverMail(recipient, "Notificación NOTASYA", message);
        return res != null && res.contains("SUCCESS");
    }
}
