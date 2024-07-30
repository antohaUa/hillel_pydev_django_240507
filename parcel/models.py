from django.db import models
from django.contrib.auth.models import User
from post_machine.models import PostMachine, Locker


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
