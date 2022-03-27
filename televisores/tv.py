

class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        TV._numTV += 1
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._marca = marca
        self._estado = estado
        self._control = None

    def setMarca(self, marca):
        self._marca = marca

    def setControl(self, control):
        self._control = control

    def setPrecio(self, precio):
        self._precio = precio

    def setCanal(self, canal):
        if self._estado:
            if self.canal <= 120 and self.canal > 0:
                self.canal = canal

    def setVolumen(self, vol):
        if self._estado:
            if vol <= 7 and vol >= 0:
                self._volumen = vol

    def getMarca(self):
        return self._marca

    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def getCanal(self):
        return self._canal

    def getVolumen(self):
        return self._volumen

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, nt):
        cls._numTV = nt

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._estado:
            if self._canal < 120:
                self._canal += 1

    def canalDown(self):
        if self._estado:
            if self._canal > 1:
                self._canal -= 1

    def volumenUp(self):
        if self._estado:
            if self._canal < 7:
                self._canal += 1

    def volumenDown(self):
        if self._estado:
            if self._canal > 0:
                self._canal -= 1

    
        
    

    
