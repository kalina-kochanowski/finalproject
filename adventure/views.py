from .models import Player, Scenario # Imports models To Be Used With Views
from django.shortcuts import render, redirect, get_object_or_404 # Imports shortcuts to be used in views
from django.views.generic import DetailView # Imports Special Views
from django.contrib.auth import login, logout # Imports login & logout to be used for those purposes
from django.contrib.auth.forms import AuthenticationForm

# View That Displays the Home Page
def index(request):
    # If the user is logged in, uses their username in the index template
    context = {}

    if request.user.is_authenticated:
        context['user_name'] = request.user.username

    return render(request, 'adventure/index.html') # Returns the Home Page

def adventure(request, scenario_id):
    # Uses the current scenario model by using its id in the database, if it is not found gives a 404 error
    scenario = get_object_or_404(Scenario, pk = scenario_id)

    decisions = scenario.choices.all() # Gets all possible choices to be used for the specific scenario

    # Puts Variables to Use in HTML with a context variable
    context = {'scenario' : scenario, "decisions" : decisions}

    #Returns the adventure game page depending on which scenario it is at
    return render(request, 'adventure/game.html', context)

# View to help redirect pages so the user cannot use the back button (Works with the Javascript file)
def jump_to_scenario(request, scenario_id):
    return redirect('adventure:game', scenario_id=scenario_id)

# A View That Displays the profile for the Player
class PlayerProfile(DetailView):
    model = Player

    template_name = 'adventure/profile.html'

# Login View
def user_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('adventure:index')  # Redirects to home page
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)

    return redirect('adventure:index')  # Redirect to the home page after logout
