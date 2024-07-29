from django.db import models


class PostMachine(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'PM: [{self.pk}]-{self.city}-{self.address}'


class Locker(models.Model):
    size = models.IntegerField()
    post_machine = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # False == no parcel inside

    def __str__(self):
        return f'Locker: [{self.pk}]-PM_ID: {self.post_machine.pk}-size: {self.size}-{self.status}'
