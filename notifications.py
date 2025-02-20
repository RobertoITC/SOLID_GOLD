from abc import ABC, abstractmethod
from typing import List
import smtplib
from email.message import EmailMessage
from twilio.rest import Client

# Interfaz de Notificación (Abstracción)
class Notification(ABC):
    @abstractmethod
    def send(self, message: str, to: str) -> bool:
        """
        Envía una notificación.
        
        Args:
            message (str): El mensaje a enviar
            to (str): Destinatario del mensaje
            
        Returns:
            bool: True si se envió correctamente, False en caso contrario
        """
        pass

# Implementación de Notificación por Email
class EmailNotification(Notification):
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send(self, message: str, to: str) -> bool:
        try:
            # Crear el mensaje
            email = EmailMessage()
            email.set_content(message)
            email['Subject'] = 'Notificación del Sistema'
            email['From'] = self.username
            email['To'] = to

            # Enviar el email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(email)
            return True
        except Exception as e:
            print(f"Error al enviar email: {str(e)}")
            return False

# Implementación de Notificación por SMS
class SMSNotification(Notification):
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send(self, message: str, to: str) -> bool:
        try:
            # Enviar SMS usando Twilio
            self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to
            )
            return True
        except Exception as e:
            print(f"Error al enviar SMS: {str(e)}")
            return False

# Servicio de Notificaciones
class NotificationService:
    def __init__(self, notification: Notification):
        """
        Inicializa el servicio con un tipo de notificación.
        
        Args:
            notification (Notification): La implementación de notificación a usar
        """
        self.notification = notification

    def send_alert(self, message: str, to: str) -> bool:
        """
        Envía una alerta usando el método de notificación configurado.
        
        Args:
            message (str): Mensaje a enviar
            to (str): Destinatario
            
        Returns:
            bool: True si se envió correctamente, False en caso contrario
        """
        return self.notification.send(message, to)

    def change_notification_method(self, notification: Notification):
        """
        Cambia el método de notificación.
        
        Args:
            notification (Notification): La nueva implementación de notificación
        """
        self.notification = notification

# Ejemplo de uso
def main():
    # Configuración para Email
    email_notification = EmailNotification(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        username="tu_email@gmail.com",
        password="tu_password"
    )

    # Configuración para SMS
    sms_notification = SMSNotification(
        account_sid="tu_account_sid",
        auth_token="tu_auth_token",
        from_number="+1234567890"
    )

    # Crear servicio con notificación por email
    notification_service = NotificationService(email_notification)

    # Enviar una notificación por email
    notification_service.send_alert(
        "¡Alerta importante!",
        "xibad38956@envoes.com"
    )

    # Cambiar a notificación por SMS
    notification_service.change_notification_method(sms_notification)

    # Enviar una notificación por SMS
    notification_service.send_alert(
        "¡Alerta importante!",
        "+16465386464"
    )

if __name__ == "__main__":
    main()