import sys
import os
import json
from subprocess import CalledProcessError

import six
from six import StringIO

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
        self.fake_stdout = StringIO()
        self.fake_stderr = StringIO()
        self.original_stderr = sys.stderr
        self.original_stdout = sys.stdout
        sys.stderr = self.fake_stderr
        sys.stdout = self.fake_stdout

    def tearDown(self):
        super(self.__class__, self).tearDown()
        sys.stderr = self.original_stderr
        sys.stdout = self.original_stdout

    @patch('docker.Client')
    def test_eval_with_docker(self, docker_client):
        expression = '1+1'
        call_command('eval', '--with-docker', expression, self.namespace)

        docker_client.assert_called_with(base_url=settings.DOCKER_BASE_URL)

    @patch('subprocess.check_output')
    def test_subprocess_raises_called_error(self, check_output):
        check_output.side_effect = CalledProcessError(2, "<console>")

        call_command('eval', '1+1', self.namespace)
        self.assertEqual(
            self.fake_stderr.getvalue(),
            "Command '<console>' returned non-zero exit status 2")
