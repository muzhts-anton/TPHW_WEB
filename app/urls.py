from django.urls import path

from app import views

app_urlpatterns = [
    path('new/', views.index, name="index"),
    path('ask/', views.ask, name="ask"),
    path('tag/<slug:tag>/', views.bender, name="tag"),
    path('settings/', views.settings, name="settings"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
    # path('question/', views.question, name="question")
]