from django.db import models

# Create your models here.
# LearningJourney model stores entry title and description
class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.full_name