# Importazioni necessarie da Django per la gestione delle viste e dei template.
from django.shortcuts import render, get_object_or_404  # render: per rendere il template; get_object_or_404: per recuperare un oggetto o sollevare un 404.
from django.http import HttpResponse, Http404, HttpResponseRedirect  # HttpResponse: per restituire una risposta HTTP; Http404: per segnalare un errore 404; HttpResponseRedirect: per reindirizzare l'utente.
from django.template import loader  # loader: per caricare manualmente un template.
from django.urls import reverse  # reverse: per ottenere dinamicamente l'URL di una view in base al suo nome.

# Importazione dei modelli definiti nell'applicazione "polls".
from polls.models import Question, Choice  
from pprint import pprint  # pprint: per stampare in modo leggibile gli attributi dell'oggetto request (utile per il debugging).

def index(request):   
    
    # Ottiene il parametro 'q' dalla query string della richiesta GET; se non presente, viene restituito None.
    filtro = request.GET.get('q', None)
    
    # Se è stato passato un filtro, esegue una ricerca nel campo question_text per trovare corrispondenze (ricerca case-insensitive).
    # NOTA: La condizione else esegue esattamente la stessa query: questo potrebbe essere un errore, 
    # perché se filtro è None, la query non restituirà tutte le domande come atteso.
    if filtro:
        question_list = Question.objects.filter(question_text__icontains=filtro)
    else:
        question_list = Question.objects.all()
    
    # Carica il template "polls/index.html" dalla directory dei template.
    template = loader.get_template("polls/index.html")
    
    # Prepara il contesto da passare al template: in questo caso, una lista di domande filtrate.
    context = {
        "latest_question_list": question_list,
    }
    
    # Rende il template con il contesto specificato e restituisce la risposta HTTP generata.
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # Tenta di recuperare la domanda con l'ID fornito.
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # Se la domanda non esiste, solleva un'eccezione Http404 con un messaggio di errore.
        raise Http404("Question does not exist")
    # Se la domanda viene trovata, viene renderizzato il template "polls/detail.html" con la domanda nel contesto.
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    # Recupera la domanda con il pk specificato. Se non esiste, restituisce una pagina 404.
    question = get_object_or_404(Question, pk=question_id)
    # Rende il template "polls/results.html" passando l'oggetto question nel contesto.
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    # Recupera la domanda per la quale l'utente sta votando; se non esiste, restituisce un errore 404.
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Tenta di recuperare la scelta selezionata dall'utente:
        # Il valore della chiave "choice" viene preso dai dati POST della richiesta.
        selected_choice = question.choices.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Se la chiave "choice" non esiste nel POST o la scelta con l'ID specificato non esiste,
        # viene ri-renderizzato il template "polls/detail.html" con un messaggio di errore.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # Se la scelta esiste, incrementa il contatore dei voti di 1.
        selected_choice.votes += 1
        # Salva l'aggiornamento nel database.
        selected_choice.save()
        # Dopo aver gestito correttamente la richiesta POST, reindirizza l'utente alla pagina dei risultati.
        # Questo previene la possibilità di reinviare accidentalmente i dati (es. ricaricando la pagina).
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
