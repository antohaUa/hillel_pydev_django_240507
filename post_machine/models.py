from django.db import models


class PostMachine(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Locker(models.Model):
    size = models.IntegerField()
    post_machine = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # False == no parcel inside

    def __str__(self):
        return f'[{self.pk}] - {self.post_machine} - size: {self.size} - {self.status}'
