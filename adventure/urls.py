# Imports To Help Display Views
from django.urls import path
from . import views

app_name = 'adventure' # Name of App To Be Used as a Way to Help With Linking Pages to Other Pages

# URL Patterns To Display Views as HTML Pages
urlpatterns = [
    path('', views.index, name = 'index'),
    path('player/<slug:slug>/', views.PlayerProfile.as_view(), name = 'profile'),
    path('scenario/<int:scenario_id>/', views.adventure, name = 'game'),
]