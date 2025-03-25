# admin.py

from django.contrib import admin
from .models import Question, Choice, Tag, Squadra

# Inline per gestire le Choice direttamente nella pagina di Question
# class ChoiceInline(admin.TabularInline):
#     model = Choice              # Il modello su cui si basa l’inline
#     extra = 1                   # Numero di form vuoti aggiuntivi
#     min_num = 0                 # Numero minimo di righe (opzionale)
#     can_delete = True           # Permette di cancellare righe dall’admin

# Registrazione del modello Question con una classe personalizzata
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # Scegliamo quali campi visualizzare nella lista delle Question
    list_display = ("question_text", "pub_date", "created_at", "updated_at")
    # Aggiunge un campo di ricerca per i campi specificati
    search_fields = ("question_text",)
    # Imposta l’ordinamento di default della lista
    ordering = ("-created_at",)
    # Permette di filtrare in base alla data di pubblicazione
    list_filter = ("pub_date",)
    # Inlines: visualizza le Choice direttamente all’interno dell’admin di Question
    # inlines = [ChoiceInline]

    # Facoltativo: personalizzazione dei campi e loro ordine nel form di dettaglio
    fieldsets = (
        ("Domanda", {
            "fields": ("question_text",)
        }),
        ("Date", {
            "fields": ("pub_date",),
            "description": "Data di pubblicazione della domanda."
        }),
        ("Timestamps automatici", {
            "fields": ("created_at", "updated_at"),
        }),
    )
    # Campi read-only, in modo che non vengano modificati manualmente
    readonly_fields = ("created_at", "updated_at")


# Registrazione del modello Choice con una classe personalizzata
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    # Scegliamo i campi da visualizzare nella lista delle Choice
    list_display = ("choice_text", "question", "votes", "created_at", "updated_at")
    # Aggiunge un campo di ricerca per i campi specificati
    search_fields = ("choice_text",)
    # Imposta l’ordinamento di default
    ordering = ("-created_at",)
    # Filtri laterali
    list_filter = ("question", "created_at")
    
    # Personalizzazione dei campi e del loro ordine nel form di dettaglio
    fieldsets = (
        ("Collegamento alla domanda", {
            "fields": ("question",)
        }),
        ("Testo dell'opzione di risposta", {
            "fields": ("choice_text",)
        }),
        ("Voti", {
            "fields": ("votes",)
        }),
        ("Timestamps automatici", {
            "fields": ("created_at", "updated_at"),
        }),
    )
    # Evitiamo che i timestamps vengano modificati manualmente
    readonly_fields = ("created_at", "updated_at")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Squadra)
class SquadraAdmin(admin.ModelAdmin):
    pass