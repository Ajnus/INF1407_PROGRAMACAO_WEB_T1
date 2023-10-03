from django.urls.conf import path
from forum import views
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

app_name = "forum"

urlpatterns = [
    path('lista/', views.PublicacaoListView.as_view(),
        name='lista-publicacoes'),
    path('', views.PublicacaoListView.as_view(),
        name='home-publicacoes'),
    path('atualiza/<int:pk>/',
        views.PublicacaoUpdateView.as_view(),
        name='atualiza-publicacao'),
    path('cria/', views.PublicacaoCreateView.as_view(),
        name='cria-publicacao'),
    path('apaga/<int:pk>/', views.PublicacaoDeleteView.as_view(),
        name='apaga-publicacao'),
]