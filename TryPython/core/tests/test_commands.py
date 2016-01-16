import sys
import os
import json
from StringIO import StringIO
from subprocess import CalledProcessError

import six

if six.PY2:
    from mock import patch
else:
    from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.core.management import call_command, CommandError


class CommandsTests(TestCase):

    def setUp(self):
        super(self.__class__, self).setUp()
        self.namespace = json.dumps({})
        self.out = StringIO()
        self.fake_stderr = StringIO()
        self.original_stderr = sys.stderr
        sys.stderr = self.fake_stderr

    def tearDown(self):
        super(self.__class__, self).tearDown()
        sys.stderr = self.original_stderr

    def test_eval_command_with_only_pypy_interact_option(self):
        with self.assertRaises(CommandError):
            call_command('eval', '1+1', self.namespace,
                         pypy_interact="pypy_interact.py", stdout=self.out)

    @patch('subprocess.check_output')
    def test_subprocess_raises_called_error(self, check_output):
        check_output.side_effect = CalledProcessError(2, "<console>")

        call_command('eval', '1+1', self.namespace)
        self.assertEqual(self.fake_stderr.getvalue(), "Command '<console>' returned non-zero exit status 2")

    @patch('subprocess.check_output')
    def test_eval_command_with_all_options_to_run_in_pypy(self, check_output):

        call_command('eval', '1+1', self.namespace,
                     pypy_interact="pypy_interact.py",
                     tmp_folder="TryPython/",
                     pypy_c="/usr/bin/pypy-c",
                     stdout=self.out)

        eval_script_path = os.path.join(settings.BASE_DIR, 'eval.py')
        check_output.assert_called_with(
            ['/usr/bin/python',
             'pypy_interact.py',
             '--tmp=TryPython/',
             '/usr/bin/pypy-c',
             eval_script_path,
             '1+1',
             '{}']
        )
