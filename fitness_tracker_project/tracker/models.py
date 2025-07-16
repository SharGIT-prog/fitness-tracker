from django.db import models

class UserProfile(models.Model):
    FOOD_CHOICES = [('Veg', 'Vegetarian'), ('Non-Veg', 'Non-Vegetarian')]
    GOAL_CHOICES = [
        ('Weight Loss', 'Weight Loss'),
        ('Weight Gain', 'Weight Gain'),
        ('Muscle Building', 'Muscle Building')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    height = models.FloatField()
    food_pref = models.CharField(max_length=10, choices=FOOD_CHOICES)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)

    def __str__(self):
        return self.name
from django.utils import timezone

class DailyLog(models.Model):
    user_email = models.EmailField()
    date = models.DateField(default=timezone.now)
    weight = models.FloatField()
    went_to_gym = models.BooleanField()
    workout_details = models.TextField(blank=True)
    calories_burned = models.IntegerField(default=0)
    free_time_minutes = models.IntegerField(blank=True, null=True)
    suggested_exercises = models.TextField(blank=True)
    milestone_achieved = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user_email} - {self.date}"
