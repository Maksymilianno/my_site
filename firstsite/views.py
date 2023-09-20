import pytest
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.views import View
from firstsite.forms import RegistrationForm, LoginForm, NewBookForm, NewReviewForm
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from firstsite.models import Review, Book, Reviewer
from django.test import RequestFactory


# Create your views here.
def home(request):
    return render(request, "base.html")


def new_view(request):
    return render(request, 'new.html')


def all_reviews(request):
    return render(request, 'all_reviews.html')


def about_me(request):
    return render(request, 'about_me.html')


def contact(request):
    return render(request, 'contact.html')


class RegisterView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, "registration_form.html", {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['hasło']
            password2 = form.cleaned_data['powtórz hasło']

            if password1 == password2:
                user_model = get_user_model()
                user = user_model.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                      email=email, password=password1)
                login(request, user)  # Zaloguj po rejestracji

                # rejestrujacy staje sie recenzentem
                reviewer = Reviewer(user=user, first_name=first_name, last_name=last_name, email=email)
                reviewer.save()

                return redirect('home')
            else:
                return render(request, 'registration_form.html', {'form': form, 'error': 'Hasła nie pasują do siebie.'})
        else:
            return render(request, 'registration_form.html', {'form': form})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "login_form.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login_form.html', {'form': form, 'error': 'Nieprawidłowe dane logowania.'})
        else:
            return render(request, 'login_form.html', {'form': form})


class LogoutView(BaseLogoutView):
    template_name = 'logout.html'


class NewReview(LoginRequiredMixin, View):
    def get(self, request):
        form = NewReviewForm()
        return render(request, 'new_review.html', {'form': form, 'message': None})

    def post(self, request):
        form = NewReviewForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            content = form.cleaned_data['content']
            rating = form.cleaned_data['rating']

            # pobierz zalogowanego uzytkownika
            user = request.user

            # tworzy nowa recenzje
            review = Review(book=book, content=content, rating=rating, user=user)
            review.save()

            message = 'Dodano recenzję'
        else:
            message = None
        return render(request, 'new_review.html', {'form': form, 'message': message})


class NewBook(LoginRequiredMixin, View):
    def get(self, request):
        form = NewBookForm()
        return render(request, 'new_book.html', {'form': form, 'message': None})

    def post(self, request):
        form = NewBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            publication_year = form.cleaned_data['publication_year']
            isbn = form.cleaned_data['isbn']
            genre = form.cleaned_data['genre']

            user = request.user

            # Tutaj dodajemy nową książkę do bazy danych
            book = Book(title=title, publication_year=publication_year, isbn=isbn, genre=genre)
            book.save()

            message = 'Dodano książkę'
        else:
            message = None

        return render(request, 'new_book.html', {'form': form, 'message': message})
