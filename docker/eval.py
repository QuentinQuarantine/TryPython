# coding: utf-8

import sys
import types
import code
import json
from io import BytesIO


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
        for function in namespace.get("functions", []):
            for statement in function.split("\\n"):
                console.push(statement)
        for statement in to_eval.split("\n"):
            if statement:
                console.push(statement)
            else:
                console.push(u'\n')

    out = AcquireStdOutAndStdErr.fake_stdout.getvalue()
    error = AcquireStdOutAndStdErr.fake_stderr.getvalue()

    # remove functions and classes in namespace
    for key, value in namespace.items():
        if isinstance(value, types.FunctionType) or isinstance(value, types.ClassType):
            del namespace[key]
    return {'out': out, 'namespace': json.dumps(namespace), 'error': error}

if __name__ == "__main__":
    to_eval = sys.argv[1]
    namespace = sys.argv[2]
    print json.dumps(_eval(to_eval, namespace=namespace))
