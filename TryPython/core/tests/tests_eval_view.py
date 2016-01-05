import json
from django.test import TestCase


class EvalViewTestCase(TestCase):

    def test_eval_view_simple_expression(self):
        response = self.client.post("/eval", {"toEval": "1+1"})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, json.dumps(
            {"out": "2\n", "err": ""}))

    def test_eval_view_name_binding(self):
        response = self.client.post("/eval", {"toEval": "a = 1"})

        self.assertEquals(response.status_code, 200)

        response = self.client.post("/eval", {"toEval": "a"})

        expected = json.dumps({u'err': u'', u'out': u'1\n'})
        self.assertJSONEqual(response.content, expected)

    def test_eval_view_that_will_raise_python_exception(self):
        response = self.client.post("/eval", {'toEval': 'a'})

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content,
                          json.dumps({"out": "", "err": 'Traceback (most recent call last):\n  File "<console>",'
                                      ' line 1, in <module>\nNameError: name \'a\' is not defined\n'}))

    def test_eval_view_function_statement(self):
        response = self.client.post("/eval", {"toEval": 'def f():\n print "x"\n'})
        self.assertEquals(response.status_code, 200)

        response = self.client.post("/eval", {"toEval": 'f()'})
        expected = json.dumps({"out": "x\n", "err": ""})
        self.assertJSONEqual(response.content, expected)

    def test_eval_lambda_function(self):
        response = self.client.post("/eval", {"toEval": 'f = lambda x: x*x'})

        self.assertEquals(response.status_code, 200)

        response = self.client.post("/eval", {"toEval": 'f(2)'})

        expected = json.dumps({"out": "4\n", "err": ""})
        self.assertJSONEqual(response.content,  expected)
