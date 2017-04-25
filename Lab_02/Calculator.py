import Validator
import AbstractFunction
from sympy import *

class Calculator(AbstractFunction):

    def add(self, first, second):
        Validator.UserValidation.validate(first, second)
        return first + second

    def subtraction(self, first, second):
        Validator.UserValidation.validate(first, second)
        return first - second

    def multiplication(self, first, second):
        Validator.UserValidation.validate(first, second)
        return first * second

    def division(self, first, second):
        Validator.UserValidation.divZero(second)
        Validator.UserValidation.validate(first, second)
        return first / second

    def logarithm(self, arg, base):
        Validator.UserValidation.validate(arg, base)
        return math.log(arg, base)

    def derivative(self, funct, degree):
        Validator.UserValidation.validate(funct, degree)
        return sympy.diff(funct, 'x', degree)