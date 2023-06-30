from abc import ABC, abstractclassmethod
class ManageElement(ABC):
    def __init__(self, elements=[]):
        self.elements = elements
        self.possibility = self._run()

    @abstractclassmethod
    def _run(self):
        pass
    
    @classmethod
    def add_word_possibility(cls, elements=[]):
        instance = cls(elements)
        return list(set(elements + instance.possibility))
    
# Getter / Setter
    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, value):
        self._elements = value or []
        
    @property
    def possibility(self):
        return self._possibility

    @possibility.setter
    def possibility(self, value):
        self._possibility = value or []