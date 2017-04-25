import abc

class AbstractValidation(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate(self, for_validation):
        pass


class UserValidation(AbstractValidation):

    @staticmethod
    def validate(first, second, numb=True):
        if not isinstance(first, int) or not isinstance(second, int):
            raise NoInstance()

        if not isinstance(first, float) or not isinstance(second, float):
            raise NoInstance()

        if not numb:
            if not isinstance(first, str):
                raise NoFunction()
            if not isinstance(first, int):
                raise NoInstance()

    @staticmethod
    def divZero(check):
        if not check:
            raise DivideZero()


class DivideZero(Exception):
    pass

class NoInstance(Exception):
    pass

class NoFunction(Exception):
    pass