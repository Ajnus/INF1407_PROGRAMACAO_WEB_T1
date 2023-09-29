from django.urls.conf import path
from forum import views

app_name = "forum"

urlpatterns = [
    path('lista/', views.PublicacaoListView.as_view(),
        name='lista-publicacoes'),
    path('', views.PublicacaoListView.as_view(),
        name='home-publicacoes'),
    path('cria/', views.PublicacaoCreateView.as_view(),
        name='cria-publicacao'),
]