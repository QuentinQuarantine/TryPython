import json
from StringIO import StringIO
from django.test import TestCase
from django.core.management import call_command, CommandError


class CommandsTests(TestCase):

    def test_eval_command(self):
        namespace = json.dumps({})
        out = StringIO()

        with self.assertRaises(CommandError):
            call_command('eval', '1+1', namespace, pypy_interact="pypy_interact.py", stdout=out)
