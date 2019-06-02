from django.urls import path
from . import views

app_name = 'stats'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),

    path('', views.index, name='index'),
    path('get_teams/', views.get_teams, name='get_teams'),
]