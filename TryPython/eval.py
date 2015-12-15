# coding: utf-8


import sys
import code
from io import BytesIO, StringIO


def get_eval_command(python_exe, project_path, eval_file=__file__):
    return [python_exe, project_path, eval_file]


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


def _eval(to_eval):
    ns = {'__builtins__': []}
    console = code.InteractiveConsole(locals=ns)

    with AcquireStdOutAndStdErr():

        for statement in to_eval.split("\n"):
            if statement:
                console.push(statement)
            else:
                console.push(u'\n')

    out_result, err_result = AcquireStdOutAndStdErr.fake_stdout.getvalue(
    ), AcquireStdOutAndStdErr.fake_stderr.getvalue()

    return out_result + '}##{' + err_result

if __name__ == "__main__":
    to_eval = sys.argv[1]
    print _eval(to_eval)
