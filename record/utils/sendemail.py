from django.core.mail import send_mail
__all__ = (
    'MailTest',
)

class MailTest():
    def certification_mail(email):
        send_mail(
            'Subject',
            'Message',
            'record@record.com',
            [email],
            fail_silently=False
        )