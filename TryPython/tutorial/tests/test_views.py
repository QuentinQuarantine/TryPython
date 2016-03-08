from django.test import TestCase
from tutorial.models import Step


class ViewsTestCase(TestCase):

    def test_step_view_that_doesnt_exists(self):
        response = self.client.post('/get_step', {'step': 1})

        self.assertEquals(response.status_code, 404)

    def test_step_view_get_first_step(self):
        Step(content="some content ...", title="Title").save()
        response = self.client.post('/get_step', {'step': 1})

        self.assertEquals(response.status_code, 200)
