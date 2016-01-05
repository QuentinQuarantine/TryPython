import ast
import sys


def isFunction(stmt):
    """
    Check if a python statement is a function
    >>> isFunction('a = 1')
    False
    >>> isFunction('def f():\\n return True\\n')
    True
    >>> isFunction('f = lambda x: x*x')
    True
    """
    ast_tree = ast.parse(stmt)
    body = ast_tree.body[0]
    try:
        return isinstance(body.value, ast.Lambda)
    except AttributeError:
        return isinstance(body, ast.FunctionDef)

if __name__ == "__main__":
    import doctest

    failure_count, _ = doctest.testmod(verbose=1)
    sys.exit(failure_count)
