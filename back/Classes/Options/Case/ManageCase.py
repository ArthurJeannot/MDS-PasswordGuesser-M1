class ManageCase:
    def __init__(self, mots=[]):
        self.mots = mots
        self.possibility = self.run()

    #Méthode a overide dans les classes filles
    def run(self):
        pass
    
# Getter / Setter
    @property
    def mots(self):
        return self._mots

    @mots.setter
    def mots(self, value):
        self._mots = value or []
        
    @property
    def possibility(self):
        return self._possibility

    @possibility.setter
    def possibility(self, value):
        self._possibility = value or []