from django import forms

from firstsite.models import Book


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Login", max_length=32)
    first_name = forms.CharField(label="Imię", max_length=64)
    last_name = forms.CharField(label="Nazwisko", max_length=64)
    email = forms.EmailField()
    password1 = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class NewReviewForm(forms.Form):
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        label='Wybierz książkę do zrecenzowania',
    )
    content = forms.CharField(
        label='Treść recenzji',
        widget=forms.Textarea()
    )
    rating = forms.IntegerField(
        label='Ocena',
        min_value=1,
        max_value=10,
        help_text='Proszę podać ocenę od 1 do 10'
    )


class NewBookForm(forms.Form):
    title = forms.CharField(label='Tytuł', max_length=128)
    publication_year = forms.IntegerField(label='Rok publikacji', min_value=1000, max_value=9999)
    isbn = forms.CharField(label='ISBN', max_length=13)
    genre = forms.CharField(label='Gatunek', max_length=64)
    authors = forms.CharField(label='Autorzy', max_length=128, required=False)
