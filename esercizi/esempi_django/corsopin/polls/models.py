# Importiamo la classe models da django.db, necessaria per definire i nostri modelli
from django.db import models

# Definizione della classe Question, che rappresenta il nostro modello "domanda"
class Question(models.Model):
    # Campo di testo per la domanda, con lunghezza massima di 200 caratteri
    question_text = models.CharField(max_length=200)
    # Data di pubblicazione, definita come DateTimeField (nel pannello admin viene mostrata come "date published")
    pub_date = models.DateTimeField("date published")
    # Campo che registra automaticamente la data e l'orario di creazione dell'istanza
    created_at = models.DateTimeField(auto_now_add=True)
    # Campo che registra automaticamente la data e l'orario di ultima modifica dell'istanza
    updated_at = models.DateTimeField(auto_now=True)

    # Classe Meta per impostazioni aggiuntive sul comportamento del modello
    class Meta:
        # Nome singolare del modello nell’admin di Django
        verbose_name = "Question"
        # Nome plurale del modello nell’admin di Django
        verbose_name_plural = "Questions"
        # Definisce l’ordinamento di default quando richiediamo un elenco di Question
        # In questo caso ordiniamo in modo discendente per data di creazione
        ordering = ["-created_at"]

    # Metodo magico per la rappresentazione in stringa dell’oggetto (comodo per admin e shell)
    def __str__(self):
        # Ritorna il testo della domanda come stringa rappresentativa
        return self.question_text


# Definizione della classe Choice, che rappresenta il modello "opzione di risposta"
class Choice(models.Model):
    # ForeignKey collega la Choice a una Question.
    # on_delete=models.CASCADE fa sì che, se la Question viene eliminata,
    # vengano eliminate anche tutte le Choice collegate.
    # related_name="choices" ci permette di accedere alle Choice da una Question usando question.choices
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )
    # Campo di testo per l'opzione di risposta, con lunghezza massima di 200 caratteri
    choice_text = models.CharField(max_length=200)
    # Campo di tipo intero per contare i voti di ogni opzione, con valore di default = 0
    votes = models.IntegerField(default=0)
    # Campo che registra automaticamente la data e l'orario di creazione dell'istanza
    created_at = models.DateTimeField(auto_now_add=True)
    # Campo che registra automaticamente la data e l'orario di ultima modifica dell'istanza
    updated_at = models.DateTimeField(auto_now=True)

    # Classe Meta con impostazioni aggiuntive per il modello Choice
    class Meta:
        # Nome singolare del modello nell’admin di Django
        verbose_name = "Choice"
        # Nome plurale del modello nell’admin di Django
        verbose_name_plural = "Choices"
        # Impostiamo l’ordinamento di default per data di creazione in ordine discendente
        ordering = ["-created_at"]

    # Metodo magico per la rappresentazione in stringa dell’oggetto
    def __str__(self):
        # Ritorna il testo della scelta come stringa rappresentativa
        return self.choice_text

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

class Squadra(models.Model):
    name = models.CharField(max_length=200)
    sconfitte_consective = models.IntegerField(default=0)
    vittorie_consective = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Squadra"
        verbose_name_plural = "Squadre"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name