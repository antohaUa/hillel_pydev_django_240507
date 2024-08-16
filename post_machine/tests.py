from django.test import TestCase, Client


class TestPostMachine(TestCase):
    fixtures = ['test_db_data']

    def setUp(self):
        self.test_cl = Client()

    def test_get_post_machines(self):
        response = self.test_cl.post(f'/post_machine/')
        self.assertEquals(response.status_code, 200)

    def test_get_post_machine(self):
        response = self.test_cl.post(f'/post_machine/1/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['post_machine']['city'], 'Kyiv')
        self.assertEquals(len(response.context['lockers']), 2)
