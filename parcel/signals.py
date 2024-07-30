import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Parcel
from post_machine.models import Locker

_log = logging.getLogger(__name__)


@receiver(post_save, sender=Parcel)
def update_locker_status(sender, instance, created, **kwargs):
    """Update locker status if Parcel fired."""
    if instance.status is False:
        if instance.locker is not None:
            parcel_locker = Locker.objects.get(pk=instance.locker.pk)
            parcel_locker.status = True
            parcel_locker.save()
            _log.warning(f'Locker status updated for parcel: {instance}')
