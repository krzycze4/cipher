from abc import ABC


class AbstractFactory(ABC):
    def create_object(self):
        raise NotImplementedError
