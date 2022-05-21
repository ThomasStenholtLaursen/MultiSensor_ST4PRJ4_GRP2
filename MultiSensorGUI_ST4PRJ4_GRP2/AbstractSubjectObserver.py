from __future__ import annotations
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update_force(self, subject: Subject) -> None:
        pass
    def update_lt(self, subject: Subject) -> None:
        pass
