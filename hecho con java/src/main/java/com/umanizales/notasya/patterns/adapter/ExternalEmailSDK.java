package com.umanizales.notasya.patterns.adapter;

/**
 * SDK simulado de proveedor externo incompatible.
 */
public class ExternalEmailSDK {
    public String deliverMail(String toAddress, String subject, String body) {
        return "SUCCESS: Delivered to " + toAddress;
    }
}
