# coding: utf-8
from __future__ import print_function

import sys
import os
import subprocess
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):

    help = "Call a subprocess to eval a python expression"

    def add_arguments(self, parser):
        parser.add_argument("expression", type=str, default="")
        parser.add_argument("namespace", type=str)
        parser.add_argument("--python",
                            dest="python",
                            type=str,
                            default="/usr/bin/python",
                            help="""
            Python interpreter to run the eval script.
            """)

        parser.add_argument("--eval-script",
                            dest="eval_script",
                            type=str,
                            default=os.path.join(settings.PROJECT_DIR,
                                                 'docker', 'eval.py'),
                            help="""
            Python script to eval the expression
            The defalt script is run from docker/eval.py
            """)

    def handle(self, *args, **kwargs):
        python = kwargs.get("python")
        eval_script = kwargs.get("eval_script")
        expression = kwargs.get("expression")
        namespace = kwargs.get("namespace")

        command = [python, eval_script, expression, namespace]
        try:
            out = subprocess.check_output(command)
            if isinstance(out, bytes):
                out = out.decode('utf-8')
            print(out, file=self.stdout)
        except subprocess.CalledProcessError as err:
            sys.stderr.write(str(err),)
