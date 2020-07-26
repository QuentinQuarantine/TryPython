import os
import subprocess
import atexit
import signal

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command \
    as StaticfilesRunserverCommand


class Command(StaticfilesRunserverCommand):

    def inner_run(self, *args, **options):
        self.start_rollup()
        return super(Command, self).inner_run(*args, **options)

    def start_rollup(self):
        self.stdout.write('>>> Starting rollup')
        self.rollup_process = subprocess.Popen(
            ['yarn watch'],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write('>>> Rollup process on pid {0}'.format(self.rollup_process.pid))

        def kill_rollup_process(pid):
            self.stdout.write('>>> Closing rollup process')
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_rollup_process, self.rollup_process.pid)
