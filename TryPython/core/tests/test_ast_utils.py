import unittest

from core.ast_utils import isFunction

class AstUtilsTestCase(unittest.TestCase):

    def test_name_binding_is_not_a_function(self):
        self.assertFalse(isFunction("a = 1"))

    def test_def_statement_is_function(self):
        self.assertTrue(isFunction('def f():\n return True\n'))

    def test_lambda_statement_is_function(self):
        self.assertTrue(isFunction('f = lambda x: x*x'))