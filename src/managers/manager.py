from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractmethod
    def exit(self):
        raise NotImplementedError
