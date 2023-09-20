"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstsite import views
from firstsite.views import RegisterView, LoginView, LogoutView, NewBook, NewReview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name="home"),
    path('nowosci/', views.new_view, name="nowosci"),
    path('recenzje/', views.all_reviews, name="recenzje"),
    path('o_mnie/', views.about_me, name="o_mnie"),
    path('kontakt/', views.contact, name="kontakt"),
    path('registration_form/', RegisterView.as_view(), name='registration_form'),
    # path('recenzja<str>',views.review, name="recenzja"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('new_review/', NewReview.as_view(), name='new_review'),
    path('new_book/', NewBook.as_view(), name='new_book')

]
