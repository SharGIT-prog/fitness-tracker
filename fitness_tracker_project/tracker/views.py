from django.shortcuts import render
import datetime
import random
from .forms import UserProfileForm
from django.shortcuts import redirect
from .models import DailyLog


def signup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'tracker/signup.html', {'form': form})

from .models import DailyLog
from .forms import DailyLogForm

def log_daily_data(request):
    suggested_exercises = ''
    celebration = ''

    if request.method == 'POST':
        form = DailyLogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            # Suggest exercise if not going to gym
            if not instance.went_to_gym:
                mins = instance.free_time_minutes or 0
                if mins >= 30:
                    suggested_exercises = "🧘 Yoga + 🚶‍♂️ Walk"
                elif mins >= 15:
                    suggested_exercises = "🏃‍♂️ Jog + Stretch"
                else:
                    suggested_exercises = "🚶‍♂️ Quick walk"
                instance.suggested_exercises = suggested_exercises

            # Check for milestone
            email = instance.user_email
            past_logs = DailyLog.objects.filter(user_email=email).order_by('date')
            if past_logs.exists():
                first_weight = past_logs.first().weight
                diff = abs(instance.weight - first_weight)

                if diff >= 5:
                    instance.milestone_achieved = True
                    celebration = "🎉 Milestone Reached: You've changed your weight by 5kg! 🏆"

            instance.save()
            return render(request, 'tracker/home.html', {'celebration': celebration})

    else:
        form = DailyLogForm()

    return render(request, 'tracker/daily_log.html', {'form': form})


import random
import datetime
from django.shortcuts import render

def home(request):
    # List of motivational quotes
    quotes = [
        "Push yourself because no one else is going to do it for you.",
        "Success starts with self-discipline.",
        "Today’s pain is tomorrow’s gain.",
        "Stay hydrated. Stay strong.",
        "Progress is progress, no matter how small.",
        "No excuses. Just results.",
        "You don’t have to be extreme, just consistent.",
        "Your body can stand almost anything. It’s your mind you have to convince."
    ]

    # Pick a random quote
    today_quote = random.choice(quotes)

    # Get current date and time
    now = datetime.datetime.now()
    date = now.strftime("%A, %d %B %Y")   # Example: Tuesday, 02 July 2025
    time = now.strftime("%I:%M %p")        # Example: 08:45 PM

    # Determine hydration message based on current hour
    hour = now.hour
    hydration_message = ''

    if 6 <= hour < 12:
        hydration_message = "🌞 Good morning! Time for your first glass of water 💧"
    elif 12 <= hour < 18:
        hydration_message = "🌤️ Afternoon hydration check! Drink some water 💧"
    elif 18 <= hour < 22:
        hydration_message = "🌇 Evening hydration reminder! One more glass 💧"
    elif 22 <= hour < 24:
        hydration_message = "🌙 Final hydration check before bed 💧"

    pre_workout_message = ''
    today = now.date()
    all_logs_today = DailyLog.objects.filter(date=today)

    if all_logs_today.exists():
        for entry in all_logs_today:
            if entry.went_to_gym:
                pre_workout_message = "⏱️ Don't forget to warm up before your workout! 💪"
                break

    return render(request, 'tracker/home.html', {
        'date': date,
        'time': time,
        'quote': today_quote,
        'hydration_message': hydration_message,
        'pre_workout_message': pre_workout_message
    })

from django.http import JsonResponse
from .models import DailyLog

def weight_data_json(request):
    email = request.GET.get('email', None)
    if not email:
        return JsonResponse({'error': 'Email required in URL: ?email=your@email.com'}, status=400)

    logs = DailyLog.objects.filter(user_email=email).order_by('date')
    dates = [log.date.strftime('%Y-%m-%d') for log in logs]
    weights = [log.weight for log in logs]

    return JsonResponse({'dates': dates, 'weights': weights})


def weight_chart_page(request):
    return render(request, 'tracker/weight_chart.html')
