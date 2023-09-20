import datetime

import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from django.db import models
from firstsite.models import Book, Review, Author


@pytest.mark.django_db
def test_unauthenticated_user_cannot_add_new_book():
    # Tworzymy klienta testowego
    client = Client()

    # Definiujemy dane do utworzenia nowej książki
    book_data = {
        'title': 'Test Book',
        'publication_year': 2023,
        'isbn': '1234567890123',
        'genre': 'Test Genre',
    }

    # Tworzymy URL do widoku dodawania nowej książki
    url = reverse('new_book')

    # Próbujemy wysłać żądanie POST do widoku, jako niezalogowany użytkownik
    response = client.post(url, book_data)

    # Oczekujemy przekierowania (302) do strony logowania, ponieważ użytkownik jest niezalogowany
    assert response.status_code == 302

    # Upewniamy się, że nie została utworzona nowa książka
    assert Book.objects.count() == 0


@pytest.fixture
def logged_in_user():
    # Tworzymy użytkownika i logujemy go
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = Client()
    client.login(username='testuser', password='testpassword')
    return user, client


@pytest.mark.django_db
def test_authenticated_user_can_add_new_book(logged_in_user):
    # Tworzymy klienta testowego
    user, client = logged_in_user

    # Definiujemy dane do utworzenia nowej książki
    book_data = {
        'title': 'Test Book',
        'publication_year': 2023,
        'isbn': '1234567890123',
        'genre': 'Test Genre',
    }

    # Tworzymy URL do widoku dodawania nowej książki
    url = reverse('new_book')

    # Próbujemy wysłać żądanie POST do widoku, jako zalogowany użytkownik
    response = client.post(url, book_data)

    # Oczekujemy sukcesu, ponieważ użytkownik jest zalogowany
    assert response.status_code == 200

    # Upewniamy się, że została utworzona nowa książka
    assert Book.objects.count() == 1


@pytest.mark.django_db
def test_unauthenticated_user_cannot_add_new_review():
    # Tworzymy klienta testowego
    client = Client()

    # Definiujemy dane do utworzenia nowej recenzji
    review_data = {
        'book': 'Test Book',
        'user': 'TEST_KUBA',
        'content': 'lorem ipsum tralalala',
        'rating': '6',
        'publication_date': '2023-09-08 16:01:39.661374 +00:00'
    }

    # Tworzymy URL do widoku dodawania nowej recenzji
    url = reverse('new_review')

    # Próbujemy wysłać żądanie POST do widoku, jako niezalogowany użytkownik
    response = client.post(url, review_data)

    # Oczekujemy przekierowania (302) do strony logowania, ponieważ użytkownik jest niezalogowany
    assert response.status_code == 302

    # Upewniamy się, że nie została utworzona nowa recenzja
    assert Review.objects.count() == 0
