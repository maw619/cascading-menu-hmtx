from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chapter/', views.chapter, name='chapter'),
    path("verse/", views.verse, name="verse")
]
