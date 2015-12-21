# coding: utf-8


import sys
import code
from io import BytesIO, StringIO


class AcquireStdOutAndStdErr(object):

    original_stdout = sys.stdout
    original_stderr = sys.stderr
    fake_stdout = BytesIO()
    fake_stderr = BytesIO()

    def __enter__(self, *args):
        sys.stdout = AcquireStdOutAndStdErr.fake_stdout
        sys.stderr = AcquireStdOutAndStdErr.fake_stderr

    def __exit__(self, *args):
        sys.stdout = AcquireStdOutAndStdErr.original_stdout
        sys.stderr = AcquireStdOutAndStdErr.original_stderr


def _eval(to_eval, namespace=None):
    if namespace is None:
        namespace = {}
    else:
        namespace = eval(namespace)

    namespace['__builtins__'] = []
    console = code.InteractiveConsole(locals=namespace)

    with AcquireStdOutAndStdErr():

        for statement in to_eval.split("\n"):
            if statement:
                console.push(statement)
            else:
                console.push(u'\n')

    out = AcquireStdOutAndStdErr.fake_stdout.getvalue()
    err = AcquireStdOutAndStdErr.fake_stderr.getvalue()

    return out + '}##{' + str(namespace) + '}##{' + err

if __name__ == "__main__":
    to_eval = sys.argv[1]
    namespace = sys.argv[2]
    print _eval(to_eval, namespace=namespace)
