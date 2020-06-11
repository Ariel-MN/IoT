from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(subject, employee, email):
    send_mail(subject, f"""Hello {employee}.

You are hereby informed that {subject.lower()}.

Regards,
Dustbin-IoT - Administration.


This is an automatic message, do not reply. 
For any questions or needs, please contact your superior.

Have you received this message by mistake?
If that's the case, please send a message to info@montesariel.com and report the issue. Thank you.""",
              'dustbin.iot.app@gmail.com', [email])
    return None
