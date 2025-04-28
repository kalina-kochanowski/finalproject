# Imports To Help Display Views
from django.urls import path
from . import views

app_name = 'adventure' # Name of App To Be Used as a Way to Help With Linking Pages to Other Pages

# URL Patterns To Display Views as HTML Pages
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('player/<slug:slug>/', views.PlayerProfile.as_view(), name = 'profile'),
    path('scenario/<int:scenario_id>/', views.adventure, name = 'game'),
    path('jump/<int:scenario_id>/', views.jump_to_scenario, name = 'jump'),
]