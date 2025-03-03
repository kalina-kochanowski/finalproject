from django.contrib import admin # Imports admin - To Use my Models With admin Interface
from .models import Player # Imports the Ability to Use My Models

# Registers All Models To Be Used With admin Interface
admin.site.register(Player)
