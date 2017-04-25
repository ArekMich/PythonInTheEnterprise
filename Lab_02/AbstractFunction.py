import abc

class AbstractFunction(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add(self, first, second):
        pass

    @abc.abstractmethod
    def subtraction(self, first, second):
        pass

    @abc.abstractmethod
    def multiplication(self, first, second):
        pass

    @abc.abstractmethod
    def division(self, first, second):
        pass

    @abc.abstractmethod
    def logarithm(self, arg, base):
        pass

    @abc.abstractmethod
    def derivative(self, funct, degree):
        pass