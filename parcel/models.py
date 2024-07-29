import logging
from django.db import models
from django.contrib.auth.models import User
from post_machine.models import PostMachine, Locker
from django.db.models.signals import post_save
from django.dispatch import receiver

_log = logging.getLogger(__name__)

class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, default=None, null=True, blank=True, on_delete=models.DO_NOTHING)
    order_datetime = models.DateTimeField('date_published')
    open_datetime = models.DateTimeField('date_published', null=True, blank=True)
    status = models.BooleanField(default=False)  # True == delivered

    def __str__(self):
        return f'{self.pk} - {self.recipient} - {self.post_machine_recipient} - {self.locker}'


@receiver(post_save, sender=Parcel)
def update_locker_status(sender, instance, created, **kwargs):
    """Update locker status if Parcel fired."""
    if instance.status is False:
        if instance.locker is not None:
            parcel_locker = Locker.objects.get(pk=instance.locker.pk)
            parcel_locker.status = True
            parcel_locker.save()
            _log.warning(f'Locker status updated for parcel: {instance}')

