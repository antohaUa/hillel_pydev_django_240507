from django.test import TestCase, Client
from parcel import models as parcel_models
from post_machine import models as post_machine_models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class TestParcel(TestCase):
    # mute signals
    post_save.receivers = []
    # post_save.sender_receivers_cache.clear()
    fixtures = ['test_db_data']

    def setUp(self):
        # prepare data
        test_post_machine = post_machine_models.PostMachine.objects.get(pk=1)
        test_locker = post_machine_models.Locker.objects.filter(post_machine=test_post_machine).all()[0]
        self.locker_pk = test_locker.pk
        self.test_parcel = parcel_models.Parcel()
        self.test_parcel.recipient = User.objects.create_user(username='test_user', password='test_password')
        self.test_parcel.sender = 'Admin'
        self.test_parcel.size = 2
        self.test_parcel.post_machine_recipient = test_post_machine
        self.test_parcel.locker = test_locker
        self.test_parcel.order_datetime = '2024-07-17T19:23:28Z'
        self.test_parcel.open_datetime = '2024-07-17T19:23:28Z'
        self.test_parcel.status = False
        self.test_parcel.save()

        self.test_parcel.locker.status = True
        self.test_parcel.locker.save()

    def test_receive_parcel(self):
        test_cl = Client()

        actual_locker = post_machine_models.Locker.objects.get(pk=self.locker_pk)
        self.assertEquals(actual_locker.status, True)
        test_cl.login(username='test_user', password='test_password')
        response = test_cl.post(f'/parcel/{self.test_parcel.pk}/', data={'parcel_id': self.test_parcel.pk})
        self.assertEquals(response.status_code, 302)

        actual_parcel = parcel_models.Parcel.objects.get(pk=self.test_parcel.pk)
        self.assertEquals(actual_parcel.status, True)
        self.assertEquals(response.status_code, 302)
        actual_locker = post_machine_models.Locker.objects.get(pk=self.locker_pk)
        self.assertEquals(actual_locker.status, False)
