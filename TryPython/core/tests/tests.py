from django.test import TestCase
from core.models import Step


class ViewsTestCase(TestCase):

    def test_step_view_that_doesnt_exists(self):
        response = self.client.post('step', {'step': 1})

        self.assertEquals(response.status_code, 404)

    def test_index_view(self):
        response = self.client.get("/")

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.template_name, ['main.html'])


class ModelsTestCase(TestCase):

    def test_insert_step(self):
        step = Step(content="some content ...", title="Title")
        step.save()

        self.assertDictEqual(
            step.to_dict(),
            {'content': "some content ...", "title": "Title"})
