import os
import time
import shutil
import sys

class Sicronizar:
    def __init__(self, localOriginal, novolocal):
        self.localOriginal = localOriginal
        self.novolocal = novolocal
    
    @property
    def localOriginal(self):
        return self._localOriginal

    @localOriginal.setter
    def localOriginal(self, localOriginal):
        self._localOriginal = localOriginal

    @property
    def novolocal(self):
        return self._novolocal

    @novolocal.setter
    def novolocal(self, novolocal):
        self._novolocal = novolocal         

    def sincronizar(self):
        if os.path.exists(self.localOriginal):
            if os.path.exists(self.novolocal):
                os.remove(self.novolocal)
                shutil.copy(self.localOriginal, self.novolocal)
            else:
                shutil.copy(self.localOriginal, self.novolocal)
        else:
            pass