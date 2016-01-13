from django.test import TestCase
from core.models import Step


class ModelsTestCase(TestCase):

    def test_insert_step(self):
        step = Step(content="some content ...", title="Title")
        step.save()

        self.assertDictEqual(
            step.to_dict(),
            {'content': "some content ...", "title": "Title"})
