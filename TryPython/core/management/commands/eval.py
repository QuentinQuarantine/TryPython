# coding: utf-8
from __future__ import print_function

import sys
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
            If using in production, must call a pypy interpreter
            in a sandboxed environment
            """
                            )

        parser.add_argument("--eval-script",
                            dest="eval_script",
                            type=str,
                            default=settings.BASE_DIR + '/eval.py',
                            help="""
            Python script to eval the expression
            """
                            )

        parser.add_argument("--pypy-interact",
                            dest="pypy_interact",
                            type=str,
                            default=None,
                            help="""
            Pypy interact script
            """
                            )

        parser.add_argument("--tmp-folder",
                            dest="tmp_folder",
                            type=str,
                            default=None,
                            help="""
            Pypy sandbox tmp folder
            """
                            )

        parser.add_argument("--pypy-c",
                            dest="pypy_c",
                            type=str,
                            default=None,
                            help="""
            pypy-c script
            """
                            )

    def handle(self, *args, **kwargs):
        python = kwargs.get("python")
        pypy_interact = kwargs.get("pypy_interact")
        tmp_folder = kwargs.get("tmp_folder")
        pypy_c = kwargs.get("pypy_c")
        eval_script = kwargs.get("eval_script")
        expression = kwargs.get("expression")
        namespace = kwargs.get("namespace")

        command = [python]

        if pypy_interact is not None:
            command.append(pypy_interact)

            if not all([tmp_folder, pypy_c]):
                raise CommandError("pypy-interact option must be"
                                   "followed by tmp-folder and pypy-c options")
            else:
                command.extend(['--tmp=' + tmp_folder, pypy_c])
        if eval_script is not None:
            command.append(eval_script)

        command.extend([expression, namespace])

        try:
            out = subprocess.check_output(command)
            if isinstance(out, bytes):
                out = out.decode('utf-8')
            print(out, file=self.stdout)
        except subprocess.CalledProcessError as err:
            sys.stderr.write(str(err),)
