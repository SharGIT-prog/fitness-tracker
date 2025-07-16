from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'age', 'height', 'food_pref', 'goal']
from .models import DailyLog

class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = [
            'user_email', 'weight', 'went_to_gym', 'workout_details',
            'calories_burned', 'free_time_minutes'
        ]
