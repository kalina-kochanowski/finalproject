from django.db import models # Importing models From Django

class Player(models.Model):
    # Variables
    name = models.CharField(max_length = 200, verbose_name = "Username")
    bio = models.TextField(verbose_name = "Biography")
    slug = models.SlugField(max_length = 200, unique = True, blank = True)

    # Changes to Object Name in Admin For Ease of Use
    def __str__(self):
        return self.name

class Scenario(models.Model):
    # Variables
    title = models.CharField(max_length = 400)
    desc = models.TextField(verbose_name = "Description")

    # Changes to Object Name in Admin For Ease of Use
    def __str__(self):
        return self.title

class Choice(models.Model):
    # Variables
    scenario = models.ForeignKey(Scenario, related_name = "choices", on_delete = models.CASCADE)
    choice = models.CharField(max_length = 350)
    next_scenario = models.ForeignKey(Scenario, related_name = "next_scene", on_delete = models.CASCADE)

    # Changes to Object Name in Admin For Ease of Use
    def __str__(self):
        return self.choice + ', ' + self.scenario.title


