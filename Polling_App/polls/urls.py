from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/1
    path('<int:quesiton_id>/', views.detail, name='detail'),
    # ex: /polls/1/result/
    path('<int:quesiton_id>/results/', views.results, name='result'),
    # ex: /polls/1/votes
    path('<int:quesiton_id>/vote/', views.vote, name='result'),


]
