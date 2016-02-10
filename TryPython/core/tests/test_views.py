import json
from django.test import TestCase


class ViewsTestCase(TestCase):

    def test_index_view(self):
        response = self.client.get("/")

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.template_name, ['main.html'])


class EvalViewTestCase(TestCase):

    def test_eval_view_simple_expression(self):
        response = self.client.post("/eval", {"toEval": "1+1"})
        expected = {"out": "2\n", "err": ""}
        decoded_response = json.loads(response.content.decode("utf-8"))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(decoded_response, expected)

    def test_eval_view_name_binding(self):
        response = self.client.post("/eval", {"toEval": "a = 1"})

        self.assertEquals(response.status_code, 200)

        response = self.client.post("/eval", {"toEval": "a"})

        expected = {u'err': u'', u'out': u'1\n'}
        decoded_response = json.loads(response.content.decode('utf-8'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(decoded_response, expected)

    def test_eval_view_for_statement(self):
        response = self.client.post(
            "/eval", {"toEval": "for x in (1, 2):\n  print(x)\n"})
        expected = {u'err': u'', u'out': u'1\n2\n'}
        decoded_response = json.loads(response.content.decode("utf-8"))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(decoded_response, expected)

    def test_eval_view_while_loop(self):
        response = self.client.post(
            "/eval", {"toEval": "while 1:\n  print('hey')\n  break\n"})
        expected = {"out": "hey\n", "err": ""}
        decoded_response = json.loads(response.content.decode("utf-8"))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(decoded_response, expected)

    def test_eval_view_that_will_raise_python_exception(self):
        response = self.client.post("/eval", {'toEval': 'a'})
        expected = {"out": "",
                    "err": "Traceback (most recent call last):\n"
                    "  File \"<console>\","
                    " line 1, in <module>\nNameError: name \'a\' is not"
                    " defined\n"
                    }
        decoded_response = json.loads(response.content.decode("utf-8"))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(decoded_response, expected)

    def test_eval_view_function_statement(self):
        response = self.client.post(
            "/eval", {"toEval": 'def f():\n print("x")\n'})
        self.assertEquals(response.status_code, 200)

        response = self.client.post("/eval", {"toEval": 'f()'})
        expected = json.dumps({"out": "x\n", "err": ""}).encode("utf-8")

        self.assertEquals(response.content, expected)

    def test_eval_lambda_function(self):
        response = self.client.post("/eval", {"toEval": 'f = lambda x: x*x'})

        self.assertEquals(response.status_code, 200)

        response = self.client.post("/eval", {"toEval": 'f(2)'})
        expected = json.dumps({"out": "4\n", "err": ""}).encode("utf-8")

        self.assertEquals(response.content, expected)
