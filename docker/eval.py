# coding: utf-8
from __future__ import print_function
import sys
import types
import code
import json

from six import class_types, StringIO


class AcquireStdOutAndStdErr(object):

    original_stdout = sys.stdout
    original_stderr = sys.stderr
    fake_stdout = StringIO()
    fake_stderr = StringIO()

    def __enter__(self, *args):
        sys.stdout = AcquireStdOutAndStdErr.fake_stdout
        sys.stderr = AcquireStdOutAndStdErr.fake_stderr

    def __exit__(self, *args):
        sys.stdout = AcquireStdOutAndStdErr.original_stdout
        sys.stderr = AcquireStdOutAndStdErr.original_stderr


def eval_(to_eval, namespace=None):
    if namespace is None:
        namespace = {}
    else:
        namespace = eval(namespace)

    namespace['__builtins__'] = []
    console = code.InteractiveConsole(locals=namespace)
    with AcquireStdOutAndStdErr():
        for function in namespace.get("functions", []):
            for statement in function.split("\\n"):
                console.push(statement.encode("utf-8"))
        for statement in to_eval.split("\n"):
            if statement:
                console.push(statement)
            else:
                console.push('\n')

    out = AcquireStdOutAndStdErr.fake_stdout.getvalue()
    error = AcquireStdOutAndStdErr.fake_stderr.getvalue()

    # remove functions and classes in namespace
    for key, value in namespace.items():
        if isinstance(value, types.FunctionType) or isinstance(value, class_types):
            del namespace[key]
    return {'out': out, 'namespace': json.dumps(namespace), 'error': error}

if __name__ == "__main__":
    to_eval = sys.argv[1]
    namespace = sys.argv[2]
    json.dump(eval_(to_eval, namespace=namespace), sys.stdout)
