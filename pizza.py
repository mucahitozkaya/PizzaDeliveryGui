class pizza:
    def __init__(self,fiyat,aciklama) -> None:
        self.fiyat = fiyat
        self.aciklama = aciklama
    
    def get_description(self):
        return self.aciklama

    def get_cost(self):
        return self.fiyat

class KlasikPizza(pizza):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)
    
class MargheritaPizza(pizza):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)

class TurkPizza(pizza):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)

class DominosPizza(pizza):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)


class Decorator(pizza):
    def __init__(self,fiyat,aciklama) -> None:
        self.fiyat = fiyat
        self.aciklama = aciklama
    
    def get_description(self):
        return self.aciklama

    def get_cost(self):
        return self.fiyat

class Zeytin(Decorator):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)
    
class Mantar(Decorator):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)

class KeciPeyniri(Decorator):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)

class Et(Decorator):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)
    
class Sogan(Decorator):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)

class Misir(Decorator):
    def __init__(self,fiyat,aciklama) -> None:
        super().__init__(fiyat,aciklama)
    