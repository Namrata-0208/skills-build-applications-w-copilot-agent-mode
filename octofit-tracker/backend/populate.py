import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from octofit_tracker.models import UserProfile, Activity, Team, WorkoutSuggestion

# Create users
user1 = User.objects.create_user(username='alice', password='pass123')
user2 = User.objects.create_user(username='bob', password='pass123')

# Create profiles
profile1 = UserProfile.objects.create(user=user1, age=28, weight=65, height=170, fitness_goal='Weight loss')
profile2 = UserProfile.objects.create(user=user2, age=32, weight=75, height=180, fitness_goal='Muscle gain')

# Create activities
activity1 = Activity.objects.create(user=user1, activity_type='Running', duration=45, calories_burned=400)
activity2 = Activity.objects.create(user=user2, activity_type='Cycling', duration=60, calories_burned=500)

# Create team
team = Team.objects.create(name='Fitness Warriors')
team.members.add(user1, user2)

# Create suggestions
suggestion1 = WorkoutSuggestion.objects.create(user=user1, suggestion='Try HIIT workouts')
suggestion2 = WorkoutSuggestion.objects.create(user=user2, suggestion='Focus on strength training')

print('Test data populated successfully')

# Verify
print('Users:', User.objects.count())
print('Profiles:', UserProfile.objects.count())
print('Activities:', Activity.objects.count())
print('Teams:', Team.objects.count())
print('Suggestions:', WorkoutSuggestion.objects.count())