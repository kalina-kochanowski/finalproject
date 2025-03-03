from django.db import models # Importing models From Django

class Player(models.Model):
    # Variables
    name = models.CharField(max_length = 200, verbose_name = "Username")
    bio = models.TextField(verbose_name = "Biography")
    slug = models.SlugField(max_length = 200, unique = True, blank = True)

    # Changes to Object Name in Admin For Ease of Use
    def __str__(self):
        return self.name



