from django.urls import path

from . import views

app_name = 'classify'
urlpatterns = [
    path('', views.form, name='form'),
    path('classify/', views.classify, name='classify'),
]