from .models import Player # Imports models To Be Used With Views
from django.shortcuts import render # Imports render to Render HTML Pages
from django.views.generic import DetailView # Imports Special Views

# View That Displays the Home Page
def index(request):
    return render(request, 'adventure/index.html') # Returns the Home Page

# A View That Displays the profile for the Player
class PlayerProfile(DetailView):

    model = Player

    template_name = 'adventure/profile.html'
