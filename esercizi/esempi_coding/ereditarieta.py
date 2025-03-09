

# Classe base: definisce la struttura comune, indipendente dalla lingua

class SalutoGenerico(object):
    # Nome è un attributo di claasse
    nome = None

    # metodo magico di python, inizia con __ in questo caso è il costruttore
    def __init__(self, nome):
        self.nome = nome
    
    # metodo di classe, saluta!
    # self è l'istanza della classe stessa
    def saluta(self):
        """
        Metodo generico di saluto.
        Qui ci limitiamo a definire una firma e una logica basilare,
        ma ci aspettiamo che le sottoclassi la sovrascrivano (override).
        """
        print(f"Ciao, {self.nome}. (Saluto generico)")


# Italiano
class SalutoItaliano(SalutoGenerico):

    def saluta(self):
        """
        Override del metodo saluta() per la lingua italiana.
        """
        print(f"Ciao, {self.nome}!")

# Spagnola
class SalutoSpagnolo(SalutoGenerico):

    def saluta(self):
        """
        Override del metodo saluta() per la lingua spagnola.
        """
        print(f"¡Hola, {self.nome}!")

# Inglese
class SalutoInglese(SalutoGenerico):

    def saluta(self):
        """
        Override del metodo saluta() per la lingua inglese.
        """
        print(f"Hello, {self.nome}!")


# Giapponese
class SalutoGiapponese(SalutoGenerico):

    def saluta(self):
        """
        Override del metodo saluta() per la lingua giapponese.
        """
        print(f"こんにちは, {self.nome}！")


# Specifico che è giapponese
class SalutoGiapponeseSpecifico(SalutoGiapponese):

     def saluta(self):
         print("ti sto salutando in giappponese!!")
         return super().saluta()
     


class SalutoTutti(SalutoSpagnolo, SalutoItaliano, SalutoInglese, SalutoGiapponese):
    
    def saluta(self):
        SalutoItaliano.saluta(self)
        SalutoSpagnolo.saluta(self)
        SalutoInglese.saluta(self)
        SalutoGiapponese.saluta(self)



if __name__ == "__main__":
    # Creiamo un'istanza di ogni sottoclasse
    saluto_it = SalutoItaliano("Luca")
    saluto_es = SalutoSpagnolo("Luca")
    saluto_en = SalutoInglese("Luca")
    saluto_jp = SalutoGiapponese("Luca")

    # Utilizziamo il metodo saluta() di ciascuna istanza.
    saluto_it.saluta()   # Stampa: Ciao, Luca!
    saluto_es.saluta()   # Stampa: ¡Hola, Luca!
    saluto_en.saluta()   # Stampa: Hello, Luca!
    saluto_jp.saluta()   # Stampa: こんにちは, Luca！


    # saluto_jp = SalutoGiapponeseSpecifico("Luca")
    # saluto_jp.saluta()
    

    # saluto_tutti = SalutoTutti("Taddeo")    
    # saluto_tutti.saluta()
