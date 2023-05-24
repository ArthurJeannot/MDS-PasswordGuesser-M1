class ManageElement:
    def __init__(self, elements=[]):
        self.elements = elements
        self.possibility = self._run()

    #Méthode a overide dans les classes filles
    def _run(self):
        pass
    
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