import json
from StringIO import StringIO

from mock import patch
from django.test import TestCase
from django.core.management import call_command, CommandError


class CommandsTests(TestCase):

    def test_eval_command_with_only_pypy_interact_option(self):
        namespace = json.dumps({})
        out = StringIO()

        with self.assertRaises(CommandError):
            call_command('eval', '1+1', namespace, pypy_interact="pypy_interact.py", stdout=out)


    @patch('subprocess.check_output')
    def test_eval_command_with_all_options_to_run_in_pypy(self, check_output):
        namespace = json.dumps({})
        out = StringIO()

        call_command('eval', '1+1', namespace,
                     pypy_interact="pypy_interact.py",
                     tmp_folder="TryPython/",
                     pypy_c="/usr/bin/pypy-c",
                     stdout=out)

        check_output.assert_called_with(
            ['/usr/bin/python',
             'pypy_interact.py',
             '--tmp=TryPython/',
             '/usr/bin/pypy-c',
             '/home/yori/projects/TryPython/TryPython/eval.py',
             '1+1',
             '{}']
        )