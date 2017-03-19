from unittest import TestCase
from calchas_datamodel.integerLiteralCalchasExpression import IntegerLiteralCalchasExpression as Int
from calchas_datamodel.floatLiteralExpression import FloatLiteralCalchasExpression as Float


class TestLiteralExpression(TestCase):
    def testStr(self):
        tests = [(Int(1),
                  'Int(1)'),
                 (Float(1),
                  'Float(1)'),
                 ]
        for (tree, string) in tests:
            self.assertEqual(repr(tree), string)
