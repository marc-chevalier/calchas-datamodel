from unittest import TestCase
from calchas_datamodel.formulaFunctionExpression import FormulaFunctionExpression as Fun
from calchas_datamodel.idExpression import IdExpression as Id


class TestFunctionExpression(TestCase):
    def testStr(self):
        fun = Fun(Id('x'), Id('y'))
        self.assertEqual(repr(fun), "x -> y")
