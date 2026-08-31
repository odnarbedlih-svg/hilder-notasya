from abc import ABC, abstractmethod

class INotificationService(ABC):
    """
    Interfaz objetivo para el envío de notificaciones.
    """
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> bool:
        pass

class ExternalEmailProviderSDK:
    """
    SDK de un proveedor externo (e.g., SendGrid, AWS SES) con su propia interfaz incompatible.
    """
    def deliver_mail(self, to_address: str, subject: str, body: str) -> str:
        # Simulación de entrega exitosa
        return f"SUCCESS: Mail delivered to {to_address}"

class EmailNotificationAdapter(INotificationService):
    """
    Patrón Estructural: Adapter
    Problema que resuelve: Adapta la interfaz de un proveedor externo de correo
    a la interfaz estándar INotificationService de nuestro sistema, permitiendo intercambiar
    proveedores sin alterar la lógica de negocio.
    """
    def __init__(self, external_sdk: ExternalEmailProviderSDK):
        self.external_sdk = external_sdk

    def send_notification(self, recipient: str, message: str) -> bool:
        res = self.external_sdk.deliver_mail(
            to_address=recipient,
            subject="Notificación del Sistema NOTASYA",
            body=message
        )
        return "SUCCESS" in res
