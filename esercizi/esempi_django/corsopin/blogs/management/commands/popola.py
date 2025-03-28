from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blogs.models import Author, Category, BlogPost  # Assicurati che il nome dell'app sia corretto
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Popola il database con dati fittizi in italiano'

    def handle(self, *args, **kwargs):
        # Imposta Faker con il locale italiano
        fake = Faker("it_IT")
        User = get_user_model()

        # Creazione utenti e relativi autori con correlazione tra username, email e nome completo
        users = []
        authors = []
        for _ in range(100):
            first_name = fake.first_name()
            last_name = fake.last_name()
            # Costruiamo lo username in base al nome in minuscolo e aggiungiamo un numero casuale
            username = f"{first_name.lower()}{random.randint(1,100)}"
            email = f"{username}@example.com"
            password = 'Antani123'
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    is_staff=True,
                    is_superuser=True
                )
                # Se il modello User dispone dei campi first_name e last_name, li impostiamo
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                # Creiamo l'Author associato, utilizzando il nome completo nella bio
                author = Author.objects.create(user=user, bio=f"Biografia di {first_name} {last_name}")
                users.append(user)
                authors.append(author)
            except Exception as ex:
                self.stdout.write(self.style.ERROR("Eccezione nella creazione utente/autore: {}".format(str(ex))))

        self.stdout.write(self.style.SUCCESS("Creati {} utenti/autori.".format(len(users))))

        # Creazione categorie
        categories = []
        for _ in range(50):
            try:
                name = fake.unique.word().capitalize()
                slug = name.lower()
                category = Category.objects.create(name=name, slug=slug)
                categories.append(category)
            except Exception as ex:
                self.stdout.write(self.style.ERROR("Eccezione nella creazione categoria: {}".format(str(ex))))

        self.stdout.write(self.style.SUCCESS("Creati {} categorie.".format(len(categories))))

        # Creazione blog posts
        blog_posts = []
        for _ in range(2000):
            try:
                title = fake.sentence(nb_words=25)
                slug = '-'.join(title.split()).lower()
                content = fake.paragraph(nb_sentences=2000)
                author = random.choice(authors)
                post = BlogPost.objects.create(
                    title=title,
                    slug=slug,
                    content=content,
                    author=author
                )
                # Assegna una o più categorie al post
                chosen_categories = random.sample(categories, k=random.randint(1, len(categories)))
                post.categories.add(*chosen_categories)
                blog_posts.append(post)
            except Exception as ex:
                self.stdout.write(self.style.ERROR("Eccezione nella creazione del blog post: {}".format(str(ex))))

        self.stdout.write(self.style.SUCCESS("Creati {} blog post.".format(len(blog_posts))))

        # Aggiunta di post correlati per ogni blog post
        for post in blog_posts:
            try:
                possible_related = list(set(blog_posts) - {post})
                if possible_related:
                    related_posts = random.sample(possible_related, k=random.randint(0, min(3, len(possible_related))))
                    post.related_posts.add(*related_posts)
            except Exception as ex:
                self.stdout.write(self.style.ERROR("Eccezione nell'aggiornamento dei post correlati: {}".format(str(ex))))

        self.stdout.write(self.style.SUCCESS("Aggiornati i blog post con i post correlati."))
