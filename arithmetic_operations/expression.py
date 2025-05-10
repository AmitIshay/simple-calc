import ast
import operator
from arithmetic_operations.arithmetic_operation import ArithmeticOperation

class Expression(ArithmeticOperation):
    def calculate(self, expression, _=None):
        allowed_ops = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.USub: operator.neg,
        }
        
        
        def _eval(node):
            if isinstance(node, ast.Constant):  
                return node.n
            elif isinstance(node, ast.BinOp):  
                return allowed_ops[type(node.op)](_eval(node.left), _eval(node.right))
            elif isinstance(node, ast.UnaryOp):
                return allowed_ops[type(node.op)](_eval(node.operand))
            else:
                raise ValueError("Unsupported expression")

        parsed = ast.parse(expression, mode='eval').body
        return _eval(parsed)