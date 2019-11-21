from django.conf.urls import url
from django.urls import path

from tiendaAPI.views import CategoriaList
from rest_framework.authtoken import views


urlpatterns = [
    path('categorias/', CategoriaList.as_view()),
    url(r'^api-token-auth/', views.obtain_auth_token)
]