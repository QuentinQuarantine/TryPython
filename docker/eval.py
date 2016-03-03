# coding: utf-8
from __future__ import print_function
import sys
import types
import code
import json
from contextlib2 import redirect_stderr, redirect_stdout

from six import class_types, StringIO


def _get_console_out(to_eval, namespace):
    fake_out, fake_err = StringIO(), StringIO()
    console = code.InteractiveConsole(locals=namespace)
    with redirect_stdout(fake_out), redirect_stderr(fake_err):
        for function in namespace.get("functions", []):
            for statement in function.split("\\n"):
                console.push(statement)
        for statement in to_eval.split("\n"):
            if statement:
                console.push(statement)
            else:
                console.push('\n')
    return fake_out.getvalue(), fake_err.getvalue()


def eval_(to_eval, namespace=None):
    if namespace is None:
        namespace = {}
    else:
        namespace = eval(namespace)
    namespace['__builtins__'] = {'print': print}
    out, errors = _get_console_out(to_eval, namespace)
    new_namespace = {}
    for key, value in namespace.items():
        if key != "__builtins__":
            if not (isinstance(value, types.FunctionType) or isinstance(value, class_types)):
                new_namespace[key] = value
    return {'out': out, 'namespace': json.dumps(new_namespace), 'error': errors}

if __name__ == "__main__":
    to_eval = sys.argv[1]
    namespace = sys.argv[2]
    json.dump(eval_(to_eval, namespace=namespace), sys.stdout)
