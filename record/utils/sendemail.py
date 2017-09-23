from django.core.mail import send_mail

__all__ = (
    'MailTest',
)


class MailTest():
    @staticmethod
    def certification_mail(email, message):
        send_mail(
            'Subject',
            'http://localhost:8000/?key=' + message,
            'record@record.com',
            [email],
            fail_silently=False
        )
