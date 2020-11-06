from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from international.models import LoggedInUserInternational

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    LoggedInUserInternational.objects.get_or_create(user=kwargs.get('user')) 


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    LoggedInUserInternational.objects.filter(user=kwargs.get('user')).delete()