from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.comman.models import User

@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Website'
        message = f'Hi {instance.first_name +" "+instance.last_name},\n\nThank you for registering on our website!'
        from_email = 'mtkanimozhi@gmail.com'
        to_email = instance.email
        send_mail(subject, message, from_email, [to_email])
