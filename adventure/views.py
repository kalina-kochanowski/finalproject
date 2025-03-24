from .models import Player, Scenario # Imports models To Be Used With Views
from django.shortcuts import render, get_object_or_404 # Imports render to Render HTML Pages
from django.views.generic import DetailView # Imports Special Views

# View That Displays the Home Page
def index(request):
    return render(request, 'adventure/index.html') # Returns the Home Page

def adventure(request, scenario_id):
    # Uses the current scenario model by using its id in the database, if it is not found gives a 404 error
    scenario = get_object_or_404(Scenario, pk = scenario_id)

    decisions = scenario.choices.all() # Gets all possible choices to be used for the specific scenario

    # Puts Variables to Use in HTML with a context variable
    context = {'scenario' : scenario, "decisions" : decisions}

    #Returns the adventure game page depending on which scenario it is at
    return render(request, 'adventure/game.html', context)

# A View That Displays the profile for the Player
class PlayerProfile(DetailView):

    model = Player

    template_name = 'adventure/profile.html'
