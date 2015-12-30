import json
from django.test import TestCase
from models import Step


class ViewsTestCase(TestCase):

    def test_index_view(self):
        response = self.client.get("/")

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.template_name, ['main.html'])

    def test_eval_view(self):

        response = self.client.post("/eval", {"toEval": "1+1"})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, json.dumps({"out": "2\n", "err": "\n\n"}))

    def test_eval_view_that_will_raise_python_exception(self):

        response = self.client.post("/eval", {'toEval': 'a'})

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content,
                          json.dumps({"out": "", "err": 'Traceback (most recent call last):\n  File "<console>",'
                                      ' line 1, in <module>\nNameError: name \'a\' is not defined\n\n\n'}))

    def test_step_view_that_doesnt_exists(self):

        response = self.client.post('step', {'step': 1})

        self.assertEquals(response.status_code, 404)
